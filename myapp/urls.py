from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns=[
url(r'^index/$', views.home),
    url(r'^shop/$', views.shop),
    url(r'^shop/(\w+)$',views.shop2),
    url(r'^product/(\d+)$', views.product),
    url(r'^cart/$', views.cart),
    url(r'^checkout/$', views.checkout),
    url(r'^login/$', views.login_option),
    url(r'^login_admin/$',views.login),
    url(r'^login_user/$',views.login_user),
    url(r'^admin_page/$',views.admin_login),
    url(r'^search/$',views.search),
    url(r'^add_product/$',views.add_product),
    url(r'^delete/(\d+)$',views.delete_cart_item),
    url(r'^register/$',views.register),
    url(r'logout/$',views.logout_user),
]