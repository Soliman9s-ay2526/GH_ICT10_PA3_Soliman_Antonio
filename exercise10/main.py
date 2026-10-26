# ITS COUNTRY TIME
from pyscript import display, document  # pyright: ignore[reportMissingImports]


def countries_capital(e):
    document.getElementById('output').innerHTML = ''
    user_input = document.getElementById('input1').value.capitalize().strip()

    countries = {'Antoniostan': 'Solimananies',
             'Bosnia and Herzegovnia': 'Sarajevo',
             'Kenya': 'Nairobi'
             }
    country_checker = user_input in countries

    display_message = (f'no {user_input} found.', f'{user_input} is a CAPIIIITALLLLLLLLL')
    display(display_message[country_checker], target= 'output')


