class Env:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Env, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __repr__(self):
        attrs = vars(self)
        attrs_str = ', '.join(f"{k}={v}" for k, v in attrs.items())
        return f"Env({attrs_str})"
