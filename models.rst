************
Nengo models
************

Computational models are a vital part of research
in an increasing number of scientific domains.
One difficulty with this is that computational models
are generally too complex to be fully described
in a traditional academic publication,
making it hard for other researchers
to replicate and build upon existing results.
This is especially true
for complex neural and cognitive models,
where models can involve simulations
of millions of interacting neurons
or other complex cognitive structures.

To address this concern,
and to provide additional examples for how Nengo
has been employed in a research context,
we have created this Nengo model repository.
The goal is to provide enough information here
that a researcher can run the models
detailed in a particular publication or project,
as well as gather and analyze the resulting data.
We also want to encourage feedback
from individuals running each others' models
and to post re-implementations of each others' models.

If you are looking for simple example models for Nengo,
see the `Nengo core examples
<https://www.nengo.ai/nengo/examples.html>`_.

Model repository
================

.. raw:: html

   <script src="https://cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>
   <script src="_static/models.js"></script>
   <div class="model-controls">
     <div id="sort-dropdown" class="dropdown">
       <button class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">
         Sort by <span class="caret"></span>
       </button>
       <ul class="dropdown-menu">
         <li><a href="#" id="sort-date-asc">Date, oldest to newest</a></li>
         <li><a href="#" id="sort-date-desc">Date, newest to oldest</a></li>
         <li><a href="#" id="sort-authors">First author</a></li>
         <li><a href="#" id="sort-title">Title</a></li>
       </ul>
     </div>
     <div id="filter-dropdown" class="dropdown">
       <button class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">
         Keywords <span class="caret"></span>
       </button>
       <ul class="dropdown-menu">
         <li>
           <a href="#" id="clear-keywords">
             <span class="glyphicon glyphicon-remove-circle"></span>
             Clear
           </a>
         </li>
       </ul>
     </div>
     <div class="pagination-container">
       <ul class="pagination"></ul>
     </div>
     <input id="model-search" class="form-control search" type="text" placeholder="Search models" />
   </div>

.. model:: Bandit task
   :code: https://github.com/tbekolay/bandit-task
   :month: January
   :year: 2012
   :authors: Trevor Bekolay & Terrence C. Stewart
   :keywords: animal model,
              basal ganglia,
              context,
              learning,
              reinforcement learning
   :pub: Learning to select actions with spiking neurons in the basal ganglia
   :pub-link: http://compneuro.uwaterloo.ca/publications/stewart2012a.html
   :requires: Nengo 1.4, Matplotlib

   A set of bandit task models that show how a simulated rat
   responds in a number of different situations.
   Included are Nengo 1.4 scripts for
   a simple 3-arm bandit task,
   a 3-arm bandit task in which
   the environment changes in each block of trials,
   and two scripts in which the environment
   switches faster so that the rat
   doesn't forget about environments
   encountered early in the set of trials.
   Data, plots, and Matplotlib scripts
   to generate the plots are also included.

.. model:: Neural representations of compositional structures
   :code: https://github.com/ctn-archive/stewart-connsci2011
   :month: May
   :year: 2011
   :authors: Terrence C. Stewart, Trevor Bekolay, & Chris Eliasmith
   :keywords: neural representation, SPA
   :pub: Neural representations of compositional structures: representing and manipulating vector spaces with spiking neurons
   :pub-link: http://www.tandfonline.com/doi/abs/10.1080/09540091.2011.571761
   :requires: Matplotlib, ccmsuite

   This is a series of examples of how to
   represent and manipulate high-dimensional vectors
   using spiking neurons.

.. model:: 3-link arm models
   :code: https://github.com/ctn-archive/dewolf-simulink-arms
   :month: August
   :year: 2011
   :authors: Travis DeWolf
   :keywords: arm model, motor control
   :requires: Matlab

   Three-link arms created with MapleSim 5 and exported to Simulink.
   Includes a simple three link arm, an arm with 6 muscles,
   and an arm with 9 muscles.

