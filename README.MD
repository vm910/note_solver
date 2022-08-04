# Note cipher solver
Attempts to solve the note cipher in Underrail.

## Requirements
    python3.9.2

## Usage
    python note_solver.py <path_to_file>
    
Make sure the cipher file is formatted in the following way:

    [octave keys (cut the first 3 numbers from the number sequences)]
    [interval keyes (with or without the dot in the end, doesn't matter)]
    [octave key sequence 1]
    [octave key sequence 2]
    [octave key sequence 3]
    [octave key sequence 4]
    [note sequence 1]
    [note sequence 2]
    [note sequence 3]
    [note sequence 4]

## Example
    python note_solver.py .\examples\cipher.txt

the cipher.txt file looks like this:

    603
    perfect fifth, minor second, perfect fifth.
    66761176717166001167776
    00746710061766777116161166061
    664116747011011
    17610161707411611
    ABGbBDD#D#GGb D#DC#BB ABbDD#GGbC#D#G
    BBbGbDADC#BbAbGD#D#A BD#C#DD# GbGD#BC#DAGBBD
    GAbDDDGGb E DBbC#C#BbC#D
    D#DB D#BbGbBC#D#AC# Ab DD#GC#D

the decoded song names:

    CELESTIALTHREENOSTALGIA
    POLYCHROMATICEIGHTWATERSCAPES
    ABYSSAL0HORRORS
    THETOWERING4STARS

and thus the code is:

    3804