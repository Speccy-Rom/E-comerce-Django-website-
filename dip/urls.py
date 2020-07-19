from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from dip import settings
from cart import views
from dshop import views


urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('dshop/', include('dshop.urls', namespace='dshop')),
    path('articles/', views.articles_list, name='articles_list'),
    path('articles/<slug>/', views.articles_detail, name='articles_detail_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
