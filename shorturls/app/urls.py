from django.conf.urls import url, include

from views import link

urlpatterns = [
  url(r'^new_link/$',link.create_link,name='create_link'),
  url(r'^(\w+)?$',link.redirect_link,name='redirect_link'),
  url(r'^list/$',link.list_links,name='list_links'),

    ]