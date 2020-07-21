def inputfun():
    fileopen = open("sampleinput.txt",'r')#change to manual file later
    if fileopen.mode == 'r':
        unprocessedtabs = fileopen.read()
        print(unprocessedtabs)

        class notes():
            def __init__(self,note,strn,beat):
                self.note = note
                self.strn = strn
                self.beat = beat

        stringno = 0 #for initial blank spaces
        beats = 0
        notevar = 0
        changerow = False
        ncf = [] #notesconvertedform
        prevbeats = 0
        rowbeats = 0
        beatsdeb = ""
        noteind = ""
        openstring = False
        printnote = False #debug

        for char in unprocessedtabs:

            if char == "e":
                stringno = 1
                changerow = True
                prevbeats = rowbeats
            if char == "B":
                stringno = 2
                changerow = True
                rowbeats = beats
                beats = prevbeats
            if char == "G":
                stringno = 3
                changerow = True
                beats = prevbeats
            if char == "D":
                stringno = 4
                changerow = True
                beats = prevbeats
            if char == "A":
                stringno = 5
                changerow = True
                beats = prevbeats
            if char == "E":
                stringno = 6
                changerow = True
                beats = prevbeats

            for stringcheck in "1234567890":
                if char == stringcheck:
                    noteind += char
                    openstring = True
            if openstring and (char == "-" or char == "|" or char =="p" or char == "h"):
                notenum = int(noteind)
                openstring = False
                noteind = ""
                printnote = True

            checkstr = True
            for stringcheck in " |eBGDAE" :
                if char == stringcheck or char == "\n" or char == "\r":
                    checkstr = False
            if checkstr:
                beats += 1
                if printnote:
                    beatsdeb = beatsdeb + str(notenum)
                else:
                    beatsdeb = beatsdeb + "-"#debug

            if char== "\n" or char == "\r":
                beatsdeb = beatsdeb + "beatcount=" + str(beats) + "\n"#debug

            printnote =False

        print(beatsdeb)#debug
    return None

def main():
    inputfun()#remove when called from another func later

if __name__ == "__main__":
    main()
