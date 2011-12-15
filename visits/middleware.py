# -*- coding: utf-8 -*-
from visits import settings
from visits.models import Visit
from visits.utils import is_ignored

class CounterMiddleware:
    def process_request(self, request):
        if settings.URI_WITH_GET_PARAMS:
            Visit.objects.add_uri_visit(request, request.get_full_path())
        else:
            Visit.objects.add_uri_visit(request, request.path_info)

class BotVisitorMiddleware:
    def process_request(self, request):
        user_agent = request.META.get("HTTP_USER_AGENT", None)
        if user_agent in settings.IGNORE_USER_AGENTS:
            request.META.setdefault("IS_BOT", True)
        request.META.setdefault("IS_BOT", False)
