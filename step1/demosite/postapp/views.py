from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from postapp.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post/list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)$', PostDetailView.as_view(), name='post_detail_view'),
    url(r'^$', PostListView.as_view(), name='post_list_view'),
)
