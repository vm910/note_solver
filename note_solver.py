from collections import deque
import string
import sys

def set_notes(raw_notes):
    notes = []
    i = 0

    while i < len(raw_notes):
        if i + 1 <= len(raw_notes) - 1:
            if raw_notes[i + 1] == '#' or raw_notes[i + 1] == 'b':
                notes.append(raw_notes[i] + raw_notes[i + 1])
                i += 2
            else:
                notes.append(raw_notes[i])
                i += 1
        else:
            notes.append(raw_notes[i])
            i += 1

    return [n for n in notes if n != ' ']

def find_index(octaves, octave):
    remainders = [octave - o if octave > o else o for o in octaves]
    return remainders.index(min(remainders))

def decrypt(octaves, cipher_octaves, cipher_notes, shifted_sections):
    notes_map = { 
        "C"  :  0,
        "C#" :  1,
        "Db" :  1,
        "D"  :  2,
        "D#" :  3,
        "Eb" :  3,
        "E"  :  4,
        "F"  :  5,
        "F#" :  6,
        "Gb" :  6,
        "G"  :  7,
        "G#" :  8,
        "Ab" :  8,
        "A"  :  9,
        "A#" : 10,
        "Bb" : 10,
        "B"  : 11
    }
    decrypted = []

    for notes, octave_key in zip(cipher_notes, cipher_octaves):
        s = ''
        for note, octave in zip(notes, octave_key):
            if octave == '?':
                s += octave
            elif int(octave) not in octaves:
                s += shifted_sections[find_index(octaves, int(octave))][notes_map[note]]                
            else:
                s += shifted_sections[octaves.index(int(octave))][notes_map[note]]
        decrypted.append(s)    

    return decrypted

def main():
    interval_keys = {
        'perfect unison'   :  0, 
        'minor second'     :  1, 
        'major second'     :  2, 
        'minor third'      :  3, 
        'major third'      :  4, 
        'perfect fourth'   :  5, 
        'diminished fifth' :  6,   
        'augmented fourth' :  6, 
        'perfect fifth'    :  7, 
        'minor sixth'      :  8, 
        'major sixth'      :  9, 
        'minor seventh'    : 10, 
        'major seventh'    : 11, 
        'perfect octave'   : 12
    }
    
    data = open(sys.argv[1], 'r').readlines()

    octaves   = [int(x) for x in list(data[0].rstrip())]
    intervals = [interval_keys[x.translate(str.maketrans('', '', string.punctuation)).rstrip()] for x in data[1].split(', ')]

    section_1 = deque(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'))
    section_1.rotate(intervals[0])

    section_2 = deque(('M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'))
    section_2.rotate(intervals[0] + intervals[1])

    section_3 = deque(('Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))
    section_3.rotate(intervals[0] + intervals[2])

    octave_keys = [
        list(data[2].rstrip()),
        list(data[3].rstrip()),
        list(data[4].rstrip()),
        list(data[5].rstrip())
    ]

    notes_list = [
        set_notes(list(data[6].rstrip())), 
        set_notes(list(data[7].rstrip())), 
        set_notes(list(data[8].rstrip())), 
        set_notes(list(data[9]))
    ]

    shifted_sections = [
        list(section_1),
        list(section_2),
        list(section_3)
    ]

    solution = decrypt(octaves, octave_keys, notes_list, shifted_sections)

    print(*solution, sep = '\n')

if __name__ == "__main__":
    main()