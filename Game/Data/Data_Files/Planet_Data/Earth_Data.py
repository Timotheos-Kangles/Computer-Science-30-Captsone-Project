

import Game.Utils.Util_Functions

Ores = {
    "Blank Ore": {
        "Sell Price": 0,
        "Rarity": 0,  # 1-5
        "Description": "A blank ore that can be used to create various items."
    }
}

Tools = {
    "Pickaxes": {
        "Wooden Pickaxe": {
            "Buy Price": 10,
            "Description": "A basic wooden pickaxe used for mining soft materials."
        },
        "Iron Pickaxe": {
            "Buy Price": 50,
            "Description": "A sturdy pickaxe capable of mining stronger materials."
        }
    },
    "Drills": {
        "Basic Drill": {
            "Buy Price": 100,
            "Description": "A powered drill for faster mining."
        },
        "Advanced Drill": {
            "Buy Price": 250,
            "Description": "An advanced drill that cuts through rock efficiently."
        }
    },
    "Weapons": {
        "Stone Sword": {
            "Buy Price": 20,
            "Description": "A basic weapon for self-defense."
        },
        "Laser Gun": {
            "Buy Price": 300,
            "Description": "A futuristic weapon with high damage output."
        }
    }
}

Weapons = {
    "melee": {
        'iron sword': {
            'price': 50,
            'description': 'basic iron sword',
            'win_chance': 15 # out of 100 chance for any given event
        },
        'katana': {
            'price': 300,
            'description': 'very powerful sword',
            'win_chance': 25
        }
    },
    "guns": {
        'Pistol': {
            'price': 750,
            'description': 'basic gun. Higher win rate than katana.',
            'win_chance': 30
        },
        'AK-47': {
            'price': 1000,
            'description': 'Powerful automatic rifle. High win rate.',
            'win_chance': 50
        }
    }
}




