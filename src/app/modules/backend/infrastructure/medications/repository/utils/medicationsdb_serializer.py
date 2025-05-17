from rest_framework import  serializers
from django.utils.timezone import localtime
from src.app.modules.backend.infrastructure.medications.models.medications_model import MedicationsModel

class MedicationsSerializer(serializers.ModelSerializer):
    created_at_local = serializers.SerializerMethodField()
    updated_at_local = serializers.SerializerMethodField()

    class Meta:
        model = MedicationsModel
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def get_created_at_local(self, obj):
        if obj.created_at:
            return localtime(obj.created_at).strftime('%Y-%m-%d %H:%M:%S')
        return None

    def get_updated_at_local(self, obj):
        if obj.updated_at:
            return localtime(obj.updated_at).strftime('%Y-%m-%d %H:%M:%S')
        return None

    def to_entity_data(self):
        """Método adicional para obtener datos limpios para la entidad"""
        data = self.data.copy()
        data.pop('created_at_local', None)
        data.pop('updated_at_local', None)
        return data


