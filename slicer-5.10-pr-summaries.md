# Pull Request Summaries for Slicer 5.10

## PR-8318: Add CopyContent methods to vtkMRMLLayoutNode and vtkMRMLSequenceBrowserNode
Adds CopyContent methods to enable both vtkMRMLLayoutNode and vtkMRMLSequenceBrowserNode to be properly recorded in Sequences.

## PR-8303: Update Scene Views to use Sequences
Refactors scene views to be stored as hidden sequence nodes instead of traditional scene view nodes, reducing maintenance burden and improving consistency.

## PR-8341: Add invert colors option to Volumes module
Adds an option to reverse the order of colors in lookup tables, allowing users to apply the same color mapping regardless of whether structures have higher or lower voxel values.

## PR-8354: Add option to hide missing display nodes in sequences
Introduces a missing item mode to hide proxy display nodes that weren't present when historical scene snapshots were captured.

## PR-8148: Add Curved Planar Reformation (CPR) support to GeneralizedReformat
Ports CPR computation from Python to C++, enabling straightening and reformatting of curved anatomical structures like blood vessels or dental arches.

## PR-8349: Make all colors defined by default when setting a LUT
Ensures that when colors are set in bulk using SetAndObserveLookupTable, they're automatically marked as defined, aligning with developer expectations.

## PR-8172: Add option to show CLI executable windows on Windows
Adds SetHideWindow/GetHideWindow methods to allow CLI executables to display their own windows on Windows when needed.

## PR-8350: Refactor observations in MRML nodes
Standardizes observation patterns by upgrading to safer ObserverManager-based macros instead of lower-level VTK calls.

## PR-8238: Update VTK from 9.2.20230607 to 9.4.2
Major VTK version update addressing API deprecations, method renaming, and infrastructure modifications for compatibility with VTK 9.4.

## PR-8392: Include slice intersection mouse move info in tooltip
Adds Shift+Mouse move functionality information to the slice intersection toggle tooltip to improve feature discoverability.

## PR-8395: Select first preferred terminology if no entry is found
Enhances terminology selection to default to the first entry from preferred terminologies list instead of an arbitrary first item.

## PR-8393: Add functions to update the contents of existing scene views
Introduces UpdateNthSceneView functions to modify scene views by updating individual nodes or replacing entire contents with current scene state.

## PR-8414: Update CTK to add components to ctkVTKVolumePropertyWidget
Enables developers to change which component is active within the widget, allowing visualization and editing of transfer functions for components beyond the first.

## PR-8416: Set color picker to use basic colors tab by default
Changes color picker dialog to display basic colors tab first, de-emphasizing label-based color selection which is mostly redundant.

## PR-8428: Remove Slicer mention from Markups save to default display tooltip
Removes application name reference from tooltip to better support custom Slicer applications with different branding.

## PR-8376: Simplify qSlicerStyle removing obsolete workaround #7418
Removes obsolete workaround code that is no longer needed since underlying Qt bugs have been fixed in the fusion style.

## PR-8430: Make it easier to render large volumes on macOS
Implements automatic volume partitioning with a default maximum 3D texture size of 2048 pixels on macOS to enable rendering of large volumes.

## PR-8433: Remove old deprecation warning
Removes a deprecation warning from 2015 about vtkMRMLScalarVolumeNode no longer having a LabelMap attribute.

## PR-8436: Always show context selector in terminology navigator
Makes the context selector for choosing between terminology sources permanently visible instead of requiring section expansion.

## PR-8438: Add fast clipping shortcut for volume rendering
Introduces a performance optimization using VTK's built-in SetClippingPlanes method when specific conditions are met, with UI indicators showing whether fast or slow clipping is active.

## PR-8432: Add dicom instance number in the dataProbe
Enhances DataProbe module to display DICOM instance numbers alongside existing slice position data.

## PR-8452: Move Markups MRML JSON helper classes to MRMLCore
Relocates Markups JSON reader/writer helper classes from their original location to MRMLCore for better organization.

## PR-8459: Replace deprecated imp module with importlib to support Python 3.12+
Modernizes Python codebase by replacing deprecated imp module with contemporary importlib alternatives for Python 3.12+ compatibility.

## PR-8461: Replace deprecated assertRegexpMatches with assertRegex to support Python 3.12+
Updates unittest method calls to use assertRegex instead of deprecated assertRegexpMatches for Python 3.12+ support.

