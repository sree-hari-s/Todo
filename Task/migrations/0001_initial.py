# Generated by Django 4.2.4 on 2023-08-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task', models.CharField(max_length=250)),
                ('Is_Completed', models.BooleanField(default=False)),
                ('Created_Date', models.DateField(auto_now_add=True)),
                ('Modified_Date', models.DateField(auto_now=True)),
            ],
        ),
    ]