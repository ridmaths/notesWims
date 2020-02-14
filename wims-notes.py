from latexTools import *
from datetime import date

#############################################################################

## Classe eleve 

class Eleve:
	def __init__(self,nom,notes,coeffs):
		self.nom = nom
		self.notes = notes
		self.coeffs = coeffs

	def moyenne(self):
		moy = 0
		for note in self.notes:
			moy += note
		moy = moy/sum(self.coeffs)
		return moy

	def __str__(self):
		return self.nom


class Feuille:
	def __init__(self,numero,nom):
		self.numero = numero
		self.nom = nom

	def __str__(self):
		return self.nom

## Constantes utiles

nomClasse = "2GT4"
dateAuj = date.today()

#############################################################################

## Lecture du csv 

fichier = open("notes-wims.csv","r")
contenu = fichier.read()
fichier.close()

## Extratction des données eleves

listeEleves = contenu.split("\n")[3:-1] # On récupère sous forme STR tous les données de la classe
coeffs=[1,1,1,1] # On rajoute les coeffs pour chaque feuille

dictEleves = [] # On va ajouter chaque élève dans ce dictionnaire

# On parcourt chaque élève de la liste
for eleve in listeEleves:
	nom = eleve.split(",")[0].replace('"','') # On récupère le nom
	notesStr = eleve.split(",")[1:] # On récupère les notes sous forme STR
	notesFloat = [float(note) for note in notesStr] # Conversion des notes en float
	el = Eleve(nom,notesFloat,coeffs) # On crée l'objet ELEVE correspondant
	dictEleves.append(el) # On ajoute l'eleve


## Extratction des données feuille

listeFeuilles = contenu.split("\n")[0:2]
ligne1 = listeFeuilles[0].split(",")[1:]
ligne2 = listeFeuilles[1].split(",")[1:]
taille = len(ligne1)

dictFeuilles = []

for k in range(taille):
	numero = ligne1[k][-1]
	nom = ligne2[k].replace('"','')
	feuille = Feuille(numero,nom)
	dictFeuilles.append(feuille)


#############################################################################


## On construit le document latex 

# Début document avec le titre

document = f'''\\thispagestyle{{empty}}
\\large
\\begin{{center}}
\\textbf{{Notes des feuilles WIMS - {nomClasse} - MAJ du {dateAuj.strftime("%d/%m/%Y")}}}
\\end{{center}}

'''


# Début tableau
document += "\\begin{center} \n"
document += f"\\begin{{tabular}}{{|l|*{{{taille+1}}}{{c|}}}} \n"

# Création de la première ligne du tableau
document += "\\hline \n"
document += "\\textbf{Nom / Feuille}"
for k in range(taille):
	document += f" & Feuille {dictFeuilles[k].numero}"
document += " & {\\color{red} Moyenne }"
document += " \\\\ \n"

# On remplit le tableau avec les données élèves

for eleve in dictEleves:
	document += "\\hline \n"
	document += eleve.nom
	for note in eleve.notes:
		document += f" & {note}"
	document += f" & {{ \\color{{red}} {round(eleve.moyenne(),1)} }}"
	document += " \\\\ \n"

document += "\\hline \n"
document += "\\end{tabular} \n"
document += "\\end{center} \n \n"

# On rajoute la légende pour les feuilles 

document += "\\textbf{{Légende : }} \n" 
document += "\\begin{itemize} \n"
for feuille in dictFeuilles:
	document += f''' \\item Feuille {feuille.numero} : {feuille.nom} \n'''
document += "\\end{itemize}"

# print(document)  # TEST pour voir le doc construit

## Fin construction du document

#############################################################################

## Export en LaTex

docTex = doc_latex(document)

nomDoc = "notes"+dateAuj.isoformat()[4:]
exportLatex(nomDoc,docTex)
compLatex2pdf(nomDoc)