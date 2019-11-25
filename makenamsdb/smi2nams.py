#!/opt/conda/bin/python3.7
import sys
import recoder
import pybel 
import openbabel

def recode(smiles):
    filout=sys.stdout
    rec=recoder.Recoder()
    mol=pybel.readstring("smi",smiles)
    can_smi = mol.write("can").strip()
    mol, mol_info = rec.get_mol_info("can", can_smi, True, True)
    rec.export_mol_info(mol_info, 1, can_smi, filout, mol.molwt)

recode sys.argv[1]

