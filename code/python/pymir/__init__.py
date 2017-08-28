# Configuration object that is available for all components in the project

class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class MIRConf(Borg):
    pass


settings = MIRConf()
