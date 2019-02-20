# Community Slack Bot

Currently the only planned feature is to have a way
for users to easily add themselves to github org

Other options required setting up an intermediate domain/website.
This would have been possible but the setup and hosting would
be more work than this.
IFTTT was not a viable alternative for an intermediate domain.
It's easier to host a small python script on someone's laptop,
or a server, removing the need for a domain.

## Setup
Create a [slack application](https://api.slack.com/) 
and put the bot user oauth token in config/slack.txt. 

Create a [github token](https://github.com/settings/tokens) 
with permissions `write:org` and put that token in config/github.txt

## Running
```
python3 bot.py
```
