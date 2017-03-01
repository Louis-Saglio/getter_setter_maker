def iter_file(file_name):
    with open(file_name) as file:
        i = 0
        for ligne in file:
            i += 1
            yield {"line_num": i, "text": ligne}


def find_line_in_file(file_name, line):
    for file_line in iter_file(file_name):
        if file_line["text"] == line:
            return file_line["line_num"]
    return False


def copy_piece_of_file(file_name, start, end):
    piece_of_file = ''
    for line in iter_file(file_name):
        if start <= line["line_num"] <= end:
            piece_of_file += line["text"]
    return piece_of_file


def find_file_last_line(file_name):
    line_num = {"line_num": None, "text": "## Fichier vide ##"}
    for line_num in iter_file(file_name):
        pass
    last_line = line_num
    return last_line


def insert_line_into_file(file_name, line, where):
    """
    :param file_name: Une str du non du fichier où insérer une ligne
    :param line: Une str de la ligne à insérer
    :param where: Une str de la ligne après laquelle insérer, si elle n'existe pas ce sera insérer au début du fichier
    :return: None. La fonction agit directement sur le fichier et ne renvoi rien
    """
    if isinstance(where, int):
        where_num = where
    else:
        where_num = find_line_in_file(file_name, where)
    file_start = copy_piece_of_file(file_name, 1, where_num)
    file_end = copy_piece_of_file(file_name, where_num + 1, find_file_last_line(file_name)["line_num"])
    with open(file_name, 'w') as file:
        print(file_start, line, file_end, sep='', end='', file=file)


if __name__ == "__main__":
    a = iter_file("Exemple/origin.txt")
    for e in a:
        print(e)
    print("iter_file fonctionne")
    print(find_line_in_file("Exemple/origin.txt", "# ligne 5\n"))
    print("find_line_in_file() fonctionne")
    print(copy_piece_of_file("Exemple/origin.txt", 2, 5))
    print(find_file_last_line("Exemple/origin.txt"))
    insert_line_into_file("Exemple/origin.txt", "# ligne rajoute\n", "# ligne 4\n")
