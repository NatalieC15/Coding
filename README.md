# Programming Module Assignment - The user manual 
# Creating a BED file from an XML file
## The user requirements
The assignment for the programming module (BIOL68400) was to create a software that generates a Browser Extensible Data (BED) file from a file in a XML format containing Locus Reference Genomic (LRG) data of a region of interest (ROI).

An XML file covering the ROI can be obtained from the [LRG website](https://www.lrg-sequence.org/index.html).
LRG provides manually curated, stable reference sequences that have been generated and maintained by NCBI and EMBL-EBL. These reference sequences are designed in order to report variants consistently according to clinical reporting standards. LRG provides annotation and mapping data that define the relationship between the LRG "fixed" section sequences, the genome reference assembly (both GRCh37 and GRCh38) and all the known transcripts from RefSeq and GENCODE. The "fixed" section contains the stable genomic DNA sequence for the ROI, transcripts and proteins that are essential for reporting variants and a specific LRG exon numbering system. These highly structured records are accessible through an extensible mark-up language i.e. the XML format.[1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3965024/)

A BED file is a flexible way of defining data lines displayed in an annotation track. There are three required fields that form a BED file:
- chrom - which is the chromosome name that the reference sequence is on
- chromStart - which is the starting position of the sequence within the chromosome 
- chromEnd - which is the end position of the feature within the chromosome
There are nine optional fields of a BED file: name, score, strand, thickStart, thickEnd, itemRgb, blockCount, blockSizes, blockStarts.[2](https://genome.ucsc.edu/FAQ/FAQformat.html#format1)

For this assignment only the three required fields were of interest.
An example of a BED file with just the required fields would be:
```
chr7  127471196 127472363
chr7  127572363 127473530
chr7  127473530 127474697
chr7  127474697 127475864
chr7  127475864 127477031
```
The first column contains the chromosome number, the second the start position and the third the end position. 

### Extra requirements
On top of generating the BED file the other user requirements for this assignment were divided into three areas:
- Quality of the documentation:
   - comments in the code 
   - help documentation/user manuals
- Quality of the code:
   - Sensible variable names
   - Well-structured code with use of functions
   - Functionality of the software
- Professional standards:
   - Tests available for the code
   - Evidence of good use of GitHub
   - Usability of the code 

## Getting Started 
Instructions to get the a copy of the project up and running for development and testing purposes
.
### Prerequisites 
The programs used in the creation and running of the code were: 

The Bash Shell - A standard command processor that allows the user to type commands that do tasks such as reading and executing commands from a file.

Git - A version control software, which links the code to an online repository and allows tracking of what changes are made and who makes them. 

Text Editor - Any text editor can be used, such as notepad, notepad ++ and Atom. Different text editors have different functions which may make the process of writing code easier, e.g.  automatic color-coding of key words.

Python - This is the coding language used throughout the project. 

Therefore, it is advised that in order to utilise the code this software, or equivalent, should be downloaded.

### Installing

If your "HOME" environment variable is not set (or you don't know what this is):
Open command prompt (Open Start Menu then type cmd and press [Enter])
Type the following line into the command prompt window exactly as shown:
setx HOME "%USERPROFILE%"

Press [Enter], you should see SUCCESS: Specified value was saved.
Quit command prompt by typing exit then pressing [Enter]

Installing the bash shell and Git:

On windows, the bash shell and Git can be downloaded together from [here](https://gitforwindows.org/). When installing Git be sure to keep "Use Git from the Windows Command Prompt", "Checkout Windows-style, commit Unix-style line endings" and "Use Windows' default console window" selected. 

Setting up "HOME" environment variable in the bash shell: 

To ensure that the "HOME" environment variable is set up on the bash shell, please do the following steps: 

Open the commmand prompt by opening the Start Menu and typing cmd. Once the command prompt is open type the follwing line and execute: 
```
setx HOME "%USERPROFILE%"
```
This should result in the following coming up in the command prompt: 
```
SUCCESS: Specified value was saved.
```
Then exit the command prompt by typing exit followed by pressing enter. 

Installing python:

Anaconda can be downloaded from [here](https://www.anaconda.com/download). It should be ensured at this point when chosing the download that python version 3.x is installed, as this is the version used in the creation of this project. 

Setting up Github: 

Downloading the repository: 

Before continuing it is recommended that at an XML file of interest is downloaded from the [LRG website](https://www.lrg-sequence.org/index.html) and is saved to the XML_files folder on your Desktop in the format LRG_(x).xml, where (x) is a numerical value. When saving the file watch out for the capital and lower-case letters and make sure they are correct. Although it is possible to continue if the file of interest include LRG_1.xml, LRG_16.xml or LRG_120.xml as these have previously been downloaded to the XML_files folder as they were used for validation and verification purposes.

## Running the code
After installing the required programmes. Using GitBash, the 'cd' command should be entered to move to the correct directory that contains both the XML file of interest and the create_bed.py. As a check to determine that the user is in the correct directory the ls command should be used. See below:
```
~
$ cd Desktop/Coding/XML_files/
~/Desktop/Coding/XML_files (master)
$ ls
```
The output of this code would be:
```
LRG_1.xml create_bed.py
```
To run the code python should be used. Below is an example of how to run the programme and what the output of this should be:
```
~/Desktop/Coding/XML_files (master)
$ python create_bed.py
Enter LRG file number of interest: 
```
A numerical value can now be entered into the command line, this value is dependent on which LRG file has been previously downloaded. Only a number can be entered and negative numbers should not be used. See Section 4 for examples of error messages for invalid entries. After pressing 'ENTER', the software will run automatically and the output will be the ElementTree structure for which the remaining codes are based from to obtain the information to go into the BED file. The second part of the output is a statement to say that the LRG bed file has been created for the gene of interest from the LRG XML file that was input into the software.
```
$ python create_bed.py
Enter LRG file number of interest: 1
```
Output is the tree structure as well as:
```
LRG_1.bed file created for the gene COL1A1 from the LRG_1.xml file
```
The potential differences between the output would be the BED file name, gene name and XML file name.

To view the BED file created the less command can be used, to quit viewing the BED file press 'q':
```
$ less LRG_1.bed
Chrom   Start   End
17      5001    5229
17      6693    6887
17      7050    7084
17      7187    7222
17      7313    7414
17      8136    8207
...
:q
$
```

## The tests and their functions
### Input validation
The first tests incorporated into this software code confirm that the software responds correctly to all kinds of inputs. This is to eliminate human error and ensure that the correct LRG XML file has been selected. 
The entry of this software is a numerical value which corresponds to a XML file of interest. If any non-numerical value is entered the code will trigger an error and remind the user to enter a numerical value only. See below as an example of when 'one' is entered instead of '1':
```
$ python create_bed.py
Enter LRG file number of interest: one
Invalid input, please enter a numeric value 
Enter LRG file number of interest:_
```
The error would also be expressed if a symbol is entered instead e.g. !"£$%^&*().

The second input test determines whether or not the XML file has been downloaded by the user correctly. The output of the test when there is an error is for the user to then check that the file is located in the correct folder and has been saved in the right format e.g. LRG_(number).xml. An example is:
```
$ python create_bed.py
Enter LRG file number of interest: 2
Error, check the correct LRG XML file has been downloaded from https://www.lrg.sequence.org/, saved into the right folder (i.e. XML_files) with the correct format (e.g. LRG_1.xml).
```
### Function tests
Two functions were added to the code of the software the first being: 
```
def exon_find():
	for exon in root.findall(".//fixed_annotation/transcript/exon"):
		label.append(exon.get('label'))
		global coordinates
		coordinates = exon.find('coordinates')
		start.append(coordinates.get('start'))
		end.append(coordinates.get('end'))
	return coordinates, start, end 
```
The purpose of this function is to find the exon number and start and end coordinates of each exon within the sequence of interest. 
The second function was:
```
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
```
The purpose of this second function is to obtain the chromosome number, start and end coordinates within the XML file.

These codes were tested against LRG_1.xml to confirm that they were working correctly. To do this a test folder was created, in the XML_files folder, which contains two files. The first lrg1.py contains all the code required to make the BED file from create_bed.py without the verification steps and the additional steps such as the code to change the BED file name depending on the XML file used. 

The second file, test_lrg1.py contains the code to test the functions. Both tests check that the functions produce the output that is expected when using the LRG_1.xml file. Therefore, if a test fails is it as the functions are not extracting the correct information from LRG_1.xml file.

The test for the exon_find() function is:
```
def test_exon_find(self):
        result1 = lrg1.exon_find()
        self.assertEqual( result1, (['5001', '6693', '7050', '7187', '7313', '8136', '8435', '8638', '8855', '9407', '9577', '9970', '10112', '10273', '10441', '10664', '10975', '11162', '11310', '11540', '11812', '12014', '12193', '12457', '12599', '13593', '13790', '13947', '14112', '14616', '14754', '15150', '15716', '16044', '16260', '16532', '16728', '16908', '17102', '17365', '17630', '17845', '18003', '18491', '18657', '19103', '19518', '19718', '20133', '20620', '20992', '5001', '6693', '7050', '7187', '7313', '8136', '8435', '8638', '8855', '9407', '9577', '9970', '10112', '10273', '10441', '10664', '10975', '11162', '11310', '11540', '11812', '12014', '12193', '12457', '12599', '13593', '13790', '13947', '14112', '14616', '14754', '15150', '15716', '16044', '16260', '16532', '16728', '16908', '17102', '17365', '17630', '17845', '18003', '18491', '18657', '19103', '19518', '19718', '20133', '20620', '20992'], ['5229', '6887', '7084', '7222', '7414', '8207', '8479', '8691', '8908', '9460', '9630', '10023', '10156', '10326', '10485', '10717', '11073', '11206', '11408', '11593', '11919', '12067', '12291', '12510', '12697', '13646', '13843', '14000', '14165', '14660', '14852', '15257', '15823', '16097', '16313', '16639', '16781', '16961', '17263', '17472', '17737', '17898', '18110', '18544', '18764', '19156', '19625', '20000', '20323', '20862', '22544', '5229', '6887', '7084', '7222', '7414', '8207', '8479', '8691', '8908', '9460', '9630', '10023', '10156', '10326', '10485', '10717', '11073', '11206', '11408', '11593', '11919', '12067', '12291', '12510', '12697', '13646', '13843', '14000', '14165', '14660', '14852', '15257', '15823', '16097', '16313', '16639', '16781', '16961', '17263', '17472', '17737', '17898', '18110', '18544', '18764', '19156', '19625', '20000', '20323', '20862', '22544']))
```
This test asserts that the output of the exon_find() function when LRG_1.xml is used as an input should be the two lists with the start and end points of each exon within the COL1A1 gene. If the values in the list produced by the function do not match when the test is run it will fail. 

The test for the chromosome_find() function is:
```
 def test_chromosome_find(self):
        result = lrg1.chromosome_find()
        self.assertEqual( result, ('17' , '48259457', '48284000'))
```
This test asserts that the output of the chromosome_find() function when LRG_1.xml is used as an input should be ( '17', '48259457', '48284000'), which corresponds to the chromosome number, the gene start coordinates and gene end coordinates. If this is not the case the test fails as it is not extracting the correct information. 

### Verification of the software
Before selecting an LRG of interest, use LRG_1 as a verification of the code to check that the software is running properly after installation of the programme. This LRG_1.xml file has previously been downloaded from the [LRG website](https://www.lrg-sequence.org/index.html) and is accessible in the GitHub repository.
The user should compare the output after running the software through python to the webpage http://ftp.ebi.ac.uk/pub/databases/lrgex/LRG_1.xml to check that the LRG exon coordinates match. This can be viewed under the LRG_1 transcript section under 'All exons including UTR'.

## Future improvements and considerations
- Have an automated process to extract XML files from the [LRG website](https://www.lrg-sequence.org/index.html), rather than having to manually download them. This is likely to eliminate the likelihood of introducing human error.
- To gather the GRCh37 coordinates for the start and end of each exon.

## Versioning
This is the only version of this software as it is an assignment due on 18/01/19 and so will not be reviewed or edited in the future. However when making the software different versions were commited to Github to show the progression of the software development.

## Authors
* **Natalie Card**
* **Rebecca Sadler**

The main [contributors](https://github.com/NatalieC15/Coding/graphs/contributors) who equally participated in this project.

## Acknowledgements
- [Software Carpentry Workshop](https://anenadic.github.io/2018-11-19-manchester/) team for teaching us how to code using python and GitBash
- Andy Brass for helping us develop the code
