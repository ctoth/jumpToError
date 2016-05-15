import globalPluginHandler
import ui
import tones
import config
import api
import textInfos
import win32api

import error_finder

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = _("Jump to Error")

	def get_navigator_line(self):
		info = api.getReviewPosition().copy()
		info.expand(textInfos.UNIT_LINE)
		return info.clipboardText

	def script_goToError(self, gesture):
		(file, line) = error_finder.get_file_and_line(self.get_navigator_line())
		if file is None:
			ui.message(_("Unable to find target file and line"))
			return
		arguments = "/g %s \"%s\"" % (line, file)
		win32api.ShellExecute(0, 'open', "notepad.exe", arguments, '', 1)
	script_goToError.__doc__ = _("""Quickly open your editor to the file and line mentioned in a traceback""")

	__gestures = {
	"KB:NVDA+g":"goToError",
}
