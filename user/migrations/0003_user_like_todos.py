# Generated by Django 4.2.4 on 2023-08-24 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_comment'),
        ('user', '0002_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_todos',
            field=models.ManyToManyField(related_name='like_users', to='todo.todo'),
        ),
    ]
