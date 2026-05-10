def begrossen ():
    import random

    print ("---------------------------------------------------------------------------")
    print ("|❗❗HINWEIS❗❗                                                          |")
    print ("|Ich habe mein Bestes gegeben. Versuche nicht besser zu sein als ich 😉😂 |")
    print ("---------------------------------------------------------------------------")
    global name
    hussams_namen = ["Hussam" , "hussam" , "Hossam" , "hossam", "Hussam " , "hussam " , "Hossam " , "hossam "]
    print ("\n ✨ hallo ich bin Hussam und ich begröße Sie, kann ich wessen mit wem rede ich jetzt ? ✨ ")
    name = str(input(" --> "))
    if  name in hussams_namen :
        print ("\n das kann nicht sein !! weil ich Hussam bin und es gibt nur einen Hussam in diesem Welt :)")
        print (" versuch mal was anderes")
        name = str(input(" --> "))
        if  name in hussams_namen :
            print("\n Bssssccchhht EGAL")
            print("Ok, vielleicht bist du wirklich Hussam. Es ist okay, dann sind wir nur zwei in dieser Welt :)")
            print("Hallo Hussam, du hast einen schönen Namen, wie ich :)")

        else :
            print ("\n du hast einen schönen name " + name + "!" )
    else:
        print ("\n du hast einen schönen name " + name + "!" )

    return name

