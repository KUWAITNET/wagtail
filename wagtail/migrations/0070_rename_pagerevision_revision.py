# Generated by Django 4.0.3 on 2022-04-26 12:31

from django.conf import settings
from django.db import migrations, models


def disable_sqlite_legacy_alter_table(apps, schema_editor):
    # Fix for https://github.com/wagtail/wagtail/issues/8635
    if schema_editor.connection.vendor == "sqlite":
        schema_editor.execute("PRAGMA legacy_alter_table = OFF")


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("wagtailcore", "0069_log_entry_jsonfield"),
    ]

    atomic = False

    operations = [
        migrations.RunPython(
            disable_sqlite_legacy_alter_table,
            migrations.RunPython.noop,
        ),
        migrations.RenameModel(
            old_name="PageRevision",
            new_name="Revision",
        ),
        migrations.AlterModelOptions(
            name="revision",
            options={"verbose_name": "revision", "verbose_name_plural": "revisions"},
        ),
        migrations.AlterField(
            model_name="revision",
            name="page",
            field=models.CharField(max_length=255, verbose_name="object id"),
        ),
        migrations.RenameField(
            model_name="revision",
            old_name="page",
            new_name="object_id",
        ),
        migrations.AddField(
            model_name="revision",
            name="content_type",
            field=models.ForeignKey(
                # null=True,
                on_delete=models.CASCADE,
                related_name="+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="revision",
            name="base_content_type",
            field=models.ForeignKey(
                # null=True,
                on_delete=models.CASCADE,
                related_name="+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddIndex(
            model_name="revision",
            index=models.Index(
                fields=["content_type", "object_id"],
                name="content_object_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="revision",
            index=models.Index(
                fields=["base_content_type", "object_id"],
                name="base_content_object_idx",
            ),
        ),
    ]
