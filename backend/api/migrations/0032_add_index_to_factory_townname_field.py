# Generated by Django 2.2.13 on 2021-02-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_add_index_to_document_display_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='townname',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
    ]