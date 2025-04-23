from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serealizers import PostSerializer


class PostView(APIView):
    def get(self, request):
        post_id = request.GET.get('id')
        print(post_id)
        if not post_id:
            posts = Post.objects.all()
            data = PostSerializer(posts, many=True).data
            return Response(data)
        else:
            try:
                post = Post.objects.get(id=post_id)
                data = PostSerializer(post).data
                return Response(data)
            except Post.DoesNotExist:
                return Response({'error': 'Post not found'}, status=404)

    def post(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"Post Saved Successfully", "code":200})
        else:
             return Response({"Message":"Error fill all fields first", "code":400})
    def put(self,request):
        id = request.data['id']
        post = Post.objects.get(id=id)
        serelizer = PostSerializer(post,data=request.data)
        if serelizer.is_valid():
            serelizer.save()
            return Response({"Message":"Post Updated Successfully", "code":200})
        else:
            return Response({"Message":"Invalid Input", "code":400})
    def patch(self,request):
        try:
            id = request.data['id']
            post = Post.objects.get(id=id)
            serelizer = PostSerializer(post,data=request.data, partial=True)
            if serelizer.is_valid():
                serelizer.save()
                return Response({"Message":"Post Updated Successfully", "code":200})
            else:
                return Response({"Message":"Invalid Input", "code":400})
        except:
             return Response({"Message": "Post not found or no id provided", "code": 404})
    def delete(self,request):
        try:
            id= request.data['id']
            post=Post.objects.get(id=id)
            post.delete()
            return Response({"Message":"Post Deleted Successfully", "code":200})
        except:
            return Response({"Message": "Post not found or no id provided", "code": 404})

