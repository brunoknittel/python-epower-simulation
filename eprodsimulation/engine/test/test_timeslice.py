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

# Unit test of the time slicer class

import unittest
from datetime import datetime, timezone, timedelta

from ..timeslice import TimeSlice

class MockConfig(object):
    def __init__(self, objs):
        self._objects = objs

    def objects(self):
        return self._objects

class MockSlice(object):
    def __init__(self, slice):
        self._slice = slice

    def timeslice(self, when):
        return self._slice

class MockNoSlice(object):
    def timeslice(self, when):
        return timedelta() # == Zero
    

class TimeSliceTest(unittest.TestCase):
    def _default_slice(self):
        """
        Common definition of the default time slice
        """
        return timedelta(0, 0, 0, 0, 0, 1) # one hour

    def test_no_object(self):
        """
        The time slice returned when no object is in the simulation is one hour
        """
        ts = TimeSlice(MockConfig([]))
        self.assertEquals(ts.get(datetime.now(timezone.utc)), self._default_slice())

    def test_no_slice(self):
        """
        The time slice returned when all objects in the simulation have no
        preferred time slice is one hour
        """
        ts = TimeSlice(MockConfig([MockNoSlice(), MockNoSlice(), MockNoSlice()]))
        self.assertEquals(ts.get(datetime.now(timezone.utc)), self._default_slice())

    def test_typical(self):
        """
        The time slice returned is the smallest one returned by all objects
        in the simulation
        """
        ts = TimeSlice(MockConfig([
            MockSlice(timedelta(1)),                # 1 day
            MockSlice(timedelta(0, 1)),             # 1 second
            MockSlice(timedelta(0, 0, 0, 0, 1))     # 1 minute
        ]))

        self.assertEquals(ts.get(datetime.now(timezone.utc)), timedelta(0, 1))