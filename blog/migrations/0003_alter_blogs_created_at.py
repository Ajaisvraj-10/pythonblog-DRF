# Generated by Django 4.2.3 on 2023-08-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogs_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]
