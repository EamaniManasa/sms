# Generated by Django 5.0 on 2024-02-02 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0014_alter_signin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='Confirm_password',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='signin',
            name='Password',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='signin',
            name='birthdate',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='signin',
            name='id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
