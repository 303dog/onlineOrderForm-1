from django.conf.urls import url
from .views import CreateOrderContactPersonView


app_name = 'collar'
urlpatterns = [
    url(r'^update-delivery-details/(?P<pk>[/d]+)', CreateOrderContactPersonView.as_view(), name='orderdeliveryaddressupdate')
]