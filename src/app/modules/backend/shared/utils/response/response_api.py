from rest_framework.response import Response
from rest_framework import status
from typing import Dict, Any, Generic, TypeVar, List, TypedDict

T= TypeVar('T')


class ApiResponse(Generic[T]):
    @staticmethod
    def sucess(data=List[T], pagination=None, message="", status=status.HTTP_200_OK)-> Response:
        return Response({
            "data": data,
            "meta":{
                "pagination": pagination,
                "message": message,
                "status": status
            }
        }, status
        )

    @staticmethod
    def error(message="", status=status.HTTP_400_BAD_REQUEST, errors=None) -> Response:
        return Response({
            "data": None,
            "meta": {
                "pagination": None,
                "message": message,
                "status": status
            },
            "errors": errors
        }, status
        )

