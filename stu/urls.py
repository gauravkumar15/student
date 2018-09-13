from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'(?P<pk>\d+)/$',views.detail, name='detail'),
    url(r'new/$',views.new, name='new'),
    url(r'register/$',views.register, name='register'),
]

