from django.conf.urls import url
from .views import all_features, feature_detail, request_feature

urlpatterns = [
    url(r'^$', all_features, name='all_features'),
    url(r'^(?P<pk>\d+)/$', feature_detail, name='feature_detail'),
    url(r'^new/$', request_feature, name='request_feature'),
]