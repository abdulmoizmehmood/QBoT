import random, json, torch
from model import NeuralNet
from QW_utils import word_bag, tokenize, get_kitty

from PIL import Image                                                                                

from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "./intents.json")

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open(file_path, 'r') as file:
    intents = json.load(file)

FILE = 'data.pth'
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = 'QBot'

print('Type to chat, Type exit/quit to exit')

while True:
    phrase = input('You: ')
    if phrase == 'exit' or phrase == 'quit':
        break
    
    elif phrase == '!kitty' or phrase == '!cat':
        print(f"{bot_name}: ",get_kitty())
    else:
        phrase = tokenize(phrase)
        X = word_bag(phrase, all_words)
        X = torch.from_numpy(X.reshape(1,X.shape[0]))

        output = model(X)
        _, predicted = torch.max(output, dim = 1)
        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim = 1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.75:
            for i in intents['intents']:
                if tag == i['tag']:
                    print(f"{bot_name}: {random.choice(i['responses'])}")
        else:
            print(f"{bot_name}: I didn't quite get that, can you please rephrase?")