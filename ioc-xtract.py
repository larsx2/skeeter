#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-

import argparse

from skeeter.runner import CmdLineRunner
from skeeter.log import log

parser = argparse.ArgumentParser()
parser.add_argument('--target', 
                        help="Specify target directory to scan",
                        required=True)

parser.add_argument('--verbose', 
                        help="Be verbose about every action performed",
                        action='store_true', default=False)

parser.add_argument("--types", help="Specify IOC types to scan for",
                        default="all", 
                        choices=["all", "md5", "ipv4", "url", "email", "domain"])

args = parser.parse_args()


try:
    app = CmdLineRunner(args.target, args.verbose, types=args.types)
    app.run()
except Exception as e:
    log.error(e.message)
