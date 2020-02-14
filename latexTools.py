import os

def doc_latex(contenu):
	'''Ajoute le texte contenu dans un document latex prerempli'''
	document = '''\\documentclass[12pt,a4paper]{article} 
  
\\usepackage[utf8]{inputenc} 
\\usepackage[french]{babel} 
\\usepackage[T1]{fontenc} 
\\usepackage{fourier} 
\\usepackage{amsmath,amsfonts,amssymb} 
\\usepackage[left=2cm,right=2cm,top=1cm,bottom=0.5cm]{geometry} 
\\usepackage{xcolor} 
\\usepackage{multicol}
\\usepackage{graphicx}
 
\\setlength\\parindent{0mm}

'''
	document += '''\\begin{document}

'''
	document += contenu
	document += '''

\\end{document}'''

	return document


def exportLatex(nom,document):
	nomComplet = nom+".tex"
	fichier = open(nomComplet,"w",encoding="UTF-8")
	fichier.write(document)
	fichier.close()

def compLatex2pdf(nom):
	nomComplet = nom+".tex"
	commande1 = "pdflatex -quiet "+nomComplet
	print("[*] Compilation latex vers pdf")
	os.system(commande1)
	print("[*] Suppression des fichiers inutiles")
	Ext = [".log",".aux",]
	for e in Ext:
		commande2 = "del "+nom+e
		os.system(commande2)
	print("[*] Execution terminee")



#doc = doc_latex("COUCOU les amis, comment vaaaaaaaaaaaaa")
#exportLatex("salut",doc)
#compLatex2pdf("salut")