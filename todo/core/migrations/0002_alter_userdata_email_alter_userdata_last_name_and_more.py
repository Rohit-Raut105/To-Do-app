# Generated by Django 5.0.7 on 2024-08-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.CharField(max_length=50, verbose_name='Enter your email.'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Enter your Last  Name.'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='message',
            field=models.CharField(max_length=50, verbose_name='Enter your message.'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Enter your phone.'),
        ),
    ]
