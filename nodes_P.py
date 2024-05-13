# NOTE: well this code is olmost done
# just a few more thing are expected
# to be add in the future and those things are:
# TODO:
# -(Necessary) refactor this code
# -add the logic to detect the shorter way to get from one
# node to the other
# -add mause tracking so the script can detect
# if the user has click on a valid node
# -(MAYBE) a user interface for the script with tkinter

# NOTE: GOOD LUCK DESTRO OF THE FUTURE :)
from colorama import Fore


map = [
    ["x", "p", "x"],
    ["x", "x", "x"],
    ["x", "x", "x"],
    [" ", "x", "x"],
]


def debug(message: str, type_info: str) -> None:
    """This function helps you to debug stuff
    tipes of data
    I = Information
    W = Warning
    E = Error

    Usage:
    debug("this is some information", "I")

    """
    if type_info == "W":
        print(Fore.YELLOW + f"[WARN] {message}")
        print(Fore.RESET)
    elif type_info == "E":
        print(Fore.RED + f"[ERROR] {message}")
        print(Fore.RESET)
    else:
        print(Fore.GREEN + f"[INFO] {message}")
        print(Fore.RESET)


def get_initial_node(map: list) -> dict:
    """Pass a map (as a list) and this funtion
    will return a dictionary with all the necesary
    information about the map"""

    # get x & y axes of the whole map
    var_y = 0
    var_x = 0
    temp_row = map[0]

    for items in map:
        var_y += 1
    for items in temp_row:
        var_x += 1

    # get the positon of all the nodes
    nodes_coordinates = {}
    nodes_coordinates["var_x"] = var_x
    nodes_coordinates["var_y"] = var_y
    counter = 0
    for x, rows in enumerate(map):
        for y, item in enumerate(rows):

            if item == "p":
                nodes_coordinates['Init_node'] = [x, y]

            if item != " " and item != "":
                nodes_coordinates[f'node{counter}'] = [x, y]
                counter += 1

    debug(f"there are {var_y} rows in the y axis", "I")
    debug(f"there are {var_x} items in the x axis", "I")
    debug(f"total valid nodes found {counter}", "I")
    debug(f"DIC: {nodes_coordinates}", "I")
    print()
    return nodes_coordinates


def grap_nodes(nodes_info: dict) -> None:
    """Pass this function a node map as a dictionary
    and this function will graph it for you"""

    WALL = "#"
    NODE = "O"
    INITIAL_NODE = "@"
    WHITE_SPACE = "*"

    # graph the y axes
    print('Y')
    print()

    while (True):
        for row in range(0, nodes_info['var_y']):
            print(f"{WALL}", end=" ")

        # yep another loop to print the nodes on this collum
            for col in range(0, nodes_info['var_x']):
                if [row, col] == nodes_info['Init_node']:
                    print(INITIAL_NODE, end=" ")
                elif [row, col] in nodes_info.values():
                    print(NODE, end=" ")
                else:
                    print(WHITE_SPACE, end=" ")
            print()

        # graph the x axe
        # HACK: we start at -1 so we can graph the 0,0 node
        # plus all the other nodes that are in x
        for i in range(-1, nodes_info['var_x']):
            print(f"{WALL}", end=" ")

        print(" ", end="")
        print("X", end="")
        print()

        # graph the nodes
        break


if __name__ == "__main__":
    nodes_info = get_initial_node(map)
    grap_nodes(nodes_info)
