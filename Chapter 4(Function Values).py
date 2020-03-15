def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('en'),'Glean')
print(greet('es'),'Sally')
print(greet('fr'),'Michael')