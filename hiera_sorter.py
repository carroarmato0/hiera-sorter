#!/usr/bin/python

import sys
import os.path

# Check if at least one argument is passed
if len(sys.argv) <= 1:
	print "File argument needed";
	sys.exit(0);

# Loop over arguments ignoring first one (is filename of script)
for arg in sys.argv[1:]:
	# Check if file passed actually exists
	if not os.path.isfile(arg):
		print "%s is not a file. Quiting..." % str(arg)
		sys.exit(0);

	# [DEBUG] Some debug stuff
	#print "Filename: %s" % str(arg)

  # Our array

	# Read file
	with open(arg, 'rw') as file:
		arrayBlock_counter = 0;
		data = file.readlines();
		# Loop over every line and try to bundle in blocks
		for line in data:
			
			
			
			print line;
