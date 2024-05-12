def main() -> None:
    with open("colors.txt") as color_file:
        for color in color_file:
            print(color.strip())


if __name__ == "__main__":
    main()
