Welcome
*******

Django visits is to be used as a counter application for web site.
You have two ways of how to use this app first is to count urls (CounterMiddleware), second count object visits (aka models)

Configuration
*************

You settings file should contain the following settings 

* MIN_TIME_BETWEEN_VISITS: the minimum allowed time between visits for the user to update counter
* IGNORE_URLS: urls to ignore e.g. static urls etc.
* IGNORE_USER_AGENTS: this is used to define what user agents to ignore
* BOTS_USER_AGENTS: this is used to define whether user is real or bot is user by BotVisitorMiddleware
* REQUEST_FIELDS_FOR_HASH: used to generate unique identifier for visitor
* URI_WITH_GET_PARAMS: use get params to identify diferents uris

BOTS_USER_AGENTS by default will have the following values

::

    [
        "Teoma", "alexa", "froogle", "Gigabot", "inktomi", "looksmart", "URL_Spider_SQL", "Firefly",
        "NationalDirectory", "Ask Jeeves", "TECNOSEEK", "InfoSeek", "WebFindBot", "girafabot", "crawler",
        "www.galaxy.com", "Googlebot", "Googlebot/2.1", "Google", "Webmaster", "Scooter", "James Bond",
        "Slurp", "msnbot", "appie", "FAST", "WebBug", "Spade", "ZyBorg", "rabaz", "Baiduspider",
        "Feedfetcher-Google", "TechnoratiSnoop", "Rankivabot", "Mediapartners-Google", "Sogou web spider",
        "WebAlta Crawler", "MJ12bot", "Yandex/", "YaDirectBot", "StackRambler", "DotBot", "dotbot"
    ]

Usage
*****

* Add visits to INSTALLED_APPS

::

	INSTALLED_APPS = (
	    # ...
	    "visits",
	)

* If you want to filter some type of user agents you can define IGNORE_USER_AGENTS in your settings.py

::

    IGNORE_USER_AGENTS = ["Wget/", "curl/"]


* If you want to filter bots from real users then in MIDDLEWARE_CLASSES set 

::

	MIDDLEWARE_CLASSES = (
	    # ...
	    "visits.middleware.BotVisitorMiddleware",
	)

* If you want to count visits automatically per url the you should add CounterMiddleware to MIDDLEWARE_CLASSES

::

	MIDDLEWARE_CLASSES = (
	    # ...
	    "visits.middleware.CounterMiddleware",
	)

* If you want to count visits automatically per url with get params you should add URI_WITH_GET_PARAMS=True to your settings.py

* If you want count url visit manually you can do it the way below

::

	from visits.models import Visits

	def some_object_view(request, pk):
	    Visits.objects.add_uri_visit(request, request.META["PATH_INFO"], APP_LABEL)
	    #...
	    #...

* If you want count visits per object then it's similar to the example above

::

	from visits.models import Visits

	def some_object_view(request, pk):
	    some_obj = get_object_or_404(SOME_MODEL, pk=pk)
	    Visits.objects.add_object_visit(request, obj=some_obj)
	    #...
	    #...

* From inside of a template you can get

 * object visits using

 * url visits using get_visits templatetag

::

	{% get_vists some_object as visits %}
	{% get_vists visits_meta as visits %}

Note: to get uri visits using get_visits templatetag you should add the following to TEMPLATE_CONTEXT_PROCESSORS

::

    TEMPLATE_CONTEXT_PROCESSORS = (
        #...
        "visits.context_processors.request_meta",
    )

Have fun!
