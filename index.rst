**************************
The Nengo neural simulator
**************************

Nengo is a graphical and scripting based software package
for simulating large-scale neural systems.
The book *How to build a brain*,
which includes Nengo tutorials,
is now available.
This website also has additional information on the book.

To use Nengo,
you define groups of neurons in terms of what they represent,
and then form connections between neural groups
in terms of what computation should be performed on those representations.
Nengo then uses the Neural Engineering Framework (NEF)
to solve for the appropriate synaptic connection weights
to achieve this desired computation.
Nengo also supports various kinds of learning.
Nengo helps make detailed spiking neuron models
that implement complex high-level cognitive algorithms.

Among other things,
Nengo has been used to implement motor control,
visual attention, serial recall, action selection,
working memory, attractor networks, inductive reasoning,
path integration, and planning with problem solving
(see the model archives and publications
for details).

.. topic:: Spaun

   We've used Nengo to build Spaun,
   the world's largest functional brain model,
   which is described in
   `this Science paper <http://nengo.ca/publications/spaunsciencepaper>`_.

   .. raw:: html

      <iframe width="100%" height="400" src="https://www.youtube.com/embed/P_WRCyNQ9KY" frameborder="0" allowfullscreen></iframe>

.. topic:: Nengo summer school

   Showcasing various projects from Nengo summer school (a.k.a. Brain Camp).

   .. raw:: html

      <iframe width="100%" height="400" src="https://www.youtube.com/embed/K-o-MJJY7ss?list=PLYLu6sY3jnoVgeFX4GMFaECP_y1aAKxHE" frameborder="0" allowfullscreen></iframe>

.. toctree::
   :maxdepth: 2

   download
   projects
   build-a-brain/index
   Forum <https://forum.nengo.ai>
   users
   developers
   people
   README

.. todo:: Add overview to toctree once it's cleaned up.
