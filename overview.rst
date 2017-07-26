********
Overview
********

.. todo:: Screenshot of Jupyter notebook model?

.. todo:: Screenshot of Nengo GUI?

In Nengo, you build models by creating **ensembles** of neurons:
groups of neurons that **represent** a value.
As the pattern of activity of these neurons changes,
the value being represented changes,
as can be viewed in the Nengo GUI.
The value being represented can be a single number,
a vector (multiple numbers), or even a function.
This approach to representation
is highly distributed and robust to noise.

.. todo:: Image from 2D representation example

   `(Demo code with description)
   <https://www.nengo.ai/nengo/examples/2d_representation.html>`__
   100 leaky-integrate-and-fire neurons
   representing two numbers (a vector).
   Grey squares show membrane voltage of each neuron,
   with a yellow square indicating a spike.
   Graph shows the two values
   representing the value as it changes over time
   due to changing input.

To implement an algorithm,
you connect these ensembles of neurons.
For each **connection**,
you define a **computation** that should be performed.
Unlike traditional neural modelling,
Nengo does not require the use of a learning rule
to find connection weights between neurons.
Instead, Nengo uses the
`Neural Engineering Framework (NEF)
<http://compneuro.uwaterloo.ca/research/nef.html>`_
to find the connection weights
that will approximate that computation.

.. todo:: Image from multiplication example

   `(Demo code with description)
   <https://www.nengo.ai/nengo/examples/multiplication.html>`__
   500 leaky-integrate-and-fire neurons
   that compute the product of two numbers
   (:math:`y = x_1 \cdot x_2`).

This approach extends to **recurrent** connections as well.
This allows for the implementation of
any **dynamical system**, such as **memory**,
since networks can have dynamics
that maintain a representation in the absence of input.

.. todo:: Image from integrator example

   `(Demo code with description)
   <https://www.nengo.ai/nengo/examples/integrator.html>`__
   100 leaky-integrate-and-fire neurons that store an input over time.
   When the input is positive, the stored value increases.
   When the input is negative, it decreases.
   When the input is zero, it maintains its value.
   Mathematically, this operation is integration.

By adapting the formalisms of **control theory**,
complex dynamical systems can be implemented,
including **oscillators**, chaotic attractors, and Kalman filters.

.. todo::

   `(Demo code with description)
   <https://www.nengo.ai/nengo/examples/oscillator.html>`__
   200 leaky-integrate-and-fire neurons that form an oscillator.
   The represented value is a 2-dimensional vector (x,y).
   The recurrent connections are set
   to rotate the vector at 10 radians per second.

These basic tools allow for the creation of a vast variety of models,
including the world's largest functional brain model, Spaun,
and many other models:

.. todo:: Link Spaun (http://nengo.ca/build-a-brain/spaunvideos)

.. todo:: Link model archive
