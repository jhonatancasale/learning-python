"""from: https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3"""

import logging

logging.basicConfig(level=logging.DEBUG)

logger1 = logging.getLogger("module_1")
logger2 = logging.getLogger("module_2")

logger1.debug("Module 1 debugger")
logger2.debug("Module 2 debugger")
