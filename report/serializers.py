# backend/api/serializers.py

from rest_framework import serializers
from .models import *

class CreateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = createreport
        fields = ['id','title']