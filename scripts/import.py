import sys
import pathlib
import shutil
import hashlib
import orjson
stdout = sys.stdout
stderr = sys.stderr

output_stream = pathlib.Path(sys.argv[1])

with output_stream.open("wb", buffering=1024 * 1024 * 5) as output:
    for idx, path in enumerate(sys.stdin, 1):
        path = path.rstrip()
        p = pathlib.Path(path)

        # digest = hashlib.sha1(p.read_bytes()).hexdigest()
        # stdout.buffer.write(f"# {path} - {digest}\n".encode())
        contents = p.read_bytes()
        if path.startswith("release_data/"):
            contents = orjson.dumps(orjson.loads(contents), option=orjson.OPT_SORT_KEYS)

        output.write(f"blob\nmark :{idx}\ndata {len(contents)}\n".encode())
        output.write(contents)
        output.write(b"\n")
        print(f"{idx} {path}")
