import tkinter as tk


class ResizableCanvas(tk.Canvas):
    def _init(self):
        self.bind('<Configure>', self._on_configure)
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self._on_resize()

    def _on_configure(self, event):
        self.width = event.width
        self.height = event.height
        self._on_resize()

    def _on_resize(self):
        pass
