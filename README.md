## 0 . setting

- 가상환경 생성
- 가상환경 활성화
- `.gitignore` 생성 (python window macos django)


## 1.  django설정
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

## 2.CRUD
|CRUD|조작|SQL| 
|------|---|---|
|create|생성|INSERT|
|read|읽기|SELECT|
|update|갱신|UPDATE|
|delete|삭제|DELETE|


- modeling
    - `models.py`에서 함(class 정의)

``` python
class Post(models.Model): # 클래스의 이름을 단수로 작성 (게시물이라는 정의를 나타냄)
    title = models.CharField(max_length=100) # 글자를 저장, max_length를 꼭 작성
    content = models.TextField()
```

- migration(python -> sql로 이주)
```shell
# 번역본 생성
python manage.py makemigration
```

```shell
# DB에 반영
python manage.py migrate
```

