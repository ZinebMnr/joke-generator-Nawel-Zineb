import random

# Initial joke collection
jokes = [
 "Pourquoi les canards ont-ils autant de plumes ? Pour couvrir leur derrière.",
"Que dit une porte quand on la pousse trop fort ? Arrête de me claquer !",
"Pourquoi les maths adorent la forêt ? Parce qu’elles ont plein de racines.",
"Qu’est-ce qu’un oignon dit à un autre oignon ? On se retrouve au pot !",
"Pourquoi les vélos ne tiennent-ils pas debout tout seuls ? Parce qu’ils sont trop fatigués.",
"Que dit une poule qui a trouvé un trèfle à quatre feuilles ? C’est mon jour de chance !",
"Pourquoi les fantômes aiment-ils les ascenseurs ? Parce que ça les élève.",
"Que fait un mouton quand il a froid ? Il met un pull-over.",
"Pourquoi les horloges sont-elles toujours stressées ? Parce qu’elles sont pressées.",
"Que dit une abeille quand elle rentre chez elle ? Honey, I’m home !",
"Pourquoi les bananes vont-elles jamais à l’hôpital ? Parce qu’elles ont la peau dure."

]

def print_random_joke():
    """Print a random joke from the collection."""
    joke = random.choice(jokes)
    print(f"😂 {joke}")

if __name__ == "__main__":
    print("Bienvenue au Générateur de Blagues !")
    print_random_joke()

