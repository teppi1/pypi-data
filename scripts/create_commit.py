import sys
import time

print("reset refs/heads/main")
print("commit refs/heads/main")
print(f"author Tom Forbes <tom@tomforb.es> {int(time.time())} +0000")
print(f"committer Tom Forbes <tom@tomforb.es> {int(time.time())} +0000")
commit_message = "Fresh import"
print(f"data {len(commit_message)}")
print(commit_message)
# println!("M 100644 :{} README.md", readme_mark);
# println!("M 100644 :{} index.json", index_json_mark);
# println!();

for line in sys.stdin:
    stripped = line.strip()
    mark, path = stripped.split(' ', 1)
    print(f"M 100644 :{mark} {path}")

print()
