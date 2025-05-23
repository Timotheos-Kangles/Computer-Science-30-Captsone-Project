# Import Others
import Game.Utils.Util_Variables as UtilVars

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player
import Game.Data.Data_Files.Planet_Data.Earth_Data as EarthData
import Game.Data.Data_Files.Planet_Data.Mars_Data as MarsData


#  python -m Game.Modules.Shop.Tools_Menu 

def fetch_shop_menu():
    if Player.Data["Planet"] == "Earth":
        planet_tools = EarthData.Tools
        tool_shop_menu("Earth", planet_tools)
    elif Player.Data["Planet"] == "Mars":
        planet_tools = MarsData.Tools
        tool_shop_menu("Mars", planet_tools)

    
def tool_shop_menu(Planet, tools):
    print(f"Welcome to the {Planet} Tool Shop!")
    print("Here are the available tools:")
    print(UtilVars.spacer) 

    for index, category in enumerate(tools.keys(), 1):
        print(f"{index} | {category}")
    print(UtilVars.spacer)
    choice = int(input("Please select a category (1, 2, 3): "))
    
    if choice in range(1, len(tools) + 1):
        selected_category = list(tools.keys())[choice - 1]
        print(f"\nAvailable {selected_category}:")
        for index, tool in enumerate(tools[selected_category].keys(), 1):
            print(f"{index} | {tool}")
        
        tool_choice = int(input("Select a tool: "))
        if tool_choice in range(1, len(tools[selected_category]) + 1):
            selected_tool = list(tools[selected_category].keys())[tool_choice - 1]
            tool_data = tools[selected_category][selected_tool]
            print(UtilVars.spacer)
            print(f"Price: {tool_data['Buy Price']}")
            print(f"Description: {tool_data['Description']}")
            confirm = input("Would you like to buy this tool? (y/n): ").lower()
            if confirm == 'y':
                purchase_tool(selected_tool, tool_data['Buy Price'])
            else:
                print("Purchase cancelled.")
        else:
            print("Invalid tool selection.")
    else:
        print("Invalid category selection.")


def purchase_tool(tool, price):
    if Player.Data["Currency"]>= price:
        Player.Data["Currency"] -= price
        print(f"You have purchased {tool} for {price} money. You now have {Player.Data['Currency']} left.")
        
    elif Player.Data["Currency"] < price:
        print("You do not have enough money to purchase this tool.")
        print(f"You need {price - Player.Data['Currency']} more money.")

fetch_shop_menu()
