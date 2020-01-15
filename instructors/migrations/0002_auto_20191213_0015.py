# Generated by Django 2.2.7 on 2019-12-12 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.Course'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='slug',
            field=models.SlugField(default=123, unique=True),
            preserve_default=False,
        ),
    ]
