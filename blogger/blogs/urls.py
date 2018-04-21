from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('login',views.login,name='login'),
    path('',views.home,name='home'),
    path('create_blog',views.create_blog,name='create_blog'),
    path('create_blog_entry',views.create_blog_entry, name='create_blog_entry'),
    path('myblogs',views.myblogs,name='myblogs'),
    path('delete_blog',views.delete_blog,name="delete_blog"),
    path('<int:blog_id>',views.detail,name='detail'),
    path('login_user',auth_views.login,name = 'login_user'),
    path('logout_user',auth_views.logout,name='logout_user'),
    path('delete/<int:blog_id>',views.delete,name="delete"),
    path('create_user_form',views.create_user_form,name="create_user_form"),
    path('create_user',views.create_user,name="create_user"),
    path('forgot_password_form',views.forgot_password_form,name='forgot_password_form'),
    path('forgot_password',views.forgot_password,name="forgot_password"),
    path('change_password',views.change_password,name="change_password")
]