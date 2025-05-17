from .pagination_entity import PaginationEntity
from math import ceil


class PaginationUtils:
    def __init__(self, page: int=1, pageSize: int=0,totalItems: int=0)->None:
        self.page = page
        self.pageSize = pageSize
        self.totalItems = totalItems

    def to_dict(self)-> dict[str, int | float]:
        return {
            'page': self.page,
            'pageSize': self.pageSize,
            'pageCount': (self.totalItems/self.pageSize),
            'totalItems': self.totalItems
        }