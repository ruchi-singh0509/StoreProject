# Generated by Django 4.2.5 on 2023-09-20 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Store_Timezone",
            fields=[
                (
                    "store_id",
                    models.CharField(
                        default=None, max_length=50, primary_key=True, serialize=False
                    ),
                ),
                ("timezone", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Store_status",
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
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        max_length=25,
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Time Stamp in UTC"
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="StoreP_app.Store_Timezone",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Store_Business_Hour",
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
                (
                    "dayOfWeek",
                    models.IntegerField(
                        choices=[
                            (0, "Monday"),
                            (1, "Tuesday"),
                            (2, "Wednesday"),
                            (3, "Thursday"),
                            (4, "Friday"),
                            (5, "Saturday"),
                            (6, "Sunday"),
                        ]
                    ),
                ),
                ("start_time", models.TimeField(default="")),
                ("end_time", models.TimeField(default="")),
                (
                    "store",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="StoreP_app.Store_Timezone",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Report",
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
                (
                    "report_status",
                    models.CharField(
                        choices=[("pending", "Pending"), ("completed", "Completed")],
                        max_length=50,
                    ),
                ),
                (
                    "report_url",
                    models.FileField(blank=True, null=True, upload_to="reports"),
                ),
                (
                    "store",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reports",
                        to="StoreP_app.Store_Timezone",
                    ),
                ),
            ],
        ),
    ]
