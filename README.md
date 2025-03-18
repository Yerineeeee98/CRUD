## 0 . setting

- 가상환경 생성 (`python -m venv venv`)
- 가상환경 활성화 
- `.gitignore` 생성 (python window macos django)


##  django설정
- `pip install django`

- 프로젝트 생성
```shell
django-admin startproject crud .
```

- 앱 생성/  앱 등록(settings.py에에)
```shell
django-admin startapp posts # posts들을 관리할 앱 생성
```

- urls.py에 views 불러오기
```shell
from posts import views
```

- posts 앱에 templates 생성

- 서버 실행 (종료는 `ctrl c`)
```shell
python manage.py runserver # 터미널 창에서 ctrl 누르고 링크 클릭
```

# 🧸 CRUD TIL 🧸
|CRUD|조작|SQL| 
|------|---|---|
|create|생성|INSERT|
|read|읽기|SELECT|
|update|갱신|UPDATE|
|delete|삭제|DELETE|

## 1. index 생성

## 2. model 정의
- `models.py` 에서 정의 
- 데이터베이스와 애플리케이션 간의 구조적 연결을 쉽게 만들기 위해서
- 모델을 통해 데이터베이스의 테이블 구조를 정의하고, 이를 바탕으로 애플리케이션에서 데이터를 효율적으로 관리할 수 있게 함
- 모델은 실제 데이터베이스의 테이블을 추상화한 클래스 
- 예를 들어, `Post` 모델을 정의하면 Django는 이를 기반으로 `Post 테이블`을 데이터베이스에 생성
- ```python
     class Post(models.Model): # post라는 클래스를 정의, db `post`의 테이블을 생성하고, `post` 테이블에 저장될 데이터를 다루는 역할을 함
     title = models.CharField(max_length=100) # 글자를 저장, max_length를 꼭 작성
     content = models.TextField() # 모델에서 긴 텍스트를 저장할 수 있는 필드를 정의하는 코드
  ```
    - `title`과 `content`라는 변수를 각각 `CharField`와 `TextField`로 선언 
    - `title`과 `content`는 필드로 각 필드는 db에 저장될 데이터의 종류를 정의 
    - `title 필드`는 문자열 데이터를 저장하며, 최대 100자까지 저장할 수 있음음
    `content 필드`는 긴 텍스트 데이터를 저장하며, 글자 수에 제한이 없음

## 3. migration (python -> sql로 이주)
```shell
    # 번역본 생성
    python manage.py makemigrations
```
```shell
    # DB에 반영
    python manage.py migrate
```


## 4. admin에 모델 등록(`admin.py`)
- create super user
```shell
    python manage.py createsuperuser # test
```
```python
 from django.contrib import admin # Django의 관리자 기능을 가져옴
 from .models import Post # 우리가 만든 Post 모델을 가져옴
 
 admin.site.register(Post)
 # Post 모델을 관리자 페이지에서 관리할 수 있도록 등록
 ```
- Django의 관리자(admin) 페이지에서 Post 모델을 관리할 수 있도록 등록하는 역할

## 5. READ(ALL)기능 구현
- 모든 게시물을 읽는 기능 구현
- `index.html`에
```python
{% for post in posts %}
    <p>{{post}}</p>
    {% endfor %} # posts를 순회하면서 각 post를 <p>태그로 출력
```
- `views.py`에
    - `from .models import Post` 로 Post모델을 가져옴
    - ```python
        posts = Post.objects.all() # Post 모델의 모든 레코드를 가져옴 (QuerySet 형태)
 
        context = {
         'posts': posts,        
        }
 
        return render(request, 'index.html', context)
        ```

## 6. Read(1)기능 구현
- 게시물을 하나씩 읽는 기능 구현
- `urls.py`에 
    - `path('posts/<int:id>/', views.detail)` 
- `views.py`에
    - ```python
        def detail(request, id):
        post = Post.objects.get(id=id)
        # 데이터베이스에서 특정 ID를 가진 Post 객체를 가져오는 역할
    
        context = {
            'post': post,
            }
    
        return render(request, 'detail.html', context)
        ```
