
from google import genai

import random

client = genai.Client(api_key="Inerst-API-Key-Here")

item_list = [
    "food",
    "clothing",
    "electronic",
    "furniture",
    "sporting",
    "toy",
    "musical",
    "household",
    "automotive",
    "garden",
    "tool",
    "book",
    "movie",
    "game",
    "plant",
    "animal",
    "mineral",
    "chemical",
    "historical",
    "artistic",
    "construction",
    "medical",
    "office",
    "school",
    "travel",
    "collectible",
    "jewelry",
    "cosmetic",
    "bakery",
    "dairy",
    "produce",
    "meat",
    "beverage",
    "spice",
    "ingredient",
    "component",
    "fixture",
    "appliance",
    "utensil",
    "vessel",
    "garment",
    "accessory",
    "device",
    "implement",
    "specimen",
    "artifact",
    "structure",
    "landmark",
    "currency",
    "weapon",
    "liquid",
    "solid",
    "gas",
    "plasma",
    "fabric",
    "metal",
    "plastic",
    "wood",
    "stone",
    "glass",
    "paper",
    "ceramic",
    "rubber",
    "leather",
    "software",
    "hardware",
    "data",
    "signal",
    "energy",
    "power",
    "nutrient",
    "vitamin",
    "enzyme",
    "hormone",
    "molecule",
    "particle",
    "wave",
    "reaction",
    "process",
    "system",
    "network",
    "circuit",
    "mechanism",
    "function",
    "property",
    "quality",
    "state",
    "condition",
    "event",
    "occurrence",
    "phenomenon",
    "concept",
    "idea",
    "theory",
    "model",
    "design",
    "plan",
    "method",
    "technique",
    "material",
    "object",
    "article",
    "piece",
    "unit",
    "component",
    "element",
    "thing",
    "entity",
    "product",
    "good",
    "commodity",
    "ware",
    "detail",
    "entry",
    "instance",
    "specimen",
    "example",
    "factor",
    "constituent",
    "portion",
]



while(True):

    seed1 = random.random()
    seed2 = random.random()
    seed3 = random.random()
    #print(seed)

    generation_config = {
        "temperature": 0.01
    }

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Generate one example of specific {random.choice(item_list)} with a extremely accurate numerical attribute, make sure that the items are not the same, make sure they are the same units, provide the item and attribute's numerical value with consistent units, then state which attribute is being compared, do not add \"Here's an example\", \"Here's an example following your instructions\" or anything similar, do not use object A object B as examples, for numerical values do not add commas to seperate 100th places, do not add signs infront of numerical values, format the output as: \"object, value, object, value, Attribute\". Output should only be object, numerical value, unit, object, numerical value, unit, attribute",
    )

    print(response.text, end="")

    user_int = input()




#AIzaSyDv7V8-wQHzLuUYkPuSdh0itkkRzPpcdqo











'''
flag = True

score = 0

while(flag):

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Generate two items with a numerical attribute, provide the item and attribute's numerical value with consistent units, then state which attribute is being compared, formatted as: \"Item 1: object, value, Item 2: object, value, Attribute\". Output should only be \"object, numerical value, unit, object, numerical value, unit, attribute\". Generate only one example. Make the options hard",
    )

    response_text = response.text

    #response_text = "Elephant, 6000, kg, Blue Whale, 190000, kg, Mass"

    split_response = response_text.split(',')

    item1 = split_response[0]
    measure1 = split_response[1]
    unit = split_response[2]
    item2 = split_response[3]
    measure2 = split_response[4]
    comparison = split_response[6]

    user_input = input(f"Which is greater, the{comparison} of a/the/an {item1} (1) or{item2} (2)?\n")

    if (user_input == '1' and float(measure1) > float(measure2)):
        print("Right")
        score += 1
    elif (user_input == '2' and float(measure1) < float(measure2)):
        print("Right")
        score += 1
    else:
        print("Wrong")
        flag = False

print("Thank you for playing")
print(f"Final Score: {score}")
'''
