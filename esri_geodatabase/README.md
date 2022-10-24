# Esri GeoDatabase Template

This material contains both a template Esri File Geodatabase (FGDB) and the python script
used by the NENA Data Model Working Group to generate the FGDB. This Data Model is designed 
for users of Esri products but can also be consumed by a number of other open source GIS 
platforms.

## Getting Started

### Dependencies

* Operating System: Windows 10 (or later)
* GIS Software: ArcGIS 10.2 (or later) AND/OR ArcGIS Pro 1.x (or later)

### Installing

The folder ending with the extension ".gdb" is the template FGDB. If only interested in the template 
FGDB itself, this and the files it contains is the only content one needs to acquire. The folder can 
be placed on the target machine and then connected to via a suitable GIS application.

If interested in creating the template FGDB from a python script, the dependencies should first be met.
Once either ArcGIS 10.2 (or later) or ArcGIS Pro 1.x (or later) has been installed the 
esri_data_template_creation.py script can be downloaded to the target machine meeting the dependencies.  
	* 1) Place the python script on the target machine containing either (or both) of the two GIS software 
	   products.
	* 2) Open a command prompt by clicking on the "Start" icon, typing "cmd" and pressing enter
	* 3) Change directory (i.e. using the "cd" command) to the folder containing the python script
	* 4) Execute the script by typing "python esri_data_template_creation.py" and pressing enter
	* 5) The template FGDB can be found in the same directory as the python script
	* 6) To re-run the script, you will need to delete the previously created FGDB.  The script will not
		overwrite an existing FGDB.

## Help

For assistance please visit https://www.nena.org/page/DataStructures where contact information for the
leadership of the Data Structures Committee can be found.  

## Authors

Contributors names and contact info

Jason Horning, ENP

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release