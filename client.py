from unicodedata import name
from urllib import response
import grpc
from blog_proto import post_pb2, post_pb2_grpc
from data_proto import data_pb2, data_pb2_grpc


# with grpc.insecure_channel('localhost:50051') as channel:
#     stub = post_pb2_grpc.PostControllerStub(channel)
#     print('----- Create -----')
#     response = stub.Create(post_pb2.Post(id='gaaCgdddffggggooo',title='fuck you', content='c2'))
#     print(response)
#     print('----- List -----')
#     for post in stub.List(post_pb2.PostListRequest()):
#         print(post, end='')
#     print('----- Retrieve -----')
#     response = stub.Retrieve(post_pb2.PostRetrieveRequest(id=response.id))
#     print(response, end='')
#     print('----- Update -----')
#     response = stub.Update(post_pb2.Post(id=response.id, title='t2', content='c2'))
#     print(response, end='')
#     print('----- Delete -----')
#     stub.Destroy(post_pb2.Post(id=response.id))

# with grpc.insecure_channel('localhost:50051') as channel:
#     # stub = post_pb2_grpc.PostControllerStub(channel)
#     stub = hello_pb2_grpc.HelloworldStub(channel)
#     respond = stub.Hello(hello_pb2.Send(name = 'hello'))
# #     print("xin chao ban", respond.message)


with grpc.insecure_channel('localhost:50051') as channel:
    stub = data_pb2_grpc.PostControllerStub(channel)
    responsed = stub.Create(data_pb2.Post(name='ngo',student_id= '1814722',year ='shhh'))
    print(responsed)
