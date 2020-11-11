# redcord-python

# [DEPRECATED AND REPLACED BY [THIS](https://github.com/sethfl/redcord) VERSION, WRITTEN IN RUST]

## what is this?

`redcord-python` is a simple discord bot made with [discord.py](https://github.com/Rapptz/discord.py) that allows you to fetch a random picture from (almost) any subreddit right onto your own discord server!

## how do i use it?

all you have to do is type in `.red` and the name of a subreddit and redcord will fetch a random image for you!

#### for example...

`.red dankmemes`

`.red cursed_images`

`.red me_irl`

## how to use:

### install dependencies
 
 * python3
 * [discord.py](https://github.com/Rapptz/discord.py)
 * [praw](https://github.com/praw-dev/praw)
 
### clone the repo
 
 `git clone https://github.com/sethfl/redcord-python.git`
 
### fill out your reddit api/discord bot info in `app/redcord.py`

get your client id and client secret for reddit from [here](https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example#first-steps), along with your user agent from [here](https://github.com/reddit/reddit/wiki/API). then, make a bot on discord by following [these](https://discordpy.readthedocs.io/en/latest/discord.html) instructions. finally, use all of these keys and codes to to fill out the fields in `redcord.py` 
 
### now run it with
 
`python3 app/redcord.py`
