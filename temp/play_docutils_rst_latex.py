from docutils.core import publish_string, publish_parts, publish_doctree, publish_from_doctree
from docutils import nodes


rst_text = """

.. code::
    :class: plot
    :name: my_fug

    import matplotlib.pyplot as plt
    plt.plot([0,1], [0,1])
    plt.savefig("my_fug.pdf", format="pdf")

.. figure:: my_fug.pdf
    :name: fig:my_fug

    This is an included figure caption

     
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

    if isinstance(obj, nodes.literal_block):
        for child in obj.children:
            if isinstance(child, nodes.Text):
                exec(child)

print_children(doctree)

#latex_doc = publish_from_doctree(doctree, writer_name="latex")

#print(latex_doc)

