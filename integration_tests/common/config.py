# Base URL to be used for testing. Enables testing in different environments.
# Set in conftest.py based on command line paramete '--baseurl'
# Command line parameter is defined in conftest.py and defaults to 'hudl.com'
baseurl = ""

# Browser to be used for testing. Enables multi-browser testing.
# Set in conftest.py based on command line paramete '--browser'
# Command line parameter is defined in conftest.py and defaults to 'chrome'
browser = ""

# Host to be used for testing. Enables local or remote testing.
# Set in conftest.py based on command line paramete '--bhost'
# Command line parameter is defined in conftest.py and defaults to "local""
host = ""

# Wehther to use headless mode or not for testing.
# Set in conftest.py based on command line paramete '--headless'
# Command line parameter is defined in conftest.py and defaults to False
headless = None

#Scope  for testing.
# Set in conftest.py based on command line paramete '--scope'
# Command line parameter is defined in conftest.py and defaults to "session"
scope = ""