from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login', views.login, name='signin'),
    path('register', views.register, name='register'),
    path("logout" ,views.logout, name="logout"),
    path("profile",views.profile, name="profile"),

    #url('email-verify/(?P<token>[\w\-]+)',views.confirm_email),
    #url('resend-confirmation/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})',views.resend_confirmation_email),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
                                    name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_reset_form.html'),
                                    name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
                                    name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
                                    name='password_reset_complete'),

]