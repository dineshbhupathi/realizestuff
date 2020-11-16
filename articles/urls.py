from django.conf.urls import url
from .views import *
from articles.apis.article_api import *
from articles.apis.users_api import *
urlpatterns = [
    # url('^$', home_page_view),
    url('test/', online),
# r'^beds/(?P<pk>[0-9]*)$'
    url(r'^api/articles/(?P<pk>[0-9]*)$', ArticlesView.as_view()),
    url(r'^api/suggestions/$', SuggestionsView.as_view()),
    url(r'^api/users/$', UsersView.as_view()),
    url(r'^api/comments/(?P<post_id>[0-9]*)$', Comments.as_view()),
    url(r'^login/$', Login.as_view())





]
