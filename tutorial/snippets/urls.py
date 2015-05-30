from django.conf.urls import url
from snippets import views

'''the below module import is used for importing the foramt type in which we 
the data like json or xml'''
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
