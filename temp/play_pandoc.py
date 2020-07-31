import pypandoc

rst_text = """

.. code::
    import matplotlib.pyplot as plt
    plt.savefig("my_fug.pdf, format="pdf")

.. raw

.. figure:: my_fug.pdf
    :name: fig:my_fug

    This is an included figure caption


"""

output = pypandoc.convert(rst_text, 'latex', format='rst')
# output = pypandoc.convert(output, 'rst', format='latex')

print(output)