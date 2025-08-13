import json
import os

class Settings:
    def __init__(self, profile_path=None):
        self.profile_path = profile_path or os.path.join(os.path.dirname(__file__), 'profiles.json')
        self.settings = self.load_settings()

    def load_settings(self):
        if os.path.exists(self.profile_path):
            with open(self.profile_path, 'r') as f:
                return json.load(f)
        return {}

    def get_profile(self, name='default'):
        return self.settings.get(name, {})
