from jumpToError.error_finder import get_file_and_line

def test_get_file_and_line():
	assert get_file_and_line(r'  File "c:\users\q\code\jumpToError\test.py", line 1, in <module>') == (r"c:\users\q\code\jumpToError\test.py", 1)
