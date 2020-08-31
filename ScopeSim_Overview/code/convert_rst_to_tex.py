import glob
from docutils.core import publish_file, publish_parts

# publish_file(source_path="../rst/1_introduction.rst",
#              destination_path="../tex/1_introduction.tex",
#              writer_name="latex")


for fname in glob.glob("../rst/*.rst"):

    with open(fname) as rst_path:
        rst = rst_path.read()

    preamble = "Title\n<<<<<\nSubtitle\n>>>>>>>>\n\n"
    parts = publish_parts(preamble + rst, writer_name="latex")

    with open(fname.replace("rst", "tex"), "w") as tex_path:
        tex_path.write(parts["body"])
