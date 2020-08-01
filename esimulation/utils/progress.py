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

class Progress(object):
    """
    This defines object used to track and report progress of tasks.
    """
    def __init__(self):
        self._percent = 0.0
        self._doing = ""
        self._objs_to_notify = [ ]

    def set(self, percent, doing = ""):
        """
        Sets the current progress values
        """
        if percent < 0 or percent > 1:
            raise ValueError("Progress percent must be between 0 and 1")

        self._percent = percent
        self._doing = doing
        self._notify_all_listeners()

    def percent(self):
        return self._percent

    def doing(self):
        return self._doing
    
    def add_listener(self, obj):
        try:
            obj.on_progress_changed(self)
            self._objs_to_notify.append(obj)
        except:
            # Do not add it, it failed
            raise ValueError("Object doesn't provide method for progress notification")

    def remove_listener(self, obj):
        self._objs_to_notify.remove(obj)

    def _notify_all_listeners(self):
        """
        Calls the on_progress_changed method on all registered listeners
        """
        for o in self._objs_to_notify:
            try:
                o.on_progress_changed(self)
            except:
                # ignore errors here
                pass
    