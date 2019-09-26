"""
    VLDC Nyan bot
    ~=~=~=~=~=~=~=~=~=~=~=~=~=[,,_,,]:3

    https://github.com/egregors/vldc-bot
"""
import logging

from telegram.ext import Updater

from config import get_config
from skills.core import add_core_handlers
from skills.smile_mode import add_smile_mode
from skills.towel_mode import add_towel_mode_handlers
from skills.version import add_version_handlers


def main():
    """ Start the Smile! 😊."""
    conf = get_config()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG if conf["DEBUG"] else logging.INFO)

    updater = Updater(conf["TOKEN"], use_context=True)

    # put each skill in the different group
    class HandlersGroups:
        core = 0
        version = 1

        smile_mode = 2
        tower_mode = 3

    # init all skills
    add_core_handlers(updater, HandlersGroups.core)
    add_version_handlers(updater, HandlersGroups.version)

    add_smile_mode(updater, HandlersGroups.smile_mode)
    add_towel_mode_handlers(updater, HandlersGroups.tower_mode)

    # let's go dude
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
