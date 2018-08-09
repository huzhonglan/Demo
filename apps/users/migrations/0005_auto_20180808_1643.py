# Generated by Django 2.0.7 on 2018-08-08 08:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180808_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='导入时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Role', verbose_name='咨询师'),
        ),
    ]