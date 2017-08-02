from django.conf.urls import url
from posts import views

urlpatterns = [
	url(r'^$', views.posts_home),
	url(r'^(?P<id>\d+)/$', views.post_detail, name="detail"),
	url(r'^(?P<id>\d+)/edit/$', views.post_update, name="update"),
	url(r'^(?P<id>\d+)/delete/$', views.post_delete, name="delete"),
	url(r'^create/', views.post_create),
]
