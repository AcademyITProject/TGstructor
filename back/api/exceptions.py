from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework.response import Response


class CustomExceptionHandler(APIException):
    status_code = 400
    default_detail = 'Такой элемент не найден.'
    default_code = 'not_found'


def custom_exception_handler(exc, context):
    if isinstance(exc, CustomExceptionHandler):
        return Response({'detal': "Тут нет"}, status=exc.status_code)

    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    return response
