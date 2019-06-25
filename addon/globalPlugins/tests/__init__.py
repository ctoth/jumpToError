
import globalPluginHandler

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def get_navigator_line(self):
		info = api.getReviewPosition().copy()
		info.expand(textInfos.UNIT_LINE)
		return info.clipboardText
