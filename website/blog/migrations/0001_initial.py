# Generated by Django 2.1.5 on 2019-09-27 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitle', models.CharField(max_length=30)),
                ('blogContent', models.TextField()),
                ('blog_createdTime', models.DateTimeField(auto_now_add=True)),
                ('blog_updatedTime', models.DateTimeField(auto_now=True)),
                ('blogAuthor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='blogType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.BlogType'),
        ),
    ]
