#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("5166878", cast=int)
    API_HASH = config("fdafb41f9a67f40e34a6c67f47730a92")
    BOT_TOKEN = config("5870372680:AAENb7lbqL1oFyP2KCQRD3TJQ8Zr-ro2AE8")
    OWNER = config("762308466", default=1322549723, cast=int)
    LOG = config("-1001405282390", cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
