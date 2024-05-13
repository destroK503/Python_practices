import argparse

# define the parse object
parser = argparse.ArgumentParser(
    prog="Cowsay by Destro",
    description="This program is just like cowsay",
    epilog="LARGA VIDA A Arstotzka!!!")

parser.add_argument('--monkey',
                    help='This will use a monkey instead of the cow')

args = parser.parse_args()
