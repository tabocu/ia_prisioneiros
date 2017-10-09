import argparse

parser = argparse.ArgumentParser(description='Processa dados CSV')

parser.add_argument("-f", "--file", dest="filename", help="Arquivos CSV", metavar="FILE")

args = parser.parse_args()

print args.filename
