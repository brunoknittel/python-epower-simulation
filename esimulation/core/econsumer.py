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

class EConsumer(EObject):
    """
    This is the base class for objects that provides
    the power usage of the simulated environment.
    Implementations must be designed to support several instanciations
    and also calls in different threads on one single instance.
    """
    def consume_required(self, when, timeslice):
        """
        Asks for the required power usage at the provided time and for the given
        time slice.
        Returns a double in kWh
        """
        raise RuntimeError("EConsumer.consume_required is not implemented")

    def consume_optional(self, when, timeslice, available_kwh):
        """
        Asks for optional power usage at the provided time and for the given
        time slice.
        Returns a tuple with 1 the kWh and 2 the price paid for it
        """
        raise RuntimeError("EConsumer.consume_optional is not implemented")