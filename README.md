# QBot - Prototype QWorld ChatBot.  
Simple chatbot for qworld.net. This repository contains both the 1st crude discord chatbot (QBot_Discord Folder) and the more sophisticated and contextual pytorch implementation (QBot Folder).

- The discord version of the QBot, initially deployed (and hosted on cloud) at [repl.it](https://replit.com/@mojume/QBoT), caters mostly to the features and services required for the Open Quantum System Dynamics study group at [QWorld!](https://qworld.net/study-groups/).
- The discord implementation requires an authorization token which is stored in an .env file for security purposes, before implementation you will need to replace the token with your own.
- The discord version also has its own database (QBase) of definitons of different terms used in the literature for the study group. Look at the commands section below to elarn how to add, remove and view terms and definitions to the QBase.
- A demo for the prototype on a dummy discord server can be visited here: https://discord.gg/E7MuBARpxD

- The pytorch verson uses nltk, Feed Forward Neural net with 2 hidden layers and is based on the article (originally with tensor flow) : [https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077](https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077). This pytorch implementation closely follows the videos by [https://www.youtube.com/channel/UCbXgNpp0jedKWcQiULLbDTA](https://www.youtube.com/channel/UCbXgNpp0jedKWcQiULLbDTA).
- The pytorch version has two interfaces, run chat.py to run the chatbot inside the terminal and for the GUI (Tkinter) version run chat_gui.py.

## Installation for Pytorch Implementation

### Install PyTorch and dependencies

To install pytorch suited to your system follow the official guide [official website](https://pytorch.org/).

## QBoT Commands Discord Version

General Commands:
!OQS - for study session details.

QBase Commands:
!qbase  <term>   - definition for a quantum term or concept.
!qb_add <term> : <def>  - add  a definition to the QBase.
!qb_update <term> : <def>  - update definition.
!qb_del <term> -- delete a definition from the database.

Misc Commands:
!hey - greeting.
!kitty - random cat jpegs. (this works for both discord and pytorch implementations)


## QBoT Commands Pytorch Version
A look inside the intents.json file is self explanatory.

Misc Commands: 
!kitty or !cat - gives a link to the random cat pictures from an api.


## Customization of Pytorch Implementation
The file, [intents.json](intents.json) can be modified and running the training model against that file can fulfill the use case. The file itself is straigh forward to navigate. 
