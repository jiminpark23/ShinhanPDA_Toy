# Generated by Django 4.1.5 on 2023-01-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '주문정보 댓글', 'verbose_name_plural': '주문정보 댓글'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
    ]