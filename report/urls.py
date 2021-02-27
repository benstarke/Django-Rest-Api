from django.urls import path
from .views import *

urlpatterns = [
    path('',ListReportAPIView.as_view(),name='list-reports'),
    path('create-report/',CreateReportAPIView.as_view(),name='create-reports'),
    path('create-report/<int:id>',CreateReportDetailAPIView.as_view(),name='report-detail-view'),
]