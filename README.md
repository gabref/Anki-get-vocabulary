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

Now, following the ideias of [Gabriel Wyner](https://home.fluent-forever.com/#) for learning languages, we are going to create different types of cards in our anki using the elements the our python script will get. The types are the following:

1. Comprehension
2. Production
3. Translation

### 1 - Comprehension

What’s this word mean? How do you pronounce it?
A Comprehension card looks like this:

![Comprehension Card](/images/comprehension_card.png)

In the front of the card the word in the target language will show up, and you will have to try to remeber its meaning. The important thing is to remember the meaning, in the back of the card you will hear the audio of the word and have the IPA for the right pronunciation, but that's not the main goal here.

### 2 - Production

What’s the word for this picture/concept? Can you pronounce it?
A Production card looks like this:

![Production Card](/images/production_card.png)

Here the main goal is to remember the word in the target language and the pronunciation as well. Pay attention to the audio and the IPA in the back of the card to evaluate yourself.

### 3 - Translation

How do you say this word in the target language?
A Translation card looks like this:

![Translation Card](/images/translation_card.png)

The main goal of this type of card is to remember how to say the word in the target language, its translation from English.

### Tasks

- [x] Download Images function
- [x] Download Audio of word in French
- [x] Get the Translation of the words in the csv file
- [x] Get the IPA in French
- [x] Progress Bar
- [x] Remove Duplicates from English Words file
- [x] Move all media to */media* folder
- [ ] Deal with Exceptions
- [ ] Add table of contents to README.md
- [ ] Finish writing README.md