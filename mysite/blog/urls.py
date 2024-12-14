""" the URL pattern maps urls to views , its composed of a string pattern , a view and optionally a name  """
from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # <int:id> is a path converter , any value from the url is a string 
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name ='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed')
]