import statistics as st

nombres= input("Entrer  des nombres espacés)")
#variable qui convertit la chaine de caractere en liste de nombres
valeurs = [float(i) for i in nombres.split()]
#calcul
mode= st.mode(valeurs)
ecart_type= st.stdev(valeurs)
#afficher les valeurs
print("les valeur entres sont ;", valeurs)
print("le mode est :",mode)
print("l'ecart type est :",ecart_type)
