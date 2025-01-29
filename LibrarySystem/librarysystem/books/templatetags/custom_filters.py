from django import template

register = template.Library()

@register.filter
def get_item(obj, key):
    if obj is not None and hasattr(obj, 'get'):
        return obj.get(key)  
    return None 
