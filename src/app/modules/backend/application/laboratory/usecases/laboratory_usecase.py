from src.app.modules.backend.domain.laboratory.entity.laboratory_entity import LaboratoryEntity
from src.app.modules.backend.domain.laboratory.repository.laboratory_repository import LaboratoryRepository
from src.app.modules.backend.shared.utils.response.response_data import AllResponse


class LaboratoryUseCase:
    def __init__(self, repository: LaboratoryRepository):
        self.repository = repository

    def getAll(self, page: int, page_size: int) -> AllResponse[LaboratoryEntity]:
        try:
            listed = self.repository.getAll(page, page_size)
            return listed
        except Exception as e:
            raise e

    def getById(self, id: None) -> LaboratoryEntity:
        try:
            medication = self.repository.getById(id)
            return medication
        except Exception as e:
            raise e

    def create(self, data:LaboratoryEntity) -> LaboratoryEntity:
        try:
            value= LaboratoryEntity(**data)
            created = self.repository.create(value.to_dict())
            return created
        except Exception as e:
            raise e

    def update(self, id:str, data: LaboratoryEntity) -> LaboratoryEntity:
        try:
            value = LaboratoryEntity(id=id, **data)
            updated = self.repository.update(id, value.to_dict())
            return updated
        except Exception as e:
            raise e


