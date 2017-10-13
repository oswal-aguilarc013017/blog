from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/nuevo/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^borradores/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publicar/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/eliminar/$', views.post_remove, name='post_remove'),

]
