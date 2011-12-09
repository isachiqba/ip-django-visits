from django.db.models import get_model
from django.template import Library, Node, TemplateSyntaxError, Variable, resolve_variable
from django.utils.translation import ugettext as _

from counter.models import ObjectVisit

register = Library()

class ObjectVisitsNode(Node):
    def __init__(self, obj, context_var):
        self.obj = Variable(obj)
        self.context_var = context_var

    def render(self, context):
        obj = self.obj.resolve(context)
        context[self.context_var] = ObjectVisit.objects.filter(object_model=obj.__class__.__name__, object_id=obj.id).count()
        return ''

def do_object_visits(parser, token):
    """
    Retrive the number of visits of a model/slug
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError(_('%s tag requires exactly three arguments') % bits[0])
    if bits[2] != 'as':
        raise TemplateSyntaxError(_("second argument to %s tag must be 'as'") % bits[0])
    return ObjectVisitsNode(bits[1], bits[3])

register.tag('object_visits', do_object_visits)
