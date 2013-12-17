#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Skype4Py

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Connect the Skype object to the Skype client.
skype.Attach()

# Get SkypeName by blob. Blob can be aquired using /get uri command in skype client
print skype.FindChatUsingBlob('lGzQEDnkBL1K_pzYWAFq6D5YatgT9nXjBh3am7vhyy_4FRe_GdQF9Lql2Gjt0GdiqhRge9fuTYQwaz5ffTn8fqFUBFhT80lEYZXE4HtrOfqKFctEstvVz7mYIJMO7YrsAMwr3O_OQdx8BCv_djjL09oA')
