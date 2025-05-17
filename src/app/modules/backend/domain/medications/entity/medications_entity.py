from decimal import Decimal
from datetime import datetime
from typing import Optional


class MedicationsEntity:
    def __init__(
        self,
        id: Optional[str] = None,
        code: str = '',
        name: str = '',
        description_simple: str = '',
        description_all: str = '',
        generical_name: str = '',
        purchase_price: Decimal = Decimal('0.0'),
        sale_price: Decimal = Decimal('0.0'),
        utility: Decimal = Decimal('0.0'),
        status: bool = False,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        self.id = id
        self.code = code
        self.name = name
        self.description_simple = description_simple
        self.description_all = description_all
        self.generical_name = generical_name
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.utility = utility
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'description_simple': self.description_simple,
            'description_all': self.description_all,
            'generical_name': self.generical_name,
            'purchase_price': float(self.purchase_price),
            'sale_price': float(self.sale_price),
            'utility': float(self.utility),
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }