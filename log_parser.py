import re
import pandas as pd

def parse_auth_log(file_path):
    pattern = r'^(.*) sshd.* (Failed|Accepted) password for (?:invalid user )?(\w+) from ([\d.]+)'
    results = []

    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                time, status, user, ip = match.groups()
                results.append((time, status, user, ip))

    df = pd.DataFrame(results, columns=["Timestamp", "Status", "Username", "IP"])
    return df
