# Generated by Django 3.2.10 on 2022-02-25 19:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_tk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tk',
            field=models.CharField(default=uuid.UUID('320822e2-458a-42e1-90d1-075fb93f6288'), max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]