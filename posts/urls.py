from django.conf.urls import url
from . import views

app_name = 'posts'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^posts/(?P<post_id>\d+)/', views.posts, name='posts_list'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^about/', views.about, name='about'),
	url(r'^add/', views.add, name = 'add_post'),
]
