# Generated by Django 3.1.7 on 2021-04-20 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0004_auto_20210411_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='address_no',
            field=models.ForeignKey(blank=True, db_column='Address_No', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realEstate.address'),
        ),
        migrations.AddField(
            model_name='estate',
            name='agent',
            field=models.ForeignKey(blank=True, db_column='Agent_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realEstate.agent'),
        ),
        migrations.AddField(
            model_name='estate',
            name='user',
            field=models.ForeignKey(blank=True, db_column='User_Id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realEstate.users'),
        ),
    ]