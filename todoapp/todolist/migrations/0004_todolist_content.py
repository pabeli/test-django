# Generated by Django 3.1.3 on 2020-11-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_remove_todolist_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]