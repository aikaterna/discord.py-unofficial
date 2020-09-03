# -*- coding: utf-8 -*-

"""
Discord API Wrapper
~~~~~~~~~~~~~~~~~~~

A basic wrapper for the Discord API.

:copyright: (c) 2015-2020 Rapptz
:copyright: (c) 2020 RandomGamer123
:copyright: Note: Copyright for portions of project discord.py are held by Rapputz. All other copyright for the project is held by RandomGamer123.
:license: MIT, see LICENSE for more details.

"""

__title__ = 'discord'
__author__ = 'RandomGamer123'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015-2020 Rapptz, Copyright 2020 RandomGamer123'
__version__ = '0.17.0-beta.12'

from .client import Client, AppInfo, ChannelPermissions
from .user import User
from .game import Game
from .emoji import Emoji
from .channel import Channel, PrivateChannel
from .server import Server
from .member import Member, VoiceState
from .message import Message
from .errors import *
from .calls import CallMessage, GroupCall
from .permissions import Permissions, PermissionOverwrite
from .role import Role
from .colour import Color, Colour
from .invite import Invite
from .object import Object
from .reaction import Reaction
from . import utils, opus, compat
from .voice_client import VoiceClient
from .enums import ChannelType, ServerRegion, Status, MessageType, VerificationLevel
from collections import namedtuple
from .embeds import Embed

import logging

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=17, micro=0, releaselevel='beta', serial=12)

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
