import re

ERROR_PATTERNS = {
	'python': re.compile(r'File "(.+?)", line (\d+) .*'),
	'java': re.compile(r"^ *(?:\[javac\])? *(.+\.java):(\d+): .*"),
}

def get_file_and_line(s):
	"""Tries to get the file and line of an error message.
	Returns a tuple of (file, line) as strings, or (None, None) if it fails."""
	for name, pattern in ERROR_PATTERNS.iteritems():
		match = pattern.search(s)
		if match is not None:
			return r.group(1), r.group(2)
	return None, None
