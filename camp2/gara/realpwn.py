alpha = "AÀÁÂÃÄÅĀĂĄǍǞǠǺȀȂȦȺΆΑᵃ"
beta = "abcdefghilmnopqrstuvz"

flag = "ÁÃȦAȂÃȦAȂÃÀÀÃÄĂÃȂǠ"

enc = "".join(beta[alpha.index(x)] for x in flag)

print(enc)