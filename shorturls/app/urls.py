from django.conf.urls import url, include

import views

urlpatterns = [
  url(r'^new_link/$',views.create_link,name='create_link'),
  url(r'^(\w+)?$',views.redirect_link,name='redirect_link'),
  url(r'^list/$',views.list_links,name='list_links'),

    ]