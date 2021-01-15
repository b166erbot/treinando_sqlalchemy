from contextlib import suppress
import gi

from src.interface import App


gi.require_version('Gtk', '3.0')


from gi.repository import Gtk


def main():
    with suppress(KeyboardInterrupt):
        app = App()
        Gtk.main()

if __name__ == '__main__':
    main()
