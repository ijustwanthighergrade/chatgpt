# Generated by Django 4.1.5 on 2023-04-15 03:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0011_travel_price_alter_travel_travel_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="id",
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="member",
            name="name",
            field=models.CharField(max_length=20, verbose_name="姓名"),
        ),
        migrations.AlterField(
            model_name="sign_in",
            name="id",
            field=models.CharField(
                default=0, max_length=10, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="travel",
            name="travel_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 4, 15, 3, 3, 22, 644708, tzinfo=datetime.timezone.utc
                ),
                max_length=20,
                verbose_name="旅程時間",
            ),
        ),
    ]
