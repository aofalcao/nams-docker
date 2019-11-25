import  sys
import re
from math import sqrt


try:
    reload(recoder)
except:
    import recoder
    
try:
    reload(pybel)
except:
    import pybel 

try:
    reload(openbabel)
except:
    import openbabel



def recode(smiles):
    filout=sys.stdout
    rec=recoder.Recoder()
    mol=pybel.readstring("smi",smiles)
    can_smi = mol.write("can").strip()
    #print len(can_smi), mol.molwt, "...",
    mol, mol_info = rec.get_mol_info("can", can_smi, True, True)
    rec.export_mol_info(mol_info, 1, can_smi, filout, mol.molwt)

recode("CCC")

