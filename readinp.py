from operator import attrgetter
class notes():
    def __init__(self,note,strn,beat):
        self.note = note
        self.strn = strn
        self.beat = beat

def inputfun():
    fileopen = open("sampleinput2.txt",'r')#change to manual file later
    if fileopen.mode == 'r':
        unprocessedtabs = fileopen.read()

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
        output = "|"
        p = 0

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

            checkstr = True
            for stringcheck in " |eBGDAE" :
                if char == stringcheck or char == "\n" or char == "\r":
                    checkstr = False
            if checkstr:
                beats += 1

            for stringcheck in "1234567890":
                if char == stringcheck:
                    noteind += char
                    openstring = True
            if openstring and (char == "-" or char == "|" or char =="p" or char == "h"):
                notenum = int(noteind)
                openstring = False
                noteind = ""
                ncf.append(notes(notenum,stringno,beats))

    indnote = notes(0,0,0)
    sortedncf= sorted(ncf, key= attrgetter('beat'))
    prevbeats = sortedncf[0].beat
    for indnote in sortedncf:
        capo = 0
        if indnote.strn == 1:
            note = indnote.note + 28 + capo
        elif indnote.strn == 2:
            note = indnote.note + 23 + capo
        elif indnote.strn == 3:
            note = indnote.note + 19 + capo
        elif indnote.strn == 4:
            note = indnote.note + 14 + capo
        elif indnote.strn == 5:
            note = indnote.note + 9 + capo
        elif indnote.strn == 6:
            note = indnote.note + 4 + capo

        octave = (note//12) + 2
        key = (note%12)
        keystr = ""

        if key==0:
            keystr = "C"
        elif key==1:
            keystr = "C#"
        elif key==2:
            keystr = "D"
        elif key==3:
            keystr = "D#"
        elif key==4:
            keystr = "E"
        elif key==5:
            keystr = "F"
        elif key==6:
            keystr = "F#"
        elif key==7:
            keystr = "G"
        elif key==8:
            keystr = "G#"
        elif key==9:
            keystr = "A"
        elif key==10:
            keystr = "A#"
        elif key==11:
            keystr = "B"

        truenote = keystr+str(octave)
        if indnote.beat == prevbeats:
            output += " "+ truenote + " "
            
        else:
            if p%10 == 9:
                output += "|\n"
            p+=1
            prevbeats = indnote.beat
            output +="| " + truenote          
            
        
            
    output+=" |"
    print(output)
    return None

def main():
    inputfun()#remove when called from another func later

if __name__ == "__main__":
    main()
