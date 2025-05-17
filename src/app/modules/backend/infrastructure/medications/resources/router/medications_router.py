from django.urls import path

from src.app.modules.backend.infrastructure.medications.resources.service import medications_service

urlpatterns = [
    path('paginate', medications_service.getAll, name="getAll"),
    path('', medications_service.createMedication, name="create"),
    path('<str:id>', medications_service.medications_detail, name="detail"),
    path('update/<str:id>', medications_service.medications_detail, name="update"),
]
