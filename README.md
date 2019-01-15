# Programming Module Assignment 
## The user manual
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

## Running the code
After installing the required programmes. Using the gitBash programme, the cd command should be used to move to the correct directory that contains both the XML file of interest.
the Explain how to run the automated tests for this system
```
What does the code do? 
Describe the code 
```
### The tests and their functions
What are the tests?
??google pytest see if can include one of these 

## The output of the code
What to expect?

## Verification LRG
Before selecting an LRG of interest, use LRG_1 as a verification of the code. 

## Future considerations
- Have an automated process to extract XML files from the LRG website.
- 

## Authors
* **Natalie Card**
* **Rebecca Sadler**

The main [contributors](https://github.com/NatalieC15/Coding/graphs/contributors) who participated in this project.



