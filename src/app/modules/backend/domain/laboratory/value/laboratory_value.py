from src.app.modules.backend.domain.laboratory.entity.laboratory_entity import LaboratoryEntity


class LaboratoryValue:
    def __init__(self, value:LaboratoryEntity) -> None:
        entity= LaboratoryEntity(value)
        self.id = entity.id
        self.name = entity.name
        self.email = entity.email
        self.ruc = entity.ruc
        self.phone = entity.phone
        self.address = entity.address
        self.status = entity.status
        pass

    def to_dict(self)->dict:
        return {
            'name': self.name,
            'email': self.email,
            'ruc': self.ruc,
            'phone': self.phone,
            'address': self.address,
            'status': self.status,
        }