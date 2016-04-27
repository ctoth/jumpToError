from functools import wraps
import globalPluginHandler
import ui
import tones
import config
import api
import textInfos
import re
import win32api

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def get_navigator_line(self):
		info = api.getReviewPosition().copy()
		info.expand(textInfos.UNIT_LINE)
		return info.clipboardText

	def script_goToError(self, gesture):
		(file, line) = get_file_and_line(self.get_navigator_line())
		if file is None:
			ui.message("unknown")
			return
		arguments = "/g %s \"%s\"" % (line, file)
		win32api.ShellExecute(0, 'open', "notepad.exe", arguments, '', 1)

	__gestures = {
	"KB:NVDA+g":"goToError",
}

patterns = {
	'python': re.compile(r'File "(.+?)", line (\d+)'),
	'java': re.compile(r"^ *(?:\[javac\])? *(.+\.java):(\d+): .*"),
}



def get_file_and_line(s):
	"""Tries to get the file and line of an error message.
	Returns a tuple of (file, line) as strings, or (None, None) if it fails."""
	r = java_re.match(s)
	if r is not None:
		return r.group(1), r.group(2)
	r = python_re.search(s)
	if r is not None:
		return r.group(1), r.group(2)
	return None, None
