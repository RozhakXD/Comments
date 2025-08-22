import time

class EternalRindu:
    def __init__(self, sender, receiver):
        """
        Inisialisasi objek EternalRindu dengan nama pengirim dan penerima pesan rindu.

        Parameters
        ----------
        sender : str
            Nama pengirim pesan rindu.
        receiver : str
            Nama penerima pesan rindu.
        """
        self.sender = sender
        self.receiver = receiver
        self.messages = []

    def add_rindu(self, message):
        """
        Menambahkan pesan rindu yang ingin disampaikan pada penerima.

        Parameters
        ----------
        message : str
            Pesan rindu yang ingin disampaikan.
        """
        self.messages.append(f"Rindu untuk {self.receiver}: {message}")
        print(f"Pesan rindu untuk {self.receiver} ditambahkan... 💌✨")

    def kirim_rindu(self):
        """
        Mencetak semua pesan rindu yang telah ditambahkan menggunakan
        add_rindu(). Jika belum ada pesan rindu yang ditambahkan, maka
        akan menampilkan pesan bahwa hati ini penuh dengan rasa cinta.

        Returns
        -------
        None
        """
        print("\n🌹 Curahan Rindu dari Hati yang Dalam: 🌹")
        if self.messages:
            for message in self.messages:
                print(f"💖 {message}")
        else:
            print("🥀 Belum ada rindu yang tersampaikan, tapi sebenarnya hati ini penuh dengan rasa cinta...")

    def express_rindu(self):
        """
        Mengembalikan teks yang menggambarkan curahan rindu yang mendalam.

        Returns
        -------
        str
            Teks yang menggambarkan curahan rindu yang mendalam.
        """
        return (
            f"rindu ini tetap bertahan di hatiku, seperti bintang malam yang tak pernah hilang di gelapnya langit. 🌌✨"
        )

    def heaven_prayer(self):
        """
        Mengembalikan teks yang menggambarkan doa rindu ke surga.

        Returns
        -------
        str
            Teks yang menggambarkan doa rindu ke surga.
        """
        return (
            f"Ya Allah, aku memohon pada-Mu agar setiap rindu yang ku rasakan untuk {self.receiver} "
            f"mendekatkan kami pada jalan-Mu, mencintai sebagaimana yang Engkau ridhoi... "
            "dan semoga kami dipertemukan di Jannah-Mu kelak. Aamiin 🤲💕"
        )

    def animate_rindu(self):
        """
        Mencetak animasi teks yang menggambarkan curahan rindu yang mendalam.
        
        Animasi ini akan menampilkan teks yang menggambarkan curahan rindu
        yang mendalam, dengan efek munculnya teks secara perlahan-lahan.
        
        Returns
        -------
        None
        """
        print("\n✨ Animasi Hati yang Merindukanmu: ✨")
        for char in "Setiap helaan nafasku ada namamu, bidadariku... Aku harap kau tahu, aku merindukanmu. 🥺💕":
            print(char, end="", flush=True)
            time.sleep(0.05)
        print("\n🌹 Pada akhirnya, rindu ini adalah doa yang tak pernah berhenti. ✨")

def main():
    rindu_rozzy = EternalRindu("Rozhak Sayangkuhhh", "Bidadari yang Selalu Dirindukan")
    """
    Mencetak teks yang menggambarkan curahan rindu yang mendalam dari Rozhak
    untuk bidadari kesayanganmu. Juga menampilkan doa khusus dari Rozhak untuk
    sang bidadari dan animasi cinta yang bikin makin spesial!

    Returns
    -------
    None
    """
    rindu_rozzy.add_rindu("Aku merindukan senyummu yang menenangkan hatiku. 😘")
    rindu_rozzy.add_rindu("Meski terpisah jarak, hati ini selalu dekat denganmu... 🥰")
    rindu_rozzy.add_rindu("Doa yang tak pernah selesai adalah tentang kamu... Karena rindu ini abadi. 🕌💕")
    
    rindu_rozzy.kirim_rindu()

    print("\n🌿 Kata Hati: 🌿")
    print(rindu_rozzy.express_rindu())

    print("\n🌌 Doa untuk Rindu: 🌌")
    print(rindu_rozzy.heaven_prayer())

    rindu_rozzy.animate_rindu()

if __name__ == "__main__":
    main()