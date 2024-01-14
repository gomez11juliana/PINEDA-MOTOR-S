# Generated by Django 4.2.1 on 2023-12-30 02:33

import cliente.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, validators=[cliente.models.letras_validator], verbose_name='Nombres')),
                ('apellido', models.CharField(max_length=45, validators=[cliente.models.letras_validator], verbose_name='Apellidos')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de Ciudadania'), ('NIT', 'NIT'), ('CE', 'Cédula de Extranjería')], max_length=20, verbose_name='Tipo de Documento')),
                ('documento', models.CharField(max_length=20, validators=[cliente.models.numeros_validator, cliente.models.unique_documento_validator], verbose_name='Documento')),
                ('telefono_contacto', models.CharField(max_length=10, validators=[cliente.models.numeros_validator], verbose_name='Teléfono de contacto')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
