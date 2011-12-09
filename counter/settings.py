from django.conf import settings

# The minimum time between two counted visits (in minutes)
MIN_TIME_BETWEEN_VISITS = getattr(settings, 'MIN_TIME_BETWEEN_VISITS', 24*60)
IGNORE_URLS = getattr(settings, 'IGNORE_URLS', {})
