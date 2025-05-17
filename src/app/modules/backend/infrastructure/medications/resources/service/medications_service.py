from rest_framework.decorators import api_view

from src.app.modules.backend.infrastructure.medications.resources.controller.medications_controller import MedicationsController
from src.app.modules.backend.shared.utils.response.response_api import ApiResponse

controller = MedicationsController()

@api_view(['GET'])
def getAll(request) -> ApiResponse:
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 10))
    return controller.getAll(page=page, page_size=page_size)



@api_view(['POST'])
def createMedication(request) -> ApiResponse:
    return controller.create(request)


@api_view(['GET', 'PUT'])
def medications_detail(request, id) -> ApiResponse:
    if request.method == 'GET':
        return controller.getById(request, id)
    elif request.method == 'PUT':
        return controller.update(request, id)
    return None


