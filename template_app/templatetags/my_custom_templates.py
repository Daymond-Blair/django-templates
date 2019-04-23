from django import template

register = template.Library()


def cut(value, arg):


'''This cuts out all values of "arg" from the string.

Arguments:
    value {[type]} -- [description]
    arg {[type]} -- [description]
'''
    return value.replace(arg, '')

register.filter('cut', cut)
