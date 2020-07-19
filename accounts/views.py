from django.core.mail import send_mail
from .forms import SignUpEmailForm
from django.views.generic.edit import FormView


class EmailRegisterFormView(FormView):
    form_class = SignUpEmailForm
    success_url = "/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        username = form.cleaned_data.get('username')
        send_mail(subject='код подтверждения',
                  message=f'Спасибо за регистрацию, {username}! Ваш пароль: {password}',
                  from_email='info@SpeccyShop.ru',
                  recipient_list=[email],
                  fail_silently=False)
        return super(EmailRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(EmailRegisterFormView, self).form_invalid(form)


