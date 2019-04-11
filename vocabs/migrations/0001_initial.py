# Generated by Django 2.2 on 2019-04-11 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='主題')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名字')),
                ('mail', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=500, verbose_name='單字')),
                ('chinese', models.CharField(max_length=500, verbose_name='中文')),
                ('is_vaild', models.BooleanField(default=False, verbose_name='已刪除')),
                ('notebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocabs.Notebook', verbose_name='主題')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100, verbose_name='考試主題')),
                ('score', models.IntegerField(verbose_name='分數')),
                ('duration', models.IntegerField(verbose_name='考試時間')),
                ('test_time', models.DateTimeField(verbose_name='考試日期')),
                ('notebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocabs.Notebook', verbose_name='主題')),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocabs.User', verbose_name='使用者')),
                ('vocabs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocabs.Vocabulary', verbose_name='已標註單字')),
            ],
        ),
        migrations.CreateModel(
            name='Sharepermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.BooleanField(default=False, verbose_name='已共享')),
                ('notebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocabs.Notebook', verbose_name='主題')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocabs.User', verbose_name='共享使用者')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False, verbose_name='正確')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocabs.Test', verbose_name='考試主題')),
                ('vocabs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocabs.Vocabulary', verbose_name='單字')),
            ],
        ),
    ]
