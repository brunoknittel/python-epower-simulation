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

from esimulation.core.eobject import EObject

class EProduction(EObject):
    """
    This base class describes an object that provides electricity supply information.
    It can be from the electricity provider, a renewable resource or a storage system.
    """
    def produce_always(self, begin, end):
        """
        Returns the amount of energy that is produced no matter the drained power.
        This is for example what a solar panel or wind mild would return: no mater the power demand
        it would produce exactly that.
        """
        raise RuntimeError("EProduction produce_always is not implemented")

    def produce_on_demand(self, begin, end, kwh):
        """
        Returns the amount of energy that can be produced on demand, maximum
        the number of kwh being provided.
        It returns a tuple with first the amount of energy and second the cost of this
        energy.
        """
        raise RuntimeError("EProduction produce_on_demand is not implemented")