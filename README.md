# What this fork is about

This fork is based on the v0.16.12 version of discord.py and aims to update it for Discord's API version 7, including the new endpoint and Gateway Intents.

# Note for Migration

From version `v0.17.0-beta.4` onwards (ie. all functional versions), the file name for importing was changed from `discord` to `discord_unofficial` to prevent conflict with the updated main `discord.py` library. You will need to change your import code to `import discord_unofficial as discord` instead.
Due to updates in the aiohttp library, this does not support Python 3.4 anymore. The minimal supported version is Python 3.5.3. Although, I have only tested this on Python 3.6 and 3.7, so I do not have 100% proof if this will work with Python 3.5.3. Updating to support to Python 3.8 may be possible by updating the dependency versions, updating aiohttp to 3.6.1, and the websocket library to 8.1 or above, however the websocket library may not work with the code here.

# How to use Gateway Intents

By default, this will subscribe you to all intents, including privileged intents. To specify which intents to use, you should do so when creating the `Client` object. 

Doing the following will subscribe you to all non-privileged intents:
```py
import discord_unofficial as discord
import asyncio
client = discord.Client(use_privileged_intents=False)
```

While doing the following will allow you to specify which intents you wish to subscribe to (In the case that `use_privileged_intents` is set to ``False``, privileged intents will be not subscribed to even if they were set)

```py
import discord_unofficial as discord
import asyncio
client = discord.Client(use_privileged_intents=False, intents=0b1000011)
```

``0b1000011`` corresponds to the `GUILD_INVITES`, `GUILD_MEMBERS` and `GUILDS` Gateway intents respectively, however, as `GUILD_MEMBERS` is a privileged intent, and `use_privileged_intents` was set to ``False``, it will not be subscribed to. So the above code is the same as the following.

```py
import discord_unofficial as discord
import asyncio
client = discord.Client(intents=0b1000001)
```

# discord.py

[![PyPI](https://img.shields.io/pypi/v/discord.py-unofficial.svg)](https://pypi.python.org/pypi/discord.py/)
[![PyPI](https://img.shields.io/pypi/pyversions/discord.py-unofficial.svg)](https://pypi.python.org/pypi/discord.py/)

discord.py is an API wrapper for Discord written in Python.

This was written to allow easier writing of bots or chat logs. Make sure to familiarise yourself with the API using the [documentation][doc].

This fork runs on v0.16.12 for the most part, the original documentation for that can be found [here][docv01612]
This was modified to allow old bots that still ran on the async branch (`v0.16.12`) of the [original discord.py library][dpygithub] made by Rapptz to be compatible with Discord's upcoming v7 api.

[doc]: http://discordpy.rtfd.org/en/latest
[docv01612]: https://discordpy.readthedocs.io/en/v0.16.12/
[dpygithub]: https://github.com/Rapptz/discord.py

### Breaking Changes

The discord API is constantly changing and the wrapper API is as well. Unlike the original async branch, there will be an effort to keep backwards compatibility in all versions of this, beginning with `v0.17.0`.

I recommend joining either the [official discord.py server][guild] or the [Discord API server][ch] for help and discussion about the library.

[guild]: https://discord.gg/r3sSKJJ
[ch]: https://discord.gg/discord-api

## Installing

To install the library without full voice support, you can just run the following command:

```
python3 -m pip install -U discord.py
```

Otherwise to get voice support you should run the following command:

```
python3 -m pip install -U discord.py[voice]
```

To install the development version, do the following:

```
python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/master.zip#egg=discord.py[voice]
```

or the more long winded from cloned source:

```
$ git clone https://github.com/Rapptz/discord.py
$ cd discord.py
$ python3 -m pip install -U .[voice]
```

Please note that on Linux installing voice you must install the following packages via your favourite package manager (e.g. `apt`, `yum`, etc) before running the above command:

- libffi-dev (or `libffi-devel` on some systems)
- python<version>-dev (e.g. `python3.5-dev` for Python 3.5)

## Quick Example

```py
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run('token')
```

Note that in Python 3.4 you use `@asyncio.coroutine` instead of `async def` and `yield from` instead of `await`.

You can find examples in the examples directory.

## Requirements

- Python 3.4.2+
- `aiohttp` library
- `websockets` library
- `PyNaCl` library (optional, for voice only)
    - On Linux systems this requires the `libffi` library. You can install in
      debian based systems by doing `sudo apt-get install libffi-dev`.

Usually `pip` will handle these for you.
