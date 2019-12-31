from django.conf.urls import url
from .views import *

app_name='offline'
urlpatterns=[
    url(r'^users$',UserApiView.as_view(),name="users"),
    url(r'^user/(?P<pk>[0-9]+)$',UserRudApiView.as_view(),name="user"),
    url(r'^categories/$',CategoryApiView.as_view(),name="categories"),
    url(r'^category/(?P<pk>[0-9]+)$', CategoryRudView.as_view(), name="category"),
    url(r'^foods/(?P<food_category>[0-9]+)$',FoodApiView.as_view(),name="foods"),
    url(r'^food/(?P<pk>[0-9]+)$', FoodRudView.as_view(), name="food"),
    url(r'^orders/$', OrderApiView.as_view(), name="orders"),
    url(r'^order/(?P<pk>[0-9]+)$', OrderRudView.as_view(), name="order"),

]
