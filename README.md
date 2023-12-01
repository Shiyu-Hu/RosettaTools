# RosettaTools
Here contains useful python scripts during MD simulations using Rosetta and Amber.
## convert_file_type.py
convert pdb file to be used in Rosetta or Amber.
### usage:
1. convert Amber formatted PDB file to Rosetta formmated PDB file:  
  python convert_file_type.py AtoR ./example/5hn1.pdb ./exampel/5hn1_to_ros.pdb ./example/tmp  
 - 5hn1.pdb: input Amber PDB file  
 - 5hn1_to_ros.pdb: output Rosetta PDB file  
2. convert Rosetta formatted PDB file to Amber formmated PDB file:  
  python convert_file_type.py RtoA ./example/5hn1_ros.pdb ./exampel/5hn1_to_amber.pdb ./example/tmp  
- 5hn1_ros.pdb: input Rosetta PDB  
- 5hn1_to_amber.pdb: output Amber PDB  
- tmppath: path to store tmp files
## Required third-party software:
1. Amber22
2. Rosetta2017
3. Python3
