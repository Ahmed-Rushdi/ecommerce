def read_csv(file_path: str):
    """
    reads csv file and returns list of dictionaries with titles from first line as keys and rest as values
    """
    with open(file_path, "r") as f:
        keys = f.readline().strip().split(",")
        return [{k: v for k, v in zip(keys, line.strip().split(","))} for line in f]


def append_csv(file_path: str, payload: dict):
    """
    appends payload to file_path csv
    """
    with open(file_path, "r") as f:
        keys = f.readline().strip().split(",")

    with open(file_path, "a") as f:
        f.write("\n" + ",".join([str(payload[k]) for k in keys]))


if __name__ == "__main__":
    print(read_csv("../../orders.csv"))
