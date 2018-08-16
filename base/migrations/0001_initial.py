# Generated by Django 2.0.7 on 2018-07-20 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='Description', max_length=150)),
            ],
            options={
                'db_table': 'Country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('date', models.DateField(db_column='Date')),
                ('time', models.DateTimeField(db_column='Time')),
                ('receiptnum', models.CharField(blank=True, db_column='ReceiptNum', max_length=50, null=True)),
                ('type', models.SmallIntegerField(db_column='Type')),
                ('barcode', models.CharField(db_column='Barcode', max_length=50)),
                ('fullprice', models.DecimalField(db_column='FullPrice', decimal_places=3, max_digits=18)),
                ('actualprice', models.DecimalField(db_column='ActualPrice', decimal_places=3, max_digits=18)),
                ('qty', models.IntegerField(db_column='QTY')),
            ],
            options={
                'db_table': 'Sales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Salesfilelog',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('date', models.DateTimeField(db_column='Date')),
                ('file', models.CharField(db_column='File', max_length=250)),
                ('ok', models.SmallIntegerField(db_column='Ok')),
                ('log', models.CharField(blank=True, db_column='Log', max_length=250, null=True)),
            ],
            options={
                'db_table': 'SalesFileLog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Saleslog',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('date', models.DateField(db_column='Date')),
                ('time', models.DateTimeField(db_column='Time')),
                ('log', models.CharField(db_column='Log', max_length=250)),
                ('file', models.CharField(blank=True, db_column='File', max_length=250, null=True)),
                ('ok', models.SmallIntegerField(db_column='Ok')),
            ],
            options={
                'db_table': 'SalesLog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('barcode', models.CharField(db_column='Barcode', max_length=20)),
                ('date', models.DateField(db_column='Date')),
                ('qty', models.IntegerField(db_column='QTY')),
            ],
            options={
                'db_table': 'Stock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stocklog',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('date', models.DateField(db_column='Date')),
                ('time', models.DateTimeField(db_column='Time')),
                ('log', models.CharField(blank=True, db_column='Log', max_length=250, null=True)),
            ],
            options={
                'db_table': 'StockLog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('storecode', models.CharField(db_column='StoreCode', max_length=50)),
                ('description', models.CharField(db_column='Description', max_length=100)),
            ],
            options={
                'db_table': 'Store',
                'managed': False,
            },
        ),
    ]