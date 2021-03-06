# Generated by Django 4.0.3 on 2022-03-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0004_delete_pepperdiseases'),
    ]

    operations = [
        migrations.CreateModel(
            name='PepperDiseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('characteristics', models.TextField()),
                ('causes', models.TextField()),
                ('treatment', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
