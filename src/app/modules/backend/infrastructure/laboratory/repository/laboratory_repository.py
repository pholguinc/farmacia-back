from src.app.modules.backend.domain.laboratory.entity.laboratory_entity import LaboratoryEntity
from src.app.modules.backend.domain.laboratory.repository.laboratory_repository import LaboratoryRepository
from src.app.modules.backend.infrastructure.laboratory.models.laboratory_model import LaboratoryModel
from src.app.modules.backend.infrastructure.laboratory.repository.utils.laboratorydb_serializer import \
    LaboratorySerializer

from src.app.modules.backend.shared.utils.pagination.pagination_utils import PaginationUtils
from src.app.modules.backend.shared.utils.response.response_data import AllResponse


class LaboratoryDBRepository(LaboratoryRepository):

    def getAll(self, page: int=1, page_size: int=10) -> AllResponse[LaboratoryEntity]:
        try:
            offset = (page - 1) * page_size
            data = [LaboratoryEntity(**LaboratorySerializer(Laboratory).data) for Laboratory in LaboratoryModel.objects.all()[offset:offset+page_size]]
            return AllResponse(data=data, pagination=PaginationUtils(page, page_size, LaboratoryModel.objects.count()).to_dict())
        except Exception as e:
            raise e

    def getById(self, id:str) -> LaboratoryEntity:
        try:
            print(f"Repository received id: {id}")
            geted = LaboratoryModel.objects.filter(id=id).first()
            if not geted: return None
            return LaboratoryEntity(**LaboratorySerializer(geted).data)
        except Exception as e:
            raise e

    def create(self, data: LaboratoryEntity) -> LaboratoryEntity:
        try:
            created= LaboratoryModel.objects.create(**LaboratorySerializer(data).data)
            if not created: return None
            return LaboratoryEntity(**LaboratorySerializer(created).data)
        except Exception as e:
            raise e

    def update(self, id: str, data: LaboratoryEntity) -> LaboratoryEntity:
        try:
            instance = LaboratoryModel.objects.get(id=id)
            for field, value in LaboratorySerializer(data).data.items():
                setattr(instance, field, value)
            instance.save()
            return LaboratoryEntity(**LaboratorySerializer(instance).data)
        except LaboratoryModel.DoesNotExist:
            return None
        except Exception as e:
            raise e
