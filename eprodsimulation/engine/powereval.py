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

class PowerEval(object):
    """
    Implements several power evaluations using a list of EObjects
    """
    def __init__(self, objects):
        self._objects = objects

    def required_power(self, now, dt):
        """
        Gets the sum of all required power at a given moment and for a given time
        """
        res = 0.0
        for o in self._objects:
            if o.is_consumer():
                res += o.consume_required(now, dt)

        return res

    def produce_always(self, now, dt):
        """
        Gets the sum of produced power at a given moment and for a given time
        """
        res = 0.0
        for o in self._objects:
            if o.is_producer():
                res += o.produce_always(now, dt)

        return res

    def consume_optional(self, now, dt):
        """
        Gets