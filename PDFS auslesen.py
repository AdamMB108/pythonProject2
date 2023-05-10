from PYPDF2 import PdfFileReader

def get_meta(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        nop = pdf.getNumPages()
    print(info)
    print(nop)

if __name__ == '__main__':
    #Hier fehlt der Link des Dateipfads in dem die PDF-Datei drin ist.
