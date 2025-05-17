from src.app.modules.backend.domain.medications.entity.medications_entity import MedicationsEntity
from src.app.modules.backend.domain.medications.repository.medications_repository import MedicationsRepository
from src.app.modules.backend.shared.utils.response.response_data import AllResponse


class MedicationsUseCase:
    def __init__(self, repository: MedicationsRepository):
        self.repository = repository

    def getAll(self, page: int, page_size: int) -> AllResponse[MedicationsEntity]:
        try:
            listed = self.repository.getAll(page, page_size)
            return listed
        except Exception as e:
            raise e

    def getById(self, id: None) -> MedicationsEntity:
        print(f"Received id controller use case: {id}")
        try:
            print(f"Received id in use case: {id}")
            medication = self.repository.getById(id)
            return medication
        except Exception as e:
            raise e

    def create(self, data:dict) -> MedicationsEntity:
        try:
            medication_entity = MedicationsEntity(**data)
            created =self.repository.create(medication_entity)
            return created
        except Exception as e:
            raise e

    def update(self, id:str, data: dict) -> MedicationsEntity:
        try:
            medication_entity = MedicationsEntity(id=id, **data)
            updated = self.repository.update(id, medication_entity)
            return updated
        except Exception as e:
            raise e



