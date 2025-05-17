from django.urls import path

from src.app.modules.backend.infrastructure.laboratory.resources.service import laboratory_service

urlpatterns = [
    path('paginate', laboratory_service.getAll, name="getAll"),
    path('', laboratory_service.create, name="create"),
    path('<str:id>', laboratory_service.laboratory_detail, name="detail"),
    path('update/<str:id>', laboratory_service.laboratory_detail, name="update"),
]