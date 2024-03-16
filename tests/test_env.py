import path_setup

from src.env import Env


instance_a = Env()
instance_b = Env()

print(id(instance_a))
print(id(instance_b))
assert id(instance_a) == id(instance_b)

instance_a.var = 1
print(instance_a)
print(instance_b)
assert instance_b.var == 1
