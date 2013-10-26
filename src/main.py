
"""
To see if a list of words in a string,
we will make an array the length of the string.
The array will be initialized to false.
We will start at the end of the string.

Base Case: An empty string is a valid string / word
Rule: A string is valid from a position i
if i is a start of a word of length l and at
string[i + 1] is the start of an another word.

If we have a valid word at string[i] we will mark
the array[i] = True

We will look at each character in the string from end to front.
At each character we will check if that character is a valid word.
If that character is a valid word and the next character in the string,
aka stirng[i + 1] is a start of a valid word we will mark that location
in the array to True. If that character is not a vaild wod we will look 
at the next two characters and see if that two character string is a valid word.
Once we have a valid word we will mark the start of the word and then 
continue to the next character.

For example, the for the string "iliketoeatpie"
the array will now look like    [1100010110100]

As you notice that there is a 1 below the a in eat because at is a valid word.
This is ok. 

To split the string into words we will take the array and turn the 1's into
the length of the word.
Then with the string         "iliketoeatpie"
the array will now look like [1400020320300]

Now we will start at the beginning of the array and evey number we come acroos,
we will insert a space. With the space our string is now:
"i like to eat pie"
[1 4000 20 320 300] As you see that the first number we come across is 
how many characters belong to each word. We also see that we do not split
on the word "at" in our string because we hit the 3 below the "e" so that word
must be three letters long skipping the 2 under the "a" in at.
"""

from optparse import OptionParser
import sys, os

def main(args):
    """reads in argument and runs algorithm"""
    # Default arguments
    pathToInputFile = "./TextDocuments/sonnet.txt"
    pathToDictonary = "./TextDocuments/words.txt"

    #parce commandline agruments
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="input_file", help="Specify a path to an input file")
    parser.add_option("-d", "--Dict", dest="path_to_dictonary", help="Specity a path to a dictonary")

    (options, args) = parser.parse_args()

    if options.input_file:
        pathToInputFile = options.input_file

    if options.path_to_dictonary:
        pathToDictonary = options.path_to_dictonary

    #TODO run the algorithm with the dictonary and the file 

if __name__ == '__main__':
    main(sys.argv[1:])