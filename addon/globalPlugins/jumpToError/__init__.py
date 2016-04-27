try:
	from addon import *
except ImportError: #We're running under pytest not NVDA
	import error_finder
