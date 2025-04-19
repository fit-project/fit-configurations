import os
import sys

from fit_configurations.controller.tabs.language.language import (
    Language as LanguageController,
)


def get_language():
    controller = LanguageController()
    return controller.options["language"]
