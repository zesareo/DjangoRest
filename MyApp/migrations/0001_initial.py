# Generated by Django 2.2.5 on 2019-11-24 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('type', models.CharField(max_length=40, verbose_name='Tipo')),
                ('author', models.CharField(max_length=100, verbose_name='Autor')),
                ('creation_date', models.DateField(verbose_name='Fecha alta')),
                ('number_of_pages', models.IntegerField(null=True)),
                ('user', models.CharField(max_length=30)),
                ('borrow_date', models.DateField(verbose_name='Fecha de prestamo')),
            ],
        ),
    ]