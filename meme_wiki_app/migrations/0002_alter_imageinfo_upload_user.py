# Generated by Django 4.1.6 on 2023-03-15 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meme_wiki_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageinfo',
            name='upload_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='上传用户'),
        ),
    ]
