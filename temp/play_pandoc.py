import pypandoc

rst_text = """

.. tip::
    import matplotlib.pyplot as plt
    plt.savefig("my_fug.pdf, format="pdf")

.. raw

.. figure:: my_fug.pdf

    This is an included figure caption


"""

output = pypandoc.convert(rst_text, 'latex', format='rst')
output = pypandoc.convert(output, 'rst', format='latex')

print(output)