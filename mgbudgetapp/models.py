# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import fields
import django


class AccessRule(models.Model):
    TRAIN = 'Train'
    BUY_DIRECTLY = 'Buy Directly'
    BUY_CREDITS = 'Buy Credits'
    APPROVE_TRANSACTION = 'Approve Transaction'
    REGISTER_USER = 'Register User'
    REGISTER_PRODUCT = 'Register Product'
    ADMIN = 'Admin'
    JOONAS = 'Joonas'
    PREDEFINED_ACCESS_RULE = (
        (TRAIN, TRAIN),
        (BUY_DIRECTLY, BUY_DIRECTLY),
        (BUY_CREDITS, BUY_CREDITS),
        (APPROVE_TRANSACTION, APPROVE_TRANSACTION),
        (REGISTER_USER, REGISTER_USER),
        (REGISTER_PRODUCT, REGISTER_PRODUCT),
        (ADMIN, ADMIN),
        (JOONAS, JOONAS),
    )
    type = models.CharField(max_length=30, primary_key=True, choices=PREDEFINED_ACCESS_RULE)
    description = models.CharField(max_length=300)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


class TrainingType(models.Model):
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.description


class Fighter(models.Model):
    UNKNOWN = 'Unknown'
    BEGINNER = 'Beginner'
    ADVANCED = 'Advanced'
    COMPETITION = 'Competition'
    COACH = 'Coach'
    FIGHTER_LEVEL = (
        (UNKNOWN, UNKNOWN),
        (BEGINNER, BEGINNER),
        (ADVANCED, ADVANCED),
        (COMPETITION, COMPETITION),
        (COACH, COACH),
    )
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    credits = models.IntegerField(default=0)
    cardSkipperId = models.CharField(max_length=50)
    registered = models.DateField(default=django.utils.timezone.now)
    birthDate = models.DateField()
    level = models.CharField(max_length=100, default=UNKNOWN, choices=FIGHTER_LEVEL)
    accessRules = models.ManyToManyField(AccessRule, verbose_name='Access rules')

    def __str__(self):
        return self.name + " " + self.surname + " (" + str(self.birthDate.year) + ")"


class Product(models.Model):
    price = models.IntegerField()
    currency = models.CharField(max_length=10)
    barcode = models.CharField(max_length=300)
    registered = models.DateTimeField()
    lastEdit = models.DateTimeField()
    ageRestriction = models.IntegerField()
    name = models.CharField(max_length=100, default='Dummy')
    description = models.CharField(max_length=300)
    barcode = models.CharField(max_length=300)

    def __str__(self):
        return self.name + "(" + self.price + " " + self.currency + ")"


class WeekSchema(models.Model):
    name = models.CharField(max_length=300)
    timestamp = models.DateTimeField()
    lastEdit = models.DateTimeField()

    def __str__(self):
        return self.name


class Season(models.Model):
    SEASON = (
        (0, 'WinterSpring'),
        (1, 'Summer'),
        (2, 'AutumnWinter'),
    )
    season = models.CharField(max_length=50)
    year = models.IntegerField()
    begin = models.DateField()
    end = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    weakSchema = models.ForeignKey(WeekSchema, null=True)

    def __str__(self):
        return self.season + "(" + self.year + ")"


class Training(models.Model):
    timestamp = models.DateTimeField()
    details = models.CharField(max_length=300)
    trainingType = models.ForeignKey(TrainingType, on_delete=models.DO_NOTHING, null=False)
    coach = models.ForeignKey(Fighter, on_delete=models.DO_NOTHING, null=False, related_name='coach')
    fighters = models.ManyToManyField(Fighter, related_name='fighter')
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, null=False)

    def __str__(self):
        return self.trainingType + "(" + self.coach + ")"


class Transaction(models.Model):
    price = models.FloatField()
    currency = models.CharField(max_length=10)
    details = models.CharField(max_length=300)
    timestamp = models.DateTimeField()
    approved = models.ForeignKey(Fighter, on_delete=models.DO_NOTHING, null=True, related_name='approved')
    buyer = models.ForeignKey(Fighter, on_delete=models.DO_NOTHING, null=False, related_name='buyer')
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.buyer + " spending " + self.price + " " + self.currency + " on " + self.product


class TrainingTemplate(models.Model):
    day = fields.IntegerRangeField(min_value=0, max_value=6)
    time = fields.IntegerRangeField(min_value=0, max_value=23)
    details = models.CharField(max_length=300)
    trainingType = models.ForeignKey(TrainingType, on_delete=models.DO_NOTHING, null=False)
    weekSchemas = models.ManyToManyField(WeekSchema)

    def __str__(self):
        return self.trainingType + "(" + self.day + ", " + self.time + ")"





