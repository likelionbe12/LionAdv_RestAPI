from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User

# Create your views here.
@csrf_exempt
def post_list(request):
    """게시글 목록 조회 및 생성 View"""
    if request.method == 'GET':
        posts = Post.objects.all()
        data = []
        for post in posts:
            post_data = {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'author': post.author.username,
                'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'comments_count': post.comments.count(),
            }
            data.append(post_data)
        return JsonResponse({'posts': data}, safe=False)
    elif request.method == "POST":
        # 생성
        data = json.loads(request.body)
        user = User.objects.get(pk=data['author'])
        post = Post.objects.create(title=data['title'], content=data['content'], author=user)
        return JsonResponse({
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'author': post.author.username,
                'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'comments_count': post.comments.count(),
            }, safe=False)
    
def post_detail(request, pk):
    # 해당 pk의 값을 조회해서
    # json으로 리턴
    post = Post.objects.get(pk=pk)
    if request.method == "GET":
        data = {
            'id' : post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author.username,
            'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'comments_count': post.comments.count(),
            #'comments' : comments
        }
        return JsonResponse(data)