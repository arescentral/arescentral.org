import gzip
import os.path

EXTENSIONS = [".html", ".css", ".js"]

def setup(app):
    app.connect('build-finished', gzip_static_files)

def visit_file(arg, d, paths):
    for path in paths:
        path = os.path.join(d, path)
        if not os.path.isfile(path):
            continue
        if os.path.splitext(path)[-1] not in EXTENSIONS:
            continue
        gz_path = path + ".gz"
        if os.path.isfile(gz_path):
            if os.stat(path).st_mtime <= os.stat(gz_path).st_mtime:
                continue
        with open(path, "r") as f_in:
            with gzip.open(gz_path, "w") as f_out:
                f_out.write(f_in.read())

def gzip_static_files(app, builder):
    os.path.walk(app.builder.outdir, visit_file, None)
