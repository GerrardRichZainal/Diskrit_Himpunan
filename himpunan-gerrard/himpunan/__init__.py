"""
himpunan - library sederhana untuk operasi himpunan.
Tanpa menggunakan set() bawaan Python.
"""

from typing import Any, List, Iterable, Tuple

class Himpunan:
    def __init__(self, *args: Any):
        """Buat himpunan dari argumen tanpa duplikasi"""
        self.elemen: List[Any] = []
        for item in args:
            if item not in self.elemen:
                self.elemen.append(item)

    def __repr__(self):
        return "{" + ", ".join(map(str, self.elemen)) + "}"

    def __len__(self):
        return len(self.elemen)

    def __contains__(self, item):
        return item in self.elemen

    # tambah dan hapus elemen
    def __iadd__(self, item):
        if item not in self.elemen:
            self.elemen.append(item)
        return self

    def __isub__(self, item):
        if item in self.elemen:
            self.elemen.remove(item)
        return self

    # operasi dasar
    def __add__(self, other):
        hasil = list(self.elemen)
        for x in other.elemen:
            if x not in hasil:
                hasil.append(x)
        return Himpunan(*hasil)

    def __sub__(self, other):
        hasil = [x for x in self.elemen if x not in other.elemen]
        return Himpunan(*hasil)

    def __truediv__(self, other):
        hasil = [x for x in self.elemen if x in other.elemen]
        return Himpunan(*hasil)

    def __mul__(self, other):
        left = [x for x in self.elemen if x not in other.elemen]
        right = [x for x in other.elemen if x not in self.elemen]
        return Himpunan(*(left + right))

    def __pow__(self, other):
        return [(a, b) for a in self.elemen for b in other.elemen]

    def Komplemen(self, semesta):
        hasil = [x for x in semesta.elemen if x not in self.elemen]
        return Himpunan(*hasil)

    def ListKuasa(self):
        hasil = [[]]
        for item in self.elemen:
            hasil += [subset + [item] for subset in hasil]
        return [Himpunan(*subset) for subset in hasil]

    def __abs__(self):
        return 2 ** len(self.elemen)
