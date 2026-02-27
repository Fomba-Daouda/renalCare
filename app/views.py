# cspell:ignore viewsets
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from app.models import Patient, Medecin, Profile, Person
from app.serializer import PatientSerializer, ProfileSerializer, MedecinSerializer
from rest_framework.response import Response

# Créer toutes les opérations CRUD (create, read, update, delete)
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class MedecinViewSet(viewsets.ModelViewSet):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer
    

class ProfileViewSet(viewsets.ViewSet):
    # 🔹 CREATE (POST /profiles/)
    def create(self, request):
        person_id = request.data.get("person")

        if not person_id:
            return Response(
                {"error": "Le champ 'person' est obligatoire."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Vérifie que la personne existe
        person = get_object_or_404(Person, pk=person_id)

        # Crée ou met à jour le profil (important pour OneToOneField)
        profile, created = Profile.objects.update_or_create(
            person=person,
            defaults={
                "photo": request.data.get("photo"),
                "biography": request.data.get("biography"),
            }
        )

        serializer = ProfileSerializer(profile)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
        )


    # 🔹 UPDATE (PUT /profiles/<id>/)
    def update(self, request, pk=None):
        profile = get_object_or_404(Profile, pk=pk)

        serializer = ProfileSerializer(
            profile,
            data=request.data,
            partial=True  # permet mise à jour partielle
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


    # 🔹 LIST (GET /profiles/)
    def list(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # 🔹 RETRIEVE (GET /profiles/<id>/)
    def retrieve(self, request, pk=None):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # 🔹 DELETE (DELETE /profiles/<id>/)
    def destroy(self, request, pk=None):
        profile = get_object_or_404(Profile, pk=pk)
        profile.delete()
        return Response(
            {"message": "Profil supprimé avec succès."},
            status=status.HTTP_204_NO_CONTENT
        )
    


    
