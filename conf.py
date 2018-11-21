#!/usr/bin/env python3

from datetime import datetime
import os
import sys

sys.path.extend(os.path.dirname(__file__))
extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "nengo_sphinx_theme",
    "custom",  # Loaded from the current directory
]

suppress_warnings = ['image.nonlocal_uri']
source_suffix = ".rst"
master_doc = "index"
exclude_patterns = [
    "_build", "Thumbs.db", ".DS_Store", "_records/*.rst",
]

project = "Nengo"
copyright = "2016-2018, Applied Brain Research"
author = "Applied Brain Research"
version = release = datetime.now().strftime("%Y-%m-%d")
language = None

todo_include_todos = False

intersphinx_mapping = {
    "nengo": ("https://www.nengo.ai/nengo/", None)
}

# HTML theming
pygments_style = "friendly"
templates_path = ["_templates"]
html_static_path = ["_static"]

html_title = "Nengo"
html_theme = "nengo_sphinx_theme"
html_sidebars = {
    "**": [],
    "contributing": ["sidebar.html"],
    "how-to": ["sidebar.html"],
    "conduct": ["sidebar.html"],
    "style": ["sidebar.html"],
    "governance": ["sidebar.html"],
    "reviewing": ["sidebar.html"],
    "releasing": ["sidebar.html"],
    "caa": ["sidebar.html"],
}
html_favicon = "_static/favicon.ico"

# Other builders
htmlhelp_basename = "Nengo"

latex_elements = {
    # "papersize": "letterpaper",
    # "pointsize": "11pt",
    # "preamble": "",
    # "figure_align": "htbp",
}

latex_documents = [
    (master_doc,  # source start file
     "nengo.tex",  # target name
     "Nengo Documentation",  # title
     "Applied Brain Research",  # author
     "manual"),  # documentclass
]

man_pages = [
    # (source start file, name, description, authors, manual section).
    (master_doc, "nengo", "Nengo Documentation", [author], 1)
]

texinfo_documents = [
    (master_doc,  # source start file
     "Nengo",  # target name
     "Nengo Documentation",  # title
     author,  # author
     "Nengo",  # dir menu entry
     "Large-scale brain modelling in Python",  # description
     "Miscellaneous"),  # category
]

# Redirects are in the form (src, dst) where
# - src is the relative path from the build output directory
# - dst is the arbitrary URL you want to redirect to
redirects = [
    ("developers.html", "https://www.nengo.ai/contributing.html"),
    ("users.html", "https://www.nengo.ai/quickstart.html"),
]


def add_redirects(project, prefix, pages):
    newproject = project.replace("_", "-")
    for page in pages:
        fullpage = "%s%s%s" % (prefix, "/" if prefix != "" else "", page)
        redirects.append((
            "%s/%s" % (project, fullpage),
            "https://www.nengo.ai/%s/%s" % (newproject, fullpage),
        ))


# enhancement_proposals redirects

add_redirects("enhancement_proposals", "", [
    "001-template.html",
    "004-rejected-template.html",
    "100-pynn-backend.html",
    "400-multidim-radius.html",
    "401-probe-outputs.html",
    "402-ndarray-representation.html",
    "403-variable-synapse-defaults.html",
    "404-java-backend.html",
    "index.html",
    "README.html",
])

# nengo_extras redirects

add_redirects("nengo_extras", "", [
    "deeplearning.html",
    "deeplearning-examples.html",
    "dists.html",
    "index.html",
    "learning_rules.html",
    "networks.html",
    "neurons.html",
    "processes.html",
    "vision.html",
    "vision-examples.html",
    "visualization.html",
    "visualization-examples.html",
])

# nengo_1.4 redirects

add_redirects("nengo_1.4", "", [
    "getting_started.html",
    "index.html",
    "nef_algorithm.html",
])
add_redirects("nengo_1.4", "advanced", [
    "dragndrop.html",
    "experiments.html",
    "gpu.html",
    "index.html",
    "ipython_notebook.html",
    "large_ensembles.html",
    "layout.html",
    "matlab.html",
])
add_redirects("nengo_1.4", "demos", [
    "2drepresentation.html",
    "addition.html",
    "armcontrol.html",
    "basalganglia.html",
    "combining.html",
    "communication.html",
    "controlledintegrator.html",
    "controlledintegrator2.html",
    "controlledoscillator.html",
    "convolve.html",
    "index.html",
    "integrator.html",
    "learn_communicate.html",
    "learn_product.html",
    "learn_square.html",
    "manyneurons.html",
    "multiplication.html",
    "oscillator.html",
    "question.html",
    "question_control.html",
    "question_memory.html",
    "singleneuron.html",
    "spa_sequence.html",
    "spa_sequencerouted.html",
    "squaring.html",
    "twoneurons.html",
    "vehicle.html",
])
add_redirects("nengo_1.4", "scripting", [
    "api.html",
    "basics.html",
    "ensembles.html",
    "index.html",
    "simplenodes.html",
    "speed.html",
    "tips.html",
    "weights.html",
])
add_redirects("nengo_1.4", "tutorials", [
    "1-representation.html",
    "2-linear-transformation.html",
    "3-nonlinear-transformation.html",
    "4-dynamics.html",
    "5-cognitive.html",
    "index.html",
])
add_redirects("nengo_1.4", "videos", [
    "1-construction.html",
    "2-workspace.html",
    "3-simulation.html",
    "4-moreplots.html",
    "5-scripting.html",
    "index.html",
])