.. model:: Somatosensory working memory
   :code: https://github.com/ctn-archive/singh-jneurosci2006
   :month: April
   :year: 2006
   :authors: Ray Singh & Chris Eliasmith
   :keywords: somatosensory,
              working memory
   :pub: Higher-dimensional neurons explain the tuning and dynamics of working memory cells
   :pub-link: http://compneuro.uwaterloo.ca/files/publications/singh.2006.pdf
   :requires: Nengo 1.4

   This model is based on that published in
   Singh, R., Eliasmith, C. (2006).
   Higher-dimensional neurons explain the tuning and dynamics
   of working memory cells. Journal of Neuroscience. 26, 3667-3678.
   It is not the exact published model
   (contact the authors for the original matlab code),
   but it functions the same way.

.. model:: Spatiotemporal processing and coincidence detection
   :code: https://github.com/ctn-archive/joshi-liu-2011
   :month: July
   :year: 2011
   :authors: Siddharth Joshi & Shih-Chii Liu
   :keywords: artificial retina,
              audition,
              vision
   :requires: artificial retina, Nengo 1.4, Matlab

   The aim of this project was to connect a retina and cochlea to
   Nengo and create a co-incidence detector. We get information from
   jAER using UDP packets, and we can feed this into the coincidence
   detector we've created in Nengo. The detector will light up if
   orientations from the retina and 48 channels of the cochlea are all
   active. Results A coincidence detector was created the layout of
   this is shown below, as can be seen it's a tree like structure
   where a thresholding unit is created and then cascaded with
   multiplier units. Code to help interface the retina to other
   networks, with a small spatiotemporal filtering example is
   here. This is used by the sparse coding model in this archive.

.. model:: Working memory for multidimensional functions
   :code: https://github.com/ctn-archive/corneil-gevaert-2009
   :month: April
   :year: 2009
   :authors: Dane Corneil & Tim Gevaert
   :keywords: attractor network,
              function representation,
              working memory
   :requires: Nengo 1.4, Matlab

   This project is an extension of the dynamic working memory example
   presented in section 8.3 of Neural Engineering (Eliasmith and
   Anderson, 2003), much of the system description overlaps. The
   subpopulation under consideration in that case was the Lateral
   Intraparietal Area (LIP) of the neocortex of macaque monkeys. This
   population exhibits the behaviour of storing memories of salient
   stimuli, and has been studied extensively by researchers. The
   results of these studies indicate that multiple bumps of varying
   heights can be encoded by the LIP to represent multiple stimuli in
   the spatial field (represented by ``v``), as well as a non-spatial
   characteristic of each stimulus ``f(v)``. Research by Colby and
   Goldberg suggests that ``f(v)`` represents the attentional
   resources given to the stimuli, while research by Andersen et
   al. suggests that it represents intention to move to the object.

.. model:: Magic squares
   :code: https://github.com/ctn-archive/stefanini-2011
   :month: July
   :year: 2011
   :authors: Fabio Stefanini
   :keywords: game
   :requires: Nengo 1.4

   One of the biggest challenges of the neuromorphic engineering
   community is to be able to build disruptive systems that can
   efficiently perform complex tasks. Even though many tasks have been
   tackled using traditional approaches based on digital electronics,
   there is now the chance to achieve better results with less power
   consumption and more robustness to noise of natural
   environments. The Nengo software constitutes a powerful to explore
   the computational capabilities of neural systems to perform complex
   cognitive tasks, such as solving puzzles. In this work we chose the
   Magic Square and Sudoku problems to explore the possibilities of
   neural architectures using the NEF approach.

