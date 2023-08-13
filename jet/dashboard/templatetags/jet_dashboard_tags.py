from django import template
from jet.dashboard.utils import get_current_dashboard

register = template.Library()
assignment_tag = register.assignment_tag if hasattr(register, 'assignment_tag') else register.simple_tag


@assignment_tag(takes_context=True)
def get_dashboard(context, location):
    dashboard_cls = get_current_dashboard(location)

    app_label = context['request'].resolver_match.kwargs.get('app_label')

    return dashboard_cls(context, app_label=app_label)
