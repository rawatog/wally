from django import template

register = template.Library()

@register.filter
def session_liked(anonymous_likes, session_key):
    return anonymous_likes.filter(session_key=session_key).exists()
