# Generated by Django 3.0.3 on 2020-03-20 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweeterapp', '0006_remove_user_post_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
    ]
