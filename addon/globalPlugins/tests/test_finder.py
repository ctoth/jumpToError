from jumpToError.error_finder import get_file_and_line

def test_python_pattern():
	assert get_file_and_line(r'  File "c:\users\q\code\jumpToError\test.py", line 1, in <module>') == (r"c:\users\q\code\jumpToError\test.py", 1)

def test_pdb_pattern():
	assert get_file_and_line(r'> c:\users\q\code\app_framework\app_framework\shutdown.py(8)shutdown()') == (r'c:\users\q\code\app_framework\app_framework\shutdown.py', 8)

def test_pdb_breakpoint_pattern():
  assert get_file_and_line(r'Breakpoint 1 at c:\users\tyler\captcha_api\env\lib\site-packages\flask_user\__init__.py:393') == (r'c:\users\tyler\captcha_api\env\lib\site-packages\flask_user\__init__.py', 393)
