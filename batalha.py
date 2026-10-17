from os import system
import random

system('cls')


class Personagem:
    def __init__(self, nome, energia, dano):
        self.nome = nome
        self.energia = energia
        self.dano = dano

    def atacar(self, inimigo):
        energia_anterior = inimigo.energia
        inimigo.energia -= self.dano

        # Evita energia negativa
        inimigo.energia = max(inimigo.energia, 0)

        print(f'{self.nome} atacou {inimigo.nome}, causando {self.dano} de dano.')
        print(
            f'{inimigo.nome} tinha {energia_anterior} '
            f'e agora tem {inimigo.energia} de energia.\n'
        )

        if inimigo.energia == 0:
            print(f'{inimigo.nome} foi derrotado por {self.nome}!\n')


print("=" * 50)
print("Bem-vindo ao jogo de batalha!")
print("=" * 50)

# Criando os personagens
mago = Personagem("Mago", 100, 20)
guerreiro = Personagem("Guerreiro", 120, 15)
personagem_random = Personagem(
    "Random",
    random.randint(80, 150),
    random.randint(10, 25)
)

# Lista com todos os personagens
personagens = [mago, guerreiro, personagem_random]

# A batalha continua enquanto houver mais de um personagem vivo
while sum(1 for p in personagens if p.energia > 0) > 1:

    # Seleciona somente personagens vivos
    vivos = [p for p in personagens if p.energia > 0]

    # Escolhe o atacante e o personagem atacado
    atacar = random.choice(vivos)

    # O atacante não pode atacar a si mesmo
    possiveis_alvos = [p for p in vivos if p != atacar]
    atacado = random.choice(possiveis_alvos)

    # Executa o ataque
    atacar.atacar(atacado)

# Identifica o vencedor
vencedores = [p for p in personagens if p.energia > 0]

print("=" * 50)

if vencedores:
    vencedor = vencedores[0]
    print(f"O VENCEDOR É: {vencedor.nome}!")
    print(f"Energia restante: {vencedor.energia}")
else:
    print("Todos os personagens foram derrotados!")

print("=" * 50)
print("Fim da batalha!")