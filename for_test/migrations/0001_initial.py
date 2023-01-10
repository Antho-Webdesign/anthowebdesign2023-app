# Generated by Django 4.1.1 on 2022-10-14 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('date_created_on', models.DateTimeField(auto_now_add=True)),
                ('project_status', models.IntegerField(choices=[('en_cours', 'En cours'), ('en_ligne', 'En ligne'), ('cancelled', 'Suspendu')], default=0)),
                ('language_tags', models.CharField(max_length=50)),
                ('project_thumbnail', models.ImageField(default='images/portfolio/project/default.png', upload_to='images/portfolio/project/')),
                ('category', models.CharField(choices=[('web', 'Web'), ('mobile', 'Mobile'), ('desktop', 'Desktop'), ('other', 'Other')], default='web', max_length=50)),
                ('project_url', models.URLField(default='#')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['-date_created_on'],
            },
        ),
    ]
