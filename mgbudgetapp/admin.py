# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Product
from .models import Season
from .models import TrainingType
from .models import AccessRule
from .models import Fighter
from .models import WeekSchema
from .models import Training
from .models import Transaction
from .models import TrainingTemplate


admin.site.register(Product)
admin.site.register(Season)
admin.site.register(TrainingType)
admin.site.register(AccessRule)
admin.site.register(Fighter)
admin.site.register(WeekSchema)
admin.site.register(Training)
admin.site.register(Transaction)
admin.site.register(TrainingTemplate)