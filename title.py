import sys
import os

class Title:
    def __init__(self):
        """Initialize the Title object."""
        pass

    def init(self):
        """Initialize the title object (if not already initialized)."""
        if not hasattr(self, "_initialized"):
            # This ensures the Title instance is created only once
            self._initialized = True
            self.set_title("")

    def set_title(self, title):
        """Set the console window title for supported platforms."""
        if sys.platform == "win32":
            # For Windows, use the 'title' command
            os.system(f'title {title}')
        elif sys.platform == "darwin" or sys.platform == "linux" or sys.platform == "cygwin":
            # For UNIX-like systems (Linux, macOS), use escape sequences
            print(f"\033]0;{title}\007", end="", flush=True)

    def __call__(self, title):
        """Allow the title to be set directly as a callable."""
        self.set_title(title)

# Initialize a global instance for use in the module
title = Title()
