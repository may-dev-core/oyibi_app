from config.settings.base import *

try:
    from .production import *
    
except expression as identifier:
    from .local import *
else:
    pass    
