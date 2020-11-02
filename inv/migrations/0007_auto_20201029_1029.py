# Generated by Django 3.1.2 on 2020-10-29 13:29

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0006_auto_20201029_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacion',
            name='piso',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='edificio', chained_model_field='edificio', null=True, on_delete=django.db.models.deletion.CASCADE, to='inv.piso'),
        ),
        migrations.AlterField(
            model_name='asignacion',
            name='sala',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='piso', chained_model_field='piso', null=True, on_delete=django.db.models.deletion.CASCADE, to='inv.sala'),
        ),
    ]
