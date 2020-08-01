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

# Unit tests of the configuration file parser class

import unittest
from datetime import datetime
from dateutil.tz import tzutc

from ..config import Config
from ...eobjects.electricity_provider import ElectricityProvider

class ConfigTest(unittest.TestCase):
    def _dir_configs(self):
        return './esimulation/core/test/configfiles/'

    def test_file_doesnt_exist(self):
        """
        Ensures a FileNotFoundError is raised when the provided config file doesn't exist
        """
        with self.assertRaises(FileNotFoundError):
            Config("/i/definitely/do/not/exist")

    def test_minimal(self):
        """
        Ensure a minimal file is parsed properly.
        It has no power producer nor power consumer.
        """
        c = Config(self._dir_configs() + 'minimal.json')
        self.assertEquals("", c.name())
        self.assertEquals(0, len(c.objects()))
        self.assertEquals(datetime(2015, 2, 1, 2, 34, 43, 511000, tzinfo=tzutc()), c.timeBegin())
        self.assertEquals(datetime(2015, 2, 7, 18, 55, 0, tzinfo=tzutc()), c.timeEnd())

    def test_fullblown(self):
        """
        Ensures a configuration file making use of all possible
        configuration entires is loaded properly.
        """
        c = Config(self._dir_configs() + 'fullblown.json')

        self.assertEquals("Full blown mad config for tests", c.name())
        self.assertEquals(datetime(1984, 12, 23, 22, 30, 43, tzinfo=tzutc()), c.timeBegin())
        self.assertEquals(datetime(2020, 7, 26, 23, 6, 1, tzinfo=tzutc()), c.timeEnd())

        # In objects, there is one and only one
        self.assertEquals(1, len(c.objects()))

        o = c.objects()[0]
        self.assertTrue(isinstance(o, ElectricityProvider))