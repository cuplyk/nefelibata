"""from django import template
from markdown2 import markdown

register = template.Library()

@register.filter
def render_markdown(content):
  return markdown(content)

"""

from django import template
from django.utils.safestring import mark_safe
import markdown2
register = template.Library()

@register.filter
def render_markdown(content):
    # Convert Markdown content to HTML
    html_content = markdown2.markdown(content)

    # Apply code syntax highlighting with highlight.js
    html_content = '<div class="markdown">' + html_content + '</div>'
    return mark_safe(html_content)