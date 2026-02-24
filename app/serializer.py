from rest_framework import serializers
from app.models import Patient

# Transformer les objets Python (souvent les modèles) en JSON (ou XML) 
# pour que le front ou les clients API puissent les consommer

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "lastName", "firstName", "phoneNumber", "email", "createAt"]
        read_only_fields = ["id", "createAt"]