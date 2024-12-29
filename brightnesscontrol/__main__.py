import argparse

def main():
    parser = argparse.ArgumentParser(description="Brightness dimmer beyond")

    parser.add_argument("--about", help="Take your brightness level to beyond its limits!", action="store_true")

    args = parser.parse_args()

    if args.about:
        print("Take your brightness level to beyond its limits!")

if __name__ == "__main__":
    main()