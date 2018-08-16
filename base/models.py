# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Country(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Country'

class Sales(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    storeid = models.ForeignKey('Store', models.DO_NOTHING, db_column='StoreID')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    receiptnum = models.CharField(db_column='ReceiptNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=50)  # Field name made lowercase.
    fullprice = models.DecimalField(db_column='FullPrice', max_digits=18, decimal_places=3)  # Field name made lowercase.
    actualprice = models.DecimalField(db_column='ActualPrice', max_digits=18, decimal_places=3)  # Field name made lowercase.
    qty = models.IntegerField(db_column='QTY')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sales'


class Salesfilelog(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    file = models.CharField(db_column='File', max_length=250)  # Field name made lowercase.
    ok = models.SmallIntegerField(db_column='Ok')  # Field name made lowercase.
    log = models.CharField(db_column='Log', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalesFileLog'


class Saleslog(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    storeid = models.ForeignKey('Store', models.DO_NOTHING, db_column='StoreID')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    log = models.CharField(db_column='Log', max_length=250)  # Field name made lowercase.
    file = models.CharField(db_column='File', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ok = models.SmallIntegerField(db_column='Ok')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalesLog'


class Stock(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    storeid = models.ForeignKey('Store', models.DO_NOTHING, db_column='StoreID')  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=20)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    qty = models.IntegerField(db_column='QTY')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stock'

class Vw_Sales(models.Model):
    store_desc = models.CharField(db_column='StoreDesc', max_length=100)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID')  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=10, primary_key=True)  # Field name made lowercase.
    sales_amount = models.DecimalField(db_column='SalesAmount', decimal_places=2, max_digits=20)  # Field name made lowercase.
    sales_qty = models.IntegerField(db_column='SalesQty')  # Field name made lowercase.
    sales_price_avg = models.DecimalField(db_column='SalesPriceAvg', decimal_places=2, max_digits=20)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', decimal_places=2, max_digits=20)  # Field name made lowercase.
    sales_perc = models.DecimalField(db_column='SalesPerc', decimal_places=2, max_digits=20)  # Field name made lowercase.
    GM = models.DecimalField(db_column='GM', decimal_places=2, max_digits=20)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_Sales'

class Stocklog(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    storeid = models.ForeignKey('Store', models.DO_NOTHING, db_column='StoreID')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    log = models.CharField(db_column='Log', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockLog'


class Store(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    storecode = models.CharField(db_column='StoreCode', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100)  # Field name made lowercase.
    countryid = models.ForeignKey(Country, models.DO_NOTHING, db_column='CountryID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Store'
