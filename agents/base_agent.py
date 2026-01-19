class BaseAgent:
    def __init__(self, name):
        self.name = name
        self._trace = {}

    def run(self, *args, **kwargs):
        raise NotImplementedError("Each agent must implement run()")

    def trace(self):
        return self._trace
