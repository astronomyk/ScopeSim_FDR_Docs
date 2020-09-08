import glob
import os.path as pth
from scopesim import rc
from scopesim.reports import rst_utils as ru
from docutils.core import publish_file, publish_parts

# [!37] excludes ScopeSim_templates and Spextra
# for fname in glob.glob("../rst/[!37]*.rst"):

# for fname in glob.glob("../rst/*.rst"):
#     print(fname)
#     with open(fname) as rst_path:
#         rst = rst_path.read()
#
#     preamble = "Title\n<<<<<\nSubtitle\n>>>>>>>>\n\n"
#     parts = publish_parts(preamble + rst, writer_name="latex")
#     if "1_" in fname:
#         print(parts["whole"])
#
#     with open(fname.replace("rst", "tex"), "w") as tex_path:
#         tex_path.write(parts["body"])
#


for fname in glob.glob("../rst/*.rst"):
    print(pth.basename(fname))
    with open(fname) as rst_path:
        rst_text = rst_path.read()

    f_out = pth.basename(fname).replace("rst", "tex")
    ru.latexify_rst_text(rst_text, filename=f_out, path="../tex/")

    rc.__config__["!SIM.reports.image_path"] = "../images/"
    ru.plotify_rst_text(rst_text)
