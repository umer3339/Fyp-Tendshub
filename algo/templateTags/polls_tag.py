from  django import template
register = template.Library()

def counter(count):
    count =count + 1
    return count

register.filter('counter',counter)