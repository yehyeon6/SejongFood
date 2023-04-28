# Generated by Django 4.1 on 2023-04-25 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_sejong_b_delete_sejong"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sejong_A",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField(null=True)),
                ("cate1", models.TextField(null=True)),
                ("cate2", models.TextField(null=True)),
                ("cate3", models.TextField(null=True)),
                ("catemix", models.TextField(null=True)),
                ("dong", models.TextField(null=True)),
                ("lon", models.FloatField(null=True)),
                ("lat", models.FloatField(null=True)),
                ("store_type", models.TextField(null=True)),
                ("star", models.FloatField(null=True)),
                ("review_ori", models.TextField(null=True)),
                ("review_qty", models.FloatField(null=True)),
                ("menu_keyword", models.TextField(null=True)),
                ("address", models.TextField(null=True)),
                ("call", models.TextField(null=True)),
                ("review_okt", models.TextField(null=True)),
                ("positive", models.FloatField(null=True)),
            ],
            options={
                "db_table": "Sejong_A",
                "managed": False,
            },
        ),
        migrations.DeleteModel(
            name="Sejong_b",
        ),
    ]