# Programming Module Assignment - The user manual 
# Section 1:
The assignment for the programming module (BIOL68400) was to create a software that generates a Browser Extensible Data (BED) file from a file in a XML format containing Locus Reference Genomic (LRG) data of a region of interest. 
The XML file was obtained from the [LRG website](https://www.lrg-sequence.org/index.html).
The LRG website provides manually curated, stable reference sequences that have been generated and maintained by NCBI and EMBL-EBL. These reference sequences are designed in order to report variants consistently according to clinical reporting standards. LRG provides annotation and mapping data that define the relationship between the LRG "fixed" section sequences, the genome reference assembly (both GRCh37 and GRCh38) and all the known transcripts from RefSeq and GENCODE. The "fixed" section contains the stable genomic DNA sequence for the region of interest (ROI), transcripts and proteins that are essential for reporting variants and a specific LRG exon numbering system. These highly structured records are accessible through an extensible mark-up language i.e. the XML format. (reference https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3965024/)

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
## Getting Started (Becca part) 

### Prerequisites (What needs to be installed to run the software and how to install them - maybe give examples?)

### Installing (a step by step series of examples that tell you how to get everything running - with examples)

# Section 2:
## Running the code
After installing the required programmes. Using the GitBash programme, the cd command should be entered to move to the correct directory that contains both the XML file of interest and the pythontest.txt. As a check to determine that the user is in the correct directory the ls command should be used. See below:
```
~
$ cd Desktop/Coding/XML_files/
~/Desktop/Coding/XML_files (master)
$ ls
```
The output of this code would be:
```
LRG_1.xml pythontest.txt
```
To run the code python should be used. Below is an example of how to run the programme and what the output of this should be:
```
~/Desktop/Coding/XML_files (master)
$ python pythontest.txt
Enter LRG file number of interest: 
```
A numerical value can now be entered into the command line, this value is dependent on what LRG file have been previously downloaded. Only a number can be entered and negative numbers should not be used. See below for invalid entries. After pressing 'ENTER', the software will run automatically and the output will be the ElementTree structure for which the remaining codes are based from to obtain the information to go into the BED file. The second part of the output is a statement to say that the LRG bed file has been created for the gene of interest from the LRG XML file that was input into the software.
```
$ python pythontest.txt
Enter LRG file number of interest: 1
```
Output is the tree structure as well as:
```
LRG_1.bed file created for the gene COL1A1 from the LRG_1.xml file
```
The potential differences between the output would be the BED file name, gene name and XML file name.

# Section 3:
## The tests and their functions
### Input validation
What are the tests?
The main tests incorporated into this software is to confirm that it responds correctly to all kinds of inputs.

??google pytest see if can add anymore tests

### Verification of the software
Before selecting an LRG of interest, use LRG_1 as a verification of the code. 
Another test is a visual test to check that the code is running properly after being downloaded. This requires the user to firstly download the LRG_1 file from the [LRG website](https://www.lrg-sequence.org/index.html) to the correct XML_files folder. The software can then be run using python 

## Future considerations
- Have an automated process to extract XML files from the [LRG website](https://www.lrg-sequence.org/index.html), rather than having to manually download them. This is likely to eliminate the likelihood of introducing human error.
- 

## Authors
* **Natalie Card**
* **Rebecca Sadler**

The main [contributors](https://github.com/NatalieC15/Coding/graphs/contributors) who equally participated in this project.



