from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('findbus/', views.findbus, name='findbus'),
    path('seebookings/', views.seebookings, name='seebookings'),
    path('travel-history/', views.travel_history, name='travel_history'),
    path('cancellings/', views.cancellings, name='cancellings'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('success/', views.success, name='success'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile'),
    path('selectseats/<int:bus_id>/', views.select_seats, name='select_seats'),
    path('confirm_booking/<int:bus_id>/', views.confirm_booking, name='confirm_booking'),
    path('download_ticket/<int:book_id>/', views.download_ticket, name='download_ticket'),
    path('review/<int:book_id>/', views.submit_review, name='submit_review'),
    path('verify-ticket/', views.verify_ticket, name='verify_ticket'),
    path('sendotp/', views.send_otp, name='sendotp'),
    path('validate-promo/', views.validate_promo, name='validate_promo'),
    path('save-favourite/', views.save_favourite, name='save_favourite'),
    path('delete-favourite/<int:fav_id>/', views.delete_favourite, name='delete_favourite'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('export-excel/', views.export_bookings_excel, name='export_excel'),
    path('monthly-report/', views.monthly_report, name='monthly_report'),
    path('operator/register/', views.operator_register, name='operator_register'),
]
