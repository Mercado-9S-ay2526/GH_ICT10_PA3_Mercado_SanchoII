from pyscript import display, document

def countries_capital(e):
    document.getElementById('output').innerHTML = ''
    
  
    user_input = document.getElementById('input1').value.strip().title()

    countries = {
        'Madagascar': 'Antananarivo',
        'Mongolia': 'Ulaanbaatar',
        'Egypt': 'Cairo',
        'Philippines': 'Manila',
        'Denmark': 'Copenhagen',
        'Chile': 'Santiago'
    }

    is_present = user_input in countries

    messages = {
        False: f"Sorry, {user_input} is not in the list.",
        True: f"{user_input} is in the list. Capital: {countries.get(user_input)}"
    }

    display(messages[is_present], target='output')