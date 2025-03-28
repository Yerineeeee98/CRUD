from django.shortcuts import render, redirect
from .models import Post


# Create your views here.

def index(request):
    posts = Post.objects.all() # Post 모델의 모든 레코드를 가져옴 (QuerySet 형태)
    
    context = {
        'posts': posts,
        
        
    }
    return render(request, 'index.html', context)

def detail(request, id):
    post = Post.objects.get(id = id)
    
    context = {
        'post': post,
        
        
    }
    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title') 
    content = request.GET.get('content')
    
    post = Post()
    post.title = title # 오른쪽 타이틀을 왼쪽 타이틀에 저장
    post.content = content
    post.save() # 장고에서 만든 save함수 
    # 마지막 번호
    
    # return redirect('/index/') # index(전체 게시물)로 가기
    return redirect(f'/posts/{post.id}/') # str이라서 f스트링으로 감싸주기

def delete(request, id):
    post = Post.objects.get(id=id) # 게시물 찾기
    post.delete() # delete 라는 메서드 실행
    
    return redirect('/index/')


def edit(request, id):
    post = Post.objects.get(id=id) 
   
    context = {
       'post': post,
     }
    
    return render(request, 'edit.html', context)
    
def update(request, id):
    # 기존 정보 가져오기
    post = Post.objects.get(id=id)
    
    # 새로운 정보 가져오기
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # 기존정보를 새로운 정보로 바꾸기
    post.title = title
    post.content = content
    post.save()
    
    return redirect(f'/posts/{post.id}')