def scan_log(file_path):
    issues = []

    try:
        with open(file_path, "r") as file:
            for line_no, line in enumerate(file, start=1):
                if any(keyword in line for keyword in ["ERROR", "FAIL", "CRITICAL"]):
                    issues.append(f"Line {line_no}: {line.strip()}")

    except FileNotFoundError:
        return ["WARNING: Log file missing – investigation required"]

    return issues if issues else ["No critical issues found"]