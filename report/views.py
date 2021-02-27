from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from report.serializers import *



class ListReportAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = createreport.objects.all()
        serializer = CreateReportSerializer(snippets, many=True)
        return Response(serializer.data)


class CreateReportAPIView(generics.CreateAPIView):
    queryset = createreport.objects.all()
    serializer_class = CreateReportSerializer




class CreateReportDetailAPIView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, id):
        try:
            return createreport.objects.get(id=id)
        except createreport.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = CreateReportSerializer(snippet)
        return Response(serializer.data)


    