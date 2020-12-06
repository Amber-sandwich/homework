作业完成过程
#代码的用意
##需要注意的地方
###平时遇到的问题
 
 一、建立仓库
     1、建立远程仓库
     2、获取公钥
     ssh-keygen
     cat ~/.ssh/id_rsa.
     ###之前在建仓库的时候出现了认证问题
        在csdn上查找解决方案：
        git remote add origin d push destination
        git push -u origin master
        git push --set-upstream origin master
     3、克隆仓库到本地
     cd repos/
     git clone git@github.com:Amber-sandwich/homework.git
     cd homework
     ##一定一定要注意路径！！血与泪的教训呜呜呜！！！
     4、建立链接
     git commit -m "" #本地仓库更新
     git push #上传到远程仓库
 
 二、建立应用软件
    1、建立路径
    django-admin startproject mysite
    python manage.py runserver #仓库初始化：出现了！小火箭！
    2、创建app
    python manage.py startapp polls
    ##小技巧：table键防止打错
    3、应用程序开发
    ①关于model
      python manage.py startapp news
      cd news/
      ls
      __init__.py  admin.py  apps.py  migrations/  models.py  tests.py  views.py
      cd ..  #返回上一级
      ##注意路径！！
      
      编辑文件：
      class Reporter(models.Model):
      full_name = models.CharField(max_length=70)

       def __str__(self):
         return self.full_name

      class Article(models.Model):
         pub_date = models.DateField()
         headline = models.CharField(max_length=200)
         content = models.TextField()
         reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

      def __str__(self):
         return self.headline
    
    ②隐藏文件
      gitignore # **.文件类型
    
    ③迁移
      python manage.py migrate
      python manage.py makemigrations #文件中的数据库设置以及应用程序随附的数据库迁移来创建任何必要的数据库表
    ④认证
      runsever后admin
    ⑤进入登陆界面
      admin.site.register(models.Reporter)
      ###建立外键：admin.site.register(models.Reporter) 将reporter添加到后台管理
    ⑥创建urls
    一旦其中一个URL模式匹配，Django就会调用给定的视图，这是一个Python函数。每个视图都传递了一个请求对象（其中包含请求元数据）以及在模式中捕获的值。
      from django.urls import path

      from . import views

      urlpatterns = [
            path('articles/<int:year>/', views.year_archive),
            path('articles/<int:year>/<int:month>/', views.month_archive),
            path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
         ]
      from django.urls import path

      from . import views

      urlpatterns = [
          path('articles/<int:year>/', views.year_archive),  
          #path('articles/<int:year>/<int:month>/', views.month_archive),
          #path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
      ]
   ⑦编辑views
      from django.shortcuts import render

      from .models import Article

      def year_archive(request, year):
         a_list = Article.objects.filter(pub_date__year=year)
         context = {'year': year, 'article_list': a_list}
         return render(request, 'news/year_archive.html', context)
   ⑧编辑html文件
   base.html
   year_achieve.html

三、课堂操作
建立文件上传功能
打开views
from django.shortcuts import render
from .models import Article
from .models import Student, Homework
from django.views.generic.edit import CreateView

'''def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)'''

class HomeworkCreate(CreateView):
    model = Homework
    template_name = 'homework_form.html'
    fields = ['headline','attach','remark', 'student']

创建homework_form html文件
<html>
<body>
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>
</body>
</html>
修改views文件
from django.urls import path

from . import views

urlpatterns = [
    path('hw/create/', views.HomeworkCreate.as_view()),
    #path('articles/<int:year>/',view.year_archive),
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    #path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]

修改models文件
from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=70)
    #age = models.IntegerField()
    class Sex(models.IntegerChoices):
        MALE = 1, '男'
        FEMALE = 2, '女'
        OTHER = 3, '其他'

    sex = models.IntegerField(choices=Sex.choices)

    def __str__(self):
        return self.full_name

class Homework(models.Model):
    commit_date = models.DateField()
    headline = models.CharField(max_length=200)
    attach = models.FileField()
    remark = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
修改admin文件
admin.site.register(models.Student)
添加文件上传功能测试：
PS C:\Users\85425\repos\homework\mysite> .\manage.py makemigrations
PS C:\Users\85425\repos\homework\mysite> python manage.py migrate  
Traceback (most recent call last):
  File "C:\Users\85425\repos\homework\mysite\manage.py", line 22, in <module>
    main()
  File "C:\Users\85425\repos\homework\mysite\manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\management\__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\management\__init__.py", line 395, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\management\base.py", line 330, in run_from_argv
    self.execute(*args, **cmd_options)
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\management\base.py", line 371, in execute
    output = self.handle(*args, **options)
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\management\base.py", line 85, in wrapped
    res = handle_func(*args, **kwargs)
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\management\commands\migrate.py", line 75, in handle
    self.check(databases=[database])
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\management\base.py", line 392, in check
    all_issues = checks.run_checks(
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\checks\registry.py", line 70, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\checks\urls.py", line 13, in check_url_config
    return check_resolver(resolver)
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\checks\urls.py", line 23, in check_resolver
    return check_method()
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\urls\resolvers.py", line 408, in check
    for pattern in self.url_patterns:
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\utils\functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\urls\resolvers.py", line 589, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\utils\functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\urls\resolvers.py", line 582, in urlconf_module
    return import_module(self.urlconf_name)
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 790, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "C:\Users\85425\repos\homework\mysite\mysite\urls.py", line 21, in <module>
    path('news/', include('news.urls')),
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\site-packages\django\urls\conf.py", line 34, in include
    urlconf_module = import_module(urlconf_module)
  File "C:\Users\85425\AppData\Local\Programs\Python\Python39\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 786, in exec_module
  File "<frozen importlib._bootstrap_external>", line 923, in get_code
  File "<frozen importlib._bootstrap_external>", line 853, in source_to_code
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "C:\Users\85425\repos\homework\mysite\news\urls.py", line 1
    from django.urls import path
        ^
SyntaxError: invalid non-printable character U+00A0
PS C:\Users\85425\repos\homework\mysite> git commit -m "添加文件上传功能"
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   mysite/settings.py
        modified:   mysite/urls.py
        modified:   news/models.py
        modified:   news/views.py
        modified:   ../readme.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        news/migrations/0001_initial.py
        news/templates/
        news/urls.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\85425\repos\homework\mysite> git push
Everything up-to-date

###runserver后出现了问题：{
	"resource": "/c:/Users/85425/repos/homework/mysite/news/urls.py",
	"owner": "python",
	"code": "syntax-error",
	"severity": 8,
	"message": "invalid non-printable character U+00A0 (<unknown>, line 1)",
	"source": "pylint",
	"startLineNumber": 1,
	"startColumn": 6,
	"endLineNumber": 1,
	"endColumn": 6
是个异常空格问题！（居然会有这样的问题！震惊！）

###进入create页面出现问题：
  Error during template rendering
  In template C:\Users\85425\repos\homework\mysite\news\templates\homework_form.html, error at line 4

##最后认证网页可上传文件了！！
campaign_kv6xcK5.pptx
campaign_LQXh8Jt.pptx
campaign.pptx
