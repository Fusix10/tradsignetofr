# Recherche de mots

def rechercher_mot(dictionnaire, mot):
    for francais, ireglif in dictionnaire.items():
        if mot == francais:
            return f"{mot} -> {ireglif}"
        if mot == ireglif:
            return f"{mot} -> {francais}"
    return "Mot non trouvé."

# Dictionnaire sous forme de données
mots = {
    "chat": "zrek",
    "chien": "darlu",
    "maison": "vornel",
    "arbre": "surbi",
    "soleil": "norlan",
    "lune": "feren",
    "terre": "kalro",
    "ciel": "nirto",
    "feu": "jalk",
    "eau": "xeni",
    "vent": "duvor",
    "sable": "rount",
    "nourriture": "belrim",
    "vêtements": "florbi",
    "voiture": "girnok",
    "livre": "jurfin",
    "porte": "nalbrin",
    "fenêtre": "serlut",
    "chaise": "tramel",
    "table": "yondar",
    "lit": "krelti",
    "mur": "dralok",
    "plafond": "yelkon",
    "route": "zarkul",
    "manger": "fustir",
    "boire": "grolen",
    "parler": "viklad",
    "marcher": "lervid",
    "regarder": "morfrin",
    "entendre": "dubrak",
    "penser": "maltra",
    "aimer": "jolbri",
    "jouer": "krenar",
    "dormir": "bultran",
    "apprendre": "glodir",
    "travailler": "korvin",
    "petit": "zarki",
    "grand": "virto",
    "rapide": "jurmel",
    "lent": "gansik",
    "fort": "rondal",
    "faible": "nufel",
    "chaud": "tremin",
    "froid": "kelbor",
    "joli": "brenik",
    "sale": "vuldro",
    "propre": "dirlen",
    "heureux": "gralti",
    "triste": "fonruk",
    "énervé": "mirgon",
    "amour": "dorfel",
    "vie": "jalko",
    "mort": "bruno",
    "rêve": "kalbri",
    "magie": "turvon",
    "force": "drentu",
    "liberté": "kormin",
    "paix": "furdal",
    "espoir": "zeldan",
    "je": "ka",
    "moi": "rok",
    "tu": "ja",
    "toi": "lir",
    "il": "ko",
    "elle": "ra",
    "nous": "fen",
    "vous": "tir",
    "ils": "ral",
    "elles": "nor",
    "et": "zi",
    "ou": "no",
    "mais": "rek",
    "si": "ji",
    "non": "gru",
    "oui": "bro",
    "bonjour": "fliron",
    "merci": "dolvir",
    "s’il vous plaît": "nultri",
    "au revoir": "serdu",
    "gauche": "firnol",
    "droite": "keltor",
    "devant": "narki",
    "derrière": "folmin",
    "pourquoi": "gronfir",
    "comment": "balruk",
    "quoi": "drenvil",
    "quand": "furnok",
    "danger" : "vronkil",
    "attention" : "flurak",
    "aide" : "kelsor",
    "fuir" : "dolmak",
    "ennemi" : "gruvel",
    "blessure" : "tarnok",
    "urgence" : "braltar",
    "risque" : "vildar",
    "piège" : "snarok",
    "protéger" : "darsil"
}

# Interface console
if __name__ == "__main__":
    print("Bienvenue dans le traducteur Français <-> Iréglif !")
    while True:
        mot_a_chercher = input("Entrez un mot à chercher (ou 'quit' pour quitter) : ").strip()
        if mot_a_chercher.lower() == "quit":
            print("Au revoir !")
            break
        resultat = rechercher_mot(mots, mot_a_chercher)
        print(resultat)