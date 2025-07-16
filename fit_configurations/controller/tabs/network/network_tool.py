from fit_configurations.model.tabs.network.network_tool import NetworkToolModel


from sqlalchemy.inspection import inspect

class NetworkToolController:
    _configuration = {}

    def __init__(self):
        self.model = NetworkToolModel()
        self._configuration = self.model.get()

    @property
    def configuration(self):
        instance = self._configuration[0]
        return {
            column.key: getattr(instance, column.key)
            for column in inspect(instance).mapper.column_attrs
        }

    @configuration.setter
    def configuration(self, configuration):
        self.model.update(configuration)
