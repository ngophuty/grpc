from django.test import TestCase
import grpc
from django_grpc_framework.test import RPCTestCase
from data_proto import data_pb2, data_pb2_grpc
from blog.models import Post


class PostServiceTest(RPCTestCase):
    def test_create_post(self):
        stub = data_pb2_grpc.PostControllerStub(self.channel)
        response = stub.Create(data_pb2.Post(name='title', student_id='content',year= 's'))
        # self.assertEqual(response.name, 'title')
        # self.assertEqual(response.c, 'content')
        # self.assertEqual(Post.objects.count(), 1)
        print (response)

    # def test_list_posts(self):
    #     Post.objects.create(title='title1', content='content1')
    #     Post.objects.create(title='title2', content='content2')
    #     stub = post_pb2_grpc.PostControllerStub(self.channel)
    #     post_list = list(stub.List(post_pb2.PostListRequest()))
    #     self.assertEqual(len(post_list), 2)