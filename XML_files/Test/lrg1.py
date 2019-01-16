#importing ElementTree and parsing the XML file
import xml.etree.ElementTree as ET
tree = ET.parse('LRG_1.xml')
root = tree.getroot()

# This is code to find the exon start and end coordinates 
#Addition of code to create lists
start =[]
end = []
label = []
def exon_find():
	for exon in root.findall(".//fixed_annotation/transcript/exon"):
		label.append(exon.get('label'))
		global coordinates
		coordinates = exon.find('coordinates')
		start.append(coordinates.get('start'))
		end.append(coordinates.get('end'))
	return start, end

exon_find()
	
#Finding the chromosome number within the XML file
def chromosome_find():
	for annotation_set in root.findall(".//updatable_annotation/annotation_set[@type='lrg']"):
		mapping = annotation_set.find('mapping')
		global chrom
		chrom = mapping.get('other_name')
		global chromstart
		chromstart = mapping.get('other_start')
		global chromend
		chromend = mapping.get('other_end')
	return chrom, chromstart, chromend

chromosome_find()
	
f = open("lrg.bed", "w")
f.write("Chrom" + "\t" + "Start" + "\t" + "End" + "\n")
for i in range(len(start)):
	f.write(str(chrom) + "\t" + str(start[i]) + "\t" + str(end[i]) + "\n")

f.close()
