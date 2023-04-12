from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

JOB = (
    ('开发', '开发'),
    ('测试', '测试'),
    ('产品', '产品'),
    ('运维', '运维')
)

class Users(AbstractUser):
    real_name = models.CharField(verbose_name='真实姓名', max_length=10)
    job = models.CharField(verbose_name='岗位', choices=JOB, max_length=10)
    def __str__(self):
        return self.real_name
    class Meta:
        verbose_name = '用户表'