from django.db import models
from apps.common.models import BaseModel
# Create your models here.

class NeedsCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='分类名称', max_length=15)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '需求分类'

CATEGORY = (
    (0, '运营需求'),
    (1, '外部需求'),
    (2, '自发需求')
)

NEEDSTATUS = (
    (0, '未启动'),
    (1, '需求沟通中'),
    (2, '进行中'),
    (3, '验收完成'),
    (4, '已撤销')
)

class Needs(BaseModel):
    id = models.AutoField(primary_key=True)
    zentao_id = models.IntegerField(verbose_name='禅道ID', null=True, blank=True)
    name = models.CharField(verbose_name='需求名称', max_length=100)
    url = models.CharField(verbose_name='需求链接', max_length=200)
    proposer = models.CharField(verbose_name='提出方', max_length=10)
    pm = models.CharField(verbose_name='产品经理', max_length=10)
    version = models.CharField(verbose_name='版本', max_length=20, null=True, blank=True)
    status = models.IntegerField(verbose_name='需求状态', choices=NEEDSTATUS, default=0)
    review_time = models.DateTimeField(verbose_name='需求评审时间', blank=True, null=True, default=None)
    description = models.CharField(verbose_name='备注', max_length=300)
    categray = models.IntegerField(verbose_name='所属分类', choices=CATEGORY)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '需求池'
        permissions = (
            ['edit_need', '编辑需求内容'],
        )
