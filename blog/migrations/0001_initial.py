# Generated by Django 5.0.3 on 2024-03-27 20:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
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
                ("title", models.CharField(max_length=300, unique=True)),
                ("slug", models.SlugField(editable=False, max_length=300, unique=True)),
                ("content", models.TextField()),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Published")], default=0
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="post_images/"),
                ),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("tags", models.ManyToManyField(related_name="posts", to="blog.tag")),
            ],
            options={
                "ordering": ["-created_on"],
            },
        ),
    ]
