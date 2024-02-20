#!/usr/bin/env python3

"""
App name: BashTube
Author: TrollSkull
Github: https://github.com/TrollSkull
Version: 3.0
"""

import sys
import logging

from lib.main import main
from lib.core.exceptions import BashTubeExceptions

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def main():
    setup_logging()
    try:
        main()
    except BashTubeExceptions as e:
        logging.error(f"BashTube Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
