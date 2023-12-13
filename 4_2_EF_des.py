import random

def simulation_des(n):
    occurences = [0] * 11  # Liste pour compter les occurrences de chaque somme possible (2 à 12)
    total_simulations = n
    
    for _ in range(total_simulations):
        de1 = random.randint(1, 6)  # Lancer du premier de
        de2 = random.randint(1, 6)  # Lancer du deuxieme de
        somme = de1 + de2  # Calcul de la somme
        
        occurences[somme-2] += 1  
    
    print("Résultats de la simulation pour", total_simulations, "lancers de dés :")
    print("Somme\tProbabilité\tOccurrences")
    
    for i, occurence in enumerate(occurences):
        somme = i + 2  # Ajouter 2 pour obtenir la somme
        probabilite = occurence / total_simulations  # Calcul de la probabilité
        
        print(somme, "\t", probabilite, "\t\t", occurence)

# Demander a l'utilisateur le nombre de simulations a effectuer
nombre_simulations = int(input("Combien de fois voulez-vous simuler le lancer de deux dés ? "))

# simulation
simulation_des(nombre_simulations)
