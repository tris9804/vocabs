from django.db import models

class Notebook(models.Model):
    name = models.CharField('主題', max_length=100)

    def __str__(self):
        return self.name


class Vocabulary(models.Model):
    english = models.CharField('單字', max_length=500)
    chinese = models.CharField('中文', max_length=500)
    notebook = models.ForeignKey(Notebook, models.CASCADE, verbose_name='主題')
    is_vaild = models.BooleanField('已刪除', default=False)

    def __str__(self):
        return self.english


class Test(models.Model):
    test_name = models.CharField('考試主題', max_length=100)
    notebook = models.ForeignKey(Notebook, models.CASCADE, verbose_name='主題')
    score = models.IntegerField('分數')
    duration = models.IntegerField('考試時間')
    test_time = models.DateTimeField('考試日期')

    def __str__(self):
        return self.test_name


class Record(models.Model):
    vocabs = models.ForeignKey(Vocabulary, models.CASCADE, verbose_name='單字')
    is_correct = models.BooleanField('正確', default=False)
    test = models.ForeignKey(Test, models.CASCADE, verbose_name='考試主題')

    

class User(models.Model):
    name = models.CharField('名字', max_length=100)
    mail = models.EmailField('Email', unique=True)

    def __str__(self):
        return self.name


class Star(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name='使用者')
    vocabs = models.ForeignKey(Vocabulary, models.CASCADE, verbose_name='已標註單字')

    


class Sharepermission(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name='共享使用者')
    notebook = models.ForeignKey(Notebook, models.CASCADE, verbose_name='主題')
    permission = models.BooleanField('已共享', default=False)

    def __str__(self):
        return '{} has been shared to {}'.format(self.notebook, self.user)

    
