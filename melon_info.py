from melons import melons

def print_melons(melons):
    """Print each melon with corresponding attribute information."""

    #Capitalizes melon name and assigns variables in dict
    for melon_name, attributes in melons.items():
        print(melon_name.upper())
        
        #Assigns variables in nested dict
        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')
        print('------------------')

print_melons(melons)