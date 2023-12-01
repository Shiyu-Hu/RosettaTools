# -*- coding: utf-8 -*-

import os
import sys

#this messes up prolines at the N-termini, so handle those with the
#other proline atoms below
termini2R = {
  " H1 ": "1H  ",
  " H2 ": "2H  ",
  " H3 ": "3H  ",
}

termini2A = {  
  "1H  ":  " H1 ",
  "2H  ":  " H2 ",
  "3H  ":  " H3 ",
}

rename2R = {
# PDB3.2       ->  rosetta  
  ("ALA", " HB1"): "1HB ",
  ("ALA", " HB2"): "2HB ",
  ("ALA", " HB3"): "3HB ",
  ("ARG", " HB2"): "1HB ",
  ("ARG", " HB3"): "2HB ",
  ("ARG", " HG2"): "1HG ",
  ("ARG", " HG3"): "2HG ",
  ("ARG", " HD2"): "1HD ",
  ("ARG", " HD3"): "2HD ",
  ("ARG", "HH11"): "1HH1",
  ("ARG", "HH12"): "2HH1",
  ("ARG", "HH21"): "1HH2",
  ("ARG", "HH22"): "2HH2",
  ("ASN", " HB2"): "1HB ",
  ("ASN", " HB3"): "2HB ",
  ("ASN", "HD21"): "1HD2",
  ("ASN", "HD22"): "2HD2",
  ("ASP", " HB2"): "1HB ",
  ("ASP", " HB3"): "2HB ",
  ("CYS", " HB2"): "1HB ",
  ("CYS", " HB3"): "2HB ",
  ("CYS", " HB2"): "1HB ",
  ("CYS", " HB3"): "2HB ",
  ("GLN", " HB2"): "1HB ",
  ("GLN", " HB3"): "2HB ",
  ("GLU", " HB2"): "1HB ",
  ("GLU", " HB3"): "2HB ",
  ("GLU", " HG2"): "1HG ",
  ("GLU", " HG3"): "2HG ",
  ("GLN", " HG2"): "1HG ",
  ("GLN", " HG2"): "1HG ",
  ("GLN", " HG3"): "2HG ",
  ("GLN", " HG3"): "2HG ",
  ("GLN", " HG2"): "1HG ",
  ("GLN", " HG3"): "2HG ",
  ("GLN", "HE21"): "1HE2",
  ("GLN", "HE22"): "2HE2",
  ("GLY", " HA2"): "1HA ",
  ("GLY", " HA3"): "2HA ",
  ("HIS", " HB2"): "1HB ",
  ("HIS", " HB3"): "2HB ",
  ("ILE", "HG12"): "1HG1",
  ("ILE", "HG13"): "2HG1",
  ("ILE", "HG21"): "1HG2",
  ("ILE", "HG22"): "2HG2",
  ("ILE", "HG23"): "3HG2",
  ("ILE", "HD11"): "1HD1",
  ("ILE", "HD12"): "2HD1",
  ("ILE", "HD13"): "3HD1",
  ("LEU", " HB2"): "1HB ",
  ("LEU", " HB3"): "2HB ",
  ("LEU", "HD11"): "1HD1",
  ("LEU", "HD12"): "2HD1",
  ("LEU", "HD13"): "3HD1",
  ("LEU", "HD21"): "1HD2",
  ("LEU", "HD22"): "2HD2",
  ("LEU", "HD23"): "3HD2",
  ("LYS", " HB2"): "1HB ",
  ("LYS", " HB3"): "2HB ",
  ("LYS", " HG2"): "1HG ",
  ("LYS", " HG3"): "2HG ",
  ("LYS", " HD2"): "1HD ",
  ("LYS", " HD3"): "2HD ",
  ("LYS", " HE2"): "1HE ",
  ("LYS", " HE3"): "2HE ",
  ("LYS", " HZ1"): "1HZ ",
  ("LYS", " HZ2"): "2HZ ",
  ("LYS", " HZ3"): "3HZ ",
  ("MET", " HB2"): "1HB ",
  ("MET", " HB3"): "2HB ",
  ("MET", " HG2"): "1HG ",
  ("MET", " HG3"): "2HG ",
  ("MET", " HE1"): "1HE ",
  ("MET", " HE2"): "2HE ",
  ("MET", " HE3"): "3HE ",
  ("PHE", " HB2"): "1HB ",
  ("PHE", " HB3"): "2HB ",
  ("PRO", " H2 "): "1H  ", # this is a special case for termini
  ("PRO", " H3 "): "2H  ", # this is a special case for termini
  ("PRO", " HB2"): "1HB ",
  ("PRO", " HB3"): "2HB ",
  ("PRO", " HG2"): "1HG ",
  ("PRO", " HG3"): "2HG ",
  ("PRO", " HD2"): "1HD ",
  ("PRO", " HD3"): "2HD ",
  ("SER", " HB2"): "1HB ",
  ("SER", " HB3"): "2HB ",
  ("THR", "HG21"): "1HG2",
  ("THR", "HG22"): "2HG2",
  ("THR", "HG23"): "3HG2",
  ("TRP", " HB2"): "1HB ",
  ("TRP", " HB3"): "2HB ",
  ("TYR", " HB2"): "1HB ",
  ("TYR", " HB3"): "2HB ",
  ("TYR", "HG21"): "1HG2",
  ("TYR", "HG22"): "2HG2",
  ("TYR", "HG23"): "3HG2",
  ("VAL", "HG11"): "1HG1",
  ("VAL", "HG12"): "2HG1",
  ("VAL", "HG13"): "3HG1",
  ("VAL", "HG21"): "1HG2",
  ("VAL", "HG22"): "2HG2",
  ("VAL", "HG23"): "3HG2",
}


