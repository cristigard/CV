# Generated by Django 3.2.10 on 2022-02-25 10:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_tk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tk',
            field=models.CharField(default=uuid.UUID('2da298e1-2b57-47de-9f93-59608a654eeb'), max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
