from re import template
from django.urls import path
from . import views

app_name="application"

urlpatterns=[
    path('',views.default,name='home'),
    path('staff',views.staff_view.as_view(),name='staff'),
    path('student',views.student_view.as_view(),name='student'),
    path('student_form',views.student_form_view.as_view(),name='student-form'),
    path('staff_form',views.staff_form_view.as_view(),name='staff-form'),
    path('message/<str:name>',views.send_email_collectively.as_view(),name='message-form'),
    path('send/',views.send_email.as_view(),name='send-mail'),
]   