rename2A = {
# rosetta       ->   PDB3.2
  ("ALA", "1HB "): " HB1" ,
  ("ALA", "2HB "): " HB2" ,
  ("ALA", "3HB "): " HB3" ,
  ("ARG", "1HB "): " HB2" ,
  ("ARG", "2HB "): " HB3" ,
  ("ARG", "1HG "): " HG2" ,
  ("ARG", "2HG "): " HG3" ,
  ("ARG", "1HD "): " HD2" ,
  ("ARG", "2HD "): " HD3" ,
  ("ARG", "1HH1"): "HH11" ,
  ("ARG", "2HH1"): "HH12" ,
  ("ARG", "1HH2"): "HH21" ,
  ("ARG", "2HH2"): "HH22" ,
  ("ASN", "1HB "): " HB2" ,
  ("ASN", "2HB "): " HB3" ,
  ("ASN", "1HD2"): "HD21" ,
  ("ASN", "2HD2"): "HD22" ,
  ("ASP", "1HB "): " HB2" ,
  ("ASP", "2HB "): " HB3" ,
  ("CYS", "1HB "): " HB2" ,
  ("CYS", "2HB "): " HB3" ,
  ("CYS", "1HB "): " HB2" ,
  ("CYS", "2HB "): " HB3" ,
  ("GLN", "1HB "): " HB2" ,
  ("GLN", "2HB "): " HB3" ,
  ("GLU", "1HB "): " HB2" ,
  ("GLU", "2HB "): " HB3" ,
  ("GLU", "1HG "): " HG2" ,
  ("GLU", "2HG "): " HG3" ,
  ("GLN", "1HG "): " HG2" ,
  ("GLN", "1HG "): " HG2" ,
  ("GLN", "2HG "): " HG3" ,
  ("GLN", "2HG "): " HG3" ,
  ("GLN", "1HG "): " HG2" ,
  ("GLN", "2HG "): " HG3" ,
  ("GLN", "1HE2"): "HE21" ,
  ("GLN", "2HE2"): "HE22" ,
  ("GLY", "1HA "): " HA2" ,
  ("GLY", "2HA "): " HA3" ,
  ("HIS", "1HB "): " HB2" ,
  ("HIS", "2HB "): " HB3" ,
  ("ILE", "1HG1"): "HG12" ,
  ("ILE", "2HG1"): "HG13" ,
  ("ILE", "1HG2"): "HG21" ,
  ("ILE", "2HG2"): "HG22" ,
  ("ILE", "3HG2"): "HG23" ,
  ("ILE", "1HD1"): "HD11" ,
  ("ILE", "2HD1"): "HD12" ,
  ("ILE", "3HD1"): "HD13" ,
  ("LEU", "1HB "): " HB2" ,
  ("LEU", "2HB "): " HB3" ,
  ("LEU", "1HD1"): "HD11" ,
  ("LEU", "2HD1"): "HD12" ,
  ("LEU", "3HD1"): "HD13" ,
  ("LEU", "1HD2"): "HD21" ,
  ("LEU", "2HD2"): "HD22" ,
  ("LEU", "3HD2"): "HD23" ,
  ("LYS", "1HB "): " HB2" ,
  ("LYS", "2HB "): " HB3" ,
  ("LYS", "1HG "): " HG2" ,
  ("LYS", "2HG "): " HG3" ,
  ("LYS", "1HD "): " HD2" ,
  ("LYS", "2HD "): " HD3" ,
  ("LYS", "1HE "): " HE2" ,
  ("LYS", "2HE "): " HE3" ,
  ("LYS", "1HZ "): " HZ1" ,
  ("LYS", "2HZ "): " HZ2" ,
  ("LYS", "3HZ "): " HZ3" ,
  ("MET", "1HB "): " HB2" ,
  ("MET", "2HB "): " HB3" ,
  ("MET", "1HG "): " HG2" ,
  ("MET", "2HG "): " HG3" ,
  ("MET", "1HE "): " HE1" ,
  ("MET", "2HE "): " HE2" ,
  ("MET", "3HE "): " HE3" ,
  ("PHE", "1HB "): " HB2" ,
  ("PHE", "2HB "): " HB3" ,
  ("PRO", "1H  "): " H2 " ,
  ("PRO", "2H  "): " H3 " ,
  ("PRO", "1HB "): " HB2" ,
  ("PRO", "2HB "): " HB3" ,
  ("PRO", "1HG "): " HG2" ,
  ("PRO", "2HG "): " HG3" ,
  ("PRO", "1HD "): " HD2" ,
  ("PRO", "2HD "): " HD3" ,
  ("SER", "1HB "): " HB2" ,
  ("SER", "2HB "): " HB3" ,
  ("THR", "1HG2"): "HG21" ,
  ("THR", "2HG2"): "HG22" ,
  ("THR", "3HG2"): "HG23" ,
  ("TRP", "1HB "): " HB2" ,
  ("TRP", "2HB "): " HB3" ,
  ("TYR", "1HB "): " HB2" ,
  ("TYR", "2HB "): " HB3" ,
  ("TYR", "1HG2"): "HG21" ,
  ("TYR", "2HG2"): "HG22" ,
  ("TYR", "3HG2"): "HG23" ,
  ("VAL", "1HG1"): "HG11" ,
  ("VAL", "2HG1"): "HG12" ,
  ("VAL", "3HG1"): "HG13" ,
  ("VAL", "1HG2"): "HG21" ,
  ("VAL", "2HG2"): "HG22" ,
  ("VAL", "3HG2"): "HG23" ,
}

