from django.template import Library, Node, TemplateSyntaxError, Variable
from django.utils.translation import ugettext as _
from django.db.models import Sum

from visits.models import Visit

register = Library()


class VisitsNode(Node):
    def __init__(self, obj, context_var):
        self.obj = Variable(obj)
        self.context_var = context_var

    def render(self, context):
        obj = self.obj.resolve(context)
        context[self.context_var] = Visit.objects.filter(
                object_model=obj.__class__.__name__,
                object_id=obj.id
        ).aggregate(visits_sum=Sum('visits'))['visits_sum']
        return ''


def do_object_visits(parser, token):
    """
    Retrive the number of visits of a model/slug
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError(
                _('%s tag requires exactly three arguments') % bits[0]
        )
    if bits[2] != 'as':
        raise TemplateSyntaxError(
                _("second argument to %s tag must be 'as'") % bits[0]
        )
    return VisitsNode(bits[1], bits[3])

register.tag('object_visits', do_object_visits)