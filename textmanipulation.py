# -*- coding : utf-8 -*-

REGEX_TITLE = r"^([A-Z].*)+"
REGEX_EMAILS = r"[\w\-_.]+@[\w\-_.]+"
REGEX_ABSTRACT = r"(Abstract(-|.| |\n))\n? ?((.|\n)*)(?=(1(\n| |( \n)|. )Introduction)|(I. INTRODUCTION))"
REGEX_NO_ABSTRACT = r"(?<=\n)(.|\n)*(?=(1(\n| |( \n)|. )Introduction)|(I. INTRODUCTION))"
REGEX_REFERENCES = r"(?<=References|REFERENCES)+((.|\n)*)"
REGEX_TABREFERENCES = r"\[[0-9|, ]+\]"

# Retire les caracteres indesirables d'un String
def preCleanText(text):
    # 2 espaces -> 1
    text = text.replace("  ", ' ')
    # è UTF-8
    text = text.replace("`e", 'è')
    # é UTF-8
    text = text.replace("´e", 'é')
    # retour à la ligne mot coupe
    text = text.replace("- \n", '')
    
    return text

def pasCleanText(text):
    # Pour que le texte soit sur une seule ligne
    text = text.replace('\n', ' ')
    text = text.replace('\n\n', '\n')
    return text

def allClean(text):
    text = preCleanText(text)
    text = pasCleanText(text)

    return text

# Passe la premiere lettre du nom et prenom des auteurs en majuscule
def authorFormat(authors):
    newAuthors = []
    for author in authors:
        newAuthors.append(author.title())
    return newAuthors

# Arrange le texte ecris dans le fichier .xml a partir des attributs de pdfTPT
def arrangeTXT(pdfTPT):
    mergeAll = pdfTPT.filename + '\n' + pdfTPT.title + '\n'

    for author in pdfTPT.authors:
        mergeAll += author + '; '
    mergeAll += '\n'

    for email in pdfTPT.emails:
        mergeAll += email + '; '
    mergeAll += '\n'

    mergeAll += pdfTPT.abstract + '\n'

    for reference in pdfTPT.references:
        mergeAll += reference + ";\n"

    return mergeAll

def arrangeXML(pdfTPT):
    mergeAll = "<article>\n"
    mergeAll += "\t<preamble> " + pdfTPT.filename + " </preamble>\n"
    mergeAll += "\t<titre> " + pdfTPT.title + " </title>\n"
    mergeAll += "\t<auteurs>\n"
    
    '''
    i = 0
    for author in pdfTPT.authors:
        mergeAll = "\t\t<auteur>\n"
        mergeAll = "\t\t\t<name>\n " + author + " </name>\n"
        mergeAll = "\t\t\t<mail> " + pdfTPT.emails[i] + " </mail>\n"
        mergeAll = "\t\t</auteur>\n"

        i+=1
    '''
    
    mergeAll += "\t</auteurs>\n"
    mergeAll += "\t<abstract> " + pdfTPT.abstract + " </abstract>\n"
    for reference in pdfTPT.references:
        if reference != "":
            mergeAll += "\t\t<biblio> " + reference + " </biblio>\n"
    mergeAll += "</article>"

    return mergeAll
