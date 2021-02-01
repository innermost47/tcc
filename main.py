import time

def menu():
    choix = input(
        "Que préfères tu faire maintenant ? Gérer un épisode en lien avec de la colère ou faire de la restructuration cognitive ? colère/restructuration")
    if choix == "colère":
        colère()
    if choix == "restructuration":
        restructuration()

def menu2():
    choix = input(
        "Que préfères tu faire maintenant ? Gérer un épisode en lien avec de la colère, faire de la restructuration cognitive ou t'arrêter là ? colère/restructuration/stop")
    if choix == "colère":
        colère()
    if choix == "restructuration":
        restructuration()
    if choix == "stop":
        print("Ok ! Je te remercie pour ta participation à ce programme de TCC ! À bientôt" + username + " !")

def colère():
    def programme():
        protagoniste = input("Tout d'abord, quel est le prénom de la personne avec laquelle la situation contrariante dont tu as envie de me parler est arrivée ? ")
        print("Ok, merci ;) ")
        time.sleep(2)
        input(
            "Alors dis moi, quelle est la situation qui t'a mis en colère avec " + protagoniste + " ? Décris la moi de la manière la plus objective possible: ")
        time.sleep(2)
        print("Ok... J'imagine qu'en effet tu ais pu te sentir en colère...")
        time.sleep(3)
        grave = input("Et en même temps... J'ai envie de te poser une petite question... Avec toute ma bienveillance... Si tu prends le temps d'y réfléchir... Est ce que c'est grave ? oui/non ")
        if grave == "oui":
            time.sleep(2)
            input("Avec toute ma sympathie... En quoi est ce grave ? ")
            print("Ok... Je comprends...")
            time.sleep(2)
            input("Et en même temps... En quoi est ce grave ? ")
            print("D'accord...")
            time.sleep(2)
            question = input("Est ce que tu es ok pour continuer le programme ? oui/non ")
            if question == "oui":
                input("D'après toi, comment " + protagoniste + " perçoit cette situation ? ")
                print("ok. Très bien.")
                time.sleep(2)
                input("D'après toi, quelles sont les pensées de " + protagoniste + " vis à vis de cette situation ? ")
                print("ok ;)")
                time.sleep(2)
                input("Quelles sont ses émotions ? ")
                print("En effet c'est possible...")
                time.sleep(2)
                input("Qu'est ce qui est important pour " + protagoniste + " dans cette situation ? ")
                print("Effectivement, c'est probable...")
                time.sleep(2)
                input("Que penses tu pouvoir apprendre de " + protagoniste + " dans cette situation ? ")
                print("En effet, c'est une bonne piste...")
                time.sleep(2)
                input("Dis moi, en quoi " + protagoniste + " est différent de toi " + username + " ? ")
                print("Ok.")
                time.sleep(2)
                input("Et quels sont vos points communs ? ")
                print("D'accord.")
                time.sleep(2)
                input("Comment cela serait pour toi de te sentir comme " + protagoniste + " dans cette situation ? ")
                print("Je comprends " + username + ".")
                time.sleep(4)
            else:
                print("D'accord...")
                time.sleep(3)
                input("Comment est ce que tu te sens ici et maintenant ? ")
                print("J'imagine oui...")
                time.sleep(2)
                answer = input("Que souhaites tu faire maintenant ? Voir une autre situation, retourner au menu ou t'arrêter là ? (situation/menu/stop) ")
                if answer == "situation":
                    programme()
                if answer == "menu":
                    menu2()
                else:
                    print("Ok ! Je te remercie pour ta participation à ce programme de TCC ! À bientôt" + username + " !")

        else:
            time.sleep(2)
            print("Ok.")
            input("D'après toi, comment " + protagoniste + " perçoit cette situation ? ")
            print("ok. Très bien.")
            time.sleep(2)
            input("D'après toi, quelles sont les pensées de " + protagoniste + " vis à vis de cette situation ? ")
            print("ok ;)")
            time.sleep(2)
            input("Quelles sont ses émotions ? ")
            print("En effet c'est possible...")
            time.sleep(2)
            input("Qu'est ce qui est important pour " + protagoniste + " dans cette situation ? ")
            print("Effectivement, c'est probable...")
            time.sleep(2)
            input("Que penses tu pouvoir apprendre de " + protagoniste + " dans cette situation ? ")
            print("En effet, c'est une bonne piste...")
            time.sleep(2)
            input("Dis moi, en quoi " + protagoniste + " est différent de toi " + username + " ? ")
            print("Ok.")
            time.sleep(2)
            input("Et quels sont vos points communs ? ")
            print("D'accord.")
            time.sleep(2)
            input("Comment cela serait pour toi de te sentir comme " + protagoniste + " dans cette situation ? ")
            print("Je comprends " + username + ".")
            time.sleep(4)

    programme()
    input("Comment est ce que tu te sens ici et maintenant ? ")
    print("J'imagine oui...")
    time.sleep(2)
    answer = input("Que souhaites tu faire maintenant ? Voir une autre situation, retourner au menu ou t'arrêter là ? (situation/menu/stop) ")
    if answer == "situation":
        programme()
    if answer == "menu":
        menu2()
    else:
        print("Ok ! Je te remercie pour ta participation à ce programme de TCC ! À bientôt" + username + " !")


