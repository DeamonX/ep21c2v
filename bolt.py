import kosar


class Bolt:
    """
    A vásárlásokat kezelő osztály. Az osztály egyetlen attribútuma a kosarak listája.
    """

    def __init__(self):
        """
        A bolt létrehozásakor beállítja az osztály attribútumait.
        """
        pass

    def feladat_1(self, filepath: str) -> list:
        """
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """
        print("1. feladat: A kosar.txt beolvasása.")
        adatok=[]
        try:
            inputTxt = open(filepath,"r")
            aru = inputTxt.readline().strip()
            while(aru!=""):
                d ={}
                while(aru!='F'):
                    if aru in d:
                        d[aru]+=1
                    else:
                        d[aru]=1
                    aru = inputTxt.readline().strip()
                adatok.append(kosar.Kosar(d))
                aru = inputTxt.readline().strip()
            inputTxt.close()
            return adatok
        except FileNotFoundError:
            print("File nem található!")
        pass

    def feladat_2(self,adatok:list) -> None:
        """
        Kiírja, hányan fizettek a pénztárnál.
        """

        print(f"2. feladat: {len(adatok)} alkalommal fizettek a pénztárnál.")
        pass

    def feladat_3(self,adatok:list) -> None:
        """
        Bekéri egy vásárlás sorszámát és kiírja:
            - hány darab árucikk volt a kosárban,
            - mely árucikkekből és milyen mennyiségben vásároltak,
            - a vásárlás összegét.
        """
        sorszamS=(input("3. feladat: Adja meg a vásárlás sorszámát: "))
        if(sorszamS.isnumeric() and int(sorszamS)>0 and int(sorszamS)<=len(adatok)):
            sorszam = int(sorszamS)
            d=adatok[sorszam-1]
            print(f"{d.termekek_szamanak_lekerdezese()} termék volt a kosárban.")
            d.kosar_tartalmanak_kiiratasa()
            print(f"\nA vásárlás összege: {d.osszeg_lekerdezese()}Ft")
        else:
            print("Nem volt ilyen sorszámmal vásárlás.")
        pass
    def feladat_4(self,adatok:list) -> None:
        """
        Bekéri egy árucikk nevét és kiírja:
            - melyik vásárlásnál vettek először a termékből
            - melyik vásárlásnál vettek utoljára a termékből
            - összesen hány alkalommal vásároltak a termékből
        """
        item = input("4. feladat: Adja meg az árucikk nevét: ")
        elso=0
        utolso=0
        counter=0
        match=0
        for i in adatok:
            if i.arucikk_mennyisegenek_lekerdezese(item)!=0:
                if elso==0:
                    elso=counter+1
                match+=1
                utolso=counter+1
            counter+=1
        if elso ==0:
            print("Nem vásároltak ebből a termékből.")
        else:
            print(f"Első vásárlás sorszáma: {elso}\nUtolsó vásárlás sorszáma: {utolso}\n{match} alkalommal vásároltak az árucikkből.")
        pass

    def feladat_5(self, filepath: str,adatok:list) -> None:
        """
        Elmenti a megadott fájlba a vásárlásonként fizetendő összeget.
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """
        print("5. feladat: A vásárlások összegének mentése az osszeg.txt fájlba.")
        outputTxt=open(filepath,"w")
        for i in adatok:
            outputTxt.write(str(i.osszeg_lekerdezese())+"\n")
        outputTxt.close()
        pass
