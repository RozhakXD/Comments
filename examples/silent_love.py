class SilentLove:
    def __init__(self, your_name, loved_one):
        """
        Inisialisasi objek SilentLove dengan nama Anda dan nama yang
        dicintai.

        Parameters
        ----------
        your_name : str
            Nama Anda.
        loved_one : str
            Nama yang dicintai.
        """
        self.your_name = your_name
        self.loved_one = loved_one
        self.is_visible = False

    def express_silently(self):
        """
        Mengembalikan teks yang menggambarkan ekspresi cinta dalam diam.
        Jika cinta ini tidak terlihat, maka teks akan mengandung doa
        yang mengalir penuh harap. Jika cinta ini terlihat, maka teks
        akan mengatakan bahwa cinta ini terlihat oleh yang dicintai.

        Returns
        -------
        str
            Teks yang menggambarkan ekspresi cinta dalam diam.
        """
        if not self.is_visible:
            return (
                f"Meski cinta {self.your_name} buat {self.loved_one} tetap tersembunyi, "
                "namun setiap doa mengalir penuh harap~ 🤲✨"
            )
        return f"{self.your_name}'s love is visible to {self.loved_one}! 💞"

    def love_in_prayers(self):
        """
        Mengembalikan teks yang menggambarkan doa cinta dalam diam.
        Teks ini mengandung doa untuk diberikan lindungan-Nya dan selalu
        dalam keadaan baik.

        Returns
        -------
        str
            Teks yang menggambarkan doa cinta dalam diam.
        """
        return (
            f"Ya Rabb, mohon jagalah hati dia yang aku cintai. "
            f"Semoga {self.loved_one} selalu dalam lindungan-Mu 🕌💕. "
            "Meski tak terucap, perasaanku akan selalu sampai lewat doa... Amin 🤲✨"
        )

    def wait_for_jannah(self):
        """
        Mengembalikan teks yang menggambarkan harapan cinta dalam diam untuk berjumpa di akhirat.
        Teks ini mengandung doa untuk diberikan surga-Nya dan berjumpa dengan orang yang dicintai di akhirat.

        Returns
        -------
        str
            Teks yang menggambarkan harapan cinta dalam diam.
        """
        return (
            f"Cinta dalam diam {self.your_name} ini semoga berbuah manis di akhirat, "
            "bisa bertemu dalam surga-Mu Ya Allah... 🕌🌸"
        )

def main():
    """
    Menampilkan contoh penggunaan kelas SilentLove dengan nama 'Rozhak' dan 'Bidadari'.
    Mencetak teks-teks yang menggambarkan cinta dalam diam tersebut.
    """
    my_silent_love = SilentLove("Rozhak", "Bidadari")
    print("💌 Pesan Cinta Dalam Diam: 💌")
    print(my_silent_love.express_silently())
    print()
    print("✨ Doa Khusus: ✨")
    print(my_silent_love.love_in_prayers())
    print()
    print("🌹 Harapan Abadi: 🌹")
    print(my_silent_love.wait_for_jannah())

    print("\n🌙 Kata Hati Dalam Diam: 🌙")
    for i in range(3):
        print(f"{i+1}. Cintaku dalam diam padamu semakin tulus setiap harinya~ 🥀💖")

if __name__ == "__main__":
    main()