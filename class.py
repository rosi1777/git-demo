class Kucing:

    def __init__(self, name, age, type):
        self.nama = name
        self.umur = age
        self.jenis = type

    def walk(self):
        return self.nama + " is walking"


kucing1 = Kucing("Simba", 3, "Persian")

print(kucing1.walk())
