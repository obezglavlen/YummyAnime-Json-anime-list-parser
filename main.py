import json


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_file(path, str):
    with open(path, "w") as file:
        file.write(str)


def create_list_by_list_id(dict, list_id):
    return [title["title"] for title in dict if title["list_id"] == list_id]


def main():
    json = read_file("anime-list.json")

    tmp = create_list_by_list_id(json, 1)
    write_file("anime-list-result_inprocess.txt", "\n".join(tmp))

    tmp = create_list_by_list_id(json, 2)
    write_file("anime-list-result_notstarted.txt", "\n".join(tmp))

    tmp = create_list_by_list_id(json, 3)
    write_file("anime-list-result_completed.txt", "\n".join(tmp))

    tmp = create_list_by_list_id(json, 4)
    write_file("anime-list-result_favorite.txt", "\n".join(tmp))

    tmp = create_list_by_list_id(json, 5)
    write_file("anime-list-result_abandoned.txt", "\n".join(tmp))


if __name__ == "__main__":
    # main()
    print("yummyanime.club dont work at the moment")
