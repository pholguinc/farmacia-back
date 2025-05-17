from typing import Optional

class LaboratoryEntity:
    def __init__(
        self,
        id: Optional[str] = None,
        name: str = '',
        email: str = '',
        ruc: str = '',
        phone: str = '',
        address: str = '',
        status: bool = False
    ) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.ruc = ruc
        self.phone = phone
        self.address = address
        self.status = status

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'ruc': self.ruc,
            'phone': self.phone,
            'address': self.address,
            'status': self.status,
        }