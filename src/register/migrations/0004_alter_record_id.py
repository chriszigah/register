# Generated by Django 4.2.11 on 2024-05-03 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_alter_record_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.UUIDField(default='16375b7915fa43b0a91e5dade5d48d5b', editable=False, primary_key=True, serialize=False),
        ),
    ]