.. model:: Lamprey locomotion and tuning
   :code: https://github.com/ctn-archive/kleinhans-2011
   :month: July
   :year: 2011
   :authors: Ashley Kleinhans, Terrence C. Stewart
   :keywords: animal model,
              attractor network,
              locomotion
   :requires: Nengo 1.4

   Our goal was to use Nengo to simulate previously recorded (A. Cohen
   et al. '82) motor sensory data of the lamprey and to see if the
   simulation reacted, or could react, in the same way as the in vivo
   recordings (A. McClellan and A. Hagevik '97; Vogelstein et al.)
   when turning motion was stimulated.

.. model:: Sparse coding in real-time
   :code: https://github.com/ctn-archive/shapero-joshi-2011
   :month: July
   :year: 2011
   :authors: Sam Shapero, Siddharth Joshi
   :keywords: artificial retina,
              sparse coding,
              vision
   :requires: silicon retina, Nengo 1.4

   The spike based visual saliency project takes spike events from the
   Silicon Retina and ports them into the Neural Engineering Framework
   (NEF) in order to identify the visually salient portions of the
   video seen by the retina. Sparse coding and saliency computations
   are achieved in NEF with several layers of spiking neurons with
   strong lateral inhibitions. Five network files are included in this
   project. This is related to the spatiotemporal processing project
   also in this model archive.

.. model:: Reliable PSCs without observable downstream effects
   :code: https://github.com/ctn-archive/tripp-ccortex2007
   :month: August
   :year: 2007
   :authors: Bryan Tripp & Chris Eliasmith
   :keywords: neural representation,
              spike timing
   :pub: Neural populations can induce reliable postsynaptic currents
         without observable spike rate changes or precise spike timing
   :pub-link: https://academic.oup.com/cercor/article/17/8/1830/316338
   :requires: Matlab

   Matlab code related to Tripp BP & Eliasmith C, 2006, Neural
   populations can induce reliable post-synaptic currents without
   observable spike rate changes or precise spike timing.

.. model:: Normalization for probabilistic inference with neurons
   :code: https://github.com/ctn-archive/eliasmith-biocyber2011
   :month: May
   :year: 2011
   :authors: Chris Eliasmith & James Martens
   :keywords: statistical inference,
              normalization,
              probability theory
   :pub: Normalization for probabilistic inference with neurons
   :pub-link: http://www.springerlink.com/content/j7117u2675r27jv0/
   :requires: Matlab, Nengo 1.4

   Recently, there have been a number of proposals regarding how
   biologically plausible neural networks might perform probabilistic
   inference (Rao, 2004; Eliasmith and Anderson, 2003; Ma et al.,
   2006; Sahani and Dayan, 2003). To be able to repeatedly perform
   such inference, it is essential that the represented distributions
   be appropriately normalized. Past approaches have considered
   normalization mechanisms independently of inference, often leaving
   them unexplored, or appealing to a notion of divisive normalization
   that requires pooling across many neurons. Here we demonstrate how
   normalization and inference can be combined into an appropriate
   connection matrix, eliminating the need for pooling or a
   division-like operation. We algebraically demonstrate that such a
   solution is available regardless of the inference being
   performed. We show that such a solution is relevant to neural
   computation by implementing it in a recurrent spiking neural
   network.

.. model:: Population models of temporal differentiation
   :code: https://github.com/ctn-archive/tripp-ncomp2010
   :month: February
   :year: 2010
   :authors: Bryan Tripp & Chris Eliasmith
   :keywords: differentiation,
              neural coding,
              neural dynamics
   :pub: Population models of temporal differentiation
   :pub-link: https://www.mitpressjournals.org/doi/abs/10.1162/neco.2009.02-09-970
   :requires: Nengo 1.4

   This package contains the simulation software for Tripp &
   Eliasmith, Population models of temporal differentiation, Neural
   Computation. The enclosed code consists of Java classes, which
   contain the models, and Python scripts, which automate loading and
   simulation of the models.

.. model:: Fine-tuning and the stability of recurrent neural networks
   :code: https://github.com/ctn-archive/macneil-plos2011
   :month: September
   :year: 2011
   :authors: David MacNeil & Chris Eliasmith
   :keywords: attractor network,
              learning,
              neural dynamics,
              neural integrator
   :pub: Fine-tuning and the stability of recurrent neural networks
   :pub-link: http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0022885
   :requires: Matlab

   A central criticism of standard theoretical approaches to
   constructing stable, recurrent model networks is that the synaptic
   connection weights need to be finely-tuned. This criticism is
   severe because proposed rules for learning these weights have been
   shown to have various limitations to their biological
   plausibility. Hence it is unlikely that such rules are used to
   continuously fine-tune the network in vivo. We describe a learning
   rule that is able to tune synaptic weights in a biologically
   plausible manner. We demonstrate and test this rule in the context
   of the oculomotor integrator, showing that only known neural
   signals are needed to tune the weights. We demonstrate that the
   rule appropriately accounts for a wide variety of experimental
   results, and is robust under several kinds of
   perturbation. Furthermore, we show that the rule is able to achieve
   stability as good as or better than that provided by the linearly
   optimal weights often used in recurrent models of the
   integrator. Finally, we discuss how this rule can be generalized to
   tune a wide variety of recurrent attractor networks, such as those
   found in head direction and path integration systems, suggesting
   that it may be used to tune a wide variety of stable neural
   systems.

.. model:: Tic tac toe
   :code: https://github.com/ctn-archive/shekhar-2011
   :month: July
   :year: 2011
   :authors: Ravi Shekhar
   :keywords: game
   :requires: Nengo 1.4

   The motivation for this project came from last year when we tried
   to build a spiking neural network that can play hearts (card
   game). Then we did not have a framework like Nengo to work on so we
   had to build everything from scratch. This year since we had the
   Nengo framework, I wanted to try the project again. I talked to
   Chris about building a game and especially a Hearts game, he
   encouraged me saying it can be done but it will be difficult to
   build. He suggested we should start with something smaller maybe
   like comparing cards or something. We settled on Tic Tac Toe. It is
   a small enough game with few basic rules. This seemed like a
   problem that can be tackled during the Telluride workshop.

.. model:: Neural path integrator
   :code: https://github.com/ctn-archive/conklin-compneuro2005
   :month: March
   :year: 2005
   :authors: Yan Wu, John Conklin & Chris Eliasmith
   :keywords: attractor network,
              hippocampus,
              locomotion,
              neural control,
              subiculum
   :pub: A controlled attractor network model of path integration in the rat
   :pub-link: http://www.springerlink.com/content/q01qun6kk45x28m3/
   :requires: Matlab, Nengo 1.4

   Cells in several areas of the hippocampal formation show place
   specific firing patterns, and are thought to form a distributed
   representation of an animal’s current location in an
   environment. Experimental results suggest that this representation
   is continually updated even in complete darkness, indicating the
   presence of a path integration mechanism in the rat. Adopting the
   Neural Engineering Framework (NEF) presented by Eliasmith and
   Anderson (2003) we derive a novel attractor network model of path
   integration, using heterogeneous spiking neurons. The network we
   derive incorporates representation and updating of position into a
   single layer of neurons, eliminating the need for a large external
   control population, and without making use of multiplicative
   synapses. An efﬁcient and biologically plausible control mechanism
   results directly from applying the principles of the NEF. We
   simulate the network for a variety of inputs, analyze its
   performance, and give three testable predictions of our model.

.. model:: Wason selection task
   :code: https://github.com/ctn-archive/eliasmith-cogsci2005
   :year: 2005
   :authors: Chris Eliasmith
   :keywords: context,
              learning,
              wason
   :pub: Cognition with neurons: a large-scale,
         biologically realistic model of the Wason task
   :pub-link: http://compneuro.uwaterloo.ca/files/publications/eliasmith.2005.pdf
   :requires: Nengo 1.4

   The Wason selection task. Two experimental conditions show that the
   model can learn to process rules differently depending on context,
   and that it can generalize to new rules within a context.

.. model:: Cognitive control
   :code: https://github.com/ctn-archive/stewart-cogsci2010
   :month: January
   :year: 2010
   :authors: Terrence C. Stewart
   :keywords: basal ganglia,
              neural control
   :pub: Symbolic reasoning in spiking neurons:
         a model of the cortex/basal ganglia/thalamus Loop
   :pub-link: http://compneuro.uwaterloo.ca/files/publications/stewart.2010a.pdf
   :requires: Nengo 1.4

   Three examples of sequences of actions controlled by the basal
   ganglia. First, the model follows a fixed sequence A->B->C->D,
   etc. Second, the model has a fixed routing of information from
   visual to working memory. This interrupts the sequencing ability,
   trapping it at the first value. Third, we use the thalamus to gate
   the flow of information. This allows the sequence to be started
   based on a visual cue, and then have that visual cue be ignored
   while going through the sequence.

.. model:: RBM deep belief network for visual digit recognition
   :code: https://github.com/ctn-archive/tang-2012
   :month: June
   :year: 2012
   :authors: Yichuan Tang, Terrence C. Stewart & Chris Eliasmith
   :keywords: machine learning, vision
   :requires: Nengo 1.4

   A spiking neuron model for digit recognition, created by training
   an RBM Deep Belief Network on the MNIST database, then converting
   the resulting model to spiking neurons via Nengo.

.. model:: Spaun (1.0)
   :code: https://github.com/ctn-archive/spaun1.0
   :month: November
   :year: 2012
   :authors: Chris Eliasmith,
             Terrence C. Stewart,
             Xuan Choo,
             Trevor Bekolay,
             Travis DeWolf,
             Yichuan Tang &
             Daniel Rasmussen
   :keywords: arm model,
              basal ganglia,
              induction,
              inference,
              learning,
              neural coding,
              reinforcement learning,
              vision
   :pub: A large-scale model of the functioning brain
   :pub-link: http://compneuro.uwaterloo.ca/publications/eliasmith2012.html
   :requires: Nengo 1.4

   Spaun is a biologically realistic model of cognition that is not
   only able to perform multiple (at least 10) cognitive, perceptual,
   and motor tasks, but also utilizes the same model parameters across
   all tasks. Spaun is able to perform tasks that encompass strictly
   visual tasks (e.g. recognition of handwritten digits), memory tasks
   (e.g. forward and backward recall of a list), simple cognitive
   tasks (e.g. counting), and complex fluid intelligence tasks
   (e.g. solving the Raven's Progressive Matrices).

.. model:: Sequence rule generation in Raven's Progressive Matrices
   :code: https://github.com/ctn-archive/rasmussen-cogsci2011
   :month: January
   :year: 2011
   :authors: Daniel Rasmussen & Chris Eliasmith
   :keywords: induction, SPA
   :pub: A neural model of rule generation in inductive reasoning
   :pub-link: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1756-8765.2010.01127.x
   :requires: Nengo 1.4

   This is one aspect of a model designed to generate the rules needed
   to solve a popular test of intelligence, Raven's Progressive
   Matrices. This component generates a particular type of rule, which
   we call "sequences". These are patterns defined by an iterative
   transformation (e.g., the sequence 9, 10, 11 is defined by the
   iterative transformation +1). Given Raven's matrices represented in
   a mathematical, vector-based form, this component can then generate
   the sequence transformations that define those matrices and use
   them to find an answer to the problem.

.. model:: Hemineglect
   :code: https://github.com/ctn-archive/leigh-ebr2015
   :month: March
   :year: 2015
   :authors: Steven Leigh,
             James Danckert &
             Chris Eliasmith
   :keywords: learning, PPC
   :pub: Modelling the differential effects of prisms
         on perception and action in neglect
   :pub-link: https://link.springer.com/article/10.1007/s00221-014-4150-3
   :requires: Matlab, Nengo 1.4

   Damage to the right parietal cortex often leads to a syndrome known
   as unilateral neglect in which the patient fails to attend or
   respond to stimuli in left space. Recent work attempting to
   rehabilitate the disorder has made use of rightward-shifting prisms
   that displace visual input further rightward. After a brief period
   of adaptation to prisms many of the symptoms of neglect show
   improvements that can last for hours or longer depending on the
   adaptation procedure. Recent work has shown, however, that
   differential effects of prisms can be observed on actions (which
   are typically improved) and perceptual biases (which often remain
   unchanged). Here we present a computational model capable of
   explaining some basic symptoms of neglect (line bisection
   behaviour), the effects of prism adaptation in both healthy
   controls and neglect patients and the observed dissociation between
   action and perception following prisms. The results of our
   simulations support recent contentions that prisms primarily
   influence behaviours normally thought to be controlled by the
   dorsal stream.

Add your model
==============

If you have created a Nengo model,
we want to add it to this list!
If you are not comfortable editing
a reStructuredText file,
please `make a new issue on Github
<https://github.com/nengo/nengo.github.io/issues/new>`_
telling us about your model.
We may ask you a few questions
to have a complete record of your model.

If you want to add it yourself,
`edit the models.rst file
<https://github.com/nengo/nengo.github.io/edit/src/models.rst>`_
and add the details for your project.
Project details are specified as follows.

.. code-block:: rst

   .. model:: Title of the model
      :code: Link to model code
      :month: Month model was created or published (optional)
      :year: Year model was created or published
      :authors: Who created the model
      :keywords: Comma-separated list of keywords;
                 use existing keywords if possible
      :pub: Title of publication about the model (optional)
      :pub-link: Link to the model publication (optional)
      :requires: Comma-separated list of model requirements

      Long-form description of the model.
      This description is parsed as reStructuredText,
      so you can *italicize text*, **bold it**, or
      `add links <https://www.nengo.ai/>`_.

See the other models in ``models.rst`` for examples.
