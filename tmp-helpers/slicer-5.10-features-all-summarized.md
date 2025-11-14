# Slicer 5.10 Features - Aggregated Summary

This document aggregates related pull requests into unified feature descriptions, providing a high-level overview of the major features and improvements in Slicer 5.10.

## Major Platform Features

### Multi-Layer Slice Rendering Infrastructure
**Related PRs:** 8277, 8278, 8279, 8280

Slicer 5.10 introduces foundational infrastructure for rendering arbitrary numbers of layers in slice views. This groundwork generalizes the SliceLogic and SliceCompositeNode APIs by replacing hardcoded background/foreground/label layers with dynamic "Nth Layer" functions. The refactoring supports opacity management, volume assignment, and pipeline updates for future multi-layer rendering capabilities beyond the current three-layer limit.

### Enhanced Scene View Management
**Related PRs:** 8303, 8393, 8607

Scene views have been modernized to use hidden sequence nodes for storage instead of traditional scene view nodes, improving maintainability and enabling consistent logic across Sequences, Scene Views, and future Undo/Redo functionality. Users can now update existing scene views and select specific nodes to capture through an Advanced section in the scene views dialog, providing more granular control over scene state management.

### Volume Rendering Improvements
**Related PRs:** 8341, 8438, 8739, 8414

Volume rendering becomes significantly more powerful and user-friendly with interactive transfer function adjustment in 3D views using mouse gestures, fast clipping shortcuts that leverage VTK's built-in optimizations, color inversion options for flexible visualization regardless of voxel values, and multi-component volume property handling with component selection controls. A new "Follow Slice Views" option synchronizes window/level, color tables, and thresholds between 2D and 3D displays.

### DICOM Enhancements
**Related PRs:** 8432, 8538, 8121

DICOM functionality expands with instance number display in the DataProbe module, PET modality support in the CreateDICOMSeries CLI, and TLS authentication for secure DICOM communication through the Sender and Listener modules using private keys, certificates, and CA file configuration.

### Segmentation Workflow Improvements
**Related PRs:** 8247, 8354, 8666

Segmentation workflows benefit from a context menu visibility toggle for quickly showing/hiding selected segments, options to hide display nodes missing from historical sequence snapshots, and extraction of segment editor logic into a standalone VTK class for use in non-Qt contexts and improved architectural modularity.

### Python 3.12 Upgrade
**Related PRs:** 8459, 8461, 8466, 8488, 8489, 8548

Slicer 5.10 upgrades from Python 3.9.10 to Python 3.12.10, modernizing the codebase with contemporary APIs including importlib (replacing deprecated imp module), assertRegex (replacing assertRegexpMatches), updated pydicom interfaces, and PyConfig-based initialization. The upgrade enables access to structural pattern matching, type union operators, enhanced error messages, and new Python 3.10-3.12 standard library features.

## New Core Modules

### Curved Planar Reformation (CPR)
**Related PR:** 8148

The GeneralizedReformat module now supports Curved Planar Reformation, porting Python-based CPR computation into high-performance C++ for straightening and reformatting curved anatomical structures like blood vessels and dental arches with professional-grade visualization quality.

### Line Profile Module
**Related PR:** 8435

A new LineProfile module enables computation and visualization of intensity profiles along lines or curves in medical images, integrating with existing markup nodes for line/curve definition and table nodes for storing computed profiles.

## Additional User-Facing Features

### Volume Cropping with Reorientation
**Related PR:** 8737

The Crop Volume module gains reorientation capabilities with Fit to Volume alignment modes (align to volume axes, world coordinate axes, or keep current orientation), helping users align cropped volume axes to anatomical directions for easier segmentation workflows.

### Enhanced Sample Data Download
**Related PR:** 8736

Custom sample data downloads improve with automatic GitHub/Dropbox URL conversion, batch multi-URL download support, and filename preservation, making it easier to load external datasets.

### Configurable Filename Lengths
**Related PR:** 8245

Filename length limits become platform-configurable with sensible defaults (50 characters on Windows for compatibility, 1000 characters on macOS/Linux for flexibility), allowing users to choose between Windows compatibility and preserving long node names in filenames.

### Smart Default Node Selection
**Related PR:** 8306

Modules (Segmentations, Transforms, VolumeRendering, Volumes, Models) now automatically select the first suitable node when opened, eliminating an unnecessary click in typical workflows.

### CLI Window Visibility Control on Windows
**Related PR:** 8172

Windows users can now configure CLI modules to show their executable windows through SetHideWindow/GetHideWindow methods, enabling interactive viewers and debugging scenarios while maintaining default hidden behavior for backward compatibility.

### Improved Tooltips and Discoverability
**Related PR:** 8392

Keyboard shortcut information (Shift+Mouse move) is added to slice intersection tooltips, improving discoverability of existing features.

### Sequence Recording Support for Additional Nodes
**Related PR:** 8318

LayoutNode and SequenceBrowserNode can now be properly recorded in Sequences through new CopyContent methods.

## New Extensions (20 total)

### Medical Image Segmentation
- **CADSWholeBodyCTSeg**: One-click automated segmentation of 167 anatomical structures in whole-body CT scans
- **UpperAirwaySegmentator**: nnUNet-based automatic upper airway segmentation on CT/CBCT for dental imaging
- **SlicerMultiverSeg**: Interactive segmentation through in-context learning with few annotated examples
- **NeuroStrip**: CNN-based brain extraction (skull stripping) from MRI scans

### Image Registration and Analysis
- **SlicerANTsPy**: ANTsPy integration for pairwise/groupwise registration, template creation, and morphometric analysis
- **DenseCorrespondenceAnalysis**: 3D surface shape analysis combining landmarks with automated dense registration

### Medical Image Synthesis and Conversion
- **ModalityConverter**: Deep learning-based medical image-to-image translation (MRI-to-CT, CBCT-to-CT)

### Surgical Planning and Simulation
- **SlicerOrbitSurgerySim**: Orbital fracture repair planning with surgical plate registration and fit metrics
- **EVARSim**: Stent placement visualization and simulation for endovascular aneurysm repair
- **DBSCoalignment**: Deep Brain Stimulation trajectory optimization with brain shift compensation

### Clinical Imaging Workflows
- **SlicerHeadCTDeid**: Head CT de-identification removing DICOM metadata, burned-in text, and facial features
- **ClassAnnotation**: Medical image annotation workflow with diagnostic labeling and quality control
- **IGSpineDeformity**: Spinal deformity analysis using freehand ultrasound with Cobb angle measurements

### Functional and Nuclear Medicine Imaging
- **ASLtoolkit**: Arterial Spin Labelling MRI processing and brain perfusion analysis
- **SPECTRecon**: 3D SPECT image reconstruction from raw projection data with customizable algorithms
- **RadioembolizationDosimetry**: Voxel-based liver radioembolization dosimetry for Y-90 microsphere treatments

### Research and Specialized Applications
- **SlicerOpenLIFU**: Focused ultrasound neuromodulation interface for Openwater's OpenLIFU platform
- **AnatomyCarve**: Interactive anatomical visualization through customizable segment clipping

### Developer Tools
- **LayerDisplayableManager**: New architecture for layered rendering pipelines with centralized management
