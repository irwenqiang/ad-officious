import json



class PreProceeding(object):
	def __init__(self):
		pass

	def join_unit_ad_type_priority(self, infile, outfile):

		#json_data = open("/data/dale/21945")
		json_data = open(infile)
		#print type(json_data)
		data = json.load(json_data)
		#print type(data)			

		out = file(outfile, 'w')

		dictAd = data['Ad']
		dictItemProfile = data['ItemProfile']

		keyAd = dictAd.keys()
		keyItemProfile = dictItemProfile.keys()

		for i in xrange(len(data['Ad'].keys())):
			
			#print keyAd[i]
			out.write(keyAd[i])
			out.write("\t")
			item_id = dictAd[keyAd[i]]['item_id']
			#print item_id
			#out.write(str(item_id))
			#out.write(" ")
			
			dictItemProfileV = dictItemProfile.values()
			for i in xrange(len(dictItemProfileV)):
				if item_id == dictItemProfileV[i]['item_id']:
					
					out.write(str(dictItemProfileV[i]['item_priority']))
					out.write("\t")
					out.write(dictItemProfileV[i]['item_type'])

			out.write("\n")

		out.close()


	def remove_cpd(self, infile, outfile):
		f = file(infile)
		out = file(outfile, 'w')

		for line in f:
			if not line.strip().split()[2] == 'CPD':
				out.write(line)

		out.close()
	
	def find_multitype(self, infile):
		admt = {}
		f = file(infile)
		for line in f:
			lines = line.split("\t")
			if lines[0] not in admt:
				admt[lines[0]] = line
			elif lines[0] in admt:
				admt[lines[0]].append(line)

		for key, value in admt.items():
			if len(value) > 1:
				print key, value
			
if __name__ == "__main__":
	pp = PreProceeding()
	infile = ""
	outfile = ""

	#pp.join_unit_ad_type_priority()

	infile = "ad_id"
	outfile = "ad_id_not_cpd"
	#pp.remove_cpd(infile, outfile)
	pp.find_multitype(outfile)

