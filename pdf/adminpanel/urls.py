from django.contrib.auth import views as auth_views
from django.urls import path
from .views import Dashboard, NotificationView, NotificationCount, DailyRenewableGenerationReportView, \
    DailyRenewableGenerationReportISGSView, StateControlAreaView, ReadNotifications

app_name = 'adminpanel'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('report-1/', DailyRenewableGenerationReportView.as_view(), name='report-1'),
    path('report-2/', DailyRenewableGenerationReportISGSView.as_view(), name='report-2'),
    path('report-3/', StateControlAreaView.as_view(), name='report-3'),
    path('notification/', NotificationView.as_view(), name='notification'),
    path('notification-count/', NotificationCount.as_view(), name='notification-count'),
    path('read-notification/', ReadNotifications.as_view(), name='read-notification'),
    path('change-password/',
         auth_views.PasswordChangeView.as_view(
             template_name='change_password.html'),
         name='change-password'),
    path('password-change-done',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='change_password_done.html'),
         name='password_change_done'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html'
         ),
         name='password_reset'),
]
