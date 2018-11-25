from django.conf.urls import url
from . import views
from .views import CustomerMiniFawmUpdate
from .views import ThanksView
from .views import VertexLitePDFView

app_name = 'miniFawn'
urlpatterns = [
    url(r'(?P<hash>[\w]{15,18})/$', views.miniFawnForm, name='hash_check'),
    url(r'update-order-form/(?P<hash>[\w]{15,18})/(?P<pk>[\d]+)/$', CustomerMiniFawmUpdate.as_view(), name='miniFawn_customer_form'),
    url(r'delivery-address/(?P<hash>[\w]{15,18})/(?P<pk>[\d]+)/$', views.customer_deliver_address, name='miniFawn_delivery_form'),
    url(r'^thanks/(?P<hash>[\w]{15,18})/(?P<pk>[\d]+)/$', ThanksView.as_view(), name='thanks'),
    url(r'^pdf/(?P<pk>[\d]+).pdf$', VertexLitePDFView.as_view(), name='pdf'),
]