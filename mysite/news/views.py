from django.shortcuts import render
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