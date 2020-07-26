Solar Simulation

Copyright 2020 Knittel Bruno <bruno@knittel.fr>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



To Do
[ ] Define interfaces for power consumption input
[ ] Define interfaces for power production input
[ ] Define simulation interface for power storage
[ ] Implement power production from electricty provider
[ ] Implement power production based on solar surface, angle and a solar power provider info
[ ] Generate report
[ ] Configuration of the simulation using a configuration file

Purpose
I wanted to know the impact of photovoltaïc panels, house battery and even some
automation to make things run when sun power is here (e.g. dryer or washing machine).
My house has some mean to record it's electricity usage per hour, and I wanted to use this data
as a basis for the simulation.

Simulation configuration
The first thing you'll need is a simulation configuration file. It's in JSON format
and describes what you want to simulate.


Running the simulation
Once you have this file, running the simulation is as simple as:
eprodsimulation --config=<path to config file>