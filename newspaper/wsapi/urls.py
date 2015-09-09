from django.conf.urls import patterns, url

urlpatterns = patterns(
    'newspaper.wsapi',
    url(r'^article/$', 'views.add_article',
        name='article_add'),
)
