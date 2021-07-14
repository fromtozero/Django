from django.db import models
from django.contrib.auth.models import AbstractUser
#django 2.0以上版本开始用djang.urls
from django.urls import reverse
from django.utils.html import strip_tags
from ckeditor_uploader.fields import RichTextUploadingField

class loguser(AbstractUser):
    #用户信息，继承AbstractUser，可以生成系统用户
    # 增加一个字段来存储用户昵称，在博客相关网页上显示这个名字
    nikename = models.CharField(max_length=32,verbose_name="昵称",blank=True)
    telephone = models.CharField(max_length=11, null=True, unique=True)
    """
    head_img存储用户头像，在数据库表中存储的是文件的相对地址，字段值形式为upload_to的值/filename。
    图片文件的实际地址由settings.py中的MEDIA_ROOT和head_img中的upload_to决定的，地址为/MEDIA_ROOT的值/upload_to的值/filename
    """
    head_img = models.ImageField(upload_to='headimage', blank=True, null=True, verbose_name='头像')  # 头像

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "用户信息表"
        verbose_name_plural = verbose_name

class Category(models.Model):
    #一定要继承 models.Model 类！
    name = models.CharField(max_length=32,verbose_name='分类名')
    #CharField 的 max_length 参数指定其最大长度
    des=models.CharField(max_length=100,verbose_name='备注',null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='分类'
        verbose_name_plural='分类'


class Tag(models.Model):
    name = models.CharField(max_length=32,verbose_name='标签名')
    des = models.CharField(max_length=100, verbose_name='备注', null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='标签'
        verbose_name_plural='标签'

class Blog(models.Model):
    title = models.CharField(max_length=70,verbose_name='文章标题')# 文章标题
    body = RichTextUploadingField(verbose_name='文本内容')# 文章正文，我们使用了 RichTextUploadingField
    created_time = models.DateTimeField(verbose_name='创建时间')# 文章的创建时间,存储时间的字段用 DateTimeField 类型。
    modified_time = models.DateTimeField(verbose_name='修改时间')# 文章的最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    excerpt = models.CharField(max_length=200, blank=True,verbose_name='文章摘要') # 指定blank=True 参数值后就可以允许空值了。
    """category是设置文章分类的字段,与前面定义得到Category是多对一的关系,即多个博客文章可归于一类.
    ForeignKey()中参数Category指定外键关联的数据模型(数据库表)的名称，on_delete = models.CASCADE指明如果在Categroy中删除一条记录，
    与这条记录有关的博客记录也会被删除."""
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类')
    """ tags是标签字段，一篇博客文章可以右多个标签，一个标签下可以有多篇博客文章，因此用ManyToManyFiled类型设置多对多的关联关系
     这里标签tags指定blank=True以允许博客文章没有标签"""
    tags = models.ManyToManyField(Tag, blank=True,verbose_name='标签')
    author = models.ForeignKey(loguser,on_delete=models.CASCADE,verbose_name='作者')
    # 记录博客文章阅读量，起始值设置为0
    # 后面代码为这个字段定义一个increase_views()函数，文章每被查看一次，该字段值加1
    views = models.IntegerField(default=0,verbose_name='查看次数')
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # increase_views把views字段值加1，然后调用save()方法将更改后的值保存到数据库，注意self的用法
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    # 重写save()方法，目的是为了自动提取摘要内容
    def save(self, *args, **kwargs):
        if not self.excerpt:
            # 如果没有填写摘要
            self.excerpt = strip_tags(self.body)[:118]
            super(Blog, self).save(*args, **kwargs)  # 调用父类的 save 方法将数据保存到数据库中
        else:
            super(Blog, self).save(*args, **kwargs)  # 调用父类的 save 方法将数据保存到数据库中
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-created_time']
        verbose_name = '文档管理表'
        verbose_name_plural = '文档管理表'

