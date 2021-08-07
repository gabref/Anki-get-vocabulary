# Anki-get-vocabulary
Script that takes words in a file and searches correspondent translation for the anki deck. 

## What is [Anki](https://apps.ankiweb.net/)?
**Anki** is a SRS (Spaced Repetition Study) program that helps with the memorization of anything. In this case we are using Anki for
memorizing french vocabulary.

The ideia of SRS is that when you're about to forget for example the french word for "chest", you are reminded of that "potrine" is the way you say it. 

For my deck, I wanted the following elements in the card:
- English Word
- French Word
  - When feminine and masculin exists, show both
- IPA (International Phonetic Alphabet)
- Image
- Sound

![My Image Deck](https://discord.com/channels/@me/825418727150845972/873644338956075018)

### Tasks

- [x] Download Images function
- [x] Download Audio of word in French
- [x] Get the Translation of the words in the csv file
- [x] Get the IPA in French
- [x] Progress Bar
- [x] Remove Duplicates from English Words file
- [x] Move all media to */media* folder
- [ ] Deal with Exceptions
- [ ] Finish writing README.md