- `detail.html`에
    - ```html
        <h1>detail</h1>
        <h3>{{post.title}}</h3> <!-- 제목을 가져옴-->
        <p>{{post.content}}</p> <!-- 내용을 가져옴 -->
        <a href="/index/">home</a> <!-- home을 클릭하면 index링크로 돌아가기-->
      ```

## 7. Create 기능 구현
- 게시물을 생성하는 기능
- `urls.py`
    - `path('posts/new/', views.new),`
       `path('posts/create/', views.create)`
- `views.py`
    - 사용자가 보낸 GET 요청에서 title과 content 값을 가져와서 새로운 Post 객체를 생성하고 데이터베이스에 저장하는 역할
    - ```python
        def create(request):
        title = request.GET.get('title') # title이라는 키의 값을 가져옴
        content = request.GET.get('content') # content라는 키의 값을 가져옴
        post = Post() # 빈 post 객체 생성
        post.title = title # 사용자가 입력한 제목 저장
        # post는 Post모델의 객체, 즉 데이터베이스의 한 행
        # title은 사용자가 입력한 값이 들어가는 변수
        # 사용자가 입력한 제목을 post 객체의 title 필드에 저장하는 과정
        # post 객체이는 사용자가 입력한 title과 content가 저장되어 있음
        post.content = content # 사용자가 입력한 내용 저장장
        post.save() # 데이터베이스에 새로운 게시글 저장장
        
        return redirect(f'/posts/{post.id}/') 
        # redirect()는 웹페이지를 자동으로 다른 url로 이동시키는 함수
        # f-string을 사용해서 url을 동적으로 생성
        # 예를 들어, post.id = 3 -> '/post/3/'로 변환
        # 해당 게시글의 상세 페이지로 이동됨
        ```
-  `new.html`
    ```python
        <form action="/posts/create/">
        <input type="text" name="title">
        <input type="text" name="content">
        <input type="submit">
        </form>

        ```
- `index.html`
    - `<a href="/posts/new/">new</a>`

## 8. Delete기능 구현
- 게시물을 삭제하는 기능
- `urls.py`
    - `    path('posts/<int:id>/delete/', views.delete)`

- `views.py`
    - ``` python
        def delete(request):
        post = Post.objects.get(id=id) # 게시물을 하나씩 
        post.delete() # 삭제
        return redirect('/index/') # 홈으로 돌아가기
      ```

- `detail.html`
    - 상세페이지에 특정게시물을 삭제하는 링크만 추가
    - ```html
        <a href="/posts/{{post.id}}/delete">delete</a>
        </body>
      ```
        

## 9. Update기능 구현
- 게시물을 수정하는 기능 
- `urls.py`
    - `path('posts/<int:id>/edit/', views.edit)` # 수정하고
    - `path('posts/<int:id>/update/', views.update)` # 수정한것을 업데이트하기
- `views.py`
```python
def edit(request, id):
    post = Post.objects.get(id=id)
    
    context = {
        'post': post,
        
    }
    return render(request, 'edit.html', context)
```
```python
def update(request, id):
    # 기존정보 가져오기
    post = Post.objects.get(id=id)
    
    # 새로운 정보 가져오기
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # 기존 정보를 새로운 정보로 바꾸기
    post.title = title
    post.content = content
    post.save()
    
    return redirect(f'/posts/{post.id}/')
```

- `edit.html`
```python
<form action="/posts/{{post.id}}/update/"> 
# 폼은 제출 시 /posts/{post.id}/update/로 이동
    # <input> 태그 (사용자 입력 필드)
    # 기본값으로 post.title을 표시
         <input type="text" value="{{post.title}}" name="title">
         <input type="text" value="{{post.content}}" name="content">
         <input type="submit">
     </form>
```

- `detail.html`
    -   `<a href="/posts/{{post.id}}/edit/">update</a>` update 하이퍼 링크 추가하기