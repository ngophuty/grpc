from email import message
import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from data.models import Infor
from data.serializers import InforProtoSerializer


class InforService (Service):

    def Create(self,requets,context):
        serializer = InforProtoSerializer(message= requets)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message


