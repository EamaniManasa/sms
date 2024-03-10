# Generated by Django 5.0 on 2024-03-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursemodule', '0007_alter_facultycourse_courseid'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultycourse',
            name='facultyname',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='facultycourse',
            name='courseid',
            field=models.IntegerField(unique=True),
        ),
    ]
