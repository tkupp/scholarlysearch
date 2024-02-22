from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework import permissions
from rest_framework import serializers



class Elseiver_api_response(serializers.Serializer):
    results = serializers.IntegerField()
    currentPage = serializers.IntegerField()
    pageSize = serializers.IntegerField()
    
class Api_swagger_parameters():
    
    def query_string_field(description):
        return openapi.Parameter(
            'q',
            openapi.IN_PATH,
            description=description,
            required=True,
            type=openapi.TYPE_string
        )
