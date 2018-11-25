from django.conf.urls import url
from . import views
from .views import CustomerTrapTransmitterUpdate
from .views import ThanksView
from .views import VertexLitePDFView

app_name = 'trapTransmitter'
urlpatterns = [
    url(r'(?P<hash>[\w]{15,18})/$', views.trapTransmitterForm, name='hash_check'),
    url(r'update-order-form/(?P<hash>[\w]{15,18})/(?P<pk>[\d]+)/$',
        CustomerTrapTransmitterUpdate.as_view(),
        name='trapTransmitter_customer_form'),
    url(r'delivery-address/(?P<hash>[\w]{15,18})/(?P<pk>[\d]+)/$',
        views.customer_deliver_address,
        name='trapTransmitter_delivery_form'),
    url(r'^thanks/(?P<hash>[\w]{15,18})/(?P<pk>[\d]+)/$', ThanksView.as_view(), name='thanks'),
    url(r'^pdf/(?P<pk>[\d]+).pdf$', VertexLitePDFView.as_view(), name='pdf'),
]