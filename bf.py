code = "++++++++++[>,.<.]"
position = 0

memory = {}
pointer = 0
inputBuffer = ""

def getPointerValue():
    try:
        return memory[pointer]
    except:
        return 0

while position < len(code):
    char = code[position]
    if char == "#":
        print("DEBUG: cell {} = {}".format(pointer, getPointerValue()))
    elif char == ">":
        pointer += 1
    elif char == "<":
        pointer -= 1
    elif char == "+":
        memory[pointer] = getPointerValue() + 1
    elif char == "-":
        memory[pointer] = getPointerValue() - 1
    elif char == ".":
        print(chr(getPointerValue()), end="")
    elif char == ",":
        if inputBuffer == "":
            inputBuffer = input("The program asks for input: ")
        memory[pointer] = ord(inputBuffer[0])
        inputBuffer = inputBuffer[1:]        
    elif char == "[":
        if getPointerValue() == 0:
            position += 1
            endsToIgnore = 0
            while position < len(code):
                char = code[position]
                if char == "[":
                    endsToIgnore += 1
                elif char == "]":
                    if endsToIgnore > 0:
                        endsToIgnore -= 1
                    else:
                        break
                position += 1
    elif char == "]" and getPointerValue() != 0:
            position -= 1
            startsToIgnore = 0
            while position > 0:
                char = code[position]
                if char == "]":
                    startsToIgnore += 1
                elif char == "[":
                    if startsToIgnore > 0:
                        startsToIgnore -= 1
                    else:
                        position -= 1
                        break
                position -= 1
    position += 1
