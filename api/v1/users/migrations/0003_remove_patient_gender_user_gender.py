# Generated by Django 4.0.2 on 2022-04-10 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_doctor_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='gender',
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
            preserve_default=False,
        ),
    ]
