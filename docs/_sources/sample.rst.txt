sampleを記述
==================================

Code
----------------

`` .. code-block:: `` を用いることでコードをハイライトすることができます。

.. code-block:: go
    :caption: hello.go

    package main

    import "fmt"

    func main() {
        fmt.Println("Hello, world!")
    }

.. code-block:: c++
    :caption: hello.cc

    int main() {
        std::cout << std::endl;
        return 0;
    }

PlantML
----------------
   
.. uml::
    :align: center
       
    A --> B: request
    return response
    
.. uml::
    :align: center
       
    Alice -> Bob: Hi!
    Alice <- Bob: How are you?
    
    
Math
----------------
.. math::
    \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}  
    
    {a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}
    
Jupyter
----------------
.. .. jupyter-execute::

..     import numpy as np
..     import plotly.express as px
    
..     x = np.linspace(0, 1, 100)
..     y = np.sin(x)

..     fig = px.line(x=x, y=y)
..     display(fig)
   
.. jupyter-execute::
  
   import numpy as np
   from matplotlib import pyplot
   %matplotlib inline
    
   x = np.linspace(1E-3, 2 * np.pi)
 
   pyplot.plot(x, np.sin(x) / x)
   pyplot.plot(x, np.cos(x))
   pyplot.grid()