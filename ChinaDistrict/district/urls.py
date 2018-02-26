from django.urls import path, re_path
from district import views

urlpatterns = [
    path('', views.index, name='district'),
    re_path(r'(?P<code>[0-9]{6})', views.get_district_info),
]
