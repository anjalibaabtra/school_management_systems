# Generated by Django 4.1.1 on 2022-10-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrationpanel", "0006_adminuser_joindate_adminuser_salary_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentFee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Email", models.TextField(default="", max_length=100)),
                ("TotalFee", models.IntegerField(default=0, max_length=50)),
                ("PendingFee", models.IntegerField(default=0, max_length=50)),
                ("PaidFee", models.IntegerField(default=0, max_length=50)),
            ],
        ),
    ]