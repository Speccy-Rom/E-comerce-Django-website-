from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            data = {"last_name": user.last_name, "first_name": user.first_name, "email": user.email}
            form = OrderCreateForm(request.POST, initial=data)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.username = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/created.html', {'order': order})
    else:
        user = request.user
        data = {}
        if user.is_authenticated:
            data["last_name"] = user.last_name
            data["first_name"] = user.first_name
            data["email"] = user.email
        form = OrderCreateForm(initial=data)
    return render(request, 'orders/create.html',
                  {'cart': cart,
                   'form': form})
