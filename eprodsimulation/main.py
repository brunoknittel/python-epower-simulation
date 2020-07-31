# Copyright 2020 Knittel Bruno <bruno@knittel.fr>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ---- END OF LICENSE TEXT ----

# Main program entry point:
#   defines and parses command line arguments
#   and then run the simulation

import argparse

from core.config import Config
from core.engine import Engine

if __name__ == "__main__":
    # Command line parsing
    parser = argparse.ArgumentParser(description='Electrical production and usage simulator.')
    parser.add_argument('conf', type=str, nargs=1, help='path to the simulation configuration file')

    args = parser.parse_args()

    # Load the configuration file...
    config = Config(args.conf)

    # ...create the engine and...
    engine = Engine(config)

    # FIRE!
    engine.run()

    # hum...at some point we might want to display some progress
    # and maybe even some results ;-)

