import time

class BurbuloRusiavimas:
    def __init__(self, sarasas):
        self.sarasas = sarasas

    def rusiuoti(self):
        n = len(self.sarasas)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.sarasas[j] > self.sarasas[j+1] :
                    self.sarasas[j], self.sarasas[j+1] = self.sarasas[j+1], self.sarasas[j]

my_ist = BurbuloRusiavimas(nerusiuotas_sarasas)

start_time = time.time()
my_list.rusiuoti()
end_time = time.time()

print("Surūšiuotas sąrašas:", rusytuvas.sarasas)
print("Rūšiavimo laikas:", end_time - start_time, "sekundės")
