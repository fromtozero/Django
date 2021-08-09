# Django
使用Django框架创建了一个简单的Blog系统，由于Django自带了一个后台管理器，所以这部分我就没写，只是自己定义了在后台管理页面上
显示的数据。


版本
1.python3.6
2.djang2.1.4

![image](https://user-images.githubusercontent.com/52987463/125735991-ab33e094-d216-48d9-9006-ebd3dc610fb1.png)

# 项目功能描述
    主要分为4大功能模块，用户登录功能，文章评论功能，发布和修改功能，文章分类。登录首页之后可以查看所有文章的信息，但是此时只能查看，不能修改。
用户登录之后可以对文章进行评论，发布新的文章等。

# 项目流程
    首先输入URL,根据不同的url调用后台的views中的方法。views中方法会结合数据库，从数据库中获取数据，将数据传递到前端html
代码中，最终呈现在前端页面上。


# 项目实现
## 1 创建数据库表
    首先建立起对应的数据库表，根据Django的ORM模型，分别建立文章表（评论在对应的文章下面），用户表，文章分类表，标签表。
## 2 业务处理层
    1.用户注册的时候需要对用户名和密码设置一些条件，满足条件时才能创建成功。
    2.用户登录到首页之后看到所有文章信息，创建一个文章首页的办法。
    3.当用户需要对文章进行操作时，必须在用户登录的前提下才能进行，在用户登录时获取用户名和密码与数据库中的信息进行比较，如果登录成功，就用session保存用户的信息，
    如果不一致，则返回登录页面。
    4.用户登录之后可以发布，修改和删除文章。首先根据用户的id找到用户的文章，然后在用户自己的文章中进行操作。点击用户可以显示出该用户的所有文章
    其次，才对选中的文章进行操作。
    5.新建和删除文章也是必须在登陆之后才能进行。操作时需要获取用户的信息，这些信息在用户登录的时候就以及保存在session中。当新建和删除信息后都重定向到用户页面。