def erste_teil_witzen ():
    import random
    print (" " + name + ", wie geht es dir ?")
    wie_geht_es_er = str(input(" --> "))
    gehts_gut =["gut" , "Gut" , "gut " , "Gut " , "ok" , "Ok", "ok " , "Ok ","super " , "Super " , "super" , "Super" ,"wünderbar " , "Wünderbar " , "wünderbar" , "Wünderbar", "nicht schlecht " , "nicht schlecht", "inordnung" , "inordnung ", "Inordnung ", "Inordnung"]
    gehts_schlecht = ["schlecht","nicht gut","schlecht ","nicht gut ", "nicht inordnung" , "nicht inordnung " ]


    while wie_geht_es_er not in gehts_gut and wie_geht_es_er not in gehts_schlecht:
        print (" sorry ich habe nicht verstanden")
        print (" kannst du bitte wiederholen? ")
        wie_geht_es_er = str(input(" --> "))
    if wie_geht_es_er in gehts_gut :
        print ("\n das freut mich ! ")
    if wie_geht_es_er in gehts_schlecht :
        print ("\n oh nee das freut mich nicht, ")
        print (" aber ich weiss wie kann ich dein proplem lösen :) ")
        print (" soll ich dir einen witz schreiben? ")
        witz_antwort = str(input(" --> "))
        while witz_antwort != "nein" and witz_antwort != "ja":
            print (" du hast was falsch eingegeben ")
            print (" bitte nur mit ja oder nein antworten ")
            witz_antwort = str(input(" --> "))
        if witz_antwort == "nein" :
            print (" eyy ich will nur helfen ")
        while witz_antwort != "nein":
            if witz_antwort == "ja" :
                witz1 = " \n Freitagabend: \n „Schatz, sollen wir uns ein schönes Wochenende machen?“ \n „Klar!“ \n „Klasse, dann bis Montag!“"
                witz2 = " \n „Ich würde ja gerne ein paar Kilos verlieren.\n Aber ich verliere nie. \n Ich bin ein Gewinner!“"
                Witz3 = " \n Ein Pärchen streift spät abends durch die Gassen von Paris.\n Sagt der Mann: „Schau mal da oben eine Sternschnuppe, Du darfst dir etwas wünschen.” \n Sagt die Frau: „Ich will dich heiraten.” \n Sagt der Mann: „Ich glaube, es war doch nur ein Blitz"
                witzen = random.choice([witz1, witz2, Witz3])
                print (witzen)
                print ("\n geht dir jetzt besser ? ")
                antwort_nach_die_witze = str(input("  --> "))
                while antwort_nach_die_witze != "nein" and antwort_nach_die_witze != "ja":
                    print (" du hast was falsch eingegeben ")
                    print (" bitte nur mit ja oder nein antworten ")
                    antwort_nach_die_witze = str(input(" --> "))
                if antwort_nach_die_witze == "ja":
                    print ("\n das freut mich")
                    print (" soll ich ein andere witz schreiben ? ")
                    witz_antwort = str(input(" --> "))
                    while witz_antwort != "nein" and witz_antwort != "ja":
                        print (" du hast was falsch eingegeben ")
                        print (" bitte nur mit ja oder nein antworten ")
                        witz_antwort = str(input(" --> "))
                    if witz_antwort == "nein":
                        print (" haha siehst du ich kenne dein mediziene 😂")
                    else :
                        while witz_antwort != "nein" :
                            print ("\n ok hier ist ein andere \n\n"
                                "|| || || || || || || ||\n"
                                "\/ \/ \/ \/ \/ \/ \/ \/")
                            print ("---------------------------------------------------------------------------")
                            print ("|❗❗HINWEIS❗❗                                                          |")
                            print ("|wenn ist die gleiche witz dir angegeben dann drück bitte auf ja 😉😂     |")
                            print ("---------------------------------------------------------------------------")
                            print ("|| || || || || || || ||\n"
                                "\/ \/ \/ \/ \/ \/ \/ \/")
                            witz1 = " \n Freitagabend: \n „Schatz, sollen wir uns ein schönes Wochenende machen?“ \n „Klar!“ \n „Klasse, dann bis Montag!“"
                            witz2 = " \n „Ich würde ja gerne ein paar Kilos verlieren.\n Aber ich verliere nie. \n Ich bin ein Gewinner!“"
                            Witz3 = " \n Ein Pärchen streift spät abends durch die Gassen von Paris.\n Sagt der Mann: „Schau mal da oben eine Sternschnuppe, Du darfst dir etwas wünschen.” \n Sagt die Frau: „Ich will dich heiraten.” \n Sagt der Mann: „Ich glaube, es war doch nur ein Blitz"
                            witzen = random.choice([witz1, witz2, Witz3])
                            print (witzen)
                            print ("\n soll ich ein andere witz schreiben ? ")
                            witz_antwort = str(input(" --> "))
                            while witz_antwort != "nein" and witz_antwort != "ja":
                                print (" du hast was falsch eingegeben ")
                                print (" bitte nur mit ja oder nein antworten ")
                                witz_antwort = str(input(" --> "))
                        print ("gut")
                else : 
                    print (" eyyyy was mit dir, warum bist unfreundlich")
                    print (" soll ich dir einen andere witz schreiben? ")
                    witz_antwort = str(input(" --> "))
                    while witz_antwort != "nein" and witz_antwort != "ja":
                        print (" du hast was falsch eingegeben ")
                        print (" bitte nur mit ja oder nein antworten ")
                    while witz_antwort != "nein" :
                        print ("\n ok hier ist ein andere \n\n"
                                "|| || || || || || || ||\n"
                                "\/ \/ \/ \/ \/ \/ \/ \/")
                        print ("---------------------------------------------------------------------------")
                        print ("|❗❗HINWEIS❗❗                                                          |")
                        print ("|wenn ist die gleiche witz dir angegeben dann drück bitte auf ja 😉😂     |")
                        print ("---------------------------------------------------------------------------")
                        print ("|| || || || || || || ||\n"
                               "\/ \/ \/ \/ \/ \/ \/ \/")
                        witz1 = " \n Freitagabend: \n „Schatz, sollen wir uns ein schönes Wochenende machen?“ \n „Klar!“ \n „Klasse, dann bis Montag!“"
                        witz2 = " \n „Ich würde ja gerne ein paar Kilos verlieren.\n Aber ich verliere nie. \n Ich bin ein Gewinner!“"
                        Witz3 = " \n Ein Pärchen streift spät abends durch die Gassen von Paris.\n Sagt der Mann: „Schau mal da oben eine Sternschnuppe, Du darfst dir etwas wünschen.” \n Sagt die Frau: „Ich will dich heiraten.” \n Sagt der Mann: „Ich glaube, es war doch nur ein Blitz"
                        witzen = random.choice([witz1, witz2, Witz3])
                        print (witzen)
                        print ("\n soll ich ein andere witz schreiben ? ")
                        witz_antwort = str(input(" --> "))
                        while witz_antwort != "nein" and witz_antwort != "ja":
                            print (" du hast was falsch eingegeben ")
                            print (" bitte nur mit ja oder nein antworten ")
                            witz_antwort = str(input(" --> "))
                    if witz_antwort == "nein":
                        print ("\n ok ")

        ####

