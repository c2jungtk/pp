from django.conf.urls import url, include

from .views import *
from board import views
urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    # url(r'^$', ProductListView.as_view(), name='product_list'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^(?P<pk>\d+)/update/$', ProductUpdateView.as_view(), name='product_update'),
    url(r'^(?P<pk>\d+)/delete/$', ProductDeleteView.as_view(), name='product_delete'),
    url(r'^new/$', ProductCreateView.as_view(), name='product_new'),
    url(r'^(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    # url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

]