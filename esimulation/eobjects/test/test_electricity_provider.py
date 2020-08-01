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

import unittest
from datetime import datetime, timezone, timedelta

from ..electricity_provider import ElectricityProvider

class ElectricityProviderTest(unittest.TestCase):

    def setUp(self):
        config = {
            "price_per_kWh_sold": 0.147,
            "price_per_kWh_bought": 0.10
        }
        p = ElectricityProvider()
        p.load(config)
        self._p = p
        self._now = datetime.now(timezone.utc)
        self._dt = timedelta(1)

    def test_not_loaded(self):
        """
        Ensures that an error is raised when trying to use an
        electricity provider that hasn't been configured.
        This doesn't need the setUp method
        """
        p = ElectricityProvider()
        when = datetime.now(timezone.utc)
        dt = timedelta(1)

        with self.assertRaises(RuntimeError):
            p.consume_optional(when, dt, 100)

        with self.assertRaises(RuntimeError):
            p.consume_required(when, dt)

        with self.assertRaises(RuntimeError):
            p.produce_always(when, dt)

        with self.assertRaises(RuntimeError):
            p.produce_on_demand(when, dt, 100)

    def test_produce_always(self):
        self.assertEquals(0, self._p.produce_always(self._now, self._dt))

    def test_produce_on_demand(self):
        res = self._p.produce_on_demand(self._now, self._dt, 100.0)
        self.assertEquals(res[0], 100.0)
        self.assertEquals(res[1], 100.0 * 0.147)

    def test_consume_required(self):
        self.assertEquals(0, self._p.consume_required(self._now, self._dt))

    def test_consume_optional(self):
        res = self._p.consume_optional(self._now, self._dt, 100.0)
        self.assertEquals(res[0], 100.0)
        self.assertEquals(res[1], 100.0 * 0.10)

