import os
import configparser

config = configparser.ConfigParser()

config.read(os.path.join(os.path.dirname(__file__), '.env'))

for (key, value) in config.items('variables'):
    os.environ[key] = value
    
    
# Testing, remove this
print("ApiKey: " + os.environ.get('elsevier-api-key'))