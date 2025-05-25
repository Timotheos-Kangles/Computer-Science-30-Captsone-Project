Game/
│
├── Classes/                    # Core data structures (OOP-style classes)
│   ├── Player.cs
│   ├── Planet.cs
│   ├── Inventory.cs
│   ├── Item.cs
│   └── Event.cs
│
├── Data/                       # Game and player data
│   ├── Controllers/            # Scripts that manage loading/saving
│   │   ├── SaveManager.cs
│   │   ├── LoadManager.cs
│   │   └── DataValidator.cs
│   ├── Files/                  # Static or serialized files (txt, JSON, etc.)
│   │   ├── playerdata.txt
│   │   ├── planets.json
│   │   └── items.json
│   └── Schemas/                # (Optional) Definitions for validation/structure
│       └── PlayerSchema.cs
│
├── Modules/                    # Feature-specific systems
│   ├── MapSystem/              # Planet/map selection
│   │   ├── PlanetPicker.cs
│   │   └── MapUIController.cs
│   │
│   ├── ShopSystem/             # Buying and selling
│   │   ├── ShopManager.cs
│   │   ├── PricingLogic.cs
│   │   └── ShopUI.cs
│   │
│   ├── FurnaceSystem/          # Smelting ores
│   │   ├── FurnaceManager.cs
│   │   ├── SmeltQueue.cs
│   │   └── OreDefinitions.cs
│   │
│   ├── InventorySystem/        # Managing items and tools
│   │   ├── InventoryManager.cs
│   │   └── ItemDatabase.cs
│   │
│   └── EventSystem/            # Dynamic world events (pirates, etc.)
│       ├── PirateEvent.cs
│       ├── EventSpawner.cs
│       └── EventDecisionUI.cs
│
├── Utils/                      # Reusable helper functions/utilities
│   ├── Logger.cs
│   ├── RandomUtils.cs
│   └── MathHelpers.cs
│
├── Docs/                       # (Optional) Design docs, diagrams, notes
│   └── README.md
│
└── Main.cs                     # Entry point / game loop
