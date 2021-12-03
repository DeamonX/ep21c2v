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
        pass

    def osszeg_lekerdezese(self) -> int:
        """
        A vásárlás összegének lekérdezése.

        :return: A vásárlás összege Ft-ban.
        """
        pass

    def termekek_lekerdezese(self) -> dict[str, int]:
        """
        Az árucikk-mennyiség párok lekérdezése.

        :return: Az árucikkek nevei és mennyiségei.
        """
        pass

    def termekek_szamanak_lekerdezese(self) -> int:
        """
        A kosárban lévő termékek számának lekérdezése.

        :return: Hány darab termék van a kosárban.
        """
        pass

    def arucikk_mennyisegenek_lekerdezese(self, arucikk: str) -> int:
        """
        Egy árucikknek a kosárban megtalálható mennyiségének lekérdezése.

        :param arucikk: A vizsgált árucikk neve.
        :return: A vizsgált árucikk mennyisége a kosárban.
        """
        pass

    def kosar_tartalmanak_kiiratasa(self) -> None:
        """
        Kiírja a kosár tartalmát a konzolra.
        """
        pass
