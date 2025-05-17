from rest_framework.views import APIView

from src.app.modules.backend.application.laboratory.usecases.laboratory_usecase import LaboratoryUseCase
from src.app.modules.backend.infrastructure.laboratory.repository.laboratory_repository import LaboratoryDBRepository
from src.app.modules.backend.infrastructure.laboratory.repository.utils.laboratorydb_serializer import \
    LaboratorySerializer
from src.app.modules.backend.infrastructure.medications.repository.utils.medicationsdb_serializer import \
    MedicationsSerializer
from src.app.modules.backend.shared.utils.mesages import ErrorCrudMessage, SuccessCrudMessage
from src.app.modules.backend.shared.utils.response.response_api import ApiResponse
from rest_framework import status

class LaboratoryController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = LaboratoryDBRepository()
        self.usecase = LaboratoryUseCase(self.repository)

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

    def create(self, request) -> ApiResponse:
        try:
            serializer = MedicationsSerializer(data=request.data)
            if serializer.is_valid():
                created_entity = self.usecase.create(serializer.validated_data)
                return ApiResponse.sucess(
                    data=created_entity.to_dict(),
                    message=SuccessCrudMessage.create(),
                    status=status.HTTP_201_CREATED
                )
            return ApiResponse.error(
                message=ErrorCrudMessage.get(),
                status=status.HTTP_400_BAD_REQUEST,
                errors=serializer.errors
            )
        except Exception as e:
            return ApiResponse.error(
                message=ErrorCrudMessage.get(),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                errors=str(e)
            )

    def update(self, request, id) -> ApiResponse:
        try:
            serializer = LaboratorySerializer(data=request.data)
            if serializer.is_valid():
                validated_data = serializer.validated_data

                updated = self.usecase.update(id, validated_data)
                if not updated:
                    return ApiResponse.error(
                        message=ErrorCrudMessage.record_not_found(),
                        status=status.HTTP_404_NOT_FOUND
                    )

                return ApiResponse.sucess(
                    data=updated.to_dict(),
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
