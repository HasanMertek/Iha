# Generated by Django 4.2.13 on 2024-06-26 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_customer_list"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer_list",
            name="iha",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="myapp.iha",
            ),
        ),
    ]