import json


def read_file(path):
	with open(path, 'r', encoding='utf-8') as file:
		return json.dumps(json.load(file), indent=2, sort_keys=True, ensure_ascii=False).splitlines()


def write_file(path, str):
	with open(path, 'w') as file:
		file.write(str)


def create_list_by_list_id(list, list_id):
	return [list[idx].replace('"title":', '')
					 .replace(',', '')
					 .replace('"', '')
					 [5:]
			   for idx in range(1, len(list))
			   if f'"list_id": {list_id}' in list[idx - 1]]


def main():
	json = [str for str in read_file('anime-list.json') if 'title' in str or 'list_id' in str]

	tmp = create_list_by_list_id(json, 1)
	write_file('anime-list-result_inprocess.txt', '\n'.join(tmp))
	
	tmp = create_list_by_list_id(json, 2)
	write_file('anime-list-result_notstarted.txt', '\n'.join(tmp))
	
	tmp = create_list_by_list_id(json, 3)
	write_file('anime-list-result_completed.txt', '\n'.join(tmp))

	tmp = create_list_by_list_id(json, 4)
	write_file('anime-list-result_favorite.txt', '\n'.join(tmp))

	tmp = create_list_by_list_id(json, 5)
	write_file('anime-list-result_abandoned.txt', '\n'.join(tmp))


if __name__ == "__main__":
	main()
