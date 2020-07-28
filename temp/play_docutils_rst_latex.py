from docutils.core import publish_string, publish_parts, publish_doctree, publish_from_doctree
from docutils import nodes


rst_text = """

.. role:: raw-latex(raw)
   :format: latex

.. tip::
    import matplotlib.pyplot as plt
    plt.savefig("my_fug.pdf, format="pdf")

.. figure:: my_fug.pdf

    This is an included figure caption
    
    :raw-latex:`\label{fig:my_fug}`
     
"""

string = publish_string(rst_text, writer_name="latex")
parts = publish_parts(rst_text, writer_name="latex")
doctree = publish_doctree(rst_text)


def print_children(obj, level=0):
    if hasattr(obj, "children"):
        for child in obj.children:
            #print(" "*2*level, level, type(obj))
            print_children(child, level=level+1)
    if isinstance(obj, nodes.Text):
        #print("*", obj, "*")
        pass

#print_children(doctree)

latex_doc = publish_from_doctree(doctree, writer_name="latex")

print(latex_doc)

