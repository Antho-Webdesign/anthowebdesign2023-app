# Generated by Django 4.1.5 on 2023-02-08 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_project_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='image_cat',
            field=models.ImageField(blank=True, default='images/default.png', null=True, upload_to='images/portfolio/production/category/'),
        ),
    ]
