from distutils.core import setup
setup (name = 'flibustadownloader',
		version      = '0.2.1',
		url          = 'https://github.com/popovb/FlibaDownloader',
		author       = 'Boris Popov',
		author_email = 'popov.b@gmail.com',
		license      = 'GPLv3',
		description  = 'Helper for download daily updates from flibusta net',
		packages     = ['flibaloader'],
		scripts      = ['FlibustaDownloader.py'],)

