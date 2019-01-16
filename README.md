# Programming Module Assignment - The user manual 
## Section 1: The user requirements
The assignment for the programming module (BIOL68400) was to create a software that generates a Browser Extensible Data (BED) file from a file in a XML format containing Locus Reference Genomic (LRG) data of a region of interest (ROI).

An XML file covering the ROI can be obtained from the [LRG website](https://www.lrg-sequence.org/index.html).
LRG provides manually curated, stable reference sequences that have been generated and maintained by NCBI and EMBL-EBL. These reference sequences are designed in order to report variants consistently according to clinical reporting standards. LRG provides annotation and mapping data that define the relationship between the LRG "fixed" section sequences, the genome reference assembly (both GRCh37 and GRCh38) and all the known transcripts from RefSeq and GENCODE. The "fixed" section contains the stable genomic DNA sequence for the ROI, transcripts and proteins that are essential for reporting variants and a specific LRG exon numbering system. These highly structured records are accessible through an extensible mark-up language i.e. the XML format. (reference https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3965024/)

A BED file is a flexible way of defining data lines displayed in an annotation track. There are three required fields that form a BED file:
- chrom - which is the chromosome name that the reference sequence is on
- chromStart - which is the starting position of the sequence within the chromosome 
- chromEnd - which is the end position of the feature within the chromosome
There are nine optional fields of a BED file: name, score, strand, thickStart, thickEnd, itemRgb, blockCount, blockSizes, blockStarts. For this assignment only the three required fields were of interest. 
(reference https://genome.ucsc.edu/FAQ/FAQformat.html#format1) 

An example of a BED file with just the required fields would be:
```
chr7  127471196 127472363
chr7  127572363 127473530
chr7  127473530 127474697
chr7  127474697 127475864
chr7  127475864 127477031
```
The first column contains the chromosome number, the second the start position and the third the end position. 

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

## Section 2: Getting Started (Becca part)
Instructions to get the a copy of the project up and running for development and testing purposes
### Prerequisites (What needs to be installed to run the software and how to install them - maybe give examples?)

### Installing (a step by step series of examples that tell you how to get everything running - with examples)

## Section 3: Running the code
After installing the required programmes. Using GitBash, the cd command should be entered to move to the correct directory that contains both the XML file of interest and the pythontest.py. As a check to determine that the user is in the correct directory the ls command should be used. See below:
```
~
$ cd Desktop/Coding/XML_files/
~/Desktop/Coding/XML_files (master)
$ ls
```
The output of this code would be:
```
LRG_1.xml pythontest.py
```
To run the code python should be used. Below is an example of how to run the programme and what the output of this should be:
```
~/Desktop/Coding/XML_files (master)
$ python pythontest.py
Enter LRG file number of interest: 
```
A numerical value can now be entered into the command line, this value is dependent on which LRG file has been previously downloaded. Only a number can be entered and negative numbers should not be used. See Section 4 for examples of error messages for invalid entries. After pressing 'ENTER', the software will run automatically and the output will be the ElementTree structure for which the remaining codes are based from to obtain the information to go into the BED file. The second part of the output is a statement to say that the LRG bed file has been created for the gene of interest from the LRG XML file that was input into the software.
```
$ python pythontest.py
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

## Section 4: The tests and their functions
### Input validation
The first tests incorporated into this software code confirm that the software responds correctly to all kinds of inputs. This is to eliminate human error and ensure that the correct LRG XML file has been selected. 
The entry of this software is a numerical value which corresponds to a XML file of interest. If any non-numerical value is entered the code will trigger an error and remind the user to enter a numerical value only. See below as an example of when 'one' is entered instead of '1':
```
$ python pythontest.py
Enter LRG file number of interest: one
Invalid input, please enter a numeric value 
Enter LRG file number of interest:_
```
The error would also be expressed if a symbol is entered instead e.g. !"£$%^&*().

The second input test determines whether or not the XML file has been downloaded by the user correctly. The output of the test when there is an error is for the user to then check that the file is located in the correct folder and has been saved in the right format e.g. LRG_(number).xml. An example is:
```
$ python pythontest.py
Enter LRG file number of interest: 2
Error, check the correct LRG XML file has been downloaded from https://www.lrg.sequence.org/, saved into the right folder (i.e. XML_files) with the correct format (e.g. LRG_1.xml).
```
### Function tests
??google pytest see if can add anymore tests

### Verification of the software
Before selecting an LRG of interest, use LRG_1 as a verification of the code to check that the software is running properly after installation of the programme. This LRG_1.xml file has previously been downloaded from the [LRG website](https://www.lrg-sequence.org/index.html) and is accessible in the GitHub repository.
The user should compare the output after running the software through python to the [LRG_1 webpage](https:ftp.ebi.ac.uk/pub/databases/lrgex/LRG_1.xml) to check that the LRG exon coordinates match. This can be viewed under the LRG_1 transcript section under 'All exons including UTR'.


## Section 5: Future considerations
- Have an automated process to extract XML files from the [LRG website](https://www.lrg-sequence.org/index.html), rather than having to manually download them. This is likely to eliminate the likelihood of introducing human error.
- To gather the GRCh37 coordinates for the start and end of each exon.

## Section 6: Versioning
This is the only version of this software as it is an assignment due on 18/01/19 and so will not be reviewed or edited in the future. 

## Authors
* **Natalie Card**
* **Rebecca Sadler**

The main [contributors](https://github.com/NatalieC15/Coding/graphs/contributors) who equally participated in this project.

## Acknowledgements
- [Software Carpentry Workshop](https://anenadic.github.io/2018-11-19-manchester/) team for teaching us how to code using python and GitBash
- Andy Brass for helping us develop the code
