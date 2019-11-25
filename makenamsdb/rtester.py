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


def recode_file(fname_in, fname_out):
    rec=recoder.Recoder()
    hs=False
    filin=open(fname_in, "rt")
    lins=filin.readlines()
    filin.close()

    filout=open(fname_out, "wt")
    #filout_tr=open(fname_out+"_tr.nams", "wt")
    #filout_te=open(fname_out+"_te.nams", "wt")
    for lin in lins[1:]:
        ch_id, smi, act, cls = lin.split("\t")
        cid=int(ch_id.split("CHEMBL")[1])
        try:
            mol=pybel.readstring("smi",smi)
            can_smi = mol.write("can").strip()
        except:
            print(cid, "oops! cannot convert smiles: ", smiles.strip())
            continue
        hs=True if len(can_smi)==1 else False
        print(cid, len(can_smi), mol.molwt, "...",)
        if not hs and mol.molwt<800:
            #filout=filout_tr
            #if random.random()<0.2: filout=filout_te
            mol, mol_info = rec.get_mol_info("can", can_smi, hs, True)
            if mol:
                rec.export_mol_info(mol_info, cid, can_smi, filout, mol.molwt)
            else:
                print("molecule too small", smiles)
            print("Done")
        else:
            print("passed!")
    #filout_tr.close()
    #filout_te.close()
    filout.close()


def recode(smiles):
    filout=sys.stdout
    rec=recoder.Recoder()
    mol=pybel.readstring("smi",smiles)
    can_smi = mol.write("can").strip()
    #print len(can_smi), mol.molwt, "...",
    mol, mol_info = rec.get_mol_info("can", can_smi, True, True)
    rec.export_mol_info(mol_info, 1, can_smi, filout, mol.molwt)

recode("CCC")


#if __name__=="__main__":
#    import sys
#    try:
#        
#        recode_file(sys.argv[1], sys.argv[2])
#    except:
#        print "Usage: namsdb mol_file_name nams_file_name [format=[smi|inchi] [colmol=1] [colid=2]"


