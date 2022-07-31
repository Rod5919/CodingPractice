# Generated by Django 3.2.5 on 2022-07-30 05:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0002_auto_20220730_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputmodel',
            name='email',
            field=models.EmailField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inputmodel',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 30, 5, 39, 21, 520561, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='inputmodel',
            name='student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='inputmodel',
            name='subjects',
            field=models.CharField(choices=[(1, 'Math'), (2, 'Physics'), (3, 'Chemistry'), (4, 'Informatics'), (5, 'Speech')], default='Math', max_length=200),
        ),
    ]
