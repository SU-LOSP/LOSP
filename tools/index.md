---
title: Tools
permalink: /tools/
---

For further information and to download, please follow the links below.

Excellent [annotated versions][annotated] of Shakespeare's plays are provided by
the [Folger Shakespeare Library][folger].

[annotated]: http://www.folgerdigitaltexts.org/download/
[folger]: http://www.folger.edu/

## [folgerhs](https://github.com/SU-LOSP/folgerhs)

Growing Haskell toolset to parse and handle the XML annotated version of Shakespeare's
literature the Folger Shakespeare Library provides.

Pre-processed results are also available [here](/assets/folgerhs-results.zip).

## [Male&FemaleEntries.py](/tools/Male&FemaleEntries.py)

This is a python script I created that loops through every line in a given text
and counts the number of times males speak and the number of times females speak and store them in
the appropriate variables. It then created a graph from these values.

This requires the 'matplotlib' Python module to draw the graph.

## [characters.py](/tools/characters.py)

A little Python 3 script we created that fetches a Shakespeare play from
<http://shakespeare.mit.edu/> and outputs a CSV table with the times each
character appears. It takes into account when characters enter and exit the
stage and it can be used to determine when characters meet each other.

    $ python3 characters.py http://shakespeare.mit.edu/twelfth_night/full.html
    time,character
    0,CURIO
    0,DUKE ORSINO
    1,VALENTINE
    1,CURIO
    1,DUKE ORSINO
    3,VIOLA
    6,SIR ANDREW
    …

*[CSV table]: Comma Separated Values table or spreadsheet

## [StoryArcPlotter](/tools/StoryArcPlotter.py)

A Python 3 script we made that generates a graph of the story arc of a given Shakespeare play by measuring the 'happiness' level of each line in the play. Features:

 - Generates graphs of Shakespeare plays.
 - Can find notable lines in plays based on their 'happiness' level.
 - Can export data as CSV files.

Requires 'matplotlib' Python module to draw graphs.

## [Vocabalance](https://github.com/SU-LOSP/vocabalance/)

A tool that analyses the frequency with which each character uses a word,
generating a “significance index” based on:

 - How often the character uses the word
 - How often the character speaks overall
 - How often other characters use the word

We used this to perform in-depth analysis of characters on [Richard
II](/analyses/richard_ii).

Pre-processed results are also available [here](/assets/vocabalance-results.zip).

## [AntConc](http://www.laurenceanthony.net/software/antconc/)

A freeware text analysis toolkit for concordancing and text analysis. Can be used to:

- Search for individual words in an individual play or corpus of plays
- Make concordance plots
- View n-grams

## [WordHoard](http://wordhoard.northwestern.edu/)

An application for the close reading and scholarly analysis of texts, largely
used on this project for determining the log-likelihoods of specific words and
generating word clouds to display this information in a user-friendly manner.

We have [a guide for using WordHoard](wordhoard-howto.pdf).

## [Ubiqu+ity](http://vep.cs.wisc.edu/ubiq/)

Generates statistics and identifies linguistic patterns and groups.

