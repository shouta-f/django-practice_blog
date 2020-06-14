from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    # タイトル
    title = models.CharField(max_length=100)
    # 内容
    content = models.TextField()
    # 著者 on_deleteはユーザーがアカウントを削除した時書いた投稿も消えるようにするもの
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 投稿した日
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
