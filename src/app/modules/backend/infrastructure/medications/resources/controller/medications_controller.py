from rest_framework.views import APIView
from rest_framework import status
from src.app.modules.backend.application.medications.usecases.medications_usecase import MedicationsUseCase
from src.app.modules.backend.infrastructure.medications.repository.medications_repository import MedicationsDBRepository
from src.app.modules.backend.infrastructure.medications.repository.utils.medicationsdb_serializer import \
    MedicationsSerializer
from src.app.modules.backend.shared.utils.mesages import ErrorCrudMessage, SuccessCrudMessage
from src.app.modules.backend.shared.utils.response.response_api import ApiResponse

class MedicationsController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = MedicationsDBRepository()
        self.usecase = MedicationsUseCase(self.repository)

    def getById(self, request, id=None) -> ApiResponse:
        try:
            data = self.usecase.getById(id)
            if not data: return ApiResponse.error(message=ErrorCrudMessage.record_not_found(), status=status.HTTP_404_NOT_FOUND)
            return ApiResponse.sucess(data=data.to_dict(), message=SuccessCrudMessage.get(), status=status.HTTP_200_OK)
        except Exception as e:
            return ApiResponse.error(message=ErrorCrudMessage.get(), status=status.HTTP_500_INTERNAL_SERVER_ERROR, errors=str(e))


    def getAll(self, page=1, page_size=10) -> ApiResponse:
        try:
            listed = self.usecase.getAll(page, page_size)
            return ApiResponse.sucess(data=[Medication.to_dict() for Medication in listed.data], pagination=listed.pagination, message=SuccessCrudMessage.get(), status=status.HTTP_200_OK)
        except Exception as e:
            return ApiResponse.error(message=ErrorCrudMessage.get(), status=status.HTTP_500_INTERNAL_SERVER_ERROR, errors=str(e))


    def create(self, request)->ApiResponse:
        try:
            serializer = MedicationsSerializer(data=request.data)
            if serializer.is_valid():
                self.usecase.create(serializer.validated_data)
                return ApiResponse.sucess(data=None, message=SuccessCrudMessage.create(), status=status.HTTP_201_CREATED)
            return ApiResponse.error(message=ErrorCrudMessage.get(), status=status.HTTP_400_BAD_REQUEST, errors=serializer.errors)
        except Exception as e:
            return ApiResponse.error(message=ErrorCrudMessage.get(), status=status.HTTP_500_INTERNAL_SERVER_ERROR, errors=str(e))

    def update(self, request, id) -> ApiResponse:
        try:
            serializer = MedicationsSerializer(data=request.data)
            if serializer.is_valid():
                # Pasamos el ID y los datos validados al usecase
                updated_entity = self.usecase.update(id, serializer.validated_data)

                if not updated_entity:
                    return ApiResponse.error(
                        message=ErrorCrudMessage.record_not_found(),
                        status=status.HTTP_404_NOT_FOUND
                    )

                return ApiResponse.sucess(
                    data=updated_entity.to_dict(),
                    message=SuccessCrudMessage.update(),
                    status=status.HTTP_200_OK
                )

            return ApiResponse.error(
                message=ErrorCrudMessage.update(),
                status=status.HTTP_400_BAD_REQUEST,
                errors=serializer.errors
            )
        except Exception as e:
            return ApiResponse.error(
                message=ErrorCrudMessage.update(),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                errors=str(e)
            )
