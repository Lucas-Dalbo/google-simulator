import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(0, instance.__len__()):
        data = instance.search(i)
        if data["nome_do_arquivo"] == path_file:
            return (- 1)

    lines = txt_importer(path_file)
    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    
    instance.enqueue(file_dict)
    print(file_dict, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