add_redirects("nengo_1.4", "python-api", [
    "packages.html",
])
add_redirects("nengo_1.4", "python-api/nef", [
    "Network.html",
    "SimpleNode.html",
])

add_redirects("nengo_1.4", "simulator-api", [
    "packages.html"
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo", [
    "NengoException.html",
    "package-index.html",
    "TestUtil.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/dynamics", [
    "DynamicalSystem.html",
    "Integrator.html",
    "LinearSystem.html",
    "package-index.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/dynamics/impl", [
    "AbstractDynamicalSystem.html",
    "CanonicalModel.html",
    "CanonicalModelTest.html",
    "EulerIntegrator.html",
    "ImpulseIntegral.html",
    "ImpulseIntegralTest.html",
    "LTISystem.html",
    "package-index.html",
    "RK45Integrator.html",
    "RK45IntegratorTest-VanderPol.html",
    "RK45IntegratorTest.html",
    "SimpleLTISystem.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/util", [
    "ClassUtils.html",
    "DataUtils.html",
    "DataUtilsTest.html",
    "Environment.html",
    "IndexFinder.html",
    "Interpolator.html",
    "InterpolatorND.html",
    "Memory.html",
    "MU-MatrixExpander.html",
    "MU-VectorExpander.html",
    "MU.html",
    "package-index.html",
    "Probe.html",
    "ScriptGenException.html",
    "SpikePattern.html",
    "TaskSpawner.html",
    "ThreadTask.html",
    "TimeSeries.html",
    "TimeSeries1D.html",
    "VectorGenerator.html",
    "VisiblyMutable-Event.html",
    "VisiblyMutable-Listener.html",
    "VisiblyMutable-NameChangeEvent.html",
    "VisiblyMutable-NodeRemovedEvent.html",
    "VisiblyMutable.html",
    "VisiblyMutableUtils.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/util/impl", [
    "DFSIterator.html",
    "FixedVectorGenerator.html",
    "GPUThread.html",
    "LearningTask.html",
    "LinearInterpolatorND.html",
    "NEFGPUInterface.html",
    "NodeThread.html", "Rectifier.html",
    "NodeThreadPool.html",
    "package-index.html",
    "ProbeImpl.html",
    "ProbeTask.html",
    "RandomHypersphereVG.html",
    "RandomHypersphereVGTest.html",
    "RecorderImplTest.html",
    "ScriptGenerator.html",
    "SpikePatternImpl.html",
    "SpikePatternImplTest.html",
    "StatefulIndexFinder.html",
    "TimeSeries1DImpl.html",
    "TimeSeries1DImplTest.html",
    "TimeSeriesImpl.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/config/ui", [
    "AquaTreeUI.html",
    "ConfigExceptionHandler.html",
    "ConfigurationChangeListener-EditorProxy.html",
    "ConfigurationChangeListener.html",
    "ConfigurationTreeCellEditor.html",
    "ConfigurationTreeCellEditorTest.html",
    "ConfigurationTreeCellRenderer.html",
    "ConfigurationTreeModel-NullValue.html",
    "ConfigurationTreeModel-Value.html",
    "ConfigurationTreeModel.html",
    "ConfigurationTreeModelTest.html",
    "ConfigurationTreePopupListener.html",
    "MatrixEditor.html",
    "NewConfigurableDialog-ConstructionProperties.html",
    "NewConfigurableDialog.html",
    "NewConfigurableDialogTest.html",
    "package-index.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/config/impl", [
    "AbstractProperty.html",
    "ConfigurationImpl.html",
    "ListPropertyImpl.html",
    "ListPropertyImplTest.html",
    "NamedValuePropertyImpl.html",
    "NamedValuePropertyImplTest.html",
    "package-index.html",
    "SingleValuedPropertyImpl.html",
    "TemplateArrayProperty.html",
    "TemplateProperty.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/config", [
    "ClassRegistry.html",
    "Configurable.html",
    "Configuration.html",
    "ConfigurationHandler.html",
    "ConfigUtil-ConfigurationPane.html",
    "ConfigUtil.html",
    "ConfigUtilTest.html",
    "IconRegistry.html",
    "JavaSourceParser.html",
    "ListProperty.html",
    "MainHandler.html",
    "NamedValueProperty.html",
    "package-index.html",
    "Property.html",
    "SingleValuedProperty.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/config/handlers", [
    "BaseHandler.html",
    "BooleanHandler.html",
    "EnumHandler.html",
    "FloatHandler.html",
    "IntegerHandler.html",
    "LongHandler.html",
    "MatrixHandler.html",
    "MatrixHandlerBase.html",
    "package-index.html",
    "StringHandler.html",
    "UnitsHandler.html",
    "VectorHandler.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/io", [
    "DelimitedFileExporter.html",
    "DelimitedFileExporterTest.html",
    "FileManager.html",
    "MatlabExporter.html",
    "package-index.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/examples", [
    "IntegratorExample.html",
    "package-index.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/sim/impl", [
    "LocalSimulator.html",
    "package-index.html",
    "WriteToDiskSimulatorListener.html",
    "WriteToDiskSimulatorListenerTest.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/sim", [
    "package-index.html",
    "Simulator.html",
    "SimulatorEvent-Type.html",
    "SimulatorEvent.html",
    "SimulatorListener.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/plot/impl", [
    "DefaultPlotter.html",
    "package-index.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/plot", [
    "package-index.html",
    "Plotter.html",
    "PlotterFunctional.html",
    "Scope.html",
    "ScopeExample.html",
    "SolidColorIcon.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/math/impl", [
    "AbstractFunction.html",
    "CompositeApproximator.html",
    "CompositeApproximatorTest.html",
    "ConstantFunction.html",
    "ConstantFunctionTest.html",
    "Convolution.html",
    "ConvolutionTest.html",
    "DefaultFunctionInterpreter.html",
    "DefaultFunctionInterpreterTest.html",
    "ExponentialPDF.html",
    "ExponentialPDFTest.html",
    "FixedSignalFunction.html",
    "FixedSignalFunctionTest.html",
    "FourierFunction.html",
    "FourierFunctionTest.html",
    "FunctionBasisImpl.html",
    "FunctionBasisImplTest.html",
    "GaussianPDF.html",
    "GaussianPDFTest.html",
    "GradientDescentApproximator-CoefficientsSameSign.html",
    "GradientDescentApproximator-Constraints.html",
    "GradientDescentApproximator-Factory.html",
    "GradientDescentApproximator.html",
    "GradientDescentApproximatorTest.html",
    "IdentityFunction.html",
    "IdentityFunctionTest.html",
    "IndependentDimensionApproximator-EncoderFactory.html",
    "IndependentDimensionApproximator-EvalPointFactory.html",
    "IndependentDimensionApproximator-Factory.html",
    "IndependentDimensionApproximator.html",
    "IndependentDimensionApproximatorTest.html",
    "IndicatorPDF.html",
    "IndicatorPDFTest.html",
    "InterpolatedFunction.html",
    "LinearCurveFitter.html",
    "LinearCurveFitterTest.html",
    "LinearFunction.html",
    "LinearFunctionTest.html",
    "MultiLevelKLNetworkPartitioner.html",
    "NewtonRootFinder.html",
    "NewtonRootFinderTest.html",
    "NumericallDifferentiableFunctionTest.html",
    "NumericallyDifferentiableFunction-NumericalDerivative.html",
    "NumericallyDifferentiableFunction.html",
    "NumericallyDifferentiableFunctionTest.html",
    "package-index.html",
    "PDFFunction.html",
    "PDFFunctionTest.html",
    "PiecewiseConstantFunction.html",
    "PiecewiseConstantFunctionTest.html",
    "PoissonPDF.html",
    "PoissonPDFTest.html",
    "Polynomial.html",
    "PolynomialCurveFitter.html",
    "PolynomialCurveFitterTest.html",
    "PolynomialTest.html",
    "PostfixFunction.html",
    "PostfixFunctionTest.html",
    "SigmoidFunction.html",
    "SigmoidFunctionTest.html",
    "SimpleFunctions-Acos.html",
    "SimpleFunctions-Asin.html",
    "SimpleFunctions-Atan.html",
    "SimpleFunctions-Cos.html",
    "SimpleFunctions-Exp.html",
    "SimpleFunctions-Fold.html",
    "SimpleFunctions-InverseNormal.html",
    "SimpleFunctions-Ln.html",
    "SimpleFunctions-Log10.html",
    "SimpleFunctions-Log2.html",
    "SimpleFunctions-Max.html",
    "SimpleFunctions-Min.html",
    "SimpleFunctions-Normal.html",
    "SimpleFunctions-Pow.html",
    "SimpleFunctions-Sin.html",
    "SimpleFunctions-Sqrt.html",
    "SimpleFunctions-Tan.html",
    "SimpleFunctions.html",
    "SimpleFunctionsTest.html",
    "SineFunction.html",
    "SineFunctionTest.html",
    "TimeSeriesFunction.html",
    "TimeSeriesFunctionTest.html",
    "WeightedCostApproximator-Factory.html",
    "WeightedCostApproximator.html",
    "WeightedCostApproximatorTest.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/math", [
    "ApproximatorFactory.html",
    "CurveFitter.html",
    "DifferentiableFunction.html",
    "Function.html",
    "FunctionBasis.html",
    "FunctionInterpreter.html",
    "LinearApproximator.html",
    "NetworkPartitioner.html",
    "package-index.html",
    "PDF.html",
    "PDFTools.html",
    "RootFinder.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/model/nef/impl", [
    "AdditiveGaussianExpressModel.html",
    "BiasOrigin.html",
    "BiasTermination.html",
    "DecodableEnsembleImpl.html",
    "DecodedOrigin.html",
    "DecodedOriginTest.html",
    "DecodedTermination.html",
    "DefaultExpressModel.html",
    "NEFEnsembleFactoryImpl.html",
    "NEFEnsembleImpl.html",
    "NEFEnsembleImplTest.html",
    "NEFUtil.html",
    "NEFUtilTest.html",
    "package-index.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/model/nef", [
    "DecodableEnsemble.html",
    "ExpressModel.html",
    "NEFEnsemble.html",
    "NEFEnsembleFactory.html",
    "NEFNode.html",
    "package-index.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/model/impl", [
    "AbstractEnsemble.html",
    "AbstractEnsembleTest.html",
    "AbstractNode.html",
    "BasicOrigin.html",
    "BasicTermination.html",
    "ConfigurationImplTest.html",
    "DelayedLinearExponentialTermination.html",
    "EnsembleImpl.html",
    "EnsembleImplTest-MockExpandableNode.html",
    "EnsembleImplTest.html",
    "EnsembleOrigin.html",
    "EnsembleTermination.html",
    "EnsembleTerminationTest.html",
    "FunctionInput.html",
    "FunctionInputTest.html",
    "LinearExponentialTermination.html",
    "LinearExponentialTerminationTest.html",
    "MockConfigurable-MockChildConfigurable.html",
    "MockConfigurable-MockLittleConfigurable.html",
    "MockConfigurable.html",
    "MockNode.html",
    "NetworkArrayImpl-ArrayOrigin.html",
    "NetworkArrayImpl-ArraySummedOrigin.html",
    "NetworkArrayImpl-WeightFunc.html",
    "NetworkArrayImpl.html",
    "NetworkImpl-OriginWrapper.html",
    "NetworkImpl-TerminationWrapper.html",
    "NetworkImpl.html",
    "NetworkImplTest.html",
    "NodeFactory.html",
    "NoiseFactory-NoiseImplFunction.html",
    "NoiseFactory-NoiseImplNull.html",
    "NoiseFactory-NoiseImplPDF.html",
    "NoiseFactory.html",
    "NoiseFactoryTest.html",
    "package-index.html",
    "PassthroughNode-PassthroughTermination.html",
    "PassthroughNode.html",
    "PassthroughNodeTest.html",
    "PreciseSpikeOutputImpl.html",
    "ProbeableOrigin.html",
    "ProbeableOriginTest.html",
    "ProjectionImpl.html",
    "ProjectionImplTest-MockOrigin.html",
    "ProjectionImplTest-MockTermination.html",
    "ProjectionImplTest.html",
    "RealOutputImpl.html",
    "RealOutputImplTest.html",
    "SocketUDPNode.html",
    "SpikeOutputImpl.html",
    "SpikeOutputImplTest.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/model", [
    "Ensemble.html",
    "ExpandableNode.html",
    "InstantaneousOutput.html",
    "Network.html",
    "Node.html",
    "Noise-Noisy.html",
    "Noise.html",
    "Origin.html",
    "package-index.html",
    "PlasticNodeTermination.html",
    "PreciseSpikeOutput.html",
    "Probeable.html",
    "Projection.html",
    "RealOutput.html",
    "Resettable.html",
    "SimulationException.html",
    "SimulationMode-ModeConfigurable.html",
    "SimulationMode.html",
    "SpikeOutput.html",
    "StepListener.html",
    "StructuralException.html",
    "Termination.html",
    "Units.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/model/plasticity/impl", [
    "BCMTermination.html",
    "hPESTermination.html",
    "ModulatedPlasticEnsembleTermination.html",
    "package-index.html",
    "PESTermination.html",
    "PlasticEnsembleImpl.html",
    "PlasticEnsembleTermination.html",
    "PlasticEnsembleTerminationTest.html",
    "PreLearnTermination.html",
    "STDPTermination.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/model/plasticity", [
    "package-index.html",
    "PlasticEnsemble.html",
    "ShortTermPlastic.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/model/muscle", [
    "GolgiTendonOrgan.html",
    "LinkSegmentModel.html",
    "MuscleSpindle.html",
    "package-index.html",
    "SkeletalMuscle.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/model/muscle/impl", [
    "CriticallyDampedMuscle.html",
    "HillMuscle-Dynamics.html",
    "HillMuscle.html",
    "LinkSegmentModelImpl.html",
    "LinkSegmentModelImplTest.html",
    "package-index.html",
    "SkeletalMuscleImpl.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/model/neuron", [
    "ExpandableSynapticIntegrator.html",
    "Neuron.html",
    "package-index.html",
    "SpikeGenerator.html",
    "SynapticIntegrator.html",
])
add_redirects("nengo_1.4", "simulator-api/ca/nengo/model/neuron/impl", [
    "ALIFNeuronFactory.html",
    "ALIFSpikeGenerator-Factory.html",
    "ALIFSpikeGenerator.html",
    "ALIFSpikeGeneratorTest.html",
    "DynamicalSystemSpikeGenerator.html",
    "ExpandableSpikingNeuron.html",
    "GruberNeuronFactory-GruberNeuron.html",
    "GruberNeuronFactory.html",
    "GruberSpikeGenerator-GruberDynamics.html",
    "GruberSpikeGenerator.html",
    "HodgkinHuxleySpikeGenerator-HodgkinHuxleyNeuronFactory.html",
    "HodgkinHuxleySpikeGenerator-HodgkinHuxleySystem.html",
    "HodgkinHuxleySpikeGenerator.html",
    "IzhikevichSpikeGenerator-Preset.html",
    "IzhikevichSpikeGenerator.html",
    "IzhikevichSpikeGeneratorTest.html",
    "LIFNeuronFactory.html",
    "LIFSpikeGenerator-Factory.html",
    "LIFSpikeGenerator.html",
    "LIFSpikeGeneratorTest.html",
    "LIFSpikingNeuronTest.html",
    "LinearSynapticIntegrator-Factory.html",
    "LinearSynapticIntegrator.html",
    "LinearSynapticIntegratorTest.html",
    "package-index.html",
    "PoissonSpikeGenerator-LinearFactory.html",
    "PoissonSpikeGenerator-LinearNeuronFactory.html",
    "PoissonSpikeGenerator-SigmoidFactory.html",
    "PoissonSpikeGenerator-SigmoidNeuronFactory.html",
    "PoissonSpikeGenerator.html",
    "PoissonSpikeGeneratorTest.html",
    "PyramidalNetwork-PoiraziDendriteFactory.html",
    "PyramidalNetwork.html",
    "RateFunctionSpikeGenerator-PoiraziDendriteSigmoid.html",
    "RateFunctionSpikeGenerator-PoiraziDendriteSigmoidFactory.html",
    "RateFunctionSpikeGenerator-PoiraziSomaSigmoid.html",
    "RateFunctionSpikeGenerator.html",
    "SpikeGeneratorFactory.html",
    "SpikeGeneratorOrigin.html",
    "SpikeGeneratorOriginTest.html",
    "SpikingNeuron.html",
    "SpikingNeuronFactory.html",
    "SpikingNeuronFactoryTest.html",
    "SpikingNeuronTest.html",
    "SynapticIntegratorFactory.html",
])

add_redirects("nengo_1.4", "simulator-ui-api", [
    "packages.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui", [
    "GenerateScriptAction.html",
    "NengoGraphics-ConfigurationPane.html",
    "NengoGraphics-ToggleScriptPane.html",
    "NengoGraphics.html",
    "NengoLauncher.html",
    "package-index.html",
    "RunNetworkAction.html",
    "SaveNetworkAction.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/actions", [
    "AddProbeAction.html",
    "AddProbesAction.html",
    "ClearAllAction.html",
    "ConfigureAction.html",
    "CopyAction.html",
    "CreateModelAction.html",
    "CreateModelAdvancedAction.html",
    "CutAction.html",
    "DefaultModeAction.html",
    "DirectModeAction.html",
    "GeneratePDFAction.html",
    "GeneratePythonScriptAction.html",
    "OpenNeoFileAction.html",
    "package-index.html",
    "PasteAction.html",
    "PlotFunctionAction.html",
    "PlotFunctionNodeAction.html",
    "PlotSpikePattern.html",
    "PlotTimeSeries.html",
    "RateModeAction.html",
    "RemoveModelAction.html",
    "RemoveModelsAction.html",
    "RemoveObjectAction.html",
    "RunInteractivePlotsAction.html",
    "RunSimulatorAction-RunSimulatorActivity.html",
    "RunSimulatorAction.html",
    "SaveNodeAction.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/util", [
    "AllNeoFiles.html",
    "BreakTraceFunction.html",
    "DialogPlotter.html",
    "FileExtensionFilter.html",
    "NengoClipboard-ClipboardListener.html",
    "NengoClipboard.html",
    "NengoConfigManager-UserProperties.html",
    "NengoConfigManager.html",
    "NeoFileChooser.html",
    "package-index.html",
    "ProgressIndicator.html",
    "ScriptInterruptException.html",
    "ScriptWorldWrapper.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/script", [
    "CallChainCompletor.html",
    "CommandCompletor.html",
    "HistoryCompletor.html",
    "package-index.html",
    "ScriptConsole.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/world", [
    "NengoWorld.html",
    "package-index.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib", [
    "AppFrame-AboutAction.html",
    "AppFrame-CloseAllPlots.html",
    "AppFrame-HideDebugMemory.html",
    "AppFrame-HighQualityAction.html",
    "AppFrame-LowQualityAction.html",
    "AppFrame-MediumQualityAction.html",
    "AppFrame-MinimizeAllWindows.html",
    "AppFrame-MyWindowListener.html",
    "AppFrame-RedoAction.html",
    "AppFrame-ShowDebugMemory.html",
    "AppFrame-SwitchToNavigationMode.html",
    "AppFrame-SwitchToSelectionMode.html",
    "AppFrame-TipsAction.html",
    "AppFrame-TurnOffFullScreen.html",
    "AppFrame-TurnOffGrid.html",
    "AppFrame-TurnOffTooltips.html",
    "AppFrame-TurnOnFullScreen.html",
    "AppFrame-TurnOnGrid.html",
    "AppFrame-TurnOnTooltips.html",
    "AppFrame-UndoAction.html",
    "AppFrame.html",
    "AuxillarySplitPane-HideButtonListener.html",
    "AuxillarySplitPane-Orientation.html",
    "AuxillarySplitPane.html",
    "package-index.html",
    "UserPreferences.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/actions", [
    "ActionException.html",
    "DisabledAction.html",
    "DragAction.html",
    "ExitAction.html",
    "LayoutAction.html",
    "ObjectState.html",
    "OpenURLAction.html",
    "package-index.html",
    "RemoveObjectsAction.html",
    "ReversableAction.html",
    "ReversableActionManager.html",
    "SetSplitPaneVisibleAction.html",
    "StandardAction-RunThreadType.html",
    "StandardAction-SwingAction.html",
    "StandardAction.html",
    "UserCancelledException.html",
    "ZoomToFitAction.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/objects/lines", [
    "CreateLineEndHandler.html",
    "DestroyListener.html",
    "Edge.html",
    "ILineTermination.html",
    "LineConnector.html",
    "LineOriginIcon.html",
    "LineTerminationIcon.html",
    "LineWell.html",
    "package-index.html",
])
add_redirects(
    "nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/objects/activities", [
        "package-index.html",
        "TrackedAction.html",
        "TrackedStatusMsg.html",
        "TransientMessage.html",
        "TransientStatusMessage.html",
    ])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/objects/models", [
    "ModelObject-ModelListener.html",
    "ModelObject.html",
    "package-index.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/util", [
    "ElasticLayout-LengthFunction.html",
    "ElasticLayout-SpringDimensionChecker.html",
    "ElasticLayout-SpringEdgeData.html",
    "ElasticLayout-SpringVertexData.html",
    "ElasticLayout-UnitLengthFunction.html",
    "ElasticLayout.html",
    "package-index.html",
    "UIEnvironment.html",
    "UserMessages-DialogException.html",
    "UserMessages.html",
    "Util.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/util/menus", [
    "AbstractMenuBuilder.html",
    "MenuBuilder.html",
    "package-index.html",
    "PopupMenuBuilder.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/world", [
    "Destroyable.html",
    "Droppable.html",
    "DroppableX.html",
    "Fader.html",
    "Interactable.html",
    "NamedObject.html",
    "ObjectSet.html",
    "package-index.html",
    "package-index.html",
    "PaintContext.html",
    "Pulsator.html",
    "Searchable-SearchValuePair.html",
    "Searchable.html",
    "World.html",
    "WorldLayer.html",
    "WorldObject-ChildListener.html",
    "WorldObject-Listener.html",
    "WorldObject-Property.html",
    "WorldObject.html",
    "WorldSky.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/world/elastic", [
    "Anchor.html",
    "ElasticEdge.html",
    "ElasticGround-UpdateGraphResult.html",
    "ElasticGround.html",
    "ElasticLayoutRunner-ElasticLengthFunction.html",
    "ElasticLayoutRunner.html",
    "ElasticObject.html",
    "ElasticVertex.html",
    "ElasticWorld-DoJungLayout.html",
    "ElasticWorld-JungLayoutAction.html",
    "ElasticWorld-SetElasticLayoutAction.html",
    "ElasticWorld.html",
    "FeedForwardLayout.html",
    "package-index.html",
    "SetLayoutBoundsAction.html",
    "StretchedFeedForwardLayout-VoidVertex.html",
    "StretchedFeedForwardLayout.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/world/handlers", [
    "AbstractPickHandler-Timer.html",
    "AbstractPickHandler.html",
    "AbstractStatusHandler.html",
    "EventConsumer.html",
    "KeyboardFocusHandler.html",
    "KeyboardHandler.html",
    "MouseHandler.html",
    "package-index.html",
    "PanEventHandler.html",
    "ScrollZoomHandler.html",
    "SelectionHandler-BoundsFilter.html",
    "SelectionHandler-SelectionListener.html",
    "SelectionHandler.html",
    "TooltipPickHandler.html",
    "TopWorldStatusHandler.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/world/piccolo", [
    "GroundNode.html",
    "package-index.html",
    "PiccoloChangeListener.html",
    "WorldGroundImpl-ChildFilter.html",
    "WorldGroundImpl.html",
    "WorldImpl-CloseAllWindows.html",
    "WorldImpl-MinimizeAllWindows.html",
    "WorldImpl.html",
    "WorldLayerImpl.html",
    "WorldObjectImpl-ListenerAdapter.html",
    "WorldObjectImpl.html",
    "WorldSkyImpl.html",
])
add_redirects(
    "nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/world/piccolo/objects", [
        "AbstractButton-ButtonState.html",
        "AbstractButton.html",
        "Border.html",
        "BoundsHandle.html",
        "Button.html",
        "ButtonStateHandler.html",
        "HandCursorHandler.html",
        "MenuBar.html",
        "package-index.html",
        "RectangleEdgeNode.html",
        "RectangularEdge.html",
        "SelectionBorder.html",
        "TextButton.html",
        "TooltipWrapper.html",
        "Window-MenuBarHandler.html",
        "Window-WindowState.html",
        "Window.html",
        "Wrapper.html",
    ])
add_redirects(
    "nengo_1.4",
    "simulator-ui-api/ca/nengo/ui/lib/world/piccolo/objects/icons",
    [
        "ArrowIcon.html",
        "CloseIcon.html",
        "LayoutIconBase.html",
        "LoadIcon.html",
        "MaximizeIcon.html",
        "MinimizeIcon.html",
        "package-index.html",
        "RestoreIcon.html",
        "SaveIcon.html",
        "WindowIconBase.html",
        "ZoomIcon.html",
    ])
add_redirects(
    "nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/world/piccolo/primitives", [
        "CameraPropertyChangeListener.html",
        "Image.html",
        "package-index.html",
        "Path.html",
        "PiccoloNodeInWorld.html",
        "PointerTriangle.html",
        "PXCamera.html",
        "PXEdge-EdgeShape.html",
        "PXEdge-EdgeState.html",
        "PXEdge.html",
        "PXGrid.html",
        "PXImage.html",
        "PXLayer.html",
        "PXNode-TransformChangeListener.html",
        "PXNode.html",
        "PXPath.html",
        "PXText.html",
        "Text.html",
        "Universe-TextLayoutListener.html",
        "Universe.html",
    ])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/Style", [
    "NengoStyle.html",
    "package-index.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/misc", [
    "package-index.html",
    "PointSerializable.html",
    "ShortcutKey.html",
    "WorldLayout.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/lib/exceptions", [
    "package-index.html",
    "UIException.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/dataList", [
    "DataListView.html",
    "DataPath.html",
    "DataTreeNode.html",
    "ExportAction.html",
    "ExportDelimitedFileAction.html",
    "ExportFileChooser.html",
    "ExportMatlabAction.html",
    "ExtensionFileFilter.html",
    "NaturalOrderComparator.html",
    "NengoTreeNode.html",
    "package-index.html",
    "PlotNodesAction.html",
    "ProbeDataExpandedNode.html",
    "ProbeDataNode.html",
    "ProbePlotHelper.html",
    "RenameAction.html",
    "SimulatorDataModel.html",
    "SortableMutableTreeNode.html",
    "SpikePatternNode.html",
    "TimeSeriesNode-ExtractDimenmsions.html",
    "TimeSeriesNode.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/dev", [
    "BrainViewExample.html",
    "ExampleRunner.html",
    "FuzzyLogicExample.html",
    "GFuzzyLogicExample.html",
    "package-index.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/configurable", [
    "ConfigException.html",
    "ConfigResult.html",
    "ConfigSchema.html",
    "ConfigSchemaImpl.html",
    "IConfigurable.html",
    "package-index.html",
    "Property.html",
    "PropertyInputPanel.html",
    "UserDialogs.html",
    "UserMultiPropDialog.html",
])
add_redirects(
    "nengo_1.4", "simulator-ui-api/ca/nengo/ui/configurable/managers", [
        "ConfigDialog.html",
        "ConfigDialogClosedException.html",
        "ConfigFilesFilter.html",
        "ConfigManager-ConfigMode.html",
        "ConfigManager.html",
        "ConfigTemplateDialog.html",
        "Configureable.html",
        "FileConfigurer.html",
        "package-index.html",
        "UserConfigurer.html",
        "UserTemplateConfigurer.html",
        "VerticalLayoutPanel.html",
    ])
add_redirects(
    "nengo_1.4", "simulator-ui-api/ca/nengo/ui/configurable/descriptors", [
        "package-index.html",
        "PBoolean.html",
        "PCouplingMatrix.html",
        "PFloat.html",
        "PFunction.html",
        "PFunctionArray.html",
        "PInt.html",
        "PLong.html",
        "PNodeFactory.html",
        "PString.html",
        "PTerminationWeights.html",
        "RangedConfigParam.html",
    ])
add_redirects(
    "nengo_1.4",
    "simulator-ui-api/ca/nengo/ui/configurable/descriptors/functions",
    [
        "AbstractFn.html",
        "ConfigurableFunction.html",
        "FnAdvanced.html",
        "FnConstant.html",
        "FnCustom-PExpression.html",
        "FnCustom.html",
        "FnReflective.html",
        "InterpreterFunctionConfigurer-FunctionDialog-NewFunctionAL.html",
        "InterpreterFunctionConfigurer-FunctionDialog-PreviewFunctionAL.html",
        "InterpreterFunctionConfigurer-FunctionDialog-RemoveFunctionAL.html",
        "InterpreterFunctionConfigurer-FunctionDialog.html",
        "InterpreterFunctionConfigurer.html",
        "JCustomPanel.html",
        "package-index.html",
    ])
add_redirects(
    "nengo_1.4", "simulator-ui-api/ca/nengo/ui/configurable/matrixEditor", [
        "CouplingMatrix.html",
        "CouplingMatrixImpl.html",
        "MatrixEditor.html",
        "package-index.html",
    ])
add_redirects(
    "nengo_1.4", "simulator-ui-api/ca/nengo/ui/configurable/panels", [
        "BooleanPanel.html",
        "CALIFNeuronFactory.html",
        "CLIFNeuronFactory.html",
        "CLinearNeuronFactory.html",
        "ConfigurableFunctionArray.html",
        "ConstructableNodeFactory.html",
        "CouplingMatrixPanel.html",
        "CSigmoidNeuronFactory.html",
        "CSpikingNeuronFactory.html",
        "FloatPanel.html",
        "FunctionArrayPanel-EditFunctions.html",
        "FunctionArrayPanel.html",
        "FunctionPanel-EditAction.html",
        "FunctionPanel-NewParametersAction.html",
        "FunctionPanel-PreviewFunctionAction.html",
        "FunctionPanel.html",
        "IntegerPanel.html",
        "LongPanel.html",
        "NodeFactoryPanel.html",
        "package-index.html",
        "PIndicatorPDF.html",
        "PListSelector.html",
        "PropertyTextPanel-TextError.html",
        "PropertyTextPanel-TextFieldFocusListener.html",
        "PropertyTextPanel.html",
        "StringPanel.html",
        "TerminationWeightsInputPanel-EditMatrixAction.html",
        "TerminationWeightsInputPanel.html",
    ])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/audio", [
    "Clicker.html",
    "package-index.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/brainView", [
    "AbstractBrainImage2D.html",
    "BrainData-MyCanvas.html",
    "BrainData.html",
    "BrainFrontImage.html",
    "BrainImageWrapper-BrainImageMouseHandler.html",
    "BrainImageWrapper.html",
    "BrainSideImage.html",
    "BrainTopImage.html",
    "BrainViewer.html",
    "BrainViewStatusHandler.html",
    "package-index.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/models", [
    "ModelsContextMenu.html",
    "NodeContainer-ContainerException.html",
    "NodeContainer.html",
    "package-index.html",
    "UIModels.html",
    "UINeoModel.html",
    "UINeoNode-HideAllOandTAction.html",
    "UINeoNode-RenameNodeAction.html",
    "UINeoNode-ShowAllOandTAction.html",
    "UINeoNode-ShowOriginAction.html",
    "UINeoNode-ShowTerminationAction.html",
    "UINeoNode.html",
])
add_redirects(
    "nengo_1.4", "simulator-ui-api/ca/nengo/ui/models/constructors", [
        "AbstractConstructable.html",
        "CDecodedOrigin.html",
        "CDecodedTermination.html",
        "CFunctionInput.html",
        "CNEFEnsemble.html",
        "CNetwork.html",
        "ConstructableNode.html",
        "ModelFactory.html",
        "OriginInputPanel.html",
        "OriginSelector.html",
        "package-index.html",
        "PApproximator.html",
        "PEncodingDistribution-Slider.html",
        "PEncodingDistribution.html",
        "ProjectionConstructor.html",
        "PSign.html",
        "Sign.html",
        "SignItem.html",
    ])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/models/tooltips", [
    "ITooltipPart.html",
    "package-index.html",
    "Tooltip.html",
    "TooltipBuilder.html",
    "TooltipProperty.html",
    "TooltipTitle.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/models/icons", [
    "EnsembleIcon.html",
    "FunctionInputIcon.html",
    "IconImage.html",
    "IconImageNode.html",
    "ModelIcon.html",
    "NetworkIcon.html",
    "NodeContainerIcon.html",
    "NodeIcon.html",
    "package-index.html",
    "ProbeIcon.html",
    "Triangle.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/models/viewers", [
    "EnsembleViewer.html",
    "NetworkViewer-RestoreLayout.html",
    "NetworkViewer-SaveLayout.html",
    "NetworkViewer-SetOTVisiblityAction.html",
    "NetworkViewer.html",
    "NodeLayout.html",
    "NodeViewer-SortMode.html",
    "NodeViewer-SortNodesAction.html",
    "NodeViewer-ZoomToFitActivity.html",
    "NodeViewer.html",
    "NodeViewerStatus.html",
    "package-index.html",
    "PointSerializable.html",
    "ShowHideHandler.html",
])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/models/nodes", [
    "package-index.html",
    "UIEnsemble-StartCollectSpikes.html",
    "UIEnsemble-StopCollectSpikes.html",
    "UIEnsemble.html",
    "UIFunctionInput.html",
    "UIGenericNode.html",
    "UINEFEnsemble-AddDecodedOriginAction.html",
    "UINEFEnsemble-AddDecodedTerminationAction.html",
    "UINEFEnsemble-PlotDecodedOriginDistortion.html",
    "UINEFEnsemble-PlotDecodedOriginMSE.html",
    "UINEFEnsemble.html",
    "UINetwork.html",
    "UINeuron.html",
    "UINodeViewable.html",
])
add_redirects(
    "nengo_1.4", "simulator-ui-api/ca/nengo/ui/models/nodes/widgets", [
        "ExposedIcon.html",
        "package-index.html",
        "UIDecodedOrigin.html",
        "UIDecodedTermination.html",
        "UIGenericOrigin.html",
        "UIGenericTermination.html",
        "UINetworkTermination.html",
        "UIOrigin.html",
        "UIProbe.html",
        "UIProjection.html",
        "UIProjectionWell-RemoveProjectionListener.html",
        "UIProjectionWell.html",
        "UISpikeProbe.html",
        "UIStateProbe-ExportToMatlabAction.html",
        "UIStateProbe.html",
        "UITermination-DisconnectAction.html",
        "UITermination.html",
        "Widget-ExposeAction.html",
        "Widget-HideWidgetAction.html",
        "Widget-ShowWidgetAction.html",
        "Widget-UnExposeAction.html",
        "Widget.html",
    ])
add_redirects("nengo_1.4", "simulator-ui-api/ca/nengo/ui/test", [
    "CopyAndPasteTest.html",
    "DataViewerTest.html",
    "DataViewerTest2.html",
    "IntegratorExample.html",
    "NetworkViewerMemoryTest.html",
    "NetworkViewerTest.html",
    "package-index.html",
    "TestUtil.html",
])

# nengo_dl redirects

add_redirects("nengo_dl", "", [
    "backend.html",
    "builder.html",
    "examples.html",
    "extra_objects.html",
    "frontend.html",
    "graph_optimizer.html",
    "index.html",
    "installation.html",
    "introduction.html",
    "learning_rules.html",
    "neurons.html",
    "op_builders.html",
    "processes.html",
    "project.html",
    "resources.html",
    "signals.html",
    "simulator.html",
    "tensor_graph.html",
    "tensor_node.html",
    "training.html",
    "utils.html",
])
add_redirects("nengo_dl", "examples", [
    "nef_init.html",
    "pretrained_model.html",
    "spa_memory.html",
    "spa_retrieval.html",
    "spiking_mnist.html",
])