def Gender ():    
    import random
    print (" bist du einen mann oder eine Frau? ")
    Gesclecht = str(input(" --> "))
    while Gesclecht.lower() != "mann" and Gesclecht.lower() != "frau":
        print (" \n sorry ich habe nicht verstanden")
        print (" bitte antworten Sie nur mit Frau oder mann")
        print ( " " + name + ", bist du einen man oder eine Frau? ")
        Gesclecht = str(input(" --> "))
    if Gesclecht.lower() == "mann" :
        print (" \n 👍🏻")
    if Gesclecht.lower() == "frau" :
        print (" \n 😳")
        print (" ohhhh hi 😳")
        print (" hat mich gefreut dich kennen zu lernen, " + name)

def taschenrechner():
    import random
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return " Ungültige Eingabe. Division durch Null ist nicht erlaubt."
        else:
            return x / y

    print(" Wähle eine Operation:")
    print(" 1. Addition")
    print(" 2. Subtraktion")
    print(" 3. Multiplikation")
    print(" 4. Division")
    print(" Gib die Nummer der gewünschten Operation ein (1/2/3/4): ")

    operation_options = ["1", "2", "3", "4"]
    choice = input("--> ")

    while choice not in operation_options:
        print(" Wähle eine Operation. Du darfst nur die Zahlen 1, 2, 3 oder 4 eingeben:")
        print(" 1. Addition")
        print(" 2. Subtraktion")
        print(" 3. Multiplikation")
        print(" 4. Division")
        choice = input("--> ")

    num1 = input(" Gib die erste Zahl ein: ")
    while not num1.replace('.', '', 1).isdigit():
        print(" Du darfst nur Zahlen eingeben.")
        num1 = input(" Gib die erste Zahl ein: ")
    num1 = float(num1)

    num2 = input(" Gib die zweite Zahl ein: ")
    while not num2.replace('.', '', 1).isdigit():
        print(" Du darfst nur Zahlen eingeben.")
        num2 = input(" Gib die zweite Zahl ein: ")
    num2 = float(num2)

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        result = divide(num1, num2)
        print(num1, "/", num2, "=", result)

    else:
        print("Ungültige Eingabe")

