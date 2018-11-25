# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

selectable_colors = ['black', 'yellow', 'white', 'brown', 'tan', 'orange', 'red', 'green']
selectable_thickness = ['ST/ST', 'ST/SF', 'SF/SF']


class Dropoff(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    dropoffcode = models.TextField(blank=True, null=True)
    external = models.NullBooleanField()
    internal = models.NullBooleanField()
    radiocontrolled = models.NullBooleanField()
    timercontrollvalue = models.CharField(max_length=255, blank=True, null=True)
    timercontrolled = models.NullBooleanField()
    timercontrolledabsolute = models.NullBooleanField()
    timercontrolledrelative = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'DropOff'


class Producttype(models.Model):
    id = models.IntegerField(primary_key=True)
    generation = models.CharField(max_length=255, blank=True, null=True)
    hatantenne = models.NullBooleanField()
    hatbatterie = models.NullBooleanField()
    hatbeacon = models.NullBooleanField()
    hatgurt = models.NullBooleanField()
    hatcottonspacer = models.NullBooleanField()
    hatdropoff = models.NullBooleanField()
    hatexternesensoren = models.NullBooleanField()
    hatgehaeuse = models.NullBooleanField()
    hatlongrangekommunikation = models.NullBooleanField()
    hatradiokommunikation = models.NullBooleanField()
    name = models.CharField(max_length=255, blank=True, null=True)
    veraltet = models.NullBooleanField()
    typ = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProductType'


class Shortrangecomtype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ShortRangeComType'


class Animalspecies(models.Model):
    id = models.IntegerField(primary_key=True)
    hint = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animalspecies'


class Antennas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antennas'


class Batteries(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    hasdropoff = models.NullBooleanField()
    name = models.CharField(max_length=255, blank=True, null=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)
    screwthread = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batteries'


class Beltcolors(models.Model):
    id = models.IntegerField(primary_key=True)
    kommentar = models.TextField(blank=True, null=True)
    extrakosten = models.NullBooleanField()
    name = models.TextField(blank=True, null=True)
    veraltet = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltcolors'


class Beltedges(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    veraltet = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltedges'


class Beltfastener(models.Model):
    id = models.IntegerField(primary_key=True)
    dropoffavailable = models.NullBooleanField()
    value = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltfastener'


class Beltshapes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    veraltet = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltshapes'


class Beltthickness(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltthickness'


class Beltwidths(models.Model):
    id = models.IntegerField(primary_key=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltwidths'


class Comtype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    deprecated = models.NullBooleanField()
    shortname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comtype'


class Housings(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'housings'


class LongrangeContracttype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()
    postpayment = models.NullBooleanField()
    prepayment = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'longrange_contracttype'


class Pcbtype(models.Model):
    id = models.IntegerField(primary_key=True)
    deviceclass = models.TextField(blank=True, null=True)
    majorversion = models.TextField(blank=True, null=True)
    minorversion = models.TextField(blank=True, null=True)
    modelname = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'pcbtype'


class Productionrecordtype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productionrecordtype'


class Staff(models.Model):
    id = models.BigIntegerField(primary_key=True)
    initialies = models.TextField(blank=True, null=True)
    name = models.TextField(max_length=255)

    class Meta:
        managed = False
        db_table = 'staff'
