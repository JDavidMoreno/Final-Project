# Generated by Django 2.0.3 on 2018-08-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gotrees', '0006_trees_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='trees',
            name='image',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
