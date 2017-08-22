#__Author__ Mohammed Sefath Chowdhury

Conformed CAD set file tree explanation:
# Current Directory //NYJOB900360/Common/4500 VDC/4510 VDC Documents/4510.05 CAD Files/
 - *20170609 Bulletin 10 Conformed CAD set*
   (Latest approved Conformed CAD)
 - *20170801 Current (Unapproved) Conformed CAD set*
   (Latest Unapproved Conformed CAD set)
 - *Bulletins Not yet Released*
   (Conformed CAD sets seperated by Bulletin (ie: If an indivisual needed the latest conformed set up until Bulletin 15)
 - *Bulletins Unzipped*
   (All seperate Bulletins for your review)

------------------------------------------------------------------------------------------------------------------
###User Instructions
'''
Manual Overide Process
1. Open *Bulletins Unzipped*
2. Create new folder with the corresponding date and Bulletin No. (*ie: 20170804 Bulletin 17*)
3. Open a new File browser folder
4. Navigate to and create new folder in *Bulletins Not yet Released* 
5. Copy and paste all contents of latest Conformed CAD Bulletin update into new Folder (ie: if Updating 
   Bulletin 18, the conformed CAD for Bulletin 17's contents should be copied into the Bulletin 18 Folder)
6. With the previous File browsing window, in *Bulletins Unzipped*, copy and paste the .dwg files to their 
   corresponding folder in the "Conformed CAD Bulletin 'No.'" Folder (ie: A-101B would go into:
   *.../Bulletins Not yet released/20170801 Bulletin 18 Conformed CAD set/Train Hall/VOL 1.2. Architecture*)
7. This "Bulletin 18 Conformed CAD set" is now the Latest Unapproved CAD set, replace the contents of the 
   *20170801 Current (Unapproved) Conformed CAD set*, folder with this new Bulletin 18's contents.
   
Automated Process
1. Open *directoryCreator.py* located in 'M:/4500 VDC/4510 VDC Documents/4510.05 CAD Files/Python Files/'
2. Run, and input date and number of the bulletin you are working with
3. Manually unzip and place all cad files into new Bulletin folder in *Bulletins Unzipped*
4. Run RenameScript.py -> will send all cad files into their respective subdirectories
 *(//Step 4 still has yet to be updated, please manually insert cad files into new Bulletin folder in *Bulletins Not yet Released*)*
 
   
#Make sure to update the latest Approved set as Buletins get approved, and similarly, update *Bulletins not yet Released* folder
-----------------------------------------------------------------------------------------------------------------

# CADAutomator
CADAutomator monitors the current working directory for any files with the .dwg extensions. 
While CADAutomator is running, any new files that appear in the running directory will automatically be processed by a command specified in a command file.


### Requirements
1. Python
2. The Python package
```

### Usage: CADAutomator.py -c/--command COMMAND -d/--dest DEST
#### Warning! Do not make DEST the same as the current working directory. This will cause an infinite loop.

COMMAND  is the command file

DEST     is the directory to move each initial .dwg file after MotionCor2 finishes processing it. A new folder will be created if DEST does not already exist.
