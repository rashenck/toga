import sys
from pathlib import Path

import toga
from toga import App


class Paths:
    # Allow instantiating Path object via the factory
    Path = Path

    @property
    def app(self):
        try:
            return Path(sys.modules["__main__"].__file__).parent
        except AttributeError:
            # If we're running in a test suite, or at an interactive prompt,
            # the __main__ module isn't file-based.
            return Path.cwd()

    @property
    def data(self):
        return Path.home() / 'Library' / 'Application Support' / App.app.app_id

    @property
    def cache(self):
        return Path.home() / 'Library' / 'Caches' / App.app.app_id

    @property
    def logs(self):
        return Path.home() / 'Library' / 'Logs' / App.app.app_id

    @property
    def toga(self):
        """Return a path to a Toga resources
        """
        return Path(toga.__file__).parent


paths = Paths()
