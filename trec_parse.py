import re


count = 0


def parse(path: str) -> list[tuple[str, str]]:
    parsed: list[tuple[str, str]] = []
    global count
    with open(path) as f:
        data = f.read()
        matches = re.findall(r"<num> Number: (\d+)\s+<title> (.+)", data)
        for match in matches:
            parsed.append((match[0], match[1].strip()))
            count += 1
    return parsed


if __name__ == "__main__":
    parsed = parse("./downloads/trec40")
    for p in parsed:
        print(f"{p[0]}, {p[1]}")

    if count != 40:
        print("Error: count != 40")
        exit(1)
