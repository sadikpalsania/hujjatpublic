# Generated by Django 3.0.3 on 2020-06-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hujjatapp', '0005_auto_20200605_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jeducation',
            name='education_key',
            field=models.AutoField(max_length=6, primary_key=True, serialize=False, unique=True),
        ),
    ]
