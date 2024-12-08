import time


class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 5
        self.felicidade = 5
        self.saude = 5
        self.energia = 5  

    def alimentar(self):
        if self.fome < 10:
            self.fome -= 1
            if self.fome < 0: self.fome = 0
            print(f"{self.nome} foi alimentado!")
        else:
            print(f"{self.nome} não está com fome agora.")

    def brincar(self):
        if self.felicidade < 10:
            self.felicidade += 2
            self.energia -= 1
            self.fome += 1
            if self.energia < 0: self.energia = 0
            print(f"{self.nome} adorou brincar com você!")
        else:
            print(f"{self.nome} já está muito feliz!")

    def cuidar(self):
        if self.saude < 10:
            self.saude += 2
            print(f"Você cuidou da saúde de {self.nome}!")
        else:
            print(f"{self.nome} já está muito saudável!")

    def dormir(self):
        if self.energia < 10:
            self.energia += 3
            self.felicidade += 1
            self.saude += 1
            if self.energia > 10: self.energia = 10
            if self.felicidade > 10: self.felicidade = 10
            if self.saude > 10: self.saude = 10
            print(f"{self.nome} teve um ótimo descanso!")
        else:
            print(f"{self.nome} já está cheio de energia!")

    def tomar_banho(self):
        if self.saude < 10:
            self.saude += 2
            self.felicidade -= 1
            self.energia += 1
            if self.energia > 10: self.energia = 10
            if self.felicidade < 0: self.felicidade = 0
            print(f"{self.nome} tomou um banho refrescante!")
        else:
            print(f"{self.nome} já está limpo e saudável!")

    def conversar(self):
        if self.felicidade < 10:
            self.felicidade += 1
            self.energia -= 1
            self.saude += 1
            if self.felicidade < 0: self.felicidade = 0
            if self.energia < 0: self.energia = 0
            if self.saude > 10: self.saude = 10
            print(f"{self.nome} adorou a conversa!")
        else:
            print(f"{self.nome} já está muito feliz com sua companhia!")

    def status(self):
        print("\n--- Status do Bichinho ---")
        print(f"Nome: {self.nome}")
        print(f"Fome: {self.fome}/10")
        print(f"Felicidade: {self.felicidade}/10")
        print(f"Saúde: {self.saude}/10")
        print(f"Energia: {self.energia}/10")
        print("--------------------------\n")

    def passar_tempo(self):
        self.fome += 1
        self.felicidade -= 1
        self.saude -= 1
        self.energia -= 1

        if self.fome > 10: self.fome = 10
        if self.felicidade < 0: self.felicidade = 0
        if self.saude < 0: self.saude = 0
        if self.energia < 0: self.energia = 0

    def vivo(self):
        if self.fome >= 10 and self.felicidade <= 0 and self.saude <= 0 and self.energia <= 0:
            return False
        return True

    def matar(self):
        self.energia = 0
        self.saude = 0
        self.felicidade = 0
        self.fome = 10

def main():
    nome = input("Dê um nome ao seu bichinho virtual: ")
    bichinho = BichinhoVirtual(nome)

    while bichinho.vivo():
        bichinho.status()
        print("1. Alimentar")
        print("2. Brincar")
        print("3. Cuidar da saúde")
        print("4. Dormir")
        print("5. Tomar banho")
        print("6. Conversar")
        print("7. Passar tempo")
        print("8. Sair")
        escolha = input("Escolha uma ação: ")

        if escolha == "1":
            bichinho.alimentar()
        elif escolha == "2":
            bichinho.brincar()
        elif escolha == "3":
            bichinho.cuidar()
        elif escolha == "4":
            bichinho.dormir()
        elif escolha == "5":
            bichinho.tomar_banho()
        elif escolha == "6":
            bichinho.conversar()
        elif escolha == "7":
            bichinho.passar_tempo()
        elif escolha == "66":
            bichinho.matar()
        elif escolha == "8":
            print("Até mais!")
            break
        else:
            print("Escolha inválida.")

        bichinho.passar_tempo()
        time.sleep(1)

    if not bichinho.vivo():
        print(f"Infelizmente o {bichinho.nome} faleceu.")
        time.sleep(10000)

if __name__ == "__main__":
    main()
