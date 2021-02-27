from django.urls import path
from .views import *

urlpatterns = [
    path('create-report/',CreateReportAPIView.as_view(),name='create-report'),
    path('create-report/<int:id>',CreateReportDetailAPIView.as_view(),name='report-detail'),
]