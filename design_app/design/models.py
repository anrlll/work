from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Model作成のテスト
class Gadget(models.Model):
    title = models.CharField(blank=False, null=False, max_length=50)
    text = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)#作成更新日時自動保存
    updated_datatime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Top(models.Model):
    title = models.CharField(max_length=20, default="1")

    def __str__(self):
        return self.title

#ImageField使用時 : Pillowのインストール
class Photo(models.Model):
    title = models.CharField(max_length=150)
    comment = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos") #画像ファイル
    description = models.TextField(blank=True, null=True)#ガジェットの説明
    user = models.ForeignKey(User, on_delete=models.CASCADE)#Userインスタンスが削除された場合、紐付けされている投稿を削除する挙動を定義
    category = models.ForeignKey(Category, on_delete=models.PROTECT)#作成したcategoryモデルを使用して、フィールド作成
    top = models.ForeignKey(Top, on_delete=models.PROTECT)#メイン画像判定
    order = models.PositiveIntegerField(default=0,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    carousel = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    