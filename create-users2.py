#!/usr/bin/python3

# INET4031
# Makayla Schneider
# 10/27/25
# 10/27/25
#
# This version adds an interactive dry-run feature that allows the user to test
# the script safely before actually creating system accounts.

import os
import re
import sys

def main():
    # Ask the user whether to do a dry run or not
    dry_run_input = input("Run in dry-run mode? (Y/N): ").strip().lower()
    dry_run = (dry_run_input == 'y')

    for line in sys.stdin:
        # Skip lines starting with '#' (commented lines)
        match = re.match("^#", line)
        fields = line.strip().split(':')

        # If the line doesn’t have exactly 5 fields or is a comment, skip it
        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print(f"Skipping commented line: {line.strip()}")
                elif len(fields) != 5:
                    print(f"Error: Line skipped due to incorrect number of fields ({len(fields)}): {line.strip()}")
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"

        if dry_run:
            print(f"[DRY RUN] Would execute: {cmd}")
        else:
            os.system(cmd)

        print(f"==> Setting the password for {username}...")
        cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"

        if dry_run:
            print(f"[DRY RUN] Would execute: {cmd}")
        else:
            os.system(cmd)

        for group in groups:
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"
                if dry_run:
                    print(f"[DRY RUN] Would execute: {cmd}")
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
