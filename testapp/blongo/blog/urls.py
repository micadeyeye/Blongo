from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'blog.blogapp.views.index'),
    url(r'^update/', 'blog.blogapp.views.update'),
    url(r'^delete/', 'blog.blogapp.views.delete'),
)
