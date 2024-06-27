# Generated by Django 4.2.13 on 2024-06-25 09:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="iha",
            old_name="name",
            new_name="isim",
        ),
        migrations.RenameField(
            model_name="iha",
            old_name="available",
            new_name="mevcut",
        ),
        migrations.RenameField(
            model_name="iha",
            old_name="price_per_hour",
            new_name="saatlik_fiyat",
        ),
        migrations.RenameField(
            model_name="rental",
            old_name="end_time",
            new_name="baslangic_saati",
        ),
        migrations.RenameField(
            model_name="rental",
            old_name="start_time",
            new_name="bitis_saati",
        ),
    ]