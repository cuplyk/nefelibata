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
    # Convert Markdown content to HTML with fenced code blocks enabled
    html_content = markdown2.markdown(content, extras=["fenced-code-blocks"])

    # Apply syntax highlighting CSS classes
    html_content = apply_syntax_highlighting(html_content)

    return mark_safe(html_content)

def apply_syntax_highlighting(html_content):
    # Define the CSS classes for syntax highlighting
    css_classes = "hljs"  # Assuming you're using highlight.js

    # Wrap <pre><code> blocks with a <div> and apply the CSS classes
    html_content = html_content.replace("<pre><code>", f"<div class=\"{css_classes}\"><pre><code>")
    html_content = html_content.replace("</code></pre>", "</code></pre></div>")

    return html_content