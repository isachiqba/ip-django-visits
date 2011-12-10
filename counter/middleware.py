# -*- coding: utf-8 -*-
import datetime
from counter import settings
from counter.models import Visit
from counter.utils import is_ignored

class CounterMiddleware:
    def process_request(self, request):
        if "HTTP_X_FORWARDED_FOR" in request.META.keys():
            ip_address = request.META["HTTP_X_FORWARDED_FOR"]
            ip_address = ip_address.split(",")[0]
        else:
            ip_address = request.META["REMOTE_ADDR"]

        self.url = request.META["PATH_INFO"]
        request.META["REMOTE_ADDR"] = ip_address

        visitor = self.get_visitor_object(ip_address=ip_address)

        if not visitor and not is_ignored(request):
            print self.url
            visitor = Visit()
            visitor.page_visited = self.url
            visitor.visitor_ip = ip_address
            visitor.last_visit = datetime.datetime.now()
            visitor.visits = 1
            visitor.save()
        elif self.already_visited_and_can_count(visitor):
            visitor.visits += 1
            visitor.last_visit = datetime.datetime.now()
            visitor.save()
        else:
            print 'already visited'

    def can_count(self, visitor):
        delta = datetime.timedelta(days=1)
        return (visitor.last_visit + delta) < datetime.datetime.now()

    def already_visited_and_can_count(self, visitor):
        if type(visitor) != object:
            return False
        print self.can_count(visitor)
        if self.url in visitor.page_visited and self.can_count(visitor):
            return True
        else:
            return False

    def get_visitor_object(self, ip_address):
        visitor = Visit.objects.filter(
            visitor_ip=ip_address,
            page_visited=self.url
        )
        return visitor[0] if len(visitor) else None