def stein_schere_blatt():
    import random
    
    antwort_wieder_spieln = "ja"
    
    while antwort_wieder_spieln == "ja":
        print(" " + name + ", bitte wahl eins aus diesem drei (stein, schere oder blatt) ")
        stein_schere_blatt1 = ["stein", "schere", "blatt"]
        stein_schere_blatt1_choce = random.choice(stein_schere_blatt1)
        
        antwort = input(" --> ")
        
        while antwort.lower() not in ["stein", "schere", "blatt"]:
            print(" du hast was falsch eingegeben\n "
                  " " + name + ", bitte gib nur ein aus diesem antworten (stein, schere oder blatt)")
            antwort = input(" --> ")

        if antwort == stein_schere_blatt1_choce:
            print(stein_schere_blatt1_choce)
            print(" niemand ist gewonnen willst du wieder versuchen ? ")
            antwort_wieder_spieln = input(" --> ")
            
            while antwort_wieder_spieln.lower() not in ["ja", "nein"]:
                print(" du hast was falsch eingegeben  bitte nur mit ja oder nein antworten")
                antwort_wieder_spieln = input(" --> ")
            
            if antwort_wieder_spieln == "ja":
                print(" ok")
                return stein_schere_blatt()
            else:
                print(" schade ...,  ich will dich verlieren")

        if antwort == "stein" and stein_schere_blatt1_choce == "blatt" or antwort == "blatt" and stein_schere_blatt1_choce == "schere" or antwort == "schere" and stein_schere_blatt1_choce == "stein" :
            print (stein_schere_blatt1_choce)
            print (" ich habe gewonnen :)")
            print (" willst du nochmal spielen? ")
            antwort_wieder_spieln = input(" --> ")
            
            while antwort_wieder_spieln.lower() not in ["ja", "nein"]:
                print(" du hast was falsch eingegeben  bitte nur mit ja oder nein antworten")
                antwort_wieder_spieln = input(" --> ")
            
            if antwort_wieder_spieln == "ja":
                print(" ok")
                return stein_schere_blatt()
            else:
                print(" schade ...,  ich will dich verlieren")

        if antwort == "blatt" and stein_schere_blatt1_choce == "stein" or antwort == "schere" and stein_schere_blatt1_choce == "blatt" or antwort == "stein" and stein_schere_blatt1_choce == "schere" :
            print (stein_schere_blatt1_choce)
            print (" du hast gewonnen :(")
            print (" willst du nochmal spielen? ")
            antwort_wieder_spieln = input(" --> ")
            
            while antwort_wieder_spieln.lower() not in ["ja", "nein"]:
                print(" du hast was falsch eingegeben  bitte nur mit ja oder nein antworten")
                antwort_wieder_spieln = input(" --> ")
            
            if antwort_wieder_spieln == "ja":
                print(" ok")
                return stein_schere_blatt()
            else:
                print(" ja ja du hast gewonen aber ich glaube das du angst von mir hast oder haha")
                print(" bist du sicher dass du nicht spielen willst? ")
                antwort_wieder_spieln = input(" --> ")
                while antwort_wieder_spieln.lower() not in ["ja", "nein"]:
                    print(" du hast was falsch eingegeben  bitte nur mit ja oder nein antworten")
                    antwort_wieder_spieln = input(" --> ")
                    if antwort_wieder_spieln == "nein" :
                        print ("oha du hast dein meinung gewchselt ja ich weis das du wieder kommt ")
                        return stein_schere_blatt()
                    else :
                        print (" ok "+name+", wie du willst ")

