from collections import Counter

# python -m pip install lorem
# conda install -y lorem
# micromamba install -y lorem

import lorem


def main() -> None:
    pass

    # print(lorem.paragraph())

    # text_tokens = (
    #     lorem.paragraph().strip().replace(".", "").replace(",", "").split(" ")
    # )

    # print(text_tokens)

    # c = Counter(text_tokens)

    # print(c.most_common(5))
    # print(c.total())

    # more_text_tokens = (
    #     lorem.paragraph().strip().replace(".", "").replace(",", "").split(" ")
    # )

    # c.update(more_text_tokens)

    # print(c.most_common(5))
    # print(c.total())


if __name__ == "__main__":
    main()
