import glob
import os.path as pth
from scopesim import rc
from scopesim.reports import rst_utils as ru


for fname in glob.glob("../rst/*.rst"):
    print(pth.basename(fname))
    with open(fname) as rst_path:
        rst_text = rst_path.read()

    f_out = pth.basename(fname).replace("rst", "tex")
    ru.latexify_rst_text(rst_text, filename=f_out, path="../tex/",
                         float_figures=False)


for fname in glob.glob("../tex/*.tex"):
    with open(fname) as f:
        data = f.read()

    data = data.replace("begin{figure}[H]", "begin{figure}")
    data = data.replace("ref\{", r"\ref{")
    data = data.replace("\}", r"}")
    data = data.replace("citep\{", r"\citep{")
    data = data.replace("citet\{", r"\citet{")

    with open(fname, 'w') as f:
        f.write(data)

