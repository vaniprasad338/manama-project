from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index1.html'),
    # path('', error404, name='404.html'),
    path('index/', index, name='index.html'),
    path('login/', login, name='login'),
    path('cart/', cart, name='cart.html'),
    path('checkout/', checkout, name='checkout.html'),
    path('contact-us/', contactus, name='contact-us.html'),
    path('product-details/', productdetails, name='product-details.html'),
    path('shop/', cust, name='shop.html'),
    path('scoin/', scoin, name='scoin.html'),
    path('new/', cust, name='new.html'),
    path('bynow/', bynow, name='bynow'),
    path('purchase/', purchase, name='purchase'),
    path('validate/<int:cid>,<int:status>', validate, name='validate'),
    path('product_add_cart/<int:cid>,<int:id>,<int:discounted_price>/',product_add_to_cart, name='add_to_cart'),
    path('offer_add_cart/<int:cid>,<int:id>,<int:discount>/', offer_add_to_cart, name='add_to_cart1'),
    path('finish/<int:coin>,<int:cid>',finish_purchase,name='finish'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
