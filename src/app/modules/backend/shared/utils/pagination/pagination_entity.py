class PaginationEntity:
    def __init__(self, page: int=1, pageSize: int=0, pageCount: int=0, totalItems: int=0)->None:
        self.page = page
        self.pageSize = pageSize
        self.pageCount = pageCount
        self.totalItems = totalItems

    def to_dict(self)->dict:
        return {
            "page": self.page,
            "pageSize": self.pageSize,
            "pageCount": self.pageCount,
            "totalItems": self.totalItems
        }
