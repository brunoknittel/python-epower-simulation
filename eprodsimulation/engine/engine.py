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

from ..utils.progress import Progress
from .timeslice import TimeSlice
from .powereval import PowerEval

class Engine(object):
    """
    This is the simulation engine
    """
    def __init__(self, config):
        self._prg =  Progress()
        self._config = config

    def run(self):
        """
        Runs the simulation using the provided parameters.
        """
        """
        Sketch:
        from beginning to end
            dt = determine this time slice based on used objects
            needed = sum all required power consumers
            produced = sum all power production that is not optional
            de = produced - needed
            if de > 0:
                let de be consumed by the optional power consumers

            if de < 0:
                let de be provided by the on demand power producers
        """
        now = self._config.timeBegin()
        ts = TimeSlice(self._config)
        pe = PowerEval(self._config.objects())
        while now < self._config.timeEnd():
            dt = ts.get(now)

            needed = pe.required_power(now, dt)
            produced = pe.produced_always(now, dt)

            residual = 0
            missing = 0

            de = produced - needed
            # This is where we can run several scenario
            if de < 0:
                residual = pe.consume_optional(dt, abs(de))
            elif de > 0:
                missing = pe.produce_on_demand(dt, de)

            # Store the result
            self._store(now, dt, needed, produced, de, residual, missing)

    def progress(self):
        """
        Gets the object that provides progress information about this engine run
        """
        return self._prg

    def _store(self, now, dt, needed, produced, de, residual, missing):
        pass