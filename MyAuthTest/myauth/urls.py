from django.conf.urls import url

import myauth.views as auth_views

urlpatterns = [
    url(r'^$', auth_views.index, name='url_auth_index'),
    url(r'^register$', auth_views.register, name='url_register'),
    url(r'^login$', auth_views.login, name='url_login'),
    url(r'^logout$', auth_views.logout, name='url_logout'),
    url(r'^authenticate$', auth_views.authenticate, name='url_authenticate'),
]
