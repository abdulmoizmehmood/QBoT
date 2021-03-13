from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "./intents.json")

import json
import numpy as np
from QW_utils import tokenize, stem, word_bag

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from model import NeuralNet

with open(file_path, 'r') as file:
    intents = json.load(file)

all_words = []
tags = []
patntags = []

for i in intents['intents'] :
    tag = i['tag']
    tags.append(tag)
    for p in i['patterns']:
        w = tokenize(p)
        all_words.extend(w) 
        #extend because w gives an array 
        #and we dont want all_words to be an array of array
        patntags.append((w,tag))

ignore_words = ['?','.','!',',']
all_words = sorted(set([stem(w) for w in all_words if w not in ignore_words]))
tags = sorted(set(tags))

xt = []
yt = []

for (pattern_phrase, tag) in patntags:
    bag = word_bag(pattern_phrase, all_words)
    xt.append(bag)
    label = tags.index(tag)
    yt.append(label)

xt = np.array(xt)
yt = np.array(yt)

#Hyper Parameters
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(xt[0])
learning_rate = 0.01
num_epochs = 1000

class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(xt)
        self.x_data = xt
        self.y_data = yt

    # support indexing such that dataset[i] can be used to get i-th sample
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # we can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples

    
dataset = ChatDataset()
train_loader = DataLoader(dataset= dataset, batch_size= batch_size, shuffle = True, num_workers = 0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(input_size, hidden_size, output_size).to(device)

#Loss & optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)

        #frwd
        outputs = model(words)
        loss = criterion(outputs, labels)

        #back and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1)%100 == 0:
        print(f'epoch: {epoch+1}/{num_epochs}, loss= {loss.item():.4f}') 

print(f'final loss, loss= {loss.item():.4f}') 

data = {
    "model_state" : model.state_dict(),
    "input_size" : input_size,
    "output_size" : output_size,
    "hidden_size" : hidden_size,
    "all_words" : all_words,
    "tags" : tags,
}

FILE = 'data.pth'
torch.save(data, FILE)

print(f'Traning complete and file saved to {FILE}')