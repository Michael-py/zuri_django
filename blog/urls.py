from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('article/<int:post_id>/', views.details, name='details'),
    path('create/', views.add_new, name='create'),
    path('update/<str:post_id>/', views.update, name='update'),
    path('<int:post_id>/delete', views.delete, name='delete'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="blog/reset_password.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="blog/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="blog/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="blog/password_reset_done.html"), name='password_reset_complete'),
]