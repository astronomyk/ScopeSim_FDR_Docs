import glob
import os.path as pth
from scopesim import rc
from scopesim.reports import rst_utils as ru


def convert_rst_to_tex():
    for fname in glob.glob("../rst/*.rst"):
        print(pth.basename(fname))
        with open(fname) as rst_path:
            rst_text = rst_path.read()

        f_out = pth.basename(fname).replace("rst", "tex")
        ru.latexify_rst_text(rst_text, filename=f_out, path="../tex/",
                             float_figures=False)

        rc.__config__["!SIM.reports.image_path"] = "../images/"
        ru.plotify_rst_text(rst_text)


convert_rst_to_tex()
