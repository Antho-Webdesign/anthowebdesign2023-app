# Generated by Django 4.1.1 on 2022-10-30 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_test', '0027_alter_project_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category_name',
            field=models.CharField(blank=True, default='site_web', max_length=50, null=True),
        ),
    ]
