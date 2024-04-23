def total_salary(path: str) -> tuple:
    """
    Returns the total and average salary amount from the path\n
    data.txt format:\n
    "name,salary"\n"name,salary"
    """
    total_sal = 0
    count_emp = 0
    try:
        # read the file
        with open(path, "r", encoding="utf-8") as fh:
            try:
                # iterate over the file rows
                for el in fh.read().split("\n"):
                    total_sal += int(el.split(",")[-1])
                    count_emp += 1
            # if mistake in file
            except ValueError as e:
                print(e)
                return (None, None)
        # if all ok
        return (total_sal, (total_sal / count_emp))
    # if mistake in path/ file not found
    except FileNotFoundError as e:
        print(e)
        return (None, None)


if __name__ == "__main__":
    total, average = total_salary("first/salary.txt")
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )
