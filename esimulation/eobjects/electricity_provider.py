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

from esimulation.core.eproduction import EProduction
from esimulation.core.econsumer import EConsumer

class ElectricityProvider(EProduction, EConsumer):
    """
    An electricity provider able to provide as much power as required
    and able to use as much power as available at any time.
    That's typically your national electricity provider
    """
    def __init__(self):
        super().__init__(True, True)
        self._kWhPriceSold = 0
        self._kWhPriceBought = 0
        self._loaded = False

    def load(self, jsonDict):
        """
        Loads the configuration of this electricty provider from
        a dictionary providing the values specified in the configuration file.
        """
        self._kWhPriceSold = float(jsonDict['price_per_kWh_sold'])
        self._kWhPriceBought = float(jsonDict['price_per_kWh_bought'])
        self._loaded = True

    def produce_always(self, begin, timeslice):
        if not self._loaded:
            raise RuntimeError("ElecricityProvider not configured")

        return 0.0

    def produce_on_demand(self, begin, timeslice, kwh):
        if not self._loaded:
            raise RuntimeError("ElecricityProvider not configured")

        return (kwh, kwh * self._kWhPriceSold)

    def consume_required(self, when, timeslice):
        if not self._loaded:
            raise RuntimeError("ElecricityProvider not configured")

        return 0.0

    def consume_optional(self, when, timeslice, available_kwh):
        if not self._loaded:
            raise RuntimeError("ElecricityProvider not configured")

        return (available_kwh, available_kwh * self._kWhPriceBought)