## PR-8478: Bump docs dependencies to resolve vulnerability alerts
Updates lxml, pygments, and requests packages to address multiple security vulnerabilities affecting the OpenSSF security scorecard.

## PR-8466: Upgrade from python 3.9.10 to 3.12.10
Major Python upgrade enabling access to features from Python 3.10, 3.11, and 3.12 including pattern matching, enhanced error messages, and new standard library additions.

## PR-8482: Bump doc dependency pygments version to resolve vulnerability
Updates Pygments documentation dependency to resolve security vulnerability PYSEC-2023-117.

## PR-8488: Replace deprecated pydicom API usage
Removes usage of deprecated read_file and write_file functions for compatibility with pydicom 3.0.0+.

## PR-8489: Enforce python 3.12 and newer syntax
Updates Python codebase to enforce Python 3.12+ syntax standards, improving readability and modernizing code.

## PR-8425: Improve tooltip for model nodes in subject hierarchy
Improves tooltip display for model nodes containing unstructured grid data instead of only showing helpful information for poly data.

## PR-8495: Bump docs dependency urllib3 to resolve vulnerability alert
Updates urllib3 dependency to address security advisories GHSA-pq67-6m6q-mj2v and GHSA-48p4-8xcf-vxj5.

## PR-8500: Update teem from r6245 to r7265
Major Teem library update including build system improvements, API updates, CLI enhancements, and over 230 individual changes across the codebase.

## PR-8492: Update JsonCpp from 0.10.6 to 1.9.6
Updates JsonCpp nearly a decade's worth of development work including C++11/C++20 compatibility, improved locale handling, and security improvements.

## PR-8516: Support fixup overrides in app and extension packaging contexts
Introduces CMake variables for specifying additional libraries and custom rpath rules in macOS bundle packaging for both applications and extensions.

## PR-8519: Make JSON files in extensions translatable
Enables internationalization support for JSON files by detecting translatable properties via schema files and extracting strings for translation.

## PR-8527: Update CTK to include PythonQt updates
Updates CTK to incorporate PythonQt improvements addressing Qt 5.15 warnings, Python 3.13 support, memory leaks, and developer tools.

## PR-8538: Add PET support to CreateDICOMSeries CLI
Expands CreateDICOMSeries CLI module to handle PET imaging data in addition to existing DICOM series creation functionality.

## PR-8545: Increase git hook maximum line length from 160 to 180
Updates pre-commit hook maximum line length in anticipation of adopting clang-format with 180 character column limit.

## PR-8427: Add support for building against VTK version 9.5.0
Adds support for VTK 9.5.0 including enforcing C++17 minimum requirements and fixing Windows debug build issues.

## PR-8548: Update Python initialization to use PyConfig API
Modernizes Python initialization by replacing deprecated PySys_SetArgvEx and Py_NoUserSiteDirectory with PyConfig API.

## PR-8544: Update SurfaceToolbox to integrate Dynamic Modeler Revolve tool
Adds Revolve tool enabling users to create 3D models by rotating profiles around axes with adjustable angles and transformations.

## PR-8535: Enable relative import of Slicer Python-wrapped libraries
Enhances fallback mechanism for importing kits to support relative imports when distributed as standalone Python packages.

## PR-8439: Add multi-component handling for vtkMRMLVolumePropertyNode
Introduces JSON storage support and UI controls for handling multiple scalar components in volume rendering with intelligent defaults.

## PR-8588: Avoid changing selected volume rendering component when switching modes
Preserves spinbox value when switching between RGBA and independent component rendering modes.

## PR-8573: Add parameter node GUI connector for qMRMLSubjectHierarchyComboBox
Implements missing parameter node wrapper GUI connector enabling qMRMLSubjectHierarchyComboBox to read/write MRML nodes.

## PR-8607: Add widget to select any node for scene views
Introduces Advanced section in scene views dialog allowing granular control over specific nodes to capture beyond predefined categories.

## PR-8643: Set Windows registry key to use high performance graphics
Adds registry entry during installation to direct Windows to use high-performance GPU by default for better volume rendering.

## PR-8646: Add parameter node GUI connectors
Establishes connections between ctkCheckablePushButton/qSlicerSimpleMarkupsWidget/QDoubleSpinBox/ctkSliderWidget and parameter types.

