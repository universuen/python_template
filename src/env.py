class Env:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Env, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.config = {}

    def set(self, key, value):
        self.config[key] = value

    def get(self, key):
        return self.config.get(key)
