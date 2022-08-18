import os

problems = dict()
recent = dict()


def main():
    scan_dir()
    update_md()


def scan_dir():
    global problems
    global recent

    for x in os.listdir():
        if x.startswith("DAY"):
            for i in os.listdir(x):
                if not i.startswith(".") and not i.endswith(
                    ".out"
                ):  # Ignores .DS_Count && .out files
                    # Addes to count
                    ws = i[i.find("_") + 1 : i.find("]")]
                    if ws in problems:
                        problems[ws] += 1
                    else:
                        problems[ws] = 1

                    # Updates Recent
                    day = i[1 : i.find("_")]
                    rbs = "\\_"
                    if ws in recent:
                        if (
                            day
                            > recent[ws][
                                recent[ws].find("[", 1) + 1 : recent[ws].find("_")
                            ]
                        ):
                            recent[
                                ws
                            ] = f"[{i.replace('_', f'{rbs}')}]({x.replace(' ', '%20')}/{i.replace(' ', '%20')})"
                    else:
                        recent[
                            ws
                        ] = f"[{i.replace('_', f'{rbs}')}]({x.replace(' ', '%20')}/{i.replace(' ', '%20')})"


def update_md():
    global problems
    global recent

    file = "README.md"
    dl = "||:|:|"  # divider line

    with open(file, "r") as mdr:  # mdr: markdown-read
        # remove all data till table divider line
        sl = int()
        for ln, line in enumerate(mdr, 1):  # ln : line-number
            if line.startswith("|"):
                line = line.replace("-", "")
                line = line.replace(" ", "").strip()
                if line == dl:
                    sl = ln
                    break
        mdr.seek(0)
        data = mdr.readlines()
        dlen = len(data)

        for i in range(dlen - sl):
            data.pop((dlen - 1) - i)
        mdr.seek(len(data))

        # update data
        for idx in problems:
            data.append(f"| {idx} | {problems[idx]} | {recent[idx]} |\n")

        with open(file, "w") as mdw:
            mdw.writelines(data)


if __name__ == "__main__":
    main()
