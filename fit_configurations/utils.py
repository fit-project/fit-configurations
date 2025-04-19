import os
import sys

from fit_configurations.controller.tabs.language import language as LanguageController


def resolve_path(path):
    if getattr(sys, "frozen", False):
        # If the 'frozen' flag is set, we are in bundled-app mode!
        resolved_path = os.path.abspath(os.path.join(sys._MEIPASS, path))
    else:
        # Normal development mode.
        resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))

    return resolved_path


def get_version():
    return "v0.0.0"


def resolve_db_path(path):
    if getattr(sys, "frozen", False):
        if sys.platform == "win32":
            local_path = os.path.join(os.path.expanduser("~"), "AppData", "Local")
        elif sys.platform == "darwin":
            local_path = os.path.expanduser("~/Library/Application Support")
        else:
            local_path = os.path.expanduser("~/.local/share")

        resolve_db_path = os.path.join(local_path, path)
    else:
        resolve_db_path = os.path.abspath(os.path.join(os.getcwd(), path))

    return resolve_db_path


def get_platform():
    platforms = {
        "linux": "lin",
        "linux1": "lin",
        "linux2": "lin",
        "darwin": "macos",
        "win32": "win",
    }

    if sys.platform not in platforms:
        return "other"

    return platforms[sys.platform]


def get_language():
    controller = LanguageController()
    return controller.options["language"]
