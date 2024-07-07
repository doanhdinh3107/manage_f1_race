# Generated by Django 5.0.4 on 2024-04-25 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0003_racer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='racer',
            options={'ordering': ('-point',)},
        ),
        migrations.AddField(
            model_name='racer',
            name='point',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='racer',
            name='bio',
            field=models.TextField(max_length=3000),
        ),
    ]
