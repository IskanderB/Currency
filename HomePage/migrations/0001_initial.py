# Generated by Django 2.2.1 on 2019-06-16 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_titel', models.CharField(max_length=200)),
                ('article_par', models.CharField(max_length=200)),
                ('article_currency', models.CharField(max_length=200)),
                ('article_rate', models.CharField(max_length=200)),
                ('article_changes', models.CharField(max_length=200)),
                ('article_percent', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
