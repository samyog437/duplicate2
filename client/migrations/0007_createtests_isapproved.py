# Generated by Django 3.0.14 on 2022-07-01 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20220701_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='createtests',
            name='isApproved',
            field=models.BooleanField(default=False),
        ),
    ]