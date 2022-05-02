#!/usr/bin/env python3
"""
Small utility to use Pimoroni's Scroll HAT or Scroll pHAT as a ping meter.
"""

__author__ = "Marcel Keßler"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import scrollphathd as sphd
from logzero import logger
from ping3 import ping
from time import sleep
import sys


def main(args):
    """ Main entry point of the app """
    logger.info("Pinging target '%s' every %s second(s)." % (args.host, args.timer))

    if args.brightness < 0.1 or args.brightness > 1.0:
        logger.error("Brightness must be between 0.1 and 1.0 - Exiting...")
        sys.exit()

    if not args.disabledisplay:
        logger.info("Display output is enabled (Brightness: %s). " % args.brightness +
                    "Use '--disabledisplay' to disable output.")
        sphd.set_brightness(args.brightness)
    else:
        logger.info("Display output is disabled.")

    if args.verbose >= 1:
        logger.debug("Used args: %s" % args)

    # Loop
    logger.info("Starting ping loop. Use ^C to stop the script.")
    while True:
        try:
            resp = ping(args.host, timeout=args.timer, unit='ms')
            if resp is None:
                # Ping timed out
                logger.info("Ping timed out after %s second(s)." % args.timer)
                if not args.disabledisplay:
                    sphd.clear()
                    sphd.write_string("NaN")
                    sphd.show()
            else:
                # Successful ping
                logger.info("Ping took %dms." % resp)
                if not args.disabledisplay:
                    sphd.clear()
                    sphd.write_string("%dms" % resp)
                    sphd.show()
            sleep(args.timer)
        except KeyboardInterrupt:
            logger.info("Stopping ping loop. Exiting...")
            sys.exit()
        except Exception as e:
            logger.error("Ping loop caught an exception: %s" % e)
            logger.error("Retrying in 60 seconds...")
            sleep(60)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    parser.add_argument("--disabledisplay",
                        action="store_true",
                        default=False,
                        help="Add flag to disable display output")

    parser.add_argument("-H",
                        "--host",
                        action="store",
                        dest="host",
                        default="8.8.8.8",
                        help="Host to ping. Default: 8.8.8.8")

    parser.add_argument("-t",
                        "--timer",
                        action="store",
                        type=int,
                        dest="timer",
                        default=10,
                        help="Time in seconds between pings. Default: 10")

    parser.add_argument("-b",
                        "--brightness",
                        action="store",
                        type=float,
                        dest="brightness",
                        default=1.0,
                        help="Sets brightness of display. Use range between 0.1 and 1.0. Default: 1.0")

    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
