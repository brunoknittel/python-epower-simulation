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

from unittest import TestCase
from datetime import datetime, timezone, timedelta

from esimulation.core.powereval import PowerEval
from esimulation.core.eobject import EObject

class ConstantRequired(EObject):
    def __init__(self, constant):
        super().__init__(False, True)
        self._constant = constant

    def consume_required(self, when, timeslice):
        return self._constant

class PowerEvalTests(TestCase):
    """
    Tests of the power evaluation object
    """
    def test_required_power(self):
        pe = PowerEval([ConstantRequired(10), ConstantRequired(11)])
        self.assertEquals(21.0, pe.required_power(datetime.now(timezone.utc), timedelta(1)))