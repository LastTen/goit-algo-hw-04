def get_cats_info(path: str) -> list[dict]:
    """
    returns a list of dictionaries with information about each cat
    """
    cats_list = []
    try:
        # read the file
        with open(path, "r", encoding="utf-8") as fh:
            try:
                # iterate over the file rows
                for el in fh.read().split("\n"):
                    # add each row like dict to the cats_list
                    cats_list.append(
                        {
                            "id": el.split(",")[0],
                            "name": el.split(",")[1],
                            "age": el.split(",")[2],
                        }
                    )
            # if mistake in file
            except IndexError:
                return "Invalid data format"
        # if all ok
        return cats_list
    # if mistake in path/ file not found
    except FileNotFoundError as e:
        return e


if __name__ == "__main__":
    cats_info = get_cats_info("second/cats.txt")
    print(cats_info)
