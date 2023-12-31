# Generated by Django 4.2.3 on 2023-07-29 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='SUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.PositiveIntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
