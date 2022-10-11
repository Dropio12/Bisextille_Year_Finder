import Bisextille_Finder as bf

def main():
    annee_début = int(input("Entrez une année de début: "))
    annee_fin = int(input("Entrez une année de fin: "))
    print("Les années bisextilles entre "+ str(annee_début)+" et "+str(annee_fin)+" sont:")
    for i in range(annee_début, annee_fin+1):
        if bf.Determiner_Annee_Bisextille(i)== True:
            print(str(i))
if __name__ == "__main__":
    main()