from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharFiled(max_length=100) # 글자를 저장, max_length를 꼭 작성
    content = models.TextFiled()
            