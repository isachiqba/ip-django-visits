from counter.settings import *

def is_ignored(request, url=True, user_agent=True):
    if url:
        for ignored_url in settings.IGNORE_URLS:
            if request.META["PATH_INFO"].startswith(ignored_url):
                return True

    if user_agent:
        for ignored_user_agent in settings.IGNORE_USER_AGENTS:
            if ignored_user_agent in request.META["HTTP_USER_AGENT"]:
                return True
