from pprint import pprint


def sort_sneakers(sort_list, sort_by):
    return sorted(sort_list, key=lambda item: item[sort_by])


def main():
    with open("sneakers.csv", "r", encoding="utf-8") as file:
        sneakers_list = []
        file.readline()
        keywords = ["title", "color", "full price", "current price", "publish date"]
        sneakers = file.readlines()
        sneakers = [i.strip("\n").split(",") for i in sneakers]
        for i in sneakers:
            current_shoe = {}
            for j in range(len(i)):
                if i[j].replace(".", "").isdigit():
                    current_shoe[keywords[j]] = float(i[j])
                else:
                    current_shoe[keywords[j]] = i[j]
            sneakers_list.append(current_shoe)
    for i in range(len(keywords)):
        print(f"{i + 1} - {keywords[i]}")
    sort_by = keywords[int(input("Sort by: ")) - 1]
    print(sort_by)
    pprint(sort_sneakers(sneakers_list, sort_by), sort_dicts=False)


main()
