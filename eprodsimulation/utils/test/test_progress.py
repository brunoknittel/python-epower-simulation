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
from ..progress import Progress

class MockNotTestListener(object):
    """
    Just an object that doesn't provide a on_progress_changed method
    """
    pass

class MockListener(object):
    def __init__(self, fail_after_calls=0):
        self.reset()
        self._fail_after_calls = fail_after_calls

    def reset(self):
        self._notify_count = 0

    def notify_count(self):
        return self._notify_count

    def on_progress_changed(self, progress):
        self._notify_count = self._notify_count + 1
        if self._fail_after_calls > 0 and self._notify_count > self._fail_after_calls:
            raise ValueError("I had to fail")

class ProgressTest(unittest.TestCase):
    def test_ctor(self):
        p = Progress()
        self.assertEquals(p.doing(), "")
        self.assertEquals(p.percent(), 0)

    def test_set_no_listener(self):
        p = Progress()
        p.set(0.15, "testing")
        
        self.assertEquals(p.doing(), "testing", msg="Doing")
        self.assertEquals(p.percent(), 0.15, msg="percent")

    def test_set_listeners(self):
        p = Progress()
        listeners = [MockListener(), MockListener()]
        for l in listeners:
            p.add_listener(l)

        # Reset call counters on these objects
        for l in listeners:
            l.reset()

        p.set(0.94, "still testing")

        # Check the notify changed has been invoked once on every single listener
        for l in listeners:
            self.assertEquals(l.notify_count(), 1)

    def test_set_listener_invalid(self):
        """
        Tests that registering an object that doesn't have the
        required notification method fails
        """
        p = Progress()
        with self.assertRaises(ValueError):
            # Any object that doesn't have the required method
            p.add_listener(MockNotTestListener())

    def test_set_faulty_listener(self):
        """
        Tests the behavior when a listener throws an execpetion
        when being notified
        """
        p = Progress()
        p.add_listener(MockListener(fail_after_calls=1))

        # Ensure no exception is raised
        p.set(1)

    def test_set_progress_too_high(self):
        p = Progress()
        with self.assertRaises(ValueError):
            p.set(1.01)

    def test_set_progress_too_low(self):
        p = Progress()
        with self.assertRaises(ValueError):
            p.set(-0.01)
