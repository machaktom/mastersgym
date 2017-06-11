# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


def index(request):
    return HttpResponse("Index page under development")





def fighter(request, fighter_id):
    return HttpResponse("You're looking at the fighter %s." % fighter_id)

