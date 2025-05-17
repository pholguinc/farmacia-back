from src.app.modules.backend.domain.medications.entity.medications_entity import MedicationsEntity
from src.app.modules.backend.domain.medications.repository.medications_repository import MedicationsRepository
from src.app.modules.backend.infrastructure.medications.models.medications_model import MedicationsModel
from src.app.modules.backend.infrastructure.medications.repository.utils.medicationsdb_serializer import \
    MedicationsSerializer
from src.app.modules.backend.shared.utils.pagination.pagination_utils import PaginationUtils
from src.app.modules.backend.shared.utils.response.response_data import AllResponse
from django.utils import timezone
from datetime import datetime



class MedicationsDBRepository(MedicationsRepository):

    def getAll(self, page: int = 1, page_size: int = 10) -> AllResponse[MedicationsEntity]:
        try:
            offset = (page - 1) * page_size
            queryset = MedicationsModel.objects.all()[offset:offset + page_size]
            serializer = MedicationsSerializer(queryset, many=True)

            data = [MedicationsEntity(**MedicationsSerializer(med).to_entity_data())
                    for med in queryset]

            return AllResponse(
                data=data,
                pagination=PaginationUtils(
                    page,
                    page_size,
                    MedicationsModel.objects.count()
                ).to_dict()
            )
        except Exception as e:
            raise e

    def getById(self, id:str) -> MedicationsEntity:
        try:
            print(f"Repository received id: {id}")
            geted = MedicationsModel.objects.filter(id=id).first()
            if not geted: return None
            serializer = MedicationsSerializer(geted)
            entity_data = serializer.to_entity_data()
            return MedicationsEntity(**entity_data)
        except Exception as e:
            raise e

    def create(self, data: MedicationsEntity) -> MedicationsEntity:
        try:
            serializer = MedicationsSerializer(data=data.to_dict())
            serializer.is_valid(raise_exception=True)

            created = MedicationsModel.objects.create(
                **serializer.validated_data,
                created_at=datetime.now()
            )

            return MedicationsEntity(**MedicationsSerializer(created).to_entity_data())
        except Exception as e:
            raise e

    def update(self, id: str, data: MedicationsEntity) -> MedicationsEntity:
        try:
            instance = MedicationsModel.objects.get(id=id)
            serializer = MedicationsSerializer(data=data.to_dict())
            serializer.is_valid(raise_exception=True)

            for field, value in serializer.validated_data.items():
                if field not in ['created_at']:
                    setattr(instance, field, value)

            instance.updated_at = timezone.now()
            instance.save()

            return MedicationsEntity(**MedicationsSerializer(instance).to_entity_data())
        except MedicationsModel.DoesNotExist:
            return None
        except Exception as e:
            raise e
