# cspell:ignore viewsets
from django.shortcuts import render
from rest_framework import viewsets
from app.models import Patient, Medecin, Profile
from app.serializer import PatientSerializer, ProfileSerializer, MedecinSerializer
# Créer toutes les opérations CRUD (create, read, update, delete)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class MedecinViewSet(viewsets.ModelViewSet):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer
    


    
