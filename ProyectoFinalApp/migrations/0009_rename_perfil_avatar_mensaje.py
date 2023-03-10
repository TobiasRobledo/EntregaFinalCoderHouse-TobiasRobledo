# Generated by Django 4.0.5 on 2022-12-16 23:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ProyectoFinalApp', '0008_remove_perfil_rol'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='perfil',
            new_name='Avatar',
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField(blank=True, max_length=1000, null=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinatario', to=settings.AUTH_USER_MODEL)),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origen', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
