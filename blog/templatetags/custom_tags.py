from django import template
from ..models import Blog, Category,Tag
from django.db.models.aggregates import Count

# 实例化了一个template.Library类，是固定写法
register = template.Library()

# 将函数get_new_blogs()装饰为register.simple_tag
# 这样就可以在模板文件中使用{% get_new_blogs %}调用这个函数
@register.simple_tag
def get_new_blogs(num=5):
    # 通过Django orm语句返回最新的5篇文章
    # 通过create_time字段倒叙和切片操作实现
    return Blog.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return Blog.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    #  return Category.objects.all()
    return Category.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)
