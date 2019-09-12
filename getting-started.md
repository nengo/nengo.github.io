---
layout: md_page
theme: theme-blue

title: Getting started
pageTitle: Get started with Nengo
footerClasses: gradient-bottom
---

Nengo runs on Windows, Mac OS X and Linux and requires Python.
To install Nengo, we recommend using `pip`.

```bash
pip install nengo nengo-gui
```

To make sure that the installation worked, run

```bash
nengo
```

and you should see a message about the Nengo server starting,
and a webpage will open with the Nengo GUI environment.

If you do not have `pip` installed, or if you run into any errors when
installing Nengo with `pip`, expand the sections below for more detailed instructions.

`pip` will do its best to install all of Nengo's requirements when it
installs Nengo. However, if anything goes wrong during this process, you
can install Nengo's requirements manually before doing `pip install nengo`
again.

{% include install-info.html %}

## Running models

Once you have Nengo installed, there are two ways to run Nengo models.
They can be run either with the Nengo GUI, or they can be run with a
Python interpreter.

### With Nengo GUI

The [Nengo GUI](https://github.com/nengo/nengo-gui) is a web-based
interface for designing and running Nengo models. To start the GUI, open
a terminal and run the `nengo` command.

To access the GUI, you use a web browser like Google Chrome or Firefox.
You should see a depiction of the network on the left panel, and a code
editor on the right panel.

![Nengo GUI]({{ site.baseurl }}/img/gui-03.gif)

The network illustration on the left panel is interactive. You can drag
to move the network objects, scroll with the mouse to zoom in and out,
and right-click on objects to display plots that will update in real
time as the model simulates (see the
[GUI documentation](https://github.com/nengo/nengo-gui#basic-usage)
for more details).

The code editor on the right panel shows the Python code defining the
Nengo model. While you can write any Python code in this editor, we add
a few additional constraints to ensure the GUI runs smoothly:

- Your top-level network must be called `model`.
- You cannot construct a `Simulator` object, as the GUI makes its own
  `Simulator` under the hood.
- You cannot show plots created with Matplotlib, as the GUI has its
  own set of visualizations.

To access a series of tutorials that introduce you to the GUI and to the
basics of building models with Nengo, click on the folder icon at the
top-left of the GUI, select "built-in examples", and then "tutorial".

If you see a warning that says something like `Warning: Simulators
cannot be manually run inside nengo_gui`, then you are likely running a
model that is designed to run with a Python interpreter (see below for
details). If the model you are trying to run is a Nengo example, then
it's likely that a similar example exists within the built-in examples
accessible through the folder icon at the top-left of the GUI.

### With a Python interpreter

The [Nengo core](https://www.nengo.ai/nengo/) is written in
[Python](https://www.python.org/). In order to install Nengo, you likely
also installed a Python distribution, whether it be through a package
manager provided by your operating system, through
[Anaconda](https://www.continuum.io/downloads), or by some other means.
You can use Nengo through any Python interpreter, like any other Python
package.

All Python distributions come with an interpreter that you can usually
run through a terminal by typing in `python` and hitting enter. You
should see a prompt that looks like this:

```bash
$ python
Python 3.5.3 (default, Jan 19 2017, 14:11:04)
[GCC 6.3.0 20170118] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can then import `nengo` and start building models.

```python
>>> import nengo
>>> model = nengo.Network("My model")
```

Since Nengo is a normal Python package, it interacts well with other
[Scientific Python packages](https://www.scipy.org/),
including plotting libraries like [Matplotlib](https://matplotlib.org/).

The [Jupyter notebook](http://jupyter.org/) provides another way to run
Python scripts. We provide Nengo core examples as Jupyter notebooks
because you can see plots in the same interface as the code. Jupyter
notebooks are also text files, but have the extension `.ipynb`. These
are run through the Jupyter notebook. For example, after downloading
[single\_neuron.ipynb](https://github.com/nengo/nengo/blob/master/docs/examples/basic/single_neuron.ipynb),
you can start the notebook like this:

```bash
$ jupyter notebook
```

and then click on `single_neuron.ipynb` to run the example.

To access a series of tutorials that use Nengo with a Python
interpreter, [see the Nengo
documentation](https://www.nengo.ai/nengo/examples.html).

## Learning more

- [Documentation]({{ site.baseurl }}{% link documentation.html %})
- [Videos]({{ site.baseurl }}{% link videos.md %})
- [Publications]({{ site.baseurl }}{% link publications.md %})

## Reference

The following links are useful to refer to when building models.

- [Nengo core documentation](https://www.nengo.ai/nengo/)
- [Nengo modelling API](https://www.nengo.ai/nengo/frontend_api.html)
