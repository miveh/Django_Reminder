from django import template
import datetime

register = template.Library()


@register.simple_tag
def expired(expired_date_time):
    dt1 = expired_date_time.replace(tzinfo=None)
    dt2 = datetime.datetime.now()
    dt3 = dt1 - dt2
    if dt3.days <= 0:
        result = 'This task has expired!'
    else:
        result = f'{dt3.days} days until expiration'
    return result