def replace_residues(lines):
    tmplines = []
    for line in lines:
        resname=line[17:20]
        if not line.startswith('ATOM'):
            continue
        if resname=='CYX':
            tmpline=line.replace('CYX','CYS')
            tmplines.append(tmpline)
        elif resname=='HID':
            tmpline=line.replace('HID','HIS')
            tmplines.append(tmpline)
        elif resname=='HIP':
            tmpline=line.replace('HIP','HIS')
            tmplines.append(tmpline)
        elif resname=='HIE':
            tmpline=line.replace('HIE','HIS')
            tmplines.append(tmpline)
        elif resname=='GLH':
            tmpline=line.replace('GLH','GLU')
            tmplines.append(tmpline)
        elif resname=='ASH':
            tmpline=line.replace('ASH','ASP')
            tmplines.append(tmpline)
        else:
            tmplines.append(line)
    return tmplines

def AtoR(amberpdb,rosettapdb):
    """
    amberpdb : amber pdb file path
    rosettapdb : changed rosetta pdb file path 
    """
    lines = open(amberpdb,'r').readlines()
    tmplines = replace_residues(lines)
    mutfile = open(rosettapdb,'w')       
    for line in tmplines:
        line = line.strip()
        res_name = line[17:20]
        atom_name = line[12:16]
        rosetta_name = atom_name # use this by default
        if (res_name, atom_name) in rename2R:
            rosetta_name = rename2R[(res_name, atom_name)]
        else:
            if atom_name in termini2R:
                rosetta_name = termini2R[atom_name]
        newline = line[:12] + rosetta_name + line[16:]
        mutfile.write("%s\n" % newline)
    mutfile.close()

def RtoA(rosettapdb, amberpdb, tmppath):
    """
    rosettapdb : rosetta pdb file path
    amberpdb : changed amber pdb file path
    tmppath: path to store tmp pdb files
    """
    lines=open(rosettapdb, 'r').readlines()
    #tmppath = os.getcwd()
    tmplines = []
    tmpfile = os.path.join(tmppath, "tmp.pdb")
    for line in lines:
        line = line.strip()
        if line.startswith('ATOM'):
            tmplines.append(line)
    with open(tmpfile, "w") as f:
        for line in tmplines:
            res_name = line[17:20]
            atom_name = line[12:16]
            amber_name = atom_name # use this by default
            if (res_name, atom_name) in rename2A:
                amber_name = rename2A[(res_name, atom_name)]
            else:
                if atom_name in termini2A:
                    amber_name = termini2A[atom_name]
            newline = line[:12] + amber_name + line[16:]
            f.write("%s\n" % newline)
    os.system("pdb4amber -i {} -o {}".format(tmpfile, amberpdb))
    pdbname = amberpdb.split(".pdb")[0]
    os.system("mv {}_nonprot.pdb ".format(pdbname)+tmppath)  
    os.system("mv {}_renum.txt ".format(pdbname)+tmppath)
    os.system("mv {}_sslink ".format(pdbname)+tmppath)

def main(choice, input_pdb, output_pdb, tmppath):
    if choice == "AtoR":
        AtoR(input_pdb, output_pdb)
    if choice == "RtoA":
        RtoA(input_pdb, output_pdb, tmppath)

if __name__ == "__main__":
   choice=sys.argv[1]; input_pdb=sys.argv[2]; output_pdb=sys.argv[3]; tmppath=sys.argv[4]
   main(choice, input_pdb, output_pdb, tmppath)
    


