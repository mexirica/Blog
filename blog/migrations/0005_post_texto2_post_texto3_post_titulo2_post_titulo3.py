# Generated by Django 4.2 on 2023-05-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_foto_alter_post_texto'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='texto2',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='texto3',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='titulo2',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AddField(
            model_name='post',
            name='titulo3',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]
