# Automatic Summarizer

## Apps

This project is from UnB and, since a pdf file, summarizes the content, translates, and aligns it. Everything splitted in four steps (Apps) that all of them integrate the system. Next, each app and their purpose

### Converter ([PDF Miner](https://github.com/euske/pdfminer))
This app converts PDF files into TXT format

### Summarizer ([Sumy](https://github.com/miso-belica/sumy) or [PyTeaser](https://github.com/xiaoxu193/PyTeaser)) _Almost Done_
This app summarizes the TXT file and return metrics data about it

### Translator ([TextBlob](https://github.com/sloria/TextBlob)) _In Progress_
This app translates the language of the TXT summarized file (PT-BR -> FR)

### Aligner
This app aligns the TXT summarized translated file