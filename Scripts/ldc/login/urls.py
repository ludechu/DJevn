from django.conf.urls import url,include
from django.urls import path,re_path
from . import views
urlpatterns = [
    path(r'',views.login1),
    re_path(r'^login/(\d+)', views.detail),
    re_path(r'get1/', views.get1),
    re_path(r'^get2/', views.get2),
    re_path(r'^postpage/post1/', views.post1),
    re_path(r'^postpage/', views.postpage),
    re_path(r'^setcookie/', views.setcookie),
    re_path(r'^getcookie/', views.getcookie),
    re_path(r'^delcookie/', views.delcookie),
    re_path(r'^redirect/', views.redirect),
    re_path(r'^redirect1/', views.redirect1),
    re_path(r'^main/$',views.main),
    re_path(r'^login_index/$',views.login_index),
]