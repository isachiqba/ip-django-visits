# -*- coding: utf-8 -*-
from django.db import models

class Visit(models.Model):
    page_visited = models.CharField(max_length=255)
    visitor_ip = models.IPAddressField(blank=True, null=True, db_index=True)
    last_visit = models.DateTimeField(blank=True, null=True)
    visits = models.IntegerField(default=0)
    blocked = models.BooleanField(default=False)

    def __unicode__(self):
        return self.page_visited

    class Meta:
        app_label = "counter"
