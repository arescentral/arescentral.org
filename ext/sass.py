import os.path
import subprocess

EXTENSIONS = [".sass", ".scss"]

def setup(app):
    app.connect("build-finished", sass_static_files)

def visit_file(arg, d, paths):
    for path in paths:
        path = os.path.join(d, path)
        if not os.path.isfile(path):
            continue
        if path[-5:] not in EXTENSIONS:
            continue
        css_path = path[:-5] + ".css"
        if os.path.isfile(css_path):
            if os.stat(path).st_mtime <= os.stat(css_path).st_mtime:
                continue
        assert subprocess.call(["sass", path, css_path]) == 0

def sass_static_files(app, builder):
    os.path.walk(app.builder.outdir, visit_file, None)
