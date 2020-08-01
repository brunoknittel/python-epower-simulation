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

from datetime import timedelta

class TimeSlice(object):
    """
    Computes/manages the time slice used to run the simulation
    """
    def __init__(self, config):
        self._config = config

    def get(self, now):
        """
        Gets the optimal time slice to use based on the objects
        used in the simulation.
        TODO Optimization: if all objects have a constant timeslice or none at all
        do not run this method all over again
        """
        res = timedelta(0, 0, 0, 0, 0, 1)       # Default to one hour; arbitrary maximum
        zero = timedelta()
        for o in self._config.objects():
            dt = o.timeslice(now)
            if dt == zero:
                # Implementation has no preference at all, ignore
                continue

            if dt < res:
                res = dt

        return res
