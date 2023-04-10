# ChatGPT Discord Bot

To create a Discord bot that connects to the OpenAI API (GPT-4) and enables chatting with the AI by calling the /gpt command, follow these detailed steps:

## Set up a Discord bot:
a. Go to the Discord Developer Portal at https://discord.com/developers/applications

b. Log in or create a new account if you don't have one.

c. Click `New Application`, give it a name, and click `Create`.

d. Navigate to the `Bot` tab on the left sidebar and click `Add Bot`.

e. Confirm by clicking `Yes, do it!`

f. On the Bot tab, copy the `Token` as you will need it later.

### Enable privileged intents in the Discord Developer Portal:
a. Go to the Discord Developer Portal at https://discord.com/developers/applications

b. Select your bot application.

c. Navigate to the `Bot` tab on the left sidebar.

d. Scroll down to the `Privileged Gateway Intents` section.

e. Enable the `Server Members Intent` and `Message Content Intent` by toggling the switches.

f. Save the changes.

### Set up an OpenAI API key:
a. Go to https://platform.openai.com/signup and sign up for an API key, if you don't have one already.

b. After signing up, you'll be redirected to the API Dashboard.

c. Copy the API key as you will need it later.


### Install required tools and libraries:
a. Install Python 3.7 or higher from https://www.python.org/downloads/

b. Install the discord.py library by running: pip install discord.py

c. Install the openai library by running: pip install openai

Replace YOUR_OPENAI_API_KEY with the API key you obtained in step 2 and YOUR_DISCORD_BOT_TOKEN with the token you obtained in step 1.

## Run the Discord bot:
a. Open a terminal or command prompt.

b. Navigate to the directory where the gpt_discord_bot.py file is located.

c. Run the bot using the command: python gpt_discord_bot.py

d. You should see a message indicating the bot has logged in.

### Add the bot to your Discord server:
a. Go back to the Discord Developer Portal and navigate to the `OAuth2` tab.

b. In the `Scopes` section, check the `bot` box.

c. In the `Bot Permissions` section, check `Send Messages.`

d. Copy the generated URL from the `Scopes` section and paste it into your browser.

e. Choose the server where you want to add the bot and click `Authorize.`

f. Complete the captcha verification.

## Test the bot:
a. Go to your Discord server and find the bot in the user list.

b. In any text channel, type `/gpt <YOUR MESSAGE HERE>`
