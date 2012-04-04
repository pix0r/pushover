A simpe Python client for http://pushover.net/ API

Install:

    pip install https://github.com/pix0r/pushover.git

Usage:

	from pushover import pushover

	pushover(message="Hello, world",
	    token="My App Token",
		user="My User Key",
		)
	
Or using command line utility:

    pushover "Hello, world" --token="My App Token" --user="My User Key"

