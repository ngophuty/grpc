from django_grpc_framework import proto_serializers
from data.models import Infor
from data_proto import data_pb2


class InforProtoSerializer(proto_serializers.ModelProtoSerializer):

    class Meta : 
        model = Infor
        proto_class = data_pb2.Post
        fields = ['name','student_id', 'year','objections']
