from django import template
from widget_tweaks.templatetags.widget_tweaks import add_class, set_attr

register = template.Library()

@register.filter(name='common_attrs')
def common_attrs(field):
    field = add_class(field, "bg-slate-100 border-none resize-none")
    field = set_attr(field, f"placeholder:{field.label}")
    return field