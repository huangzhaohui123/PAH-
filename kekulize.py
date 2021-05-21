from rdkit.Chem import AllChem
from rdkit import Chem
from molvs import standardize_smiles
change=open("kekuliz.smi","w")
file=open("C.smi","r")
for line in file:
    a=str(line)

    try:
        x=str(standardize_smiles(a))
        m = Chem.MolFromSmiles(x)
        Chem.Kekulize(m)
        Chem.SanitizeMol(m)
        change.write(a)
    except:
        print("no")
file.close()
change.close()