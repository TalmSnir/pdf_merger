import PyPDF2
import os


def get_inputs():
    directory_name = input(
        'please enter the name of the folder the files are in (make sure it is a unique name): ')
    return directory_name


def get_pdfs_list(directory_name):
    for root, subdirs, files in os.walk('C:/'):
        for d in subdirs:
            if d == directory_name:
                normpath = os.path.normpath(root)
                path = os.path.join(normpath, d)
                return os.listdir(d), path
    return None


def pdf_merger(pdf_list, path):

    merger = PyPDF2.PdfFileMerger()
    for file in pdf_list:
        if file.endswith('.pdf'):
            merger.append(file)
    merger.write(os.path.join(path, 'merger.pdf'))


directory_name = get_inputs()

pdf_list, path = get_pdfs_list(directory_name)
pdf_merger(pdf_list, path)


# todo:
# [] add a try except
# [] gui?
# [] add a message at the end
# [] do you want to delete the seperated files?
# [] merge by what? title, sequence????
