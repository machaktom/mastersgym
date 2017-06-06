# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import fields


class AccessRule(models.Model):
    PREDEFINED_ACCESS_RULE = (
        (0, 'Train'),
        (1, 'BuyDirectly'),
        (2, 'BuyCredits'),
        (3, 'ApproveTransaction'),
        (4, 'RegisterUser'),
        (5, 'RegisterProduct'),
        (6, 'Joonas'),
    )
    type = models.CharField(max_length=30, primary_key=True, choices=PREDEFINED_ACCESS_RULE)
    description = models.CharField(max_length=300)
    added = models.DateTimeField()


class TrainingType(models.Model):
    description = models.CharField(max_length=300)


class Fighter(models.Model):
    UNKNOWN = 'Unknown'
    BEGINNER = 'Beginner'
    ADVANCED = 'Advanced'
    COMPETITION = 'Competition'
    FIGHTER_LEVEL = (
        (UNKNOWN, UNKNOWN),
        (BEGINNER, BEGINNER),
        (ADVANCED, ADVANCED),
        (COMPETITION, COMPETITION),
    )
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    credits = models.IntegerField(default=0)
    cardSkipperId = models.CharField(max_length=50)
    registered = models.DateTimeField()
    birthDate = models.DateTimeField()
    level = models.CharField(max_length=100, default=UNKNOWN, choices=FIGHTER_LEVEL)
    accessRule = models.ManyToManyField(AccessRule)


class Product(models.Model):
    price = models.IntegerField()
    currency = models.CharField(max_length=10)
    barcode = models.CharField(max_length=300)
    registered = models.DateTimeField()
    lastEdit = models.DateTimeField()
    ageRestriction = models.IntegerField()
    description = models.CharField(max_length=300)
    barcode = models.CharField(max_length=300)


class WeekSchema(models.Model):
    name = models.CharField(max_length=300)
    timestamp = models.DateTimeField()
    lastEdit = models.DateTimeField()


class Season(models.Model):
    SEASON = (
        (0, 'WinterSpring'),
        (1, 'Summer'),
        (2, 'AutumnWinter'),
    )
    season = models.CharField(max_length=50)
    year = models.IntegerField()
    begin = models.DateTimeField()
    end = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    weakSchema = models.ManyToManyField(WeekSchema)


class Training(models.Model):
    timestamp = models.DateTimeField()
    details = models.CharField(max_length=300)
    trainingType = models.ForeignKey(TrainingType, on_delete=models.DO_NOTHING, null=False)
    coach = models.ForeignKey(Fighter, on_delete=models.DO_NOTHING, null=False, related_name='coach')
    fighter = models.ManyToManyField(Fighter, related_name='fighter')
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, null=False)


class Transaction(models.Model):
    price = models.IntegerField()
    currency = models.CharField(max_length=10)
    details = models.CharField(max_length=300)
    timestamp = models.DateTimeField()
    approved = models.ForeignKey(Fighter, on_delete=models.DO_NOTHING, null=True, related_name='approved')
    buyer = models.ForeignKey(Fighter, on_delete=models.DO_NOTHING, null=False, related_name='buyer')
    product = models.ManyToManyField(Product)


class TrainingTemplate(models.Model):
    day = fields.IntegerRangeField(min_value=0, max_value=6)
    time = fields.IntegerRangeField(min_value=0, max_value=23)
    details = models.CharField(max_length=300)
    trainingType = models.ForeignKey(TrainingType, on_delete=models.DO_NOTHING, null=False)
    weekSchema = models.ManyToManyField(WeekSchema)





