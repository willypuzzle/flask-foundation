import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(1, os.path.dirname(__file__)+os.path.sep+'env'+os.path.sep+'lib'+os.path.sep+'python3.5'+os.path.sep+'site-packages')
from app.application import create

application = create()
