from flask import Flask, jsonify, render_template, request
import random
from google import genai

app = Flask(__name__, static_folder='static')

client = genai.Client(api_key="AIzaSyB0S1K3dYz0LCeFyL2aw5c5foI2mxJXs5M")

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
    "vessel",
    "weapon",
    "fabric",
    "material",
    "software",
    "nutrient",
    "process",
    "phenomenon",
    "concept",
    "example",
    "object",
    "product"
]


score = 0
game_data = {}

def generate_game_data():
    global game_data
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Generate one example of specific {random.choice(item_list)} with a extremely accurate numerical attribute, make sure that the items are not the same, make sure they are the same units, provide the item and attribute's numerical value with consistent units, then state which attribute is being compared, do not add \"Here's an example\", \"Here's an example following your instructions\" or anything similar, do not use object A object B as examples, for numerical values do not add commas to seperate 100th places, do not add signs infront of numerical values, format the output as: \"object, value, object, value, Attribute\". Output should only be object, numerical value WITHOUT STATING THE UNIT RIGHT AFTER, unit, object, numerical value, unit, attribute. No answers like '76centimeters' is permitted. The numerical value MUST be separated from the unit by a comma. Furthermore, generate an emoji that would fit for object1, object2 in that order separated by commas and at the end of the list.",
    )
    data = response.text.split(',')
    game_data = {
        "item1": data[0],
        "value1": float(data[1]),
        "unit": data[2],
        "item2": data[3],
        "value2": float(data[4]),
        "attribute": data[5],
        "emoji1": "🔴",
        "emoji2": data[7]
    }

@app.route('/')
def index():
    generate_game_data()
    return render_template('index.html', game_data=game_data, score=score)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    global score
    user_choice = request.json['choice']
    correct = False

    if (user_choice == 'higher' and game_data['value1'] > game_data['value2']) or \
       (user_choice == 'lower' and game_data['value1'] < game_data['value2']):
        score += 1
        correct = True
    else:
        score = 0

    generate_game_data()
    return jsonify({'score': score, 'correct':correct, 'game_data': game_data})

if __name__ == '__main__':
    app.run(debug=False)
