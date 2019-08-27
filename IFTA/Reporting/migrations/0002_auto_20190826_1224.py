# Generated by Django 2.2.4 on 2019-08-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reporting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='location_date',
        ),
        migrations.AlterField(
            model_name='fuel',
            name='date',
            field=models.DateTimeField(help_text='Date (mm/dd/yyyy)'),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='fuel_unit',
            field=models.CharField(choices=[('gal', 'gallons'), ('ltr', 'liters')], default='gal', help_text='Volume measurement (gallons by default)', max_length=10),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='jurisdiction',
            field=models.CharField(choices=[('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DE', 'DE'), ('DC', 'DC'), ('FL', 'FL'), ('GA', 'GA'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', ' OH'), ('OK', ' OK'), ('OR', ' OR'), ('PA', ' PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY'), ('AB', 'AB (Canada)'), ('BC', 'BC (Canada)'), ('MB', 'MB (Canada)'), ('NB', 'NB (Canada)'), ('NL', 'NL (Canada)'), ('NT', 'NT (Canada)'), ('NS', 'NS (Canada)'), ('NU', 'NU (Canada)'), ('ON', 'ON (Canada)'), ('PE', 'PE (Canada)'), ('QC', 'QC (Canada)'), ('SK', 'SK (Canada)'), ('YT', 'YT (Canada)')], help_text='Jurisdiction abbreviation', max_length=10),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='jurisdiction_name',
            field=models.CharField(choices=[('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DE', 'DE'), ('DC', 'DC'), ('FL', 'FL'), ('GA', 'GA'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', ' OH'), ('OK', ' OK'), ('OR', ' OR'), ('PA', ' PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY'), ('AB', 'AB (Canada)'), ('BC', 'BC (Canada)'), ('MB', 'MB (Canada)'), ('NB', 'NB (Canada)'), ('NL', 'NL (Canada)'), ('NT', 'NT (Canada)'), ('NS', 'NS (Canada)'), ('NU', 'NU (Canada)'), ('ON', 'ON (Canada)'), ('PE', 'PE (Canada)'), ('QC', 'QC (Canada)'), ('SK', 'SK (Canada)'), ('YT', 'YT (Canada)')], help_text='Jurisdiction abbreviation', max_length=10),
        ),
        migrations.DeleteModel(
            name='Daily_Locations',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
