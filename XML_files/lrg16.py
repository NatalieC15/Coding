#importing ElementTree and parsing the XML file
import xml.etree.ElementTree as ET
tree = ET.parse('LRG_16.xml')
root = tree.getroot()

# This is code to find the exon start and end coordinates 
#Addition of code to create lists
start =[]
end = []
label = []
for exon in root.findall(".//fixed_annotation/transcript/exon"):
	label.append(exon.get('label'))
	coordinates = exon.find('coordinates')
	start.append(coordinates.get('start'))
	end.append(coordinates.get('end'))
	
#Finding the chromosome number within the XML file
for annotation_set in root.findall(".//updatable_annotation/annotation_set[@type='lrg']"):
	mapping = annotation_set.find('mapping')
	chrom = mapping.get('other_name')
	chromstart = mapping.get('other_start')
	chromend = mapping.get('other_end')
	
f = open("lrg.bed", "w")
f.write("Chrom" + "\t" + "Start" + "\t" + "End" + "\n")
for i in range(len(start)):
	f.write(str(chrom) + "\t" + str(start[i]) + "\t" + str(end[i]) + "\n")

f.close()