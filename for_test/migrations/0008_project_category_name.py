# Generated by Django 4.1.1 on 2022-10-15 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_test', '0007_alter_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category_name',
            field=models.CharField(default='Web', max_length=50),
        ),
    ]
