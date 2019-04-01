from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from pprint import pprint
import sys
import os
from pygleif.gleif import GLEIF, Search
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
def bonds(request):
        folder = os.path.dirname(os.path.abspath(__file__))  # noqa
        sys.path.insert(0, os.path.normpath("%s/.." % folder))  # noqa
        gleif_data = GLEIF('506700GE1G29325QX363')
        gleif_search = Search('986228608')
        pprint((gleif_data.raw))
        print(gleif_data.entity.legal_jurisdiction)
        print(gleif_data.entity.legal_form)
        print(gleif_data.entity.business_register_entity_id)
        print(gleif_search.lei)
        data = [
    {
        gleif_data.entity.legal_jurisdiction,
        gleif_data.entity.legal_form,
        gleif_data.entity.business_register_entity_id,
        gleif_search.lei,
    },  
        
    
]
        
        return Response(data, status=HTTP_200_OK)
