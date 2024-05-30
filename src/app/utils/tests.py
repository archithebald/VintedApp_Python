import os
import importlib
  
def import_tests(_dir):    
    for filename in os.listdir(_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f'{filename[:-3]}'
            module = importlib.import_module(module_name)
            
            globals().update(module.__dict__)