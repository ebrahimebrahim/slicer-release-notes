# Slicer 5.10 Feature Summaries

This document provides human-readable summaries for all features, groundwork PRs, Python 3.12 compatibility updates, and new extensions in Slicer 5.10.

## Actual Features

### PR-8247: Add segment visibility toggle option
Adds a convenient context menu option to quickly toggle visibility of selected segments, useful when reviewing segmentations with many segments.

### PR-8245: Make maximum file length configurable
Introduces platform-specific configurable filename length limits (50 chars on Windows for compatibility, 1000 chars on macOS/Linux for flexibility).

### PR-8306: Select the first suitable node by default in tree views
Automatically selects the first compatible node when entering a module, saving users an unnecessary click in Segmentations, Transforms, VolumeRendering, Volumes, and Models modules.

### PR-8303: Update Scene Views to use Sequences
Refactors scene views to be stored as hidden sequence nodes instead of traditional scene view nodes, reducing maintenance burden and improving consistency.

### PR-8341: Add invert colors option to Volumes module
Adds an option to reverse the order of colors in lookup tables, allowing users to apply the same color mapping regardless of whether structures have higher or lower voxel values.

### PR-8354: Add option to hide missing display nodes in sequences
Introduces a missing item mode to hide proxy display nodes that weren't present when historical scene snapshots were captured.

### PR-8148: Add Curved Planar Reformation (CPR) support to GeneralizedReformat
Ports CPR computation from Python to C++, enabling straightening and reformatting of curved anatomical structures like blood vessels or dental arches.

### PR-8172: Add option to show CLI executable windows on Windows
Adds SetHideWindow/GetHideWindow methods to allow CLI executables to display their own windows on Windows when needed for interactive viewers.

### PR-8392: Include slice intersection mouse move info in tooltip
Adds Shift+Mouse move functionality information to the slice intersection toggle tooltip to improve feature discoverability.

### PR-8393: Add functions to update the contents of existing scene views
Introduces UpdateNthSceneView functions to modify scene views by updating individual nodes or replacing entire contents with current scene state.

### PR-8438: Add fast clipping shortcut for volume rendering
Introduces a performance optimization using VTK's built-in SetClippingPlanes method when specific conditions are met, with UI indicators showing whether fast or slow clipping is active.

### PR-8432: Add DICOM instance number in the dataProbe
Enhances DataProbe module to display DICOM instance numbers (slice numbers) alongside existing slice position data.

### PR-8538: Add PET support to CreateDICOMSeries CLI
Expands CreateDICOMSeries CLI module to handle PET imaging data in addition to existing DICOM series creation functionality.

### PR-8607: Add widget to select any node for scene views
Introduces Advanced section in scene views dialog allowing granular control over specific nodes to capture beyond predefined categories.

### PR-8435: Add line profile module
Introduces new LineProfile module to compute and visualize intensity profiles along lines or curves in medical images.

### PR-8737: Add volume reorientation to Crop Volume module
Adds reorientation section and Fit to volume alignment modes to help users align cropped volume axes to anatomical directions.

### PR-8739: Make volume rendering transfer function adjustment easier
Enables interactive window/level adjustment in 3D views with mouse gestures and adds Follow Slice Views synchronization option.

### PR-8121: Add TLS authentication support to DICOM Sender and Listener
Introduces DICOMProcessTLSMixin class managing TLS configurations (private keys, certificates, CA files) for secure encrypted DICOM communication.

### PR-8736: Improve custom sample data download
Adds automatic handling for GitHub/Dropbox links, batch download support, and filename preservation for custom sample data URLs.

## Groundwork for Future Features

### PR-8277: Generalize SliceLogic API introducing "Nth Layer" functions
Replaces hardcoded layer members with dynamic Layers list and introduces new "Nth Layer" methods for managing layers generically to support future multi-layer rendering.

### PR-8278: Generalize CompositeNode API introducing "Nth Layer" functions
Introduces indexed layer methods (GetNthLayerVolume, SetNthLayerVolume) replacing hardcoded background/foreground/label volume properties for dynamic multi-layer support.

### PR-8279: Refactor vtkMRMLSliceLogic::UpdatePipeline to use "Nth Layer" API
Refactors UpdatePipeline method to use dynamic layer iteration instead of hardcoded layer handling, streamlining pipeline composition.

### PR-8280: Generalize CompositeNode "opacity" API introducing "Nth Layer" functions
Replaces hardcoded foreground and label opacity values with flexible GetNthLayerOpacity/SetNthLayerOpacity functions supporting dynamic layer rendering.

### PR-8318: Add CopyContent methods to vtkMRMLLayoutNode and vtkMRMLSequenceBrowserNode
Adds CopyContent methods to enable both vtkMRMLLayoutNode and vtkMRMLSequenceBrowserNode to be properly recorded in Sequences.

### PR-8414: Update CTK to add components to ctkVTKVolumePropertyWidget
Enables developers to change which component is active within the widget, allowing visualization and editing of transfer functions for components beyond the first.

### PR-8658: Add API to retrieve view displayable managers without Qt widgets
Introduces Qt-independent API (GetViewDisplayableManagerByClassName) for accessing displayable managers to support headless and web-based frontends.

