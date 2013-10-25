CSCI-406-HW06
=============

*Problem 4 (40 points) You may work in pairs or groups of three on this task. You are given a string of n characters s[1: : : n], which you believe to be a corrupted text document in which all punctuation has vanished and all words have been lowercased (so that it looks something like \itwasthebestoftimes...").
Using dynamic programming, write a program that determines whether such a string can be reconstituted
as a sequence of valid words. The running time should be at most O(n^2), assuming dictionary lookups are
O(1) operations. In the event that the string is valid, make your program output the corresponding sequence
of words.

Some sample strings are provided on the course website, along with a dictionary of words. Note you will need to implement a constant time lookup for your dictionary - expected O(1) is fine - so use your favorite language's hash table implementation, or write your own.
For your write up of this exercise, please include:

** the names of the people you worked with;
** your code;
** a description of your algorithm and any other interesting aspects of your code;
** a discussion of any problems you encountered in developing code for this problem, and what you did to solve them;
** your code's output on the test document \genesis.txt".
