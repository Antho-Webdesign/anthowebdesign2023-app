# Generated by Django 4.1.1 on 2022-10-15 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_test', '0015_alter_project_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category_name',
            field=models.CharField(choices=[('site web', 'Site Web'), ('mobile', 'Mobile'), ('desktop', 'Desktop'), ('other', 'Other')], default='Web', max_length=20),
        ),
    ]
