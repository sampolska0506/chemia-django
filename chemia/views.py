from rdkit.Chem import Draw
from django.shortcuts import render
import py3Dmol
from rdkit import Chem
from rdkit.Chem import AllChem

viewOption = "2d"
def main(request):
    global viewOption
    kod = "C1CCC1"
    if "kod" in request.GET:
        kod = request.GET["kod"]
        print("Nowy kod: " + kod)


    if "view" in request.GET:
        if request.GET["view"] == "2d":
            viewOption = "2d"
        elif request.GET["view"] == "3d":
            viewOption = "3d"

    context = {
        'kod': kod,
        'viewOption': viewOption,
    }

    smiles = kod

    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)

    print("MOL: ", mol)

    img = Draw.MolToImage(mol)
    img.save('static/mol2d.png')

    AllChem.EmbedMolecule(mol)
    AllChem.UFFOptimizeMolecule(mol)

    mb = Chem.MolToMolBlock(mol)

    view = py3Dmol.view(width=500, height=500)
    view.addModel(mb, "mol")
    view.setStyle({"stick": {}})
    view.zoomTo()


    html = view._make_html()

    with open("./static/molekula.html", "w") as f:
        f.write(html)

    return render(request, 'main.html', context)

def chemia(request):
    return render(request, 'nowa.html')

