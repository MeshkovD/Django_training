# Generated by Django 2.2.7 on 2019-12-22 21:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instructors', '0004_auto_20191219_0606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
        migrations.AddField(
            model_name='instructor',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
