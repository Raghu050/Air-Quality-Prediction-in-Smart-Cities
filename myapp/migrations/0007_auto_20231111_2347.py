# Generated by Django 3.2.23 on 2023-11-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Consumer Content'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='consumer_images/', verbose_name='Consumer Image'),
        ),
    ]
