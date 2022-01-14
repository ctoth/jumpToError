try:
	from .addon import *
except ImportError: #We're running under pytest not NVDA
	from . import error_finder
