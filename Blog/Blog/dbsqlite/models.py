from django.db import models
from django.contrib.auth.models import AbstractUser


class UsersProfile(AbstractUser):
    gender_choice = (
        ('1', "男"),
        ('2', "女")
    )
    mobile = models.CharField('手机号', max_length=11, unique=True)
    gender = models.CharField(
        "性别", choices=gender_choice, default="1", max_length=1)
    avatar = models.ImageField(
        verbose_name="头像", upload_to='users/%Y/%m/%d/', max_length=128)
    age = models.IntegerField('年龄', null=True)

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
        db_table = "user"

    def __str__(self):
        return self.username


# 作者表
class Authors(models.Model):
    username = models.CharField("作者名字", max_length=128)
    age = models.CharField("年龄", max_length=128)

    class Meta:
        verbose_name = "作者表"
        verbose_name_plural = verbose_name
        db_table = "authors"


# 文章表
class ArticleProfile(models.Model):
    title = models.CharField("文章标题", max_length=128)
    content = models.TextField(
        "文章内容", null=True, blank=True, help_text="这是该作者的文章内容")
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)
    hits = models.IntegerField("点击热度",default=0)
    author = models.ForeignKey(
        Authors, related_name="article", verbose_name="作者", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "文章表"
        verbose_name_plural = verbose_name
        db_table = "article"

    def __str__(self):
        return self.title
