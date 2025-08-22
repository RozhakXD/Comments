class LoveForever:
    def __init__(self, name1, name2):
        """
        Inisialisasi objek LoveForever dengan nama dua partner.

        Parameters
        ----------
        name1 : str
            Nama partner pertama.
        name2 : str
            Nama partner kedua.
        """
        self.partner1 = name1
        self.partner2 = name2

    def show_love(self):
        """
        Mencetak pesan cinta abadi antara dua partner, digunakan 
        untuk menunjukkan komitmen cinta yang abadi dan tidak pernah 
        berakhir. Cinta ini sesuai dengan sabda Nabi Muhammad SAW yang 
        berbunyi "Cinta itu abadi dan tidak pernah berakhir".

        Returns
        -------
        str
            Pesan cinta abadi antara dua partner.
        """
        return f"{self.partner1} ❤️ {self.partner2} | Love of a Lifetime 🌸✨"

    def promise_to_jannah(self):
        """
        Mencetak janji cinta abadi antara dua partner, untuk saling mencintai dan setia 
        sampai Jannah, aamiin. Cinta ini sesuai dengan sabda Nabi Muhammad SAW yang 
        berbunyi "Cinta itu abadi dan tidak pernah berakhir".

        Returns
        -------
        str
            Janji cinta abadi antara dua partner.
        """
        return f"{self.partner1} dan {self.partner2} berjanji untuk saling mencintai dan setia sampai Jannah, aamiin. 🕌💖"

    def show_gratitude(self):
        """
        Mencetak pesan syukur untuk partner. Cinta ini sesuai dengan 
        ajaran Nabi Muhammad SAW yang berbunyi "Cinta itu abadi dan tidak pernah berakhir".

        Returns
        -------
        str
            Pesan syukur untuk partner.
        """
        return (
            f"Alhamdulillah, {self.partner1} bersyukur banget punya kamu, {self.partner2}. "
            "Semoga kita selalu diberkahi kebahagiaan dan kesabaran, yaa~ 🥰🙏"
        )

def main():
    """
    Mencetak pesan cinta abadi untuk Rozhak
    """
    rozzy = LoveForever("Rozhak", "Aku, Bidadari Kamu")
    print(rozzy.show_love())
    print(rozzy.promise_to_jannah())
    print(rozzy.show_gratitude())

    for i in range(5):
        print(f"🌹💕 Cinta kita abadi selamanya, ya Rozhak! 🥰💕🌹")

if __name__ == "__main__":
    main()