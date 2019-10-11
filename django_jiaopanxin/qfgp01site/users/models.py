from django.db import models
from django.contrib.auth.models import AbstractUser


class UsersProfile(AbstractUser):
    gender_choice = (
        ('1', "男"),
        ('2', "女")
    )
    mobile = models.CharField('手机', max_length=11)
    gender = models.CharField(
        "性别", choices=gender_choice, default="1", max_length=1)
    email = models.CharField("邮箱", max_length=128, unique=True)
    avatar = models.ImageField(
        verbose_name="头像", upload_to='users/%Y/%m/%d/', max_length=128,
        null=True, blank=True)
    age = models.IntegerField('年龄', null=True)


# class BaseProfile(models.Model):
#     os_name = models.CharField('操作系统', max_length=256)
#     machine = models.CharField('系统架构', max_length=256)
#     os_version = models.CharField('版本信息', max_length=256)
#     hostname = models.CharField('主机名', max_length=256)
#     kernel = models.CharField('内核', max_length=256)


# class CpuProfile(models.Model):
#     model_name = models.CharField('型号名字', max_length=128)
#     cpu_type = models.CharField('cpu类型', max_length=128)
#     physical_count = models.CharField('物理CPU数量', max_length=128)
#     physical_cores = models.CharField('单个CPU核心数', max_length=128)
