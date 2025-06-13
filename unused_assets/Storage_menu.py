
storage_shop_options = {
    'Earth': {
        'small_minecart': {
            'stock': 100, # how much ore can be stored before having to sell
            'price': 50,
            'description': 'stores ores'
        },
        'medium_minecart': {
            'stock': 500,
            'price': 150,
            'description': 'stores ores'
        },
        'large_minecart': {
            'stock': 1000,
            'price': 500,
            'description': 'stores ores'
        }
        }
}

def storage_shop_menu(planet):
    print(f"Welcome to the {planet} storage shop. Here you can buy minecarts to store your ores\n")

    for index, key in enumerate(storage_shop_options[planet].keys()):
        print(f'{index+1} | {key}')

    print(f'Please select an item to see details (1 - {len(storage_shop_options[planet].keys())})')

    choice = int(input('Choice: '))

    if choice in range(1, len(storage_shop_options[planet].keys())+1):
        selected_item = list(storage_shop_options[planet].keys())[choice-1]


        print(f'Price: {storage_shop_options[planet][selected_item]["price"]}')
        print(f'Description: {storage_shop_options[planet][selected_item]["description"]}')
        confirm = input('Would you like to purchase this item? (y/n)').lower()
        if confirm == 'y':
            purchase_item(selected_item, storage_shop_options[planet][selected_item]['price'])

def purchase_item(item, price):
    player_money = 1000 # will eventually be Player.mone

    if player_money >= price:
        player_money -= price
        print(f'{item} has been purchased for {price}')
        print(f'You have {player_money} money remaining')
    elif player_money < price:
        print(f'You do not have enough money to purchase this item')
        print(f'You need {item-player_money} more money')