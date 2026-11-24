#Hey das ist ein Versuch Tic Tac Toe in python zu erstellen, es ist mein Erster Versuch könnte also nicht perfekt sein

def erstelle_spielbrett():
    spielbrett = []

    for i in range(3):
        zeile = [" ", " ", " "]
        spielbrett.append(zeile)
    return(spielbrett)

def drucke_spielbrett(spielbrett):
    for zeile in spielbrett:
        print("|".join(zeile))
        print("-----")

def play_Zug(spielbrett, spieler, zeile, spalte):
    if spielbrett[zeile][spalte] == " ":
        spielbrett[zeile][spalte] = spieler
        return True
    else:
        return False

def check_win(spielbrett, spieler):
    for zeile in range(3):
        if spielbrett[zeile][0] == spielbrett[zeile][1] == spielbrett[zeile][2] == spieler:
            return True

    for spalte in range(3):
        if spielbrett[0][spalte] == spielbrett[1][spalte] == spielbrett[2][spalte] == spieler:
            return True

        if spielbrett[0][0] == spielbrett[1][1] == spielbrett[2][2] == spieler or \
            spielbrett[0][2] == spielbrett[1][1] == spielbrett[2][0] == spieler:
            return True

def check_draw(spielbrett):
    for zeile in spielbrett:
        if " " in zeile:
            return False
    return True


def play_tic_tac_toe():
    spielbrett = erstelle_spielbrett()
    aktueller_spieler = "X"

    while True:
        drucke_spielbrett(spielbrett)
        zeile = int(input(f"Spieler {aktueller_spieler}, Wähle deine Zeile 0-2)"))
        spalte = int(input(f"Spieler {aktueller_spieler}, Wähle deine Spalte 0-2)"))

        if not play_Zug(spielbrett, aktueller_spieler, zeile, spalte):
            print("Ungültig Erneut Versuchen!")
            continue
        if check_win(spielbrett, aktueller_spieler):
            drucke_spielbrett(spielbrett)
            print(f"Herzlichen Glückwunsch du hast Gewonnen Spieler {aktueller_spieler}")
            break
        elif check_draw(spielbrett):
            drucke_spielbrett(spielbrett)
            print("Unentschieden")
            break
        aktueller_spieler = "O" if aktueller_spieler == "X" else "X"

play_tic_tac_toe()