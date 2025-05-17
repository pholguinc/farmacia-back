from dataclasses import dataclass
from typing import Generic, TypeVar, List

from src.app.modules.backend.shared.utils.pagination.pagination_entity import PaginationEntity

T= TypeVar('T')

@dataclass
class AllResponse(Generic[T]):
    data: List[T]
    pagination:PaginationEntity