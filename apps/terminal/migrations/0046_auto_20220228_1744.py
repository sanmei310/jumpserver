# Generated by Django 3.1.13 on 2022-02-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0045_auto_20220228_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replaystorage',
            name='type',
            field=models.CharField(choices=[('null', 'Null'), ('server', 'Server'), ('s3', 'S3'), ('ceph', 'Ceph'), ('swift', 'Swift'), ('oss', 'OSS'), ('azure', 'Azure'), ('obs', 'OBS'), ('cos', 'COS')], default='server', max_length=16, verbose_name='Type'),
        ),
    ]