## PR-8622: Remove unnecessary threshold preview pipeline in unused views
Removes preview pipeline rendering for slice views that aren't visible or lack volume data, eliminating spammy warning messages.

## PR-8435: Add line profile module
Introduces new LineProfile module to compute and visualize intensity profiles along lines or curves in medical images.

## PR-8668: Match color label title font size to legend font size
Ensures title text of color labels scales proportionally with legend text as viewport size changes.

## PR-8669: Restore OpenGL core profile usage on Windows platform
Removes workaround forcing compatibility profile, addressing plot marker rendering issues with Nvidia GPUs.

## PR-8658: Add API to retrieve view displayable managers without Qt widgets
Introduces Qt-independent API for accessing displayable managers to support headless and web-based frontends.

## PR-8666: Split segment editor logic
Extracts business logic from Qt UI framework into new vtkSegmentEditorLogic class for use in non-Qt contexts.

## PR-8697: Make vtkITKImageWriter more robust
Adds heuristics for determining vector voxel types and support for signed char scalar types in color images.

## PR-8678: Update CompareVolumes to include optional return mapping and reuse of layout selection widget from LandmarkRegistration
Adds optional return mapping from view names to volumes and reuses layout selection widget to eliminate code duplication.

## PR-8681: Add keyboard and mouse shortcuts for Module Selector navigation
Enables module switching using mouse back/forward buttons and Alt+Left/Right Arrow keyboard shortcuts.

## PR-8004: Decouple Base, Libs, and Modules/Loadable from app-specific paths via runtime Home/Share in vtkMRMLApplicationLogic
Moves application configuration from compile-time environment variables into vtkMRMLApplicationLogic for runtime configurability and standalone library usage.

## PR-8732: Allow reading/writing of 2 component vector volumes
Extends ITK Image Writer, NRRD Storage, and Volume Archetype Reader to support 2-component vector volumes previously unsupported.

## PR-8731: Add customizable application display name property
Introduces Slicer_MAIN_PROJECT_APPLICATION_DISPLAY_NAME for user-friendly display names separate from internal programmatic names.

## PR-8736: Improve custom sample data download
Adds automatic handling for GitHub/Dropbox links, batch download support, and filename preservation for custom sample data URLs.

## PR-8737: Add volume reorientation to Crop Volume module
Adds reorientation section and Fit to volume alignment modes to help users align cropped volume axes to anatomical directions.

## PR-8739: Make volume rendering transfer function adjustment easier
Enables interactive window/level adjustment in 3D views with mouse gestures and adds Follow Slice Views synchronization option.

## PR-8121: Add TLS authentication support to DICOM Sender and Listener
Introduces DICOMProcessTLSMixin class managing TLS configurations for secure encrypted DICOM communication.

## PR-8757: Add support for storing modeling displacement field transforms
Adds optional displacement field type metadata in NRRD files to distinguish between resampling and modeling transforms.

## PR-8746: Segment Editor: class rename, MRML logic integration, and logging controls
Renames class for consistency, integrates with vtkMRMLAbstractLogic, adds verbosity control, and fixes coordinate regression.

## PR-8762: Save node attributes in volume and transform sequence files
Preserves node attributes when saving sequences in efficient .seq.nrrd format, bringing feature parity with bundle format.

## PR-8772: Add support for reading/writing 2 component sequence files
Extends vtkITK image sequence reader/writer to handle 2-component vector images with comprehensive type-specific support.

## PR-8763: Expose segment editor effect cursor functions
Makes createCursor() callable from Python and exposes setSegmentEditorEffectCursor() for programmatic cursor application.

## PR-8765: Propagate terminology when exporting segments to models
Propagates terminology metadata to exported model nodes enabling downstream consumers to access semantic information.

## PR-8801: Update CTKAppLauncher from 0.1.32 to 33
Updates launcher with automatic splash screen hiding when launched process produces output, with backward compatibility option.

## PR-8802: Show launcher splashscreen until Slicer is started
Extends launcher splash screen to remain visible until application displays its own splash screen, eliminating confusing gap.

## PR-8776: Simplify Slice view removing LightBox feature
Removes LightBox mosaic/contact sheet feature from slice views to eliminate compatibility issues and maintenance burden.

## PR-8803: Update CTK to include PythonQt minimizing commontk fork deltas
Updates CTK with latest PythonQt incorporating Python 3.12 modernization, Qt6 foundation work, and cleanup stability improvements.
