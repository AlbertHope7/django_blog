# Generated by Django 4.1.7 on 2023-02-19 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=250)),
                ("slug", models.SlugField(max_length=250)),
                ("body", models.TextField()),
                ("publish", models.DateTimeField(default=django.utils.timezone.now)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("DF", "Draft"), ("PB", "Publiish")],
                        default="DF",
                        max_length=2,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-publish"],
            },
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(
                fields=["-publish"], name="blog_post_publish_bb7600_idx"
            ),
        ),
    ]
