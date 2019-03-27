import tkinter as tk

'''
      ------------------------  000000   °°   000    0  00 00   .......
      ------------------------    00     00   0  0   0  000     .......
      ------------------------     00    00   0   0  0  00 0    .......
      ------------------------      00   00   0    000  00  00  .......
      -----------------------------------------------------------------
'''


class Flag:

    '''
    Flag(parent frame, mode) creates a dynamic flag label object.

    parent: is the parent frame for the flag.

    start: where the flag should start. It depends on mode the
    length of this start number. For more information see the
    docstring of each mode. It is recommended to leave it on default

    Flags can be the following:
    * State : defalut mode, based on stages.
    * Percentage : flag changes works with a percentage output.
    '''

    conf = {
    }

    def __init__(self, parent, start = 0):
        self._parent = parent
        self._state = start
        self._config = self.conf
        self.label = tk.Label()

    def config(**config):
        self._config = config


class StateFlag(Flag):

    '''
    State-based flag label

    conf:
        * states : states to show on flags.
        * colors : colors asociatied to each state of flag.
        * foreground : text color.
        * head : type of flag.
    '''

    conf = {
        'states' : ['To do', 'In progress', 'Done'],
        'colors' : ['red','yellow','light green'],
        'foreground' : ['black'],
        'head' : 'state'
    }

    def __init__(self, parent, start=0):
        Flag.__init__(self, parent, start)
        self.label = tk.Label(self._parent,
                                    text = self._config['states'][start],
                                    bg = self._config['colors'][start],
                                    fg = self._config['foreground'])

    def change_state(self, number):
        self._state += number
        self.label.config(text= self._config['states'][self._state],
                                bg = self._config['colors'][self._state])
        return

    def config(self, states = None, colors = None, foreground =None):
        if states != None:
            self.config['states'] = states
        if colors != None:
            self.config['colors'] = colors
        if foreground != None:
            self.config['foreground'] = foreground
        return


class PercentageFlag(Flag):

    '''
    Percentage-based state flag.

    conf:
        * colors: background colors to be shown in flag.
        * foreground: text color.
        * limit: maximum number into flag to show.
        * head: added to string to show percentage
                or anything intended.
    '''

    conf = {
        'colors' : ['green'],
        'foreground' : ['white'],
        'limit' : 100,
        'head' : '%'
    }

    def __init__(self, parent, start=0):
        Flag.__init__(parent, start)
        self._length = len(self._config['colors'])
        self.label = tk.Label(text=self._state + 'head',
                              bg=self._config['colors'][start],
                              fg = self._config['foreground'])

    def change_state(self, number):
        self._state += number
        return

    def config(self, colors = None, foreground =None,
               head = None, limit = None):
        if colors != None:
            self.config['colors'] = colors
        if foreground != None:
            self.config['foreground'] = foreground
        if limit != None:
            self.config['limit'] = limit
        if head != None:
            self.config['head'] = head
        return
