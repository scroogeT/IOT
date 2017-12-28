from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from .views import *

urlpatterns ={
    url(r'^$', index, name='index'),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^devices/$', CreateView.as_view(), name="create"),
    url(r'^devices/(?P<pk>[0-9]+)/$',DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)