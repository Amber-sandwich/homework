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
    关于model
    python manage.py startapp news
    cd news/
    ls
     __init__.py  admin.py  apps.py  migrations/  models.py  tests.py  views.py
    cd ..  #返回上一级
    ##注意路径！！
    