### PR-8666: Split segment editor logic
Extracts business logic from Qt UI framework into new vtkSegmentEditorLogic class for use in non-Qt contexts and improved modularity.

## Python 3.12 Compatibility and Modernization

### PR-8459: Replace deprecated imp module with importlib to support Python 3.12+
Modernizes Python codebase by replacing deprecated imp module (removed in Python 3.12) with contemporary importlib alternatives.

### PR-8461: Replace deprecated assertRegexpMatches with assertRegex to support Python 3.12+
Updates unittest method calls to use assertRegex instead of deprecated assertRegexpMatches (removed in Python 3.12).

### PR-8466: Upgrade from python 3.9.10 to 3.12.10
Major Python upgrade enabling access to features from Python 3.10, 3.11, and 3.12 including structural pattern matching, type union operators, enhanced error messages, and new standard library additions.

### PR-8488: Replace deprecated pydicom API usage
Removes usage of deprecated read_file and write_file functions (removed in pydicom 3.0.0) for compatibility with newer pydicom versions.

### PR-8489: Enforce python 3.12 and newer syntax
Updates Python codebase to enforce Python 3.12+ syntax standards, improving readability and modernizing code through automated pre-commit hooks.

### PR-8548: Update Python initialization to use PyConfig API
Modernizes Python initialization by replacing deprecated PySys_SetArgvEx and Py_NoUserSiteDirectory (both marked for removal in Python 3.14) with PyConfig API (PEP 587).

## New Extensions Added

### SlicerHeadCTDeid
Safely shares head CT scans by removing patient privacy information from DICOM files, detecting burned-in text, and eliminating facial features through tissue stripping to prevent identification in 3D reconstructions.

### ClassAnnotation
Facilitates medical image annotation workflows enabling users to load imaging datasets, assign diagnostic class labels, and automatically generate CSV reports with quality control features like random and manual review modes.

### DenseCorrespondenceAnalysis
Analyzes 3D surface shapes by combining manually-placed anatomical landmarks with automated dense surface registration for detailed morphological insights of complex biological structures.

### ModalityConverter
Enables medical image-to-image translation using deep learning models to convert between different imaging modalities (MRI-to-CT, CBCT-to-CT) through GPU-accelerated interface with custom model support.

### CADSWholeBodyCTSeg
Automates segmentation of 167 anatomical structures in whole-body CT scans using the CADS-model for one-click, fully automated segmentation for clinical and research applications.

### SlicerOpenLIFU
Provides interface for Openwater's OpenLIFU research platform enabling non-destructive treatment using focused ultrasound for neuromodulation, coordinating imaging, positioning, planning, and hardware control.

### LayerDisplayableManager
Introduces new architecture for managing display pipelines with layered rendering and interaction handling, simplifying visualization integration through centralized pipeline management and dependency injection.

### DBSCoalignment
Improves Deep Brain Stimulation surgery precision by combining deep learning-based subthalamic nucleus segmentation with microelectrode recording trajectory optimization while accounting for brain shift.

### UpperAirwaySegmentator
Performs fully automatic segmentation of upper airway (nasal cavity, nasopharynx, oropharynx) on CT and CBCT volumes using nnUNet deep learning framework for dental imaging applications.

### IGSpineDeformity
Analyzes spinal deformities using freehand ultrasound imaging by identifying spinal cord curves in 3D and projecting onto anatomical planes for scoliosis assessment with Cobb angle measurements.

### SPECTRecon
Reconstructs 3D SPECT medical images from raw projection data with customizable reconstruction options including system modeling, likelihood functions, and various algorithms, plus SIMIND Monte Carlo DICOM conversion.

### ASLtoolkit
Provides image processing and analysis methods for Arterial Spin Labelling MRI images, offering computational tools to process and analyze brain perfusion data from ASL protocols.

### AnatomyCarve
Enables interactive medical image visualization through customizable clipping on segments, creating detailed anatomical views comparable to medical textbooks through volumetric dataset carving.

### SlicerANTsPy
Integrates ANTsPy image processing library with graphical interfaces for medical image registration including pairwise registration, batch groupwise registration, template creation, and morphometric analysis.

### SlicerMultiverSeg
Integrates MultiverSeg model for biomedical image segmentation providing interactive Segment Editor tool for rapid segmentation through in-context learning with few annotated examples.

### NeuroStrip
Provides CNN-based skull stripping (brain masking) from MRI using NeuroStrip library, generating brain masks and optionally creating masked brain volumes through user-friendly interface.

### RadioembolizationDosimetry (Taranis)
Provides voxel-based liver radioembolization dosimetry capabilities to estimate lung shunt fractions, plan treatment doses, and quantify absorbed doses post-treatment using PET/SPECT imaging for Y-90 microsphere treatments.

### SlicerOrbitSurgerySim
Helps surgeons plan and evaluate orbital fracture repairs through interactive registration and comparison of surgical plates, calculating fit metrics to determine optimal plate design and placement.

### EVARSim
Enables visualization and simulation of stent placement along complex vessel geometries for endovascular aneurysm repair procedures, creating realistic cylindrical stents following vessel centerlines with branch selection.
