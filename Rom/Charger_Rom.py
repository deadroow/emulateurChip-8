import os


class ROM:
    """Gère le chargement et la validation d'une ROM CHIP-8."""

    def load(self, path):
        """Copie la ROM en mémoire à partir de 0x200."""
        # Vérifie que le fichier existe
        if not os.path.exists(path):
            print(f"Le chemin '{path}' n'existe pas.")
            return

        # Lit le contenu binaire de la ROM
        with open(path, "rb") as fp:
            content = fp.read()

        # Vérifie que la ROM tient dans la mémoire disponible (le programme commence à 0x200)
        available = len(self.memoir) - 0x200
        if len(content) > available:
            raise ValueError(
                f"ROM trop volumineuse : {len(content)} bytes (max : {available} bytes)"
            )

        # Recopie chaque octet en mémoire à partir de 0x200
        for i, byte in enumerate(content):
            self.memoir[0x200 + i] = byte

        print(f"ROM chargée ({len(content)} bytes) depuis '{path}'")
        return content