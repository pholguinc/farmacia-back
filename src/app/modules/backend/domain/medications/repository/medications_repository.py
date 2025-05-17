from abc import ABC, abstractmethod

from src.app.modules.backend.domain.medications.entity.medications_entity import MedicationsEntity
from src.app.modules.backend.shared.utils.response.response_data import AllResponse


class MedicationsRepository(ABC):
    @abstractmethod
    def getAll(self,page:int, page_size:int)-> AllResponse[MedicationsEntity]:
        pass

    @abstractmethod
    def getById(self, id: str) -> MedicationsEntity:
        print(f"Entering getById method in repository with id: {id}")
        pass
    @abstractmethod
    def create(self,data:MedicationsEntity) -> MedicationsEntity:
        pass

    @abstractmethod
    def update(self, id:str, data:MedicationsEntity) -> MedicationsEntity:
        pass

