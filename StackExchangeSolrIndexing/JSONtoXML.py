import json
import re
import sys
from optparse import OptionParser
from pprint import pprint

def xmlFromJson(json):
    result = '<?xml version="1.0" encoding="utf-8"?>\n'
    result += "<posts>"
   
    for i in range(len(json)):
        itemTag = "<row Id='"
        itemTag += str(i + 1)
        itemTag += "' mongoId='"
        itemTag += json[i]['_id']
        itemTag += "' Body='"
        itemTag += json[i]['text']
        itemTag += "' />"
        
        result += itemTag
        result += '\n'

    result += "</posts>"
    return result

def main(filename):
	with open(filename) as data_file:
		##retrieves the 
		data = json.load(data_file)
		xml = xmlFromJson(data)
		f = open(filename.split(".")[0] + ".xml", 'w')
		f.write(xml.encode('utf8'))
		f.close()
	#pprint(data)

if __name__ == '__main__':
    usage = 'usage: %prog [options] file'
    parser = OptionParser(usage)
    parser.add_option('-u', '--url', dest='url', default='ec2-52-10-79-212.us-west-2.compute.amazonaws.com:8080/solr/update', help='POST endpoint')
    parser.add_option('-b', '--bulk-size', dest='bulkSize', type='int', default=10000, help='Number of docs to submit in each bulk request.')

    options, args = parser.parse_args()
    if len(args) != 1:
        parser.error('The StackOverflow posts.xml file location must be specified')

    # globals
    URL = "http://"+options.url
    BULK_SIZE = options.bulkSize

    ret = main(args[0])
    sys.exit(ret)