# Generated by Django 4.1.4 on 2022-12-31 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traitimage', '0002_alter_originalimage_channels_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='originalimage',
            name='channels_number',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='originalimage',
            name='height',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='originalimage',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='originalimage',
            name='width',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sketchimage',
            name='channels_number',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sketchimage',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]
