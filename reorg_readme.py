# Add additional blank in leetcode_record.md

import os, sys, shutil


def main():
    in_file = "leetcode_record_backup.md"
    out_file = "leetcode_record.md"

    with open(in_file, "r") as in_f:
        with open(out_file, "w") as out_f:
            for line in in_f:
                record = line.strip().split('|')
                record[-3] = record[-3] + "\t"
                res = '|'.join(record)
                out_f.write(res + "\n")

            # print(record)
            # print(res)
            # sys.exit(0)


if __name__ == '__main__':
    main()
