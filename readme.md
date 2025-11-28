# 🏛️Decisioning Council!🏆
**👋Welcome to the Decisioning Council AI Agent Framework!**
This framework has the objective of helping you decide which course of action you should take. It can be used for simple dicisioning like "Should I wear a purple of blue dress for my party?" but also for more involved decisions that involve high stakes.

## 🤔 Why do I Need to Try Out This Framework?
**The Problem**

In our daily lives we need to make a lot of decisions about many different things. What to wear today? What should I eat? Should I go to the gym today given all the other things I need to do? It would be nice if we had some kind of assistant that can help us deal with all those questions and alleviate the stress they cause!

**The Solution**

As part of this Capstone submission, I have created a "Decisioning Council" that consists of 4 council members: red, blue, green, and yellow. Each has a distinct personality. A query is made by the user which provides context + several courses of action that the user wants to pick from. The council then receives that query and gives a score to each action from 0 to 5 (5 being the highest, 0 the lowest). Since each council has a distinct personality, each of them prioritizes different actions. The councillors have access to Google Search if they want to research more information about the situation. Having several councillors with varied personalities should allow to consider the situation from many angles.

The councillors submit their scores to a final Arbiter Agent that counts the scores for each action. It picks the highest scoring action and breaks ties. it also has a safeguard mechanism to prevent it from selecting actions that would cause harm to other humans, since we want our Agents to be ethical.

The framwork then responds to the user with a summary of the analysis as well as which action it recommends to take.

## 🌳 Repository Structure
.
├── .env                        # Environment variables 
├── decisioning_council/        # Main package for your agent logic
│   ├── __init__.py
│   └── agent.py    
|── sub_agents
│   ├── arbiter
│   │   ├── __init__.py
│   │   ├── prompt.py
│   │   └── agent.py 
│   ├── blue_councilor
│   │   ├── __init__.py
│   │   ├── prompt.py
│   │   └── agent.py 
│   ├── green_councilor
│   │   ├── __init__.py
│   │   ├── prompt.py
│   │   └── agent.py 
│   ├── red_councilor
│   │   ├── __init__.py
│   │   ├── prompt.py
│   │   └── agent.py
│   └── yellow_councilor
│       ├── __init__.py
│       ├── prompt.py
│       └── agent.py    
├── tests/                      
│   └──example_queries.txt     # Some sample text queries
└── README.md                   # Project documentation

## ⚙️ Setup
1. Rename .env.template to .env and update the GOOGLE_API_KEY
2. Run pip install google-adk to install the google ADK