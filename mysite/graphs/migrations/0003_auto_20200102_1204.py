# Generated by Django 2.2.6 on 2020-01-02 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0002_auto_20191117_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColonData',
            fields=[
                ('id', models.TextField(db_column='Id', primary_key=True, serialize=False)),
                ('protein_id', models.TextField(blank=True, db_column='Protein_Id', null=True)),
                ('gene_symbol', models.TextField(blank=True, db_column='Gene_Symbol', null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('number_of_peptides', models.TextField(blank=True, db_column='Number_of_peptides', null=True)),
                ('control1', models.TextField(blank=True, null=True)),
                ('control2', models.TextField(blank=True, null=True)),
                ('control3', models.TextField(blank=True, null=True)),
                ('control4', models.TextField(blank=True, null=True)),
                ('control5', models.TextField(blank=True, null=True)),
                ('kras1', models.TextField(blank=True, db_column='KRAS1', null=True)),
                ('kras2', models.TextField(blank=True, db_column='KRAS2', null=True)),
                ('kras3', models.TextField(blank=True, db_column='KRAS3', null=True)),
                ('kras4', models.TextField(blank=True, db_column='KRAS4', null=True)),
                ('kras5', models.TextField(blank=True, db_column='KRAS5', null=True)),
            ],
            options={
                'db_table': 'colon_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoPlotlyDashDashapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(max_length=110, unique=True)),
                ('base_state', models.TextField()),
                ('creation', models.DateTimeField()),
                ('update', models.DateTimeField()),
                ('save_on_change', models.BooleanField()),
            ],
            options={
                'db_table': 'django_plotly_dash_dashapp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoPlotlyDashStatelessapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(max_length=110, unique=True)),
            ],
            options={
                'db_table': 'django_plotly_dash_statelessapp',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Colon',
        ),
        migrations.DeleteModel(
            name='GraphsGene',
        ),
    ]
