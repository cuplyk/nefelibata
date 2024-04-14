from django import template
from markdown2 import markdown

register = template.Library()

@register.filter
def render_markdown(content):
  return markdown(content)

