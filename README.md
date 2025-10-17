# wordmaze-distractor-generator
A Python tool for generating distractor sentences for Word Maze tasks in psycholinguistic and bilingualism research.
This script automatically generates ungrammarical distractor sequences for Word Maze (G-Maze) experiments using linguistic information from the Gutenberg corpus and Stanza POS tagging.

## The script:

Extracts sentences from Jane Austen’s Emma (Gutenberg corpus).

Builds part-of-speech (POS) based word pools using the Stanza NLP library.

Analyzes a target sentence (e.g., “Put the rabbit that is on the towel onto the tray”).

Generates a distractor sentence by sampling random words from the corresponding POS categories.

## Notes
- The script uses austen-emma.txt from the NLTK Gutenberg corpus as the example source.

- You can adjust N_SENT to increase or decrease the corpus size.

- Relative pronouns are identified using the PronType=Rel feature.
- The following part of the code handles this feature detection:
  ```python
  if w.feats and "PronType=Rel" in w.feats:
      rel_pool.add(word)
- Since Stanza is sensitive to morphological and syntactic features, this section can be easily adapted to target other features (e.g., tense, number, gender, mood) by modifying the condition within the same structure.
- The first token is fixed as "xxx" to match the input format used in jsPsych Word Maze experiments.

- Output sentences can be directly used in Word Maze task code for experimental stimuli.
