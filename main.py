import Bisextille_Finder as bf

def main():
    annee_début = int(input("Entrez une année de début: "))
    annee_fin = int(input("Entrez une année de fin: "))
    for i in range(annee_début, annee_fin+1):
        if bf.Determiner_Annee_Bisextille(i)== True:
            print(str(i) + " est bisextille")
        else:
            print(str(i)+" n'est pas bisextille")

if __name__ == "__main__":
    main()