from django.db import models


# Create your models here.


class BookInfo(models.Model):
    """
    书籍信息
    """
    # 数据库字段信息
    name = models.CharField(max_length=254, unique=True, verbose_name='书籍名称')
    pub_date = models.DateField(null=True, verbose_name='发布时间')
    read_count = models.IntegerField(default=0, verbose_name='阅读数量')
    comment_count = models.IntegerField(default=0, verbose_name='评论数量')
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除')

    # 解决在views里调用有补全
    # e.g: BookInfo.objects.all(), 补全.all()方法
    objects = models.Manager()

    # 在admin页面中展示模型名称返回为BookInfo的书籍名称
    def __str__(self):
        return self.name
    
    class Meta:
        # 表名称 (数据库显示)
        db_table = 'book_info'
        # admin页面展示的表名称
        verbose_name = '书籍信息'


class MemberInfo(models.Model):
    """
    成员信息
    """
    # 数据库字段信息
    # gender_choices = (
    #     (0, 'male'),
    #     (1, 'female'),
    # )
    gender_choices = (
        (0, '男'),
        (1, '女'),
    )
    name = models.CharField(max_length=24, verbose_name='成员姓名')
    gender = models.SmallIntegerField(choices=gender_choices, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='作者简介')
    book = models.ForeignKey(to=BookInfo, on_delete=models.CASCADE, verbose_name='关联书籍ID')  # 数据库的字段名称: book_id
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除')

    objects = models.Manager()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'mumber_info'
        verbose_name = '成员信息'
