import csv

from sample import translate_cy_la

PAIRS_FILE_NAME = "test_pairs.csv"


def test_cy_la():
    sort_pairs()
    with open(PAIRS_FILE_NAME, newline='') as file:
        reader = csv.DictReader(file, delimiter='#')
        for pair in reader:
            source = pair['cy']
            expected = pair['la']
            conversion_result = translate_cy_la(source)
            if conversion_result:
                assert conversion_result == expected


def sort_pairs():
    """
    Utility method to sort test pairs alphabetically
    It preserves header on the top
    """
    with open(PAIRS_FILE_NAME, "r") as file:
        lines = set()
        next(file)  # skip the header
        for line in file:
            lines.add(line.strip())

    order = "0123456789AaÄäBbCcÇçDdEeFfGgĞğHhIıİiÍíJjKkQqLlMmNnÑñOoÖöPpRrSsŞşTtUuÜüVvWwXxYyZz'"
    sorted_pairs = sorted(lines, key=lambda word: [(order.index(c) if c in order else 0) for c in word])

    with open(PAIRS_FILE_NAME, "w") as file:
        file.write("la#cy\n")  # write the header
        for pair in sorted_pairs:
            file.write(f"{pair}\n")
