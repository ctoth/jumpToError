import globalPluginHandler
import ui
import tones
import config
import api
import textInfos

import os
import subprocess
import shlex
import threading

from . import error_finder


class OpenerError(Exception): pass

class SourceFileOpener(threading.Thread):

	def __init__(self, cmd, *args, **kw):
		super().__init__(*args, **kw)
		self.cmd = cmd
		from logHandler import log
		log.debug(f'cmd = {self.cmd}')
		if not os.path.isfile(shlex.split(self.cmd)[0]):
			raise OpenerError('NoEditorFileFound')		

	def run(self):
		ret = subprocess.run(
			self.cmd,
			check=True,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
		)


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
		# Command to open Notepad. The file opens only at the initial line; the '/g' flag is not recognized.
		cmd = fr'"c:\windows\notepad.exe" "{file}" /g {line}'
		# Other example working with Notpead++
		# cmd = fr'"C:\Program Files\Notepad++\notepad++.exe" "{file}" -n{line}'
		try:
			SourceFileOpener(cmd).start()
		except OpenerError as e:
			ui.message(_('Opener error: {err}.').format(err=e.args[0]))
			raise e
	script_goToError.__doc__ = _("""Quickly open your editor to the file and line mentioned in a traceback""")

	__gestures = {
	"KB:NVDA+g":"goToError",
}
