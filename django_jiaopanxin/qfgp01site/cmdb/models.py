from django.db import models
from django.utils import timezone


class IDC(models.Model):
    name = models.CharField(verbose_name='机房', max_length=128)
    city = models.CharField(verbose_name='城市', max_length=32)
    address = models.CharField(verbose_name='地址', max_length=256)

    class Meta:
        verbose_name = '机房表'
        verbose_name_plural = verbose_name
        db_table = "idc"

    def __str__(self):
        return self.name


class Cabinet(models.Model):
    """机柜表"""
    name = models.CharField(verbose_name='机柜编号', max_length=128)
    cab_lever = models.CharField(verbose_name='U 数', max_length=2)  # 机柜总共几层
    idc = models.ForeignKey(IDC, related_name="cabinet",
                            verbose_name='所属机房',  on_delete=models.CASCADE)
    # idc_id

    class Meta:
        verbose_name = '机柜表'
        verbose_name_plural = verbose_name
        db_table = "cabinet"

    def __str__(self):
        return self.name


class SysUsers(models.Model):
    user_type_choice = (
        ('1', "超级管理员"),
        ('2', "sudo 用户"),
        ('3', "普通用户"),
    )
    name = models.CharField("用户名", max_length=16)
    user_type = models.CharField(
        "用户类型", choices=user_type_choice, max_length=1, default='3')

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        db_table = "sys_users"

    def __str__(self):
        return self.name


class Memory(models.Model):
    capacity = models.CharField("内存容量", max_length=100, null=True)
    slot = models.CharField("插槽", max_length=128, null=True)
    model = models.CharField("内存类型", max_length=128, null=True)
    speed = models.CharField("速率", max_length=128, null=True)
    manufacturer = models.CharField("内存厂商", max_length=128, null=True)
    sn = models.CharField("产品序列号", max_length=128, null=True)
    server = models.ForeignKey("Server", verbose_name="服务器",
                               related_name="memory",
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = "内存表"
        verbose_name_plural = verbose_name
        db_table = "memory"

    def __str__(self):
        return f"{self.slot}--{self.capacity}"


class Disk(models.Model):
    slot = models.CharField("插槽号", max_length=100, null=True)
    type = models.CharField("硬盘类型", max_length=128, null=True)
    size = models.CharField("硬盘大小", max_length=128, null=True)
    server = models.ForeignKey("Server", verbose_name="服务器",
                               related_name="disk",
                               on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "硬盘表"
        verbose_name_plural = verbose_name
        db_table = "disk"


class Asset(models.Model):
    """
    资产信息表，所有资产公共信息（交换机，服务器，防火墙等）
    """
    device_type_choices = (
        ('1', '服务器'),
        ('2', '路由器'),
        ('3', '交换机'),
        ('4', '防火墙'),
    )
    device_status_choices = (
        ('1', '上架'),
        ('2', '在线'),
        ('3', '离线'),
        ('4', '下架'),
    )

    device_type_id = models.CharField(
        choices=device_type_choices, max_length=1, default='1')
    device_status_id = models.CharField(
        choices=device_status_choices, max_length=1, default='1')

    cabinet = models.ForeignKey('Cabinet', verbose_name='机柜号',
                                max_length=30, null=True, blank=True, on_delete=models.CASCADE)
    cabinet_order = models.CharField(
        verbose_name='机柜中序号', max_length=30, null=True, blank=True)
    latest_date = models.DateField(
        verbose_name='更新时间', default=timezone.now, null=True, blank=True)
    create_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = "资产表"
        verbose_name_plural = verbose_name
        db_table = 'asset'

    def __str__(self):
        return "{}-{}".format(self.cabinet, self.cabinet_order)


class Server(models.Model):
    asset = models.OneToOneField(Asset, related_name='server', verbose_name="资产",
                                 on_delete=models.CASCADE, null=True, blank=True)
    os_name = models.CharField('操作系统', max_length=520)
    machine = models.CharField('系统架构', max_length=520)
    host_name = models.CharField('主机名', max_length=520)
    os_version = models.CharField('系统版本', max_length=520)
    kernel = models.CharField('内核信息', max_length=520)
    model_name = models.CharField("cpu名称", max_length=128)
    cpu_type = models.CharField("cpu类型", max_length=128)
    physical_count = models.IntegerField("cpu物理颗数",)
    cpu_cores = models.IntegerField("每颗cpu核心数",)
    sysusers = models.ManyToManyField(
        SysUsers,
        verbose_name="用户",
        related_name="servers")

    class Meta:
        verbose_name = '服务器表'
        verbose_name_plural = verbose_name
        db_table = "server"

    def __str__(self):
        return self.host_name
