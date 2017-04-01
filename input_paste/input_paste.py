import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio

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
        window.set_name('window')
        window.set_title("Input Helper")
        window.set_decorated(False)

        window.set_default_size(300, 40)
        window.connect("destroy", self.destroy)

        self.entry = Gtk.Entry()
        self.entry.set_name('entry')
        self.entry.connect("key_press_event", self.on_key_press)

        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

        style_provider = Gtk.CssProvider()
        base_dir = os.path.abspath(os.path.dirname(__file__))
        css_path = os.path.join(base_dir, 'input_paste.css')
        style_provider.load_from_file(Gio.File.new_for_path(css_path))
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        window.add(self.entry)
        window.show_all()

    def main(self):
        Gtk.main()

def main():
    txt = SimpleTextInput()
    txt.main()
