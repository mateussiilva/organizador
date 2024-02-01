import os
from os.path import join, isfile, isdir, splitext
from colorama import init, Back, Fore, Style


init()  # COLORAMA INIT
HOME = os.getenv("HOME")
PATH = join(HOME, "Downloads")

STRUCT_PASTAS = {
    "arquivosFontes": ("deb", 'py', "c", "h"),
    "arquivosPDF": ("pdf",),
    "arquivosCompactados": ("zip", "xz", "gz"),
    "planilhas": ("xlsx", "xls"),
    "arquivosTEMPS": None,
}


def criar_pasta(path: str,nome: str ):
    try:
        p = join(path, nome)
        os.mkdir(p)
        print(Fore.GREEN, f"[CREATE DIR]: {p}", Style.RESET_ALL)
    except:
        print(Fore.RED, f"[DIR EXISTS]: {p}", Style.RESET_ALL)


def listar_arquivos(path: str) -> list:
    return [join(path, f) for f in os.listdir(path) if isfile(join(path, f))]


def listar_diretorios(path: str) -> list:
    return [join(path, d) for d in os.listdir(path) if isdir(join(path, d))]


def get_extensoes(arquivo: str) -> str:
    n, e = splitext(arquivo)
    return e.strip(".")


if __name__ == "__main__":
    lista_arquivos = listar_arquivos(PATH)
    lista_pastas = listar_diretorios(PATH)
    
    for pasta in STRUCT_PASTAS:
        p_pasta = join(PATH, pasta)
        if p_pasta not in lista_pastas:
            criar_pasta(pasta)

    for arquivo in lista_arquivos:
        extensao = get_extensoes(arquivo)
        print(extensao)
