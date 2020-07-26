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

import json
from datetime import datetime
import dateutil.parser

class Config(object):
    """
    This class is used to load the simulation configuration
    from a JSON configuration file.
    """
    def __init__(self, path):
        """
        Initializes the configuration using the provided configuraiton file.
        """
        self._consumers = [ ]
        self._producers = [ ]

        with open(path, 'r') as f:
            j = json.load(f)

            self._name = j.get('name', "")
            self._timeBegin = dateutil.parser.parse(j['begin'])
            print("TIME BEGIN = " + str(self._timeBegin))
            self._timeEnd = dateutil.parser.parse(j['end'])

    def name(self):
        """
        Gets the name of this simulation
        """
        return self._name

    def producers(self):
        """
        Gets the list of all objects described in this configuration
        that are electricity producers.
        """
        return self._producers

    def consumers(self):
        """
        Gets the list of all objects described in this configuration
        that are electricity consumers.
        """
        return self._consumers

    def timeBegin(self):
        """
        Gets the date and time of the start of the simulation
        """
        return self._timeBegin

    def timeEnd(self):
        """
        Gets the date and time of the end of the simulation
        """
        return self._timeEnd