'''
# LAB_FUNCTIONS_3

## write a function that takes a string as a parameter
- first check that the type of the parameter is of type str
- then, it should separates the word at any capital letter and replace it with a small letter 
- and  should return the new modified string !

Example: helloWorld --> hello world'''

def reconstruct (char : str) -> str:
    if (char.islower() == True):
        rerun: str = (char + '')
        return rerun
                #print("Test")
    else:
        rerun : str = (' '+char.lower())
        return rerun
            #if (islower(rewright)

usrtxt : str = str(input("Input Your Text:"))
for char in usrtxt:
    print(reconstruct(char), end ='')