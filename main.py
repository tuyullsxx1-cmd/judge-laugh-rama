import os

LINE = (
    "My calendar is so full of meetings about meetings that I now "
    "book meetings to recover from booking meetings."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