def spiele ():
    import random
    hussams_spiele = ["taschenrechner" , "stein_schere_blatt"]
    print(" ich habe lust auf etwas zu spielen komm ich lass dich wählen willst du " + str(hussams_spiele) + "spielen ?")
    was_willst_du_spielen = str(input(" --> "))
    while was_willst_du_spielen != "taschenrechner" and was_willst_du_spielen != "stein_schere_blatt" :
        print (" du hast was falsch eingegeben ")
        print (" bitte nur mit taschenrechner oder stein_schere_blatt antworten ")
        was_willst_du_spielen = str(input(" --> "))
    
    nochmal_spielen = "ja"
    while nochmal_spielen == "ja" :
        if was_willst_du_spielen == "taschenrechner":
            print(" "+name+", Weißt du, dass ich schnell rechnen kann?")
            print(" Schau, lass uns so spielen, dass du mir zwei Zahlen gibst, und ich muss egal wie schnell, diese schnell berechnen.")
            print(" ok ? los geht ")
            taschenrechner()
            print (" schau wie schnell bin ich hyhyhy ")
            print (" willst du nochmal spieln ? ")
            taschenrechner_spiel_antwort = str(input (" --> "))
            while taschenrechner_spiel_antwort != "nein" and taschenrechner_spiel_antwort != "ja":
                print (" du hast was falsch eingegeben ")
                print (" bitte nur mit ja oder nein antworten ")
                taschenrechner_spiel_antwort = str(input(" --> "))
            
            while taschenrechner_spiel_antwort != "nein":
                if taschenrechner_spiel_antwort == "ja" :
                    print("\n das freut mich, lass uns wieder beginnen")
                    taschenrechner()
                    print (" schau wie schnell bin ich hyhyhy ")
                    print (" willst du nochmal spieln ? ")
                    taschenrechner_spiel_antwort = str(input(" --> "))
                    while taschenrechner_spiel_antwort != "nein" and taschenrechner_spiel_antwort != "ja":
                        print (" du hast was falsch eingegeben ")
                        print (" bitte nur mit ja oder nein antworten ")
                        taschenrechner_spiel_antwort = str(input(" --> "))
                if taschenrechner_spiel_antwort == "nein" :
                    print(" Egal, ich habe gewonnen!")
        
        if was_willst_du_spielen == "stein_schere_blatt": 
            print(" haha ich möge dieses spiel ")
            print(" las uns losbeginnen ")
            stein_schere_blatt()

        print (" zu zeit ich habe nur diesem zwei spiele hoffe das hat dich gefallen ")
        print (" Ich würde gerne noch mehr Spiele mit dir spielen, aber im Moment hat mir Hussam nur diesem Zwei Spiele erklärt.\n"
            " Vielleicht werde ich beim nächsten Chat mehr Spiele kennen.")
        print (" willst du nochmal spielen? ")
        nochmal_spielen = str(input(" --> "))
        while nochmal_spielen != "nein" and nochmal_spielen != "ja":
            print (" du hast was falsch eingegeben ")
            print (" bitte nur mit ja oder nein antworten ")
        if nochmal_spielen == "ja":
            print (" was willst du spielen(taschenrechner , stein_schere_blatt)")
            was_willst_du_spielen = str(input(" --> "))
            while was_willst_du_spielen != "taschenrechner" and was_willst_du_spielen != "stein_schere_blatt" :
                print (" du hast was falsch eingegeben ")
                print (" bitte nur mit taschenrechner oder stein_schere_blatt antworten ")
                was_willst_du_spielen = str(input(" --> "))
        else :
            print (" ok wie du willst ")

def wieder_stellen ():
    import random
    print("\n soll ich den programm wieder starten  ")
    wieder_starten = str(input(" --> "))
    while wieder_starten != "nein" and wieder_starten != "ja":
        print (" du hast was falsch eingegeben ")
        print (" bitte nur mit ja oder nein antworten ")
        wieder_starten = str(input(" --> "))
    if wieder_starten == "ja" :
        run()
    else :
        print (" ok")

def run():
    import random
    global name
    name = begrossen ()
    erste_teil_witzen ()
    Gender ()
    spiele ()
    print("-------------------------------------------------------------------------------------------")
    print("|                                ❗❗ HINWEIS ❗❗                                        |")
    print("| Hier sind wir zu Ende. Ich hoffe, dass du genauso gut programmieren kannst wie ich 😉😂 |")
    print("| Programmieren ist einfach, erfordert jedoch viel Fokussierung.                          |")
    print("| Ich habe mit dem Programmierenlernen etwa Mitte September begonnen.                     |")
    print("| Wenn du jetzt beim Lernen bleibst und dich ständig verbessert,                          |")
    print("| wirst du im nächsten Jahr in einer guten Position sein.                                 |")
    print("| Wenn nicht, dann frage dich, warum du nicht letztes Jahr angefangen hast zu lernen.     |")
    print("| Das liegt ganz bei dir (Day One or One Day).                                            |")
    print("-------------------------------------------------------------------------------------------")
    wieder_stellen()


run()