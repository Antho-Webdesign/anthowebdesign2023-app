# Generated by Django 4.1.5 on 2023-01-31 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='image_cat',
            field=models.ImageField(default='images/default.png', upload_to='images/portfolio/production/category/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_thumbnail',
            field=models.ImageField(default='images/default.png', upload_to='images/portfolio/production/project/'),
        ),
    ]
