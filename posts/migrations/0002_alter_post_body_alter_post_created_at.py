# Generated by Django 5.0.1 on 2024-01-31 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(db_index=True, default='Hi', max_length=150, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created DateTime'),
        ),
    ]
