def save_output_file (path, fulllist):
	with open (path, 'w') as output_file:
		for i in fulllist:
			output_file.write ('-'*100)
			output_file.write ('Theme name: ' + i ['name'])
			output_file.write ('Url: ' + i ['url'])

			if i ['hackable']:
				output_file.write ('Can be hacked ;)')
			else:
				output_file.write ('Can\'t be hacked :(')

			output_file.write ('-'*100)
	output_file.close ()