words = [
    "casa", "albero", "notte", "sole", "montagna", "fiume", "mare", "vento", "nuvola", 
    "pioggia", "strada", "amico", "sorriso", "viaggio", "tempo", "cuore", "stella", 
    "sogno", "giorno", "libro", "porta", "luce", "ombra", "silenzio", "fiore", "luna"
]

wordschars = {word: chr(i + ord('a')) for i, word in enumerate(words)}

passphrase = "fiume-amico-casa-mare-{-amico-tempo-viaggio-mare-_-sole-tempo-montagna-giorno-viaggio-libro-_-sorriso-montagna-casa-viaggio-_-giorno-montagna-notte-porta-sogno-montagna-_-mare-fiume-strada-giorno-amico-vento-vento-mare-}"
for word in passphrase.split("-"):
    if word in wordschars:
        print(wordschars[word], end="")
    else:
        print(word, end="")