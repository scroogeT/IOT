from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns ={
    url(r'^$', index, name='index'),
    url(r'^devices/$', CreateView.as_view(), name="create"),
    url(r'^devices/(?P<pk>[0-9]+)/$',DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)