import tkinter as tk


class ToggleButton(tk.Button):
    RELIEF = 'raised', 'sunken'

    def __init__(self, master, off, on, callback=None, **kwds):
        def command():
            self.state = not self.state
            callback and callback(self.text)

        super().__init__(master, command=command, **kwds)
        self.texts = off, on
        self.state = False

    @property
    def state(self):
        return self._state

    @property
    def text(self):
        return self.texts[self._state]

    @state.setter
    def state(self, s):
        self._state = s
        self.config(text=self.text, relief=self.RELIEF[s])
