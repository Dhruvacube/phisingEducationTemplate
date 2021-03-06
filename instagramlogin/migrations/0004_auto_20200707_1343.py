# Generated by Django 3.0.7 on 2020-07-07 08:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('instagramlogin', '0003_auto_20200707_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Instagram Login',
            },
        ),
        migrations.DeleteModel(
            name='Instagram_Login',
        ),
    ]
