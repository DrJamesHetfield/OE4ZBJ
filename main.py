from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from Autokolcsonzo import Autokolcsonzo
from datetime import date, timedelta

def adatok_betoltese():
    kolcsonzo = Autokolcsonzo("Csepregi Autókölcsönző")

    #autók létrehozása
    auto1 = Szemelyauto("ABC-123", "Suzuki Swift", 5500, 5)
    auto2 = Szemelyauto("BND-007", "Aston Martin DB5", 150000, 4) #utas
    auto3 = Teherauto("KUMI-1", "Renault Master", 25000, 1500) #teherbíras

    kolcsonzo.auto_hozzaadasa(auto1)
    kolcsonzo.auto_hozzaadasa(auto2)
    kolcsonzo.auto_hozzaadasa(auto3)

    ######## alap kölcsönzött autók listája, "Előkészítés" menüpontban kért 4 bérlés (ha jól értelmeztem) ########
    
    holnap = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    holnaputan = (date.today() + timedelta(days=2)).strftime("%Y-%m-%d")

    kolcsonzo.autoberles("ABC-123", holnap)
    kolcsonzo.autoberles("ABC-123", "2026-11-02")
    kolcsonzo.autoberles("BND-007", holnap)
    kolcsonzo.autoberles("KUMI-1", holnaputan)

    return kolcsonzo

def main():
    kolcsonzo = adatok_betoltese()
    
    while True:
        print(f"\n--- {kolcsonzo.nev} Rendszer ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Elérhető autók listázása")
        print("0. Kilépés")
        
        valasztas = input("Válasszon menüpontot: ")

        if valasztas == "1":
            rendszam = input("Kérem a bérelni kívánt autó rendszámát: ")
            datum = input("Kérem a bérlés dátumát (ÉÉÉÉ-HH-NN): ")
            try:
                ar = kolcsonzo.autoberles(rendszam.upper(), datum)
                print(f"Sikeres bérlés! A bérleti díj: {ar} Ft.")
            except ValueError as e:
                print(f"Hiba: {e}")

        elif valasztas == "2":
            rendszam = input("Kérem a lemondani kívánt autó rendszámát: ")
            datum = input("Kérem a lemondandó bérlés dátumát (ÉÉÉÉ-HH-NN): ")
            try:
                kolcsonzo.berles_lemondasa(rendszam.upper(), datum)
                print("A bérlés sikeresen lemondva.")
            except ValueError as e:
                print(f"Hiba: {e}")

        elif valasztas == "3":
            print("\nAktuális bérlések:")
            if not kolcsonzo.berlesek:
                print("Jelenleg nincs aktív bérlés.")
            else:
                for b in kolcsonzo.berlesek:
                    print(f"- Rendszám: {b.auto.rendszam}, Dátum: {b.datum}")

        elif valasztas == "4":
            print("\nElérhető autók:")
            for a in kolcsonzo.autok:
                print(a.informacio())

        elif valasztas == "0":
            print("Kilépés a programból...")
            break
        else:
            print("Érvénytelen választás, kérem próbálja újra!")

if __name__ == "__main__":
    main()