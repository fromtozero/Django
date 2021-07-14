from django.contrib import admin
from .models import Blog,Category,Tag,loguser

# 定义一个自定义数据显示管理模型,需要继承ModelAdmin类
class BlogAdmin (admin.ModelAdmin):
    # 定义了管理后台列表上显示的字段
    list_display=("title","created_time","modified_time","category","author","views",)
# 注册loguser，没有自定义管理模型类，将按Django Admin后台默认页面进行管理
admin.site.register(loguser)
# 注册blog，由第二个参数。将按BlogAdmin定义进行管理
admin.site.register(Blog,BlogAdmin)
# 默认样式管理
admin.site.register(Category)
# 默认样式管理
admin.site.register(Tag)

