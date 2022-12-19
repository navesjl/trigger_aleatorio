import random

def trigger_aleatorio():
    velocidade = [ "rápido", "devagar"]
        gatilhos = [ 
            "hand sounds", "tapping", "mouth sounds", "inaudivel", "fabric scratching", "head massage", "luvas"
        ]
        velocidade_escolhida = random.choice(velocidade)
        gatilho_escolhido = random.choice(gatilhos)
        return velocidade_escolhida, gatilho_escolhido

        trigger_aleatorio ()
        print(trigger_aleatorio)
        print(str(random.randint(2,5)) + " minutos")
