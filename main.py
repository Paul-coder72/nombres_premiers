def est_premier(nombre:int) -> bool:
    est_premier = True    
    racine_nombre = nombre ** 0.5
    for i in range(2, int(racine_nombre) + 1):
        if nombre % i == 0:
            return False
    
    return est_premier

def premiers_txt(nom_fichier: str="nombres_premiers.txt", liste_premiers: list=None) -> None:
    with open(nom_fichier, "w") as fichier:
        for nombre in liste_premiers:
            fichier.write(f"{nombre}\n")

def ecrire(arg: int|str, nom: str="fichier.txt") -> None:
    with open(nom, "a") as fichier:
        fichier.write(f"{arg}\n")

def ecrire_liste_bin(n=10000000):
    for i in range(n):
        if est_premier(i):
            ecrire(1)
        else:
            ecrire(0)

def liste_premiers() -> list:
    liste = []
    with open("premiers_10M.txt", "r") as fichier:
        for ligne in fichier:
            liste.append(int(ligne.strip()))

    return liste

def ecrire_liste_premiers_py(n=1000000):
    with open("liste_premiers.py", "w") as fichier:
        fichier.write("liste = [\n")
        for i in range(n):
            if est_premier(i):
                fichier.write(f"{i},\n")
        fichier.write("]\n")

ecrire_liste_premiers_py()
