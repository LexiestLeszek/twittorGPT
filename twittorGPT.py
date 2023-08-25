from gpt4all import GPT4All
import os
from dotenv import load_dotenv
from tweety import Twitter
import random
import time

# setup a cron job:
# 1. type in terminal: "crontab -e"
# 2. type cron jobs in the format "minute hour day month python3 path/to/your_script.py"
#    (each repeated job is a separate line)
# 3. save and exit
# 4. type in terminal: "crontab -l" to check if it's there

# Generate a random delay between 1 and 337 seconds
# random_delay = random.uniform(1, 337)

# Sleep for the random delay before calling the function
# time.sleep(random_delay)

# main variable
app = Twitter("session")

# logging in. If its your first time it will use app.sign_in(), if not - app.connect()
try:
    app.connect()
    
except:
    # Load variables from .env file
    load_dotenv()
    # Access the variables with twitter account username and password
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    app.sign_in(username, password)

topic_list = [
    "AI", 
    "technology",
    "lack technology in legal domain",
    "importance of security and privacy when working with pdfs",
    "struggle of modern employees to work with documents",
    "future of work with documents",
    "random topic"
    ]

style_list = [ 
    "inspirational quote", 
    "controversial take",
    "a useful recommendation"
    ]

topic = random.choice(topic_list)
style = random.choice(style_list)

# prompt format. It includes few variables so that prompts would be different but within certain set of topics
postPrompt = f'Generate a tweet with {style} about {topic}. Only generate the tweet itself and nothing else.'

# load the text model
model = GPT4All(model_name='ggml-model-gpt4all-falcon-q4_0.bin',model_path=r"model/",allow_download=False)

# generate the tweet
tweet = model.generate(postPrompt, max_tokens=50)

# post a tweet
app.create_tweet(tweet)
print("\n",postPrompt,"\n",tweet)
