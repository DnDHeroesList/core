
import os


class Env(object):
    def __init__(self, path, env_name):
        self.env_name = os.path.join(path, env_name)
        self.env_dict = self._collect()

    def _collect(self):
        if os.path.isfile(self.env_name):
            with open(self.env_name) as f:
                envs = [line.rstrip('\n') for line in f]
                return {i.partition('=')[0]: i.partition('=')[2] for i in envs}
        else:
            return {}

    def get(self, param_name, default):
        return self.env_dict.get(param_name, os.environ.get(param_name, default))
