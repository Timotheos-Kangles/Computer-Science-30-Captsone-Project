Tool_Shop_Options = {
    "Earth": {
        "Tool1": {
            "Buy Price": 25,
            "Description": "A blank tool that can be used to create various items."
        },
        "Tool2": {
            "Buy Price": 50,
            "Description": "A blank tool that can be used to create various items."
        },
        "Tool3": {
            "Buy Price": 100,
            "Description": "A blank tool that can be used to create various items."
        }
    }
}
spacer = "-------------------------------------------------"
player_money = 1000

#def fetch_shop_menu():
    #if player.planet == "Earth":
    #    Tool_Shop_Menu("Earth")

    
def Tool_Shop_Menu(Planet):
    print(f"Welcome to the {Planet} Tool Shop!")
    print("Here are the available tools:")
    print(spacer)  
    for index, tool in enumerate(Tool_Shop_Options[Planet].keys()):
        print(f"{index+1} | {tool}")
    print(spacer)
    choice = int(input("Please select a tool to view details(1, 2, 3): "))
    
    if choice in range(1, len(Tool_Shop_Options[Planet]) + 1):
        selected_tool = list(Tool_Shop_Options[Planet].keys())[choice - 1]
        print(spacer)
        print(f"Buy Price: {Tool_Shop_Options[Planet][selected_tool]['Buy Price']}")
        print(f"Description: {Tool_Shop_Options[Planet][selected_tool]['Description']}")
        confirm = input("Would you like to buy this tool? (y/n): ").lower()
        if confirm == 'y':
            purchase_tool(selected_tool, Tool_Shop_Options[Planet][selected_tool]['Buy Price'])
        elif confirm == 'n':
            print("Purchase cancelled.")
            pass
        else:
            print("Purchase cancelled.")

def purchase_tool(tool, price):
    global player_money
    # Condtional Statements
    if player_money >= price:
        print(f"You have purchased {tool} for {price} money.")
        player_money -= price
        print(player_money)
    elif player_money < price:
        print("You do not have enough money to purchase this tool.")
        print(f"You need {price - player_money} more money.")

