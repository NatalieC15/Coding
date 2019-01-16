#Python code for developing a software to extract information from a LRG XML file to make a .bed file 
#The .bed file should contain the chromosome number for where the gene of interest is located and the start coordinates and end coordinates of the exons within the gene.
#The software includes tests for entering the LRG number of interest and whether the file has been saved into the correct folder in the correct  format. 
#There are two test loops: the first is for checking a numerical value has been entered and the second is checking if the file has been downloaded and saved correctly in the right folder and format.  
#The test works for when the LRG_<number>.xml file has been downloaded, has the correct file name and saved in the right folder. 
#The test works for when a non-numerical value is entered and reminds the user to enter only numerical values.
#The test works for when a numerical value is entered by the file does not exist and has not been downloaded from the LRG website or saved in the right location or format.  

LRG_file_number = None
#First test to see if the user has entered a numerical value:
while True:
	LRG_file_number = input('Enter LRG file number of interest: ')
	try:
		LRG_file_number = int(LRG_file_number)

		LRG_file_number = str(LRG_file_number)
		LRG_file_name = 'LRG_' + LRG_file_number + '.xml'
		#Below is a check to see if the format of the LRG_file_name is correct:
		#print(LRG_file_name)

		#Second test to check to see if the correct file has been downloaded from the LRG website, saved in the correct folder and in the right format:
		while True:
			try:
				#importing ElementTree and parsing the XML file:
				import xml.etree.ElementTree as ET
				tree = ET.parse(LRG_file_name)
				root = tree.getroot()

				root.attrib
				#{'schema_version': '1.9'} - this was the output of the above code when looking at the root attribute in the LRG_1.xml file.

				for child in root:
     					print(child.tag, child.attrib)
				#fixed_annotation {}
				#updatable_annotation {} - these were both outputs from looking at the root child relationship.

				#The code to get the tree structure:
				print(ET.tostring(root, encoding='utf8').decode('utf8'))
				#output of the code above is the tree structure to base further work on.

				#This is code to find the exon start and end coordinates (after much error, all it takes is an extra /)
				#".// - must have 2 /'s to get label information.
				start =[]
				end = []
				label = []
				#creation of lists for the exon number, and the start and end coordinates of the exons of the gene of interest.
				def exon_find():
					for exon in root.findall(".//fixed_annotation/transcript/exon"):
						label.append(exon.get('label'))
						global coordinates
						coordinates = exon.find('coordinates')
						start.append(coordinates.get('start'))
						end.append(coordinates.get('end'))
					return start, end 
				exon_find()

				#Use the print function to test the list creation for label, start and end:
				#print (label, start, end)

				#Finding the chromosome number, start and end coordinates within the XML file, this finds the build number GRCh37.p13 for LRG_1.xml file but may not converse for every file.
				#May need to find a way to pull only the GRCh37 build in the future. 
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

				#Use the print function to test the at the correct values for chromosome number, genomic start and end coordinates have been collated:
				#print(chrom, chromstart, chromend)

				#Code to extract the gene name:
				for annotation_set in root.findall(".//updatable_annotation/annotation_set[@type='lrg']"):
     					lrg_locus = annotation_set.find('lrg_locus')
     				#Print function to check that the gene name is correct:
				#print(lrg_locus.text)

				#Creation of the .bed file:
				#This code produced a bed file that contains 3 columns the chr number, the start coordinate of the exons, the end coordinate of the exons
				#Further improvement would be to extract the genomic coordinates of the exons (potentially add the chromstart number to all values in column 2 and 3)
				bed_file = 'LRG_' + LRG_file_number + '.bed'
				f = open(bed_file, "w")
				f.write("Chrom" + "\t" + "Start" + "\t" + "End" + "\n")
				for i in range(len(start)):
					f.write(str(chrom) + "\t" + str(start[i]) + "\t" + str(end[i]) + "\n")
				f.close()

				#The print code to give an output to say that the bed file has been created:
				print(bed_file,'file created for the gene',lrg_locus.text,'from the',LRG_file_name,'file')

			#The alternative output for the second test code for when the file has not been saved correctly:
			except:
				print('Error, check the correct LRG XML file has been downloaded from https://www.lrg-sequence.org/, saved into the right folder (i.e. XML_files) with the correct format (e.g. LRG_1.xml)')
			break
	#The alternative output for the first test code for if a non-numerical value is entered:
	except:
		print('Invalid input, please enter a numeric input')
		continue
	#The final code to finish the test loop and exit the software:
	break