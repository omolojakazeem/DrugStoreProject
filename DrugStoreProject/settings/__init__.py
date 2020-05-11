import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from base import *

env_name = os.getenv('ENV_NAME', 'heroku')

if env_name == 'heroku':
    from .prod_heroku import *

if env_name == 'aws':
    from .prod_aws import *

else:
    from .dev import *