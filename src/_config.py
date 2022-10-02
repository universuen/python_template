class Config:
    @classmethod
    def to_dict(cls) -> dict:
        result = dict()
        for k, v in vars(cls).items():
            if k.startswith('_') or k in ('i', 'j', 'k'):
                continue
            result[k] = v
        return result

    @classmethod
    def print_content(cls):
        print(cls.__name__)
        for k, v in cls.to_dict().items():
            print(f'\t{k}: {v}')
