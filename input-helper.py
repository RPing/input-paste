#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

import pyperclip
import pyautogui

class SimpleTextInput:
    def copy_to_clipboard(self):
        self.clipboard.set_text(self.entry.get_text(), -1)

    def destroy(self, widget, data=None):
        Gtk.main_quit()

    def on_key_press(self, widget, event):
        keyname = Gdk.keyval_name(event.keyval)
        if event.state & Gdk.ModifierType.CONTROL_MASK and keyname == 'Return' or keyname == 'Return':
            self.copy_to_clipboard()
            self.destroy(self, widget)
            p = pyautogui.position()
            pyautogui.click(p)
            pyautogui.hotkey('ctrl', 'v')
        if keyname == 'Escape':
            Gtk.main_quit()

    def __init__(self):
        # create a new window
        window = Gtk.Window()
        window.set_position(Gtk.WindowPosition.CENTER)
        window.set_title("Input Helper")
        window.set_default_size(300, 60)
        window.connect("destroy", self.destroy)
        self.entry = Gtk.Entry()
        # self.entry.set_tooltip_text("Press Ctrl-Enter or Enter to insert string")
        self.entry.connect("key_press_event", self.on_key_press)
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        window.add(self.entry)
        window.show_all()

    def main(self):
        Gtk.main()

if __name__ == "__main__":
    txt = SimpleTextInput()
    txt.main()