def restructuration():
    def croyances_irrationnelles():
        print("1- Évaluation négative de soi: te voir toi même ainsi que tes capacités de manière négative.")
        print()
        print("2- Évaluation négative des autres: voir les autres, leurs motivations, leurs intentions et leurs capacités négativement.")
        print()
        print("3- Évaluation négative des situations: t'attendre à des conséquences négatives et voir seulement les aspects négatifs d'une situation.")
        print()
        print("4- Pensée catastrophe: croire que le pire scénario se réalisera.")
        print()
        print("5- Les fausses obligations: avoir des attentes ou des exigences excessives.")
        print()
        print("6- Lire dans l'esprit des autres: croire que tu sais ce que les autres pensent ou ressentent en te basant sur leurs actions.")
        print()
        print("7- Attendre que les autres lisent dans tes pensées: croire que les autres devraient savoir ce que tu penses ou veux.")
        print()
        print("8- S'étiqueter: utiliser des étiquettes négatives pour te décrire.")
        print()
        print("9- Étiqueter les autres: utiliser des étiquettes négatives pour décrire les autres.")
        print()
        print("10- Généraliser: croire que ce qu'il s'est passé dans une situation est suceptible de se reproduire dans une autre situation.")
        print()
        print("11- Blâmer: avoir des attentes à propos du comportement des autres et critiquer autrui.")
        print()
        print("12- Contrôle interne: croire que tu devrais contrôler toutes les situations et que les résultats sont seulement le fruit de tes efforts.")
        print()
        print("13- Contrôle externe: croire que tout ce qu'il t'arrive est dû à la chance ou au destin, de telle sorte que tu n'en n'es pas responsable.")
        print()
        print("14- Personnalisation: croire que le comportement des autres ainsi que leurs réactions sont en rapport avec toi.")
        print()
        print("15- Raisonnement émotionnel: croire qu'une émotion représente la réalité sans évaluer les preuves.")
        print()

    def émotions():
        print("Ok.")
        print("Et lorsque tu te remémores cette situation, quelle est la principale émotion que tu ressens ? ")
        emotion = ""
        while emotion != "colère" and emotion != "peur" and emotion != "tristesse" and emotion != "joie" and emotion != "honte" and emotion != "culpabilité" and emotion != "regret" and emotion != "dégoût" and emotion != "confusion" and emotion != "surprise" and emotion != "mépris":
            emotion = input("colère - mépris - peur - tristesse - joie - honte - culpabilité - regret - dégoût - confusion - surprise ? ")

    def échelle():
        print("Très bien.")
        answer2 = ""
        while answer2 != "1" and answer2 != "2" and answer2 != "3" and answer2 != "4" and answer2 != "5" and answer2 != "6" and answer2 != "7" and answer2 != "8" and answer2 != "9" and answer2 != "10":
            answer2 = input("Sur une échelle de 1 à 10, 1 étant la valeur la plus faible et 10 la plus forte, quelle est l'intensité de ton ressenti ? ")

    def programme():
        print()
        print("Alors, dis moi, quelle est la situation dont tu as envie de me parler présentement ? ")
        input("Je t'invite à me la décrire de la manière la plus objective possible: ")
        print()
        time.sleep(1)
        émotions()
        time.sleep(2)
        print()
        échelle()
        time.sleep(2)
        print()
        print("Maintenant je t'invite à faire attention aux pensées que tu as lorsque tu te remémores cette situation.")
        time.sleep(1)
        input("Quelles sont elles ? ")
        print()
        time.sleep(1)
        print("Ok.")
        answer3 = ""
        while answer3 != "1" and answer3 != "2" and answer3 != "3" and answer3 != "4" and answer3 != "5" and answer3 != "6" and answer3 != "7" and answer3 != "8" and answer3 != "9" and answer3 != "10":
            answer3 = input("Sur une échelle de 1 à 10, 1 étant la valeur la plus faible et 10 la plus forte, quelle est ton degré de confiance dans ces pensées ? ")
        time.sleep(1)
        print()
        print("Très bien. Penser sur sa pensée est un exercice favorable aux changements de comportements.")
        print("Je te félicite pour ton implication dans ce travail.")
        time.sleep(2)
        print()
        print("Je vais maintenant te partager une liste de croyances irrationnelles courantes:")
        time.sleep(3)
        print()
        croyances_irrationnelles()
        print("D'après toi, les pensées que tu as par rapport à cette situation sont en lien avec quel type de croyances irrationnelles ? ")
        input("(Peut être que la croyance en question n'est pas dans la liste, je te laisse le soin de personnaliser ce point): ")
        print("D'accord.")
        time.sleep(3)
        print()
        print("Et maintenant, je t'invite à repenser la situation que tu m'as partagé d'une manière différente et plus réaliste.")
        time.sleep(2)
        print()
        input("Je te laisse me décrire cette nouvelle façon de voir: ")
        time.sleep(2)
        print()
        answer4 = ""
        while answer4 != "1" and answer4 != "2" and answer4 != "3" and answer4 != "4" and answer4 != "5" and answer4 != "6" and answer4 != "7" and answer4 != "8" and answer4 != "9" and answer4 != "10":
            answer4 = input("Sur une échelle de 1 à 10, 1 étant la valeur la plus faible et 10 la plus forte, quelle est ton degré de confiance dans cette autre façon de voir ta situation ? ")
        time.sleep(1)
        print()
        print("Très bien ! Je suis content de te voir faire ce travail ! Il est bon d'écouter ses émotions, mais il est bon de les évaluer également.")
        input("Je t'invite à fermer les yeux un instant et à te concentrer sur ton corps. Comment te sens tu ici et maintenant ? ")
        time.sleep(3)
        print()
        print("Ok :)")
        time.sleep(1)
        print()
        input("Je te propose maintenant de réfléchir à un objectif en lien avec cette situation: ")
        time.sleep(2)
        print()
        print("Super !")
        time.sleep(4)
        print()
        answer = input("Que souhaites tu faire maintenant ? Voir une autre situation, retourner au menu ou t'arrêter là ? (situation/menu/stop) ")
        if answer == "situation":
            programme()
        if answer == "menu":
            menu2()
        else:
            print("Ok ! Je te remercie pour ta participation à ce programme de TCC ! À bientôt" + username + " !")

    programme()

username = input("Bonjour, comment est ce que tu t'appelles ? ")
print()
print("Bienvenue " + username + " !")
print("Moi je m'appelle ZenBot, et je suis là pour t'accompagner dans ton programme de TCC.")
time.sleep(4)
menu()


