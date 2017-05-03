# Automatic Summarizer

## Apps

This project was made from a necessity to create a system that integrates convertion, summarization, translation and alignment of a corpus' file into one project called Automatic Summarizer.
So, since a pdf file, this Automatic Summarizer will do all of this 4 steps, described before, using existing APIs in Python for each one.
Next, each app and their purpose:

### Converter ([PDF Miner](https://github.com/euske/pdfminer))
This app converts PDF files into TXT format

### Summarizer ([Sumy](https://github.com/miso-belica/sumy), [PyTeaser](https://github.com/xiaoxu193/PyTeaser), [Summa](https://github.com/summanlp/textrank) or [Gensim](https://github.com/RaRe-Technologies/gensim)) _Almost Done_
This app summarizes the TXT file and return some metrics data

### Translator ([TextBlob](https://github.com/sloria/TextBlob)) _In Progress_
This app translates the language of the TXT summarized file (e.g.: PT-BR -> FR)

### Aligner ([Yalign](https://github.com/machinalis/yalign))
This app aligns the TXT summarized translated file

## Flowchart

![Flowchart](https://s8.postimg.org/5x2ux8smt/fluxogram.png)
