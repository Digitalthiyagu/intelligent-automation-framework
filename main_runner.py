from api_tests.api_validator import check_api
from monitors.system_monitor import system_health
from log_analyzer.log_scanner import scan_log

print("\n===== API TEST =====")
api_result = check_api("https://jsonplaceholder.typicode.com/posts/1")
print(api_result)

print("\n===== SYSTEM HEALTH =====")
health = system_health()
print(health)

print("\n===== LOG SCAN =====")
log_issues = scan_log("sample.log")
print(log_issues)