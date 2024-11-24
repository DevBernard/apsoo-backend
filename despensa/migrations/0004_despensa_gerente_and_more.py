# Generated by Django 5.1.3 on 2024-11-24 12:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despensa', '0003_rename_lista_compra_produtoquantidade_lista_compra'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='despensa',
            name='gerente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='produtoquantidade',
            unique_together={('lista_compra', 'produto')},
        ),
    ]
