from django import template # for 1.
from django.template.loader import get_template #for 2.

# 1.
register = template.Library()
def mytemp(value,arg):
    if arg == 'change':
        value = 'SBS'
        return value
    elif arg == 'title':
        value = value.title()
        return value
    else:
        return value
#<h1>{{arr|changeName:'change'}}</h1> [value hobe arr te jaa ase oita(sifat) aar 'change' jaabe arg er moddhe
register.filter('changeName',mytemp)

# 2.
def show_numbers():
    numbers = [1,2,3,4,5]
    return {'numbers' : numbers}
numberTemp = get_template('first_app_idx/number.html')
register.inclusion_tag(numberTemp)(show_numbers)