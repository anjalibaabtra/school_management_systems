# Generated by Django 4.1.1 on 2022-10-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "administrationpanel",
            "0004_remove_adminuser_email_remove_adminuser_password_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="adminuser",
            name="DOB",
            field=models.TextField(default="", max_length=100),
        ),
    ]