# Generated by Django 5.0.4 on 2024-04-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_titles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='titles',
            field=models.CharField(default='Default Title', max_length=300),
        ),
    ]
