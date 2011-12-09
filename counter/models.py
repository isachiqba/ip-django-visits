# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from counter import settings

from datetime import datetime, timedelta


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


class ObjectVisitManager(models.Manager):
    def add_visit(self, request, obj):
        visit = ObjectVisit()
        visit.ip_address = request.META.get('REMOTE_ADDR', '')
        visit.user_agent = request.META.get('HTTP_USER_AGENT', '')
        visit.object_id = obj.id
        visit.object_model = obj.__class__.__name__
        visit.time = datetime.today()
        visit.save()


class ObjectVisit(models.Model):
    """
    A visit.
    """
    ip_address = models.CharField(max_length=20)
    user_agent = models.CharField(max_length=255)
    object_id = models.CharField(max_length=255)
    object_model = models.CharField(max_length=255)
    time = models.DateTimeField()

    objects = ObjectVisitManager()

    def save(self, *args, **kwargs):
        if self.id:
            super(ObjectVisit, self).save(*args, **kwargs)
        else:
            visits = ObjectVisit.objects.filter(ip_address=self.ip_address)
            visits = visits.filter(user_agent=self.user_agent)
            visits = visits.filter(object_model=self.object_model)
            visits = visits.filter(object_id=self.object_id)
            visits = visits.filter(
                    time__gt=self.time - timedelta(
                            minutes=int(settings.MIN_TIME_BETWEEN_VISITS)
                    )
            )
            if len(visits) == 0:
                super(ObjectVisit, self).save(*args, **kwargs)

    class Meta:
        ordering = ('object_model', 'object_id')
        verbose_name = _('visit')
        verbose_name_plural = _('visits')

    def __unicode__(self):
        return u":".join([
                self.object_model,
                str(self.object_id),
                self.ip_address
        ])
