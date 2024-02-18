import os
import configparser

config = configparser.ConfigParser()

config.read(os.path.join(os.path.dirname(__file__), '.env'))

try:
    for (key, value) in config.items('variables'):
        os.environ[key] = value
    
except:
    # This is needed for GitHub Actions since .env is not available
    