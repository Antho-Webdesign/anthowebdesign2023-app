# Generated by Django 4.1.1 on 2022-10-30 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_test', '0032_alter_project_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_thumbnail',
            field=models.ImageField(default='images/portfolio/project/default.jpg', upload_to='images/portfolio/project/'),
        ),
    ]
