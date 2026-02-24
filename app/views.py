from django.shortcuts import render
from rest_framework import viewsets
from app.models import Patient
from app.serializer import PatientSerializer

# Créer toutes les opérations CRUD (create, read, update, delete)

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
