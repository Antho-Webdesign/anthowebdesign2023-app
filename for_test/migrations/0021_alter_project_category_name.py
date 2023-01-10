# Generated by Django 4.1.1 on 2022-10-15 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_test', '0020_alter_project_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category_name',
            field=models.CharField(choices=[('site web', 'Site Web'), ('appli_mobile', 'Appli Mobile'), ('appli_desktop', 'Appli Desktop'), ('other', 'Other')], default='site web', max_length=20),
        ),
    ]
