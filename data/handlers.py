from data.services import InforService
from data_proto import data_pb2_grpc


def grpc_handlers(server):
    data_pb2_grpc.add_PostControllerServicer_to_server(InforService.as_servicer(), server)