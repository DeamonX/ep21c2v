class Kosar:
    """
    Egyetlen vásárlás adatait kezelő osztály.

    Az osztály attribútumai:
        - a kosárban lévő árucikkek (név-mennyiség párok)
        - a vásárlás összege
    """

    def __init__(self, termekek: dict[str, int]) -> None:
        """
        A kosár létrehozásakor beállítja az osztály attribútumait.
        """
        self.termekek = termekek

    def osszeg_lekerdezese(self) -> int:
        """
        A vásárlás összegének lekérdezése.

        :return: A vásárlás összege Ft-ban.
        """
        sum = 0
        for i in self.termekek:
            if self.termekek[i]>3:
                sum+=1000+900+((self.termekek[i]-2)*800)
            elif self.termekek[i]==2:
                sum+=1900
            else:
                sum+=1000
        return sum

    def termekek_lekerdezese(self) -> dict[str, int]:
        """
        Az árucikk-mennyiség párok lekérdezése.

        :return: Az árucikkek nevei és mennyiségei.
        """
        d ={}
        for i in self.termekek:
            d[i]=self.termekek[i]
        return d

    def termekek_szamanak_lekerdezese(self) -> int:
        """
        A kosárban lévő termékek számának lekérdezése.

        :return: Hány darab termék van a kosárban.
        """
        sum=0
        for i in self.termekek:
            sum+=self.termekek[i]
        return sum

    def arucikk_mennyisegenek_lekerdezese(self, arucikk: str) -> int:
        """
        Egy árucikknek a kosárban megtalálható mennyiségének lekérdezése.

        :param arucikk: A vizsgált árucikk neve.
        :return: A vizsgált árucikk mennyisége a kosárban.
        """
        for i in self.termekek:
            if arucikk not in self.termekek:
                return 0
            else:
                return self.termekek[arucikk]
        pass

    def kosar_tartalmanak_kiiratasa(self) -> None:
        """
        Kiírja a kosár tartalmát a konzolra.
        """
        print("A kosár tartalma:")
        for i in self.termekek:
            print(f"\t{self.termekek[i]} {i}")
        pass
