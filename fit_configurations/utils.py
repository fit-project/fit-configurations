from fit_configurations.view.configuration import Configuration

from fit_configurations.controller.tabs.language.language import (
    Language as LanguageController,
)


def get_language():
    controller = LanguageController()
    return controller.options["language"]


def show_configuration_dialog():
    Configuration().show()
