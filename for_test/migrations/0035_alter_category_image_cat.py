# Generated by Django 4.1.1 on 2022-10-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_test', '0034_alter_category_image_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image_cat',
            field=models.ImageField(default='images/portfolio/category/default.jpg', upload_to='images/portfolio/category'),
        ),
    ]
