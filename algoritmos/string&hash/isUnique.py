"""
dado un metodo que reciba una string, comprobar si todos los caracteres son unicos o no
text = ("abcde") => true
text ("abcded) => false
"""





def isUnique (text: str) ->bool :
    for i, char1 in enumerate(text):
        for j, char2 in enumerate(text):
            if char1 == char2 and i != j:
                return False
    return True            
#MANERA MENOS EFICIENTE O(N*N)    

def isUniqueHash(text: str) -> bool:
    NUMBERS_OF_CHARS = 128    
    if (len(text) > NUMBERS_OF_CHARS): 
        return False #128 caracteres maximo, si hay 129 si o si uno se repite
    Characters = set()
    for c in text:
        if (c in Characters):
            return False
        else:
            Characters.add(c)    
    return True



print(isUniqueHash("ABCBD"))
print(isUnique("HOLAA"))