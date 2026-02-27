from rest_framework import serializers
from app.models import Patient
from app.models import Profile
from app.models import Medecin


# Transformer les objets Python (souvent les modèles) en JSON (ou XML) 
# pour que le front ou les clients API puissent les consommer

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "lastName", "firstName", "phoneNumber", "email", "address", "createAt"]
        read_only_fields = ["id", "createAt"]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id","person", "photo", "biography"]
        

class MedecinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecin
        fields = ["id", "lastName", "firstName", "phoneNumber", "email", "expertise","address","createAt"]
        read_only_fields = ["id", "createAt"]
        
