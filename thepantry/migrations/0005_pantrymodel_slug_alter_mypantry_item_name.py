# Generated by Django 4.0.2 on 2022-03-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thepantry', '0004_alter_mypantry_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pantrymodel',
            name='slug',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mypantry',
            name='item_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
