from django.conf.urls import url
from .views import CustomerSurveyUpdate
from .views import ThanksView
from .views import SurveyPDFView
from . import views

app_name = 'survey'
urlpatterns = [
    url(r'(?P<hash>[\w]{15,18})/$', views.surveyForm, name='hash_check'),
    url(r'update-order-form/(?P<hash>[\w]{15,18})/(?P<pk>[\d]+)/$', CustomerSurveyUpdate.as_view(), name='survey_customer_form'),
    url(r'delivery-address/(?P<hash>[\w]{15,18})/(?P<pk>[\d]+)/$', views.customer_deliver_address, name='survey_delivery_form'),
    url(r'^thanks/(?P<hash>[\w]{15,18})/(?P<pk>[\d]+)/$', ThanksView.as_view(), name='thanks'),
    url(r'^pdf/(?P<pk>[\d]+).pdf$', SurveyPDFView.as_view(), name='pdf'),
]