from abc import abstractmethod, ABC

from src.app.modules.backend.domain.laboratory.entity.laboratory_entity import LaboratoryEntity
from src.app.modules.backend.shared.utils.response.response_data import AllResponse


class LaboratoryRepository(ABC):
    @abstractmethod
    def getAll(self,page:int, page_size:int)-> AllResponse[LaboratoryEntity]:
        pass

    @abstractmethod
    def getById(self, id: str) -> LaboratoryEntity:
        pass
    @abstractmethod
    def create(self,data:LaboratoryEntity) -> LaboratoryEntity:
        pass

    @abstractmethod
    def update(self, id:str, data:LaboratoryEntity) -> LaboratoryEntity:
        pass

