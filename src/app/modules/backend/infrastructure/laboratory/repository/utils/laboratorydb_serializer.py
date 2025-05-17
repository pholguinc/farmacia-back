import serializers
from rest_framework import  serializers
from src.app.modules.backend.infrastructure.laboratory.models.laboratory_model import LaboratoryModel


class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoryModel
        fields = '__all__'