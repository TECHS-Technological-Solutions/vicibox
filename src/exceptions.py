class ViciboxError(Exception):
    """
    Generic Error
    """


class ViciboxFunctionDoesNotExist(ViciboxError):
    api_name = 'model'

    def __init__(self, api_name: str):
        self.api_name = api_name
        super().__init__(self)

    def __str__(self):
        return f'Provided function is not accessible via {self.api_name} API.'
