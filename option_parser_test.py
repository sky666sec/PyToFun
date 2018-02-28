from optparse import OptionParser
def main():
    usage = "usage: %prog [options] arg"
	parser = OptionParser(usage, description="custom description")

	parser.add_option("-f", "--file", dest="filename", help="read data from FILENAME.")
	parser.add_option("-v", "--version", type="string", dest="version")
	parser.add_option("-d", "--dir", action="store_true", dest="dirname")

	options, args= parser.parse_args()

	if options.filename:
		print(options.filename)
	else:
		print(parser.print_help())

if __name__ == '__main__':
	main()
