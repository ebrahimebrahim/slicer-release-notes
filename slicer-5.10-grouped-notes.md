#------------------------------------------------------------------------------
# Improvements

* Define a window icon for all windows  ([PR-8186](https://github.com/Slicer/Slicer/pull/8186))
* Support specifying extension contributors as CMake list ([PR-8175](https://github.com/Slicer/Slicer/pull/8175))
* Update BRAINSTools from 2024-05-31 to 2024-11-09 ([PR-8191](https://github.com/Slicer/Slicer/pull/8191))
* Make NSIS Windows installer prettier with application branding  ([PR-8192](https://github.com/Slicer/Slicer/pull/8192))
* Centralize retrieval of Markups Moving attributes in display node ([PR-8173](https://github.com/Slicer/Slicer/pull/8173))
* Add `ctkColorPickerButton` support with `QColor` in `parameterNodeWrapper` ([PR-8195](https://github.com/Slicer/Slicer/pull/8195))
* Generalize internal `qt_root_dir` path ([PR-8219](https://github.com/Slicer/Slicer/pull/8219))
* Update vtkAddon ([PR-8227](https://github.com/Slicer/Slicer/pull/8227))
* Warn when setting volume node with invalid vtkImageData ([PR-8178](https://github.com/Slicer/Slicer/pull/8178))
* Add support for additional NumPy types in `slicer.util.updateTableFromArray` ([PR-8180](https://github.com/Slicer/Slicer/pull/8180))
* Mark SlicerLogic UpdateBlendLayers() & UpdateFractions() helpers as static ([PR-8234](https://github.com/Slicer/Slicer/pull/8234))
* Update vtkAddon anticipating update to VTK >= 9.4 ([PR-8239](https://github.com/Slicer/Slicer/pull/8239))
* Consolidate SliceLogic calls to SetInterpolateTexture ([PR-8232](https://github.com/Slicer/Slicer/pull/8232))
* Remove support for building against VTK <= 9.1 ([PR-8244](https://github.com/Slicer/Slicer/pull/8244))
* Add segment visibility toggle option ([PR-8247](https://github.com/Slicer/Slicer/pull/8247))
* Generalize SliceLogic API introducing "Nth Layer" functions ([PR-8277](https://github.com/Slicer/Slicer/pull/8277))
* Make maximum file length configurable ([PR-8245](https://github.com/Slicer/Slicer/pull/8245))
* Generalize CompositeNode API introducing "Nth Layer" functions ([PR-8278](https://github.com/Slicer/Slicer/pull/8278))
* Refactor vtkMRMLSliceLogic::UpdatePipeline to use "Nth Layer" API ([PR-8279](https://github.com/Slicer/Slicer/pull/8279))
* Generalize CompositeNode "opacity" API introducing "Nth Layer" functions ([PR-8280](https://github.com/Slicer/Slicer/pull/8280))
* Add convenience methods to get/set terminology in segments ([PR-8296](https://github.com/Slicer/Slicer/pull/8296))
* Reduce unnecessary error reporting in segmentation SH ([PR-8299](https://github.com/Slicer/Slicer/pull/8299))
* Select the first suitable node by default in tree views ([PR-8306](https://github.com/Slicer/Slicer/pull/8306))
* Update VTK (vtkMultiVolume bounds computation fix) ([PR-8309](https://github.com/Slicer/Slicer/pull/8309))
* Remove additional code handling VTK support <= 9.1 ([PR-8310](https://github.com/Slicer/Slicer/pull/8310))
* Move singleton declaration from vtkMRMLLayoutNode constructor ([PR-8317](https://github.com/Slicer/Slicer/pull/8317))
* Add CopyContent methods to vtkMRMLLayoutNode and vtkMRMLSequenceBrowserNode ([PR-8318](https://github.com/Slicer/Slicer/pull/8318))
* Update Scene Views to use Sequences ([PR-8303](https://github.com/Slicer/Slicer/pull/8303))
* Add invert colors option to Volumes module ([PR-8341](https://github.com/Slicer/Slicer/pull/8341))
* Add option to hide missing display nodes in sequences ([PR-8354](https://github.com/Slicer/Slicer/pull/8354))
* Add Curved Planar Reformation (CPR) support to GeneralizedReformat ([PR-8148](https://github.com/Slicer/Slicer/pull/8148))
* Make all colors defined by default when setting a LUT  ([PR-8349](https://github.com/Slicer/Slicer/pull/8349))
* Add option to show CLI executable windows on Windows ([PR-8172](https://github.com/Slicer/Slicer/pull/8172))
* Refactor observations in MRML nodes ([PR-8350](https://github.com/Slicer/Slicer/pull/8350))
* Update VTK from 9.2.20230607 to 9.4.2 ([PR-8238](https://github.com/Slicer/Slicer/pull/8238))
* Include slice intersection mouse move info in tooltip ([PR-8392](https://github.com/Slicer/Slicer/pull/8392))
* Select first preferred terminology if no entry is found ([PR-8395](https://github.com/Slicer/Slicer/pull/8395))
* Add functions to update the contents of existing scene views ([PR-8393](https://github.com/Slicer/Slicer/pull/8393))
* Update CTK to add components to ctkVTKVolumePropertyWidget ([PR-8414](https://github.com/Slicer/Slicer/pull/8414))
* Set color picker to use basic colors tab by default ([PR-8416](https://github.com/Slicer/Slicer/pull/8416))
* Remove Slicer mention from Markups save to default display tooltip ([PR-8428](https://github.com/Slicer/Slicer/pull/8428))
* Simplify qSlicerStyle removing obsolete workaround #7418 ([PR-8376](https://github.com/Slicer/Slicer/pull/8376))
* Make it easier to render large volumes on macOS ([PR-8430](https://github.com/Slicer/Slicer/pull/8430))
* Remove old deprecation warning ([PR-8433](https://github.com/Slicer/Slicer/pull/8433))
* Always show context selector in terminology navigator ([PR-8436](https://github.com/Slicer/Slicer/pull/8436))
* Add fast clipping shortcut for volume rendering ([PR-8438](https://github.com/Slicer/Slicer/pull/8438))
* Add dicom instance number in the dataProbe ([PR-8432](https://github.com/Slicer/Slicer/pull/8432))
* Move Markups MRML JSON helper classes to MRMLCore ([PR-8452](https://github.com/Slicer/Slicer/pull/8452))
* Replace deprecated imp module with importlib to support Python 3.12+ ([PR-8459](https://github.com/Slicer/Slicer/pull/8459))
* Replace deprecated assertRegexpMatches with assertRegex to support Python 3.12+ ([PR-8461](https://github.com/Slicer/Slicer/pull/8461))
* Bump docs dependencies to resolve vulnerability alerts ([PR-8478](https://github.com/Slicer/Slicer/pull/8478))
* Upgrade from python 3.9.10 to 3.12.10 ([PR-8466](https://github.com/Slicer/Slicer/pull/8466))
* Bump doc dependency pygments version to resolve vulnerability ([PR-8482](https://github.com/Slicer/Slicer/pull/8482))
* Replace deprecated pydicom API usage ([PR-8488](https://github.com/Slicer/Slicer/pull/8488))
* Enforce python 3.12 and newer syntax ([PR-8489](https://github.com/Slicer/Slicer/pull/8489))
* Improve tooltip for model nodes in subject hierarchy ([PR-8425](https://github.com/Slicer/Slicer/pull/8425))
* Bump docs dependency urllib3 to resolve vulnerability alert ([PR-8495](https://github.com/Slicer/Slicer/pull/8495))
* Update teem from r6245 to r7265 ([PR-8500](https://github.com/Slicer/Slicer/pull/8500))
* Update JsonCpp from 0.10.6 to 1.9.6 ([PR-8492](https://github.com/Slicer/Slicer/pull/8492))
* Support fixup overrides in app and extension packaging contexts ([PR-8516](https://github.com/Slicer/Slicer/pull/8516))
* Make JSON files in extensions translatable ([PR-8519](https://github.com/Slicer/Slicer/pull/8519))
* Update CTK to include PythonQt updates ([PR-8527](https://github.com/Slicer/Slicer/pull/8527))
* Add PET support to CreateDICOMSeries CLI ([PR-8538](https://github.com/Slicer/Slicer/pull/8538))
* Increase git hook maximum line length from 160 to 180 ([PR-8545](https://github.com/Slicer/Slicer/pull/8545))
* Add support for building against VTK version 9.5.0 ([PR-8427](https://github.com/Slicer/Slicer/pull/8427))
* Update Python initialization to use PyConfig API ([PR-8548](https://github.com/Slicer/Slicer/pull/8548))
* Update SurfaceToolbox to integrate Dynamic Modeler Revolve tool ([PR-8544](https://github.com/Slicer/Slicer/pull/8544))
* Enable relative import of Slicer Python-wrapped libraries ([PR-8535](https://github.com/Slicer/Slicer/pull/8535))
* Add multi-component handling for vtkMRMLVolumePropertyNode ([PR-8439](https://github.com/Slicer/Slicer/pull/8439))
* Avoid changing selected volume rendering component when switching modes ([PR-8588](https://github.com/Slicer/Slicer/pull/8588))
* Add parameter node GUI connector for qMRMLSubjectHierarchyComboBox ([PR-8573](https://github.com/Slicer/Slicer/pull/8573))
* Add widget to select any node for scene views ([PR-8607](https://github.com/Slicer/Slicer/pull/8607))
* Set Windows registry key to use high performance graphics ([PR-8643](https://github.com/Slicer/Slicer/pull/8643))
* Add parameter node GUI connectors ([PR-8646](https://github.com/Slicer/Slicer/pull/8646))
* Remove unnecessary threshold preview pipeline in unused views ([PR-8622](https://github.com/Slicer/Slicer/pull/8622))
* Add line profile module ([PR-8435](https://github.com/Slicer/Slicer/pull/8435))
* Match color label title font size to legend font size ([PR-8668](https://github.com/Slicer/Slicer/pull/8668))
* Restore OpenGL core profile usage on Windows platform ([PR-8669](https://github.com/Slicer/Slicer/pull/8669))
* Add API to retrieve view displayable managers without Qt widgets ([PR-8658](https://github.com/Slicer/Slicer/pull/8658))
* Split segment editor logic ([PR-8666](https://github.com/Slicer/Slicer/pull/8666))
* Make vtkITKImageWriter more robust ([PR-8697](https://github.com/Slicer/Slicer/pull/8697))
* Update CompareVolumes to include optional return mapping and reuse of layout selection widget from LandmarkRegistration ([PR-8678](https://github.com/Slicer/Slicer/pull/8678))
* Add keyboard and mouse shortcuts for Module Selector navigation ([PR-8681](https://github.com/Slicer/Slicer/pull/8681))
* Decouple Base, Libs, and Modules/Loadable from app-specific paths via runtime Home/Share in vtkMRMLApplicationLogic ([PR-8004](https://github.com/Slicer/Slicer/pull/8004))
* Allow reading/writing of 2 component vector volumes ([PR-8732](https://github.com/Slicer/Slicer/pull/8732))
* Add customizable application display name property ([PR-8731](https://github.com/Slicer/Slicer/pull/8731))
* Improve custom sample data download ([PR-8736](https://github.com/Slicer/Slicer/pull/8736))
* Add volume reorientation to Crop Volume module ([PR-8737](https://github.com/Slicer/Slicer/pull/8737))
* Make volume rendering transfer function adjustment easier ([PR-8739](https://github.com/Slicer/Slicer/pull/8739))
* Add TLS authentication support to DICOM Sender and Listener ([PR-8121](https://github.com/Slicer/Slicer/pull/8121))
* Add support for storing modeling displacement field transforms ([PR-8757](https://github.com/Slicer/Slicer/pull/8757))
* Segment Editor: class rename, MRML logic integration, and logging controls ([PR-8746](https://github.com/Slicer/Slicer/pull/8746))
* Save node attributes in volume and transform sequence files ([PR-8762](https://github.com/Slicer/Slicer/pull/8762))
* Add support for reading/writing 2 component sequence files ([PR-8772](https://github.com/Slicer/Slicer/pull/8772))
* Expose segment editor effect cursor functions ([PR-8763](https://github.com/Slicer/Slicer/pull/8763))
* Propagate terminology when exporting segments to models ([PR-8765](https://github.com/Slicer/Slicer/pull/8765))
* Update CTKAppLauncher from 0.1.32 to 33 ([PR-8801](https://github.com/Slicer/Slicer/pull/8801))
* Show launcher splashscreen until Slicer is started ([PR-8802](https://github.com/Slicer/Slicer/pull/8802))
* Simplify Slice view removing LightBox feature ([PR-8776](https://github.com/Slicer/Slicer/pull/8776))
* Update CTK to include PythonQt minimizing commontk fork deltas ([PR-8803](https://github.com/Slicer/Slicer/pull/8803))

#------------------------------------------------------------------------------
# Performance

* Improve sequence node storage performance for simple nodes ([PR-8696](https://github.com/Slicer/Slicer/pull/8696))

#------------------------------------------------------------------------------
# Fixes

* Fix duplicated registration of Markups node in tests ([PR-8187](https://github.com/Slicer/Slicer/pull/8187))
* Fix typo in Grow From Seeds help text ([PR-8166](https://github.com/Slicer/Slicer/pull/8166))
* Add cleanup to SegmentEditorEffect ([PR-8199](https://github.com/Slicer/Slicer/pull/8199))
* Fix saving into .mrb with long node names ([PR-8214](https://github.com/Slicer/Slicer/pull/8214))
* Avoid additional error message in DICOMReaders.py ([PR-8215](https://github.com/Slicer/Slicer/pull/8215))
* Fix scene loading warning message ([PR-8216](https://github.com/Slicer/Slicer/pull/8216))
* Fix crash in vtkSlicerApplicationLogic destructor ([PR-8213](https://github.com/Slicer/Slicer/pull/8213))
* Add missing newlines and fix  indentation in `PrintSelf` ([PR-8235](https://github.com/Slicer/Slicer/pull/8235))
* Do not load DWMRI volumes as sequences ([PR-8242](https://github.com/Slicer/Slicer/pull/8242))
* Fix py_UtilTest on Windows ([PR-8252](https://github.com/Slicer/Slicer/pull/8252))
* Fix crash in SystemTools::RemoveADirectory ([PR-8250](https://github.com/Slicer/Slicer/pull/8250))
* Ensure blend pipeline is updated when setting operation Add or Subtract ([PR-8233](https://github.com/Slicer/Slicer/pull/8233))
* Avoid unnecessary error message in UpdateAddSubOperation ([PR-8257](https://github.com/Slicer/Slicer/pull/8257))
* Fix core IO manager initialization ([PR-8287](https://github.com/Slicer/Slicer/pull/8287))
* Fix qSlicerTransformsModuleWidgetTest ([PR-8291](https://github.com/Slicer/Slicer/pull/8291))
* Fix DICOM scene export ([PR-8300](https://github.com/Slicer/Slicer/pull/8300))
* Show the currently selected volume rendering preset name ([PR-8305](https://github.com/Slicer/Slicer/pull/8305))
* Fix 3D view bounds computation with multivolume rendering ([PR-8314](https://github.com/Slicer/Slicer/pull/8314))
* Fix crash in multivolume rendering ([PR-8315](https://github.com/Slicer/Slicer/pull/8315))
* Fix failing py_nomainwindow_* tests ([PR-8331](https://github.com/Slicer/Slicer/pull/8331))
* Fix invalid scene view indexing ([PR-8332](https://github.com/Slicer/Slicer/pull/8332))
* Call Modified if segment display properties changed during copy ([PR-8344](https://github.com/Slicer/Slicer/pull/8344))
* Fixing writing empty color names into ctbl format ([PR-8348](https://github.com/Slicer/Slicer/pull/8348))
* Fix excessive qMRMLSceneViewMenu::resetMenu calls ([PR-8358](https://github.com/Slicer/Slicer/pull/8358))
* Fix crash in vtkSlicerTerminologiesModuleLogic ([PR-8361](https://github.com/Slicer/Slicer/pull/8361))
* Update CTK to fix `ctkDICOMDatabase::fileValue` for non-cached files ([PR-8371](https://github.com/Slicer/Slicer/pull/8371))
* Disable logging of VTK deprecation warnings during Python autocompletion ([PR-8372](https://github.com/Slicer/Slicer/pull/8372))
* Update CTK to ensure robust Python auto-completion anticipating VTK 9.4 ([PR-8380](https://github.com/Slicer/Slicer/pull/8380))
* Fix crash when entering into Transforms module ([PR-8388](https://github.com/Slicer/Slicer/pull/8388))
* Adjust the FieldOfView to match the aspect ratio of the slice dimensions. ([PR-8370](https://github.com/Slicer/Slicer/pull/8370))
* Fix vtkMRMLMarkupsLineNode::GetLineStartPosition crash for empty node ([PR-8412](https://github.com/Slicer/Slicer/pull/8412))
* Fix volume rendering clipping for volumes with negative scalar ([PR-8403](https://github.com/Slicer/Slicer/pull/8403))
* Fix editing color list in picker widget ([PR-8417](https://github.com/Slicer/Slicer/pull/8417))
* Fix editing of segment color ([PR-8424](https://github.com/Slicer/Slicer/pull/8424))
* Restore fallback DICOM SEG upload with alternative storescu config ([PR-8401](https://github.com/Slicer/Slicer/pull/8401))
* Fix incorrect expected warnings in vtkMRMLAnnotationSceneTest ([PR-8437](https://github.com/Slicer/Slicer/pull/8437))
* Do not attempt to import obsolete qSlicerBaseQTCLIPython module ([PR-8480](https://github.com/Slicer/Slicer/pull/8480))
* Avoid invalid default when retrieving active place node class name ([PR-8487](https://github.com/Slicer/Slicer/pull/8487))
* Make color table csv file reading more robust ([PR-8472](https://github.com/Slicer/Slicer/pull/8472))
* Update CTK to improve ctkAxesWidget styling and support CMake 4+ ([PR-8493](https://github.com/Slicer/Slicer/pull/8493))
* Fix invalid typing usage in parameter node following pyupgrade ([PR-8494](https://github.com/Slicer/Slicer/pull/8494))
* Ensure deepcopy is propagated in vtkMRMLSequenceBrowserNode::CopyContent ([PR-8515](https://github.com/Slicer/Slicer/pull/8515))
* Fix runtime loading of JsonCpp library from build tree on Windows ([PR-8532](https://github.com/Slicer/Slicer/pull/8532))
* Prevent WindowLevelPreset duplication in volume display node ([PR-8542](https://github.com/Slicer/Slicer/pull/8542))
* Incorrect number of arguments given when weightAdjustment was desired. ([PR-8552](https://github.com/Slicer/Slicer/pull/8552))
* Fix reordering of subject hierarchy nodes ([PR-8422](https://github.com/Slicer/Slicer/pull/8422))
* Fix incorrect QDir assignment introduced during refactoring ([PR-8581](https://github.com/Slicer/Slicer/pull/8581))
* Fix improper Python initialization causing inconsistent interpreter state ([PR-8582](https://github.com/Slicer/Slicer/pull/8582))
* Select first component when RGBA volume rendering is selected ([PR-8587](https://github.com/Slicer/Slicer/pull/8587))
* Fix crashes caused by range-based loops over temporary Qt containers ([PR-8589](https://github.com/Slicer/Slicer/pull/8589))
* Add missing return from WriteVolumePropertyNode ([PR-8592](https://github.com/Slicer/Slicer/pull/8592))
* Add krb5-gssapi-stub to avoid GSSAPI runtime linkage issues on Linux ([PR-8598](https://github.com/Slicer/Slicer/pull/8598))
* Fix qMRMLNodeAttributeTableViewTest reintroducing empty QString init ([PR-8602](https://github.com/Slicer/Slicer/pull/8602))
* Fix system git invocation in GSSAPI stub builds and generalize executable wrapper ([PR-8613](https://github.com/Slicer/Slicer/pull/8613))
* Update CompareVolumes to fix Hot Link selection issue ([PR-8614](https://github.com/Slicer/Slicer/pull/8614))
* Fix invalid node type in GetViewNodeClasses() ([PR-8615](https://github.com/Slicer/Slicer/pull/8615))
* Make node type labels translatable ([PR-8091](https://github.com/Slicer/Slicer/pull/8091))
* Fix removal of dash characters from exported segmentation filename ([PR-8617](https://github.com/Slicer/Slicer/pull/8617))
* Replace u8‑prefixed unit suffix literals with narrow strings ([PR-8610](https://github.com/Slicer/Slicer/pull/8610))
* Avoid cursor jump on edit in extension LineEdit ([PR-8621](https://github.com/Slicer/Slicer/pull/8621))
* Initialize environment from launcher before Python to fix macOS startup ([PR-8632](https://github.com/Slicer/Slicer/pull/8632))
* Fix empty volume display histogram group box ([PR-8630](https://github.com/Slicer/Slicer/pull/8630))
* Ensure MRMLApplicationLogic is initialized in all modules, fix Colors ([PR-8644](https://github.com/Slicer/Slicer/pull/8644))
* Fix Windows graphics preference not set when installing app with admin privileges ([PR-8645](https://github.com/Slicer/Slicer/pull/8645))
* Drop unneeded nsl and nis dependencies to resolve libtirpc symbol error ([PR-8649](https://github.com/Slicer/Slicer/pull/8649))
* Restore https download on macOS fixing packaging of SSL python modules ([PR-8654](https://github.com/Slicer/Slicer/pull/8654))
* Fix traceback using line profile on 2D image ([PR-8657](https://github.com/Slicer/Slicer/pull/8657))
* Fix not returning GUI tag after connection ([PR-8667](https://github.com/Slicer/Slicer/pull/8667))
* Update CTK to ensure VTK views are always up-to-date ([PR-8672](https://github.com/Slicer/Slicer/pull/8672))
* Show all referenced series as checkboxes in DICOM popup ([PR-8605](https://github.com/Slicer/Slicer/pull/8605))
* Fix VTK errors drawing line profile plot with undefined points ([PR-8677](https://github.com/Slicer/Slicer/pull/8677))
* Fixed hidden slice edges kept appearing in 3D views ([PR-8684](https://github.com/Slicer/Slicer/pull/8684))
* Fix automatic conversion of annotation nodes ([PR-8686](https://github.com/Slicer/Slicer/pull/8686))
* Fix py_nomainwindow_test_slicer_parameter_node_wrapper_guis test ([PR-8687](https://github.com/Slicer/Slicer/pull/8687))
* Improve scene view storage and conversion, fix model visibility issues ([PR-8693](https://github.com/Slicer/Slicer/pull/8693))
* Suppress unnecessary warning for hidden subject hierarchy items ([PR-8695](https://github.com/Slicer/Slicer/pull/8695))
* Fix crash in vtkSegmentation::CollapseBinaryLabelmaps ([PR-8700](https://github.com/Slicer/Slicer/pull/8700))
* Prevent crash on SH reparent without displayable node ([PR-8701](https://github.com/Slicer/Slicer/pull/8701))
* Use UVW layer opacities when building the UVW blending pipeline ([PR-8711](https://github.com/Slicer/Slicer/pull/8711))
* Fix loading of multi-file volumes in SampleData module ([PR-8710](https://github.com/Slicer/Slicer/pull/8710))
* Fix ReverseAlpha compositing inverting opacities not layers ([PR-8712](https://github.com/Slicer/Slicer/pull/8712))
* Fix Add/Subtract compositing clobbering background input ([PR-8709](https://github.com/Slicer/Slicer/pull/8709))
* Update SampleData test for multi-file volume loading behavior ([PR-8713](https://github.com/Slicer/Slicer/pull/8713))
* Improve error reporting and fix Color module tests ([PR-8717](https://github.com/Slicer/Slicer/pull/8717))
* Manage correctly row deletion in qMRMLSubjectHierarchyCombobox ([PR-8692](https://github.com/Slicer/Slicer/pull/8692))
* Fix MIP and MinIP VolumeRendering with SSAO render pass ([PR-8719](https://github.com/Slicer/Slicer/pull/8719))
* Fix Undo/Redo in the segment editor logic ([PR-8722](https://github.com/Slicer/Slicer/pull/8722))
* Fix reading of vector volumes ([PR-8718](https://github.com/Slicer/Slicer/pull/8718))
* Make DICOMProcess init cooperative so TLS mixin is initialized ([PR-8751](https://github.com/Slicer/Slicer/pull/8751))
* Preserve `sys.path` during Slicer module discovery & add startup test ([PR-8727](https://github.com/Slicer/Slicer/pull/8727))
* Delete IO options when using native file dialog to prevent leak ([PR-8753](https://github.com/Slicer/Slicer/pull/8753))
* Fix geometry initialization from empty segmentation file ([PR-8761](https://github.com/Slicer/Slicer/pull/8761))
* Do not reset markups control points when reading XML attributes ([PR-8748](https://github.com/Slicer/Slicer/pull/8748))
* Fixed cloning of composite transforms ([PR-8768](https://github.com/Slicer/Slicer/pull/8768))
* Make mrb file loading more robust ([PR-8771](https://github.com/Slicer/Slicer/pull/8771))
* Clear existing node references before parsing new ones ([PR-8749](https://github.com/Slicer/Slicer/pull/8749))
* childwidgetvariables do not return an object with an empty attribute ([PR-8775](https://github.com/Slicer/Slicer/pull/8775))
* Fix OpenGL error at startup in debug mode ([PR-8795](https://github.com/Slicer/Slicer/pull/8795))
* Fix loading of orientation marker and fonts ([PR-8800](https://github.com/Slicer/Slicer/pull/8800))
* Ensure launcher splash-screen gets hidden on app restart ([PR-8808](https://github.com/Slicer/Slicer/pull/8808))
* Update CTK to fix AUTOMOC DCMTK/Python clash and chart refresh ([PR-8823](https://github.com/Slicer/Slicer/pull/8823))
* Fix Line Profile issues showing multiple lines ([PR-8809](https://github.com/Slicer/Slicer/pull/8809))
* Update VTK to include vtkSurfaceNets3D fix for orientation consistency ([PR-8831](https://github.com/Slicer/Slicer/pull/8831))

#------------------------------------------------------------------------------
# Documentation

* Fix links to slicer doxygen in the developer guide ([PR-8171](https://github.com/Slicer/Slicer/pull/8171))
* Dynamically generate links to slicer doxygen based on ReadTheDocs version ([PR-8176](https://github.com/Slicer/Slicer/pull/8176))
* Fix various broken documentation links in developer guide ([PR-8179](https://github.com/Slicer/Slicer/pull/8179))
* Add documentation for help menu ([PR-8169](https://github.com/Slicer/Slicer/pull/8169))
* Update Transforms module API documentation adding missing Doxygen links ([PR-8185](https://github.com/Slicer/Slicer/pull/8185))
* Update vtkMRMLSliceCompositeNode and vtkMRMLSliceLogic to use doxygen grouping markers ([PR-8231](https://github.com/Slicer/Slicer/pull/8231))
* Update BlendPipeline comment to correctly depict pipeline ([PR-8236](https://github.com/Slicer/Slicer/pull/8236))
* Remove obsolete comment from vtkMRMLSliceLogic::UpdatePipeline ([PR-8237](https://github.com/Slicer/Slicer/pull/8237))
* Improve or add comments in vtkMRMLSliceLogic::UpdatePipeline ([PR-8243](https://github.com/Slicer/Slicer/pull/8243))
* Add ambient shadows section to documentation ([PR-8304](https://github.com/Slicer/Slicer/pull/8304))
* Update model maker documentation ([PR-8313](https://github.com/Slicer/Slicer/pull/8313))
* Moved 2 modules to match application module selector ([PR-8335](https://github.com/Slicer/Slicer/pull/8335))
* Remove link to wiki from list of modules ([PR-8338](https://github.com/Slicer/Slicer/pull/8338))
* Update build instructions to warn users about CMake 4 incompatibility ([PR-8381](https://github.com/Slicer/Slicer/pull/8381))
* Fix VTK coding conventions dead link ([PR-8445](https://github.com/Slicer/Slicer/pull/8445))
* Fix entry in "Script repository / Segmentations" ([PR-8511](https://github.com/Slicer/Slicer/pull/8511))
* Add DOI and dynamic citation count badges for Slicer reference paper ([PR-8561](https://github.com/Slicer/Slicer/pull/8561))
* Fix build instructions updating Qt installer URLS for macOS and Linux ([PR-8593](https://github.com/Slicer/Slicer/pull/8593))
* Add Ubuntu 25.04 build instructions and GSS/Kerberos workaround ([PR-8634](https://github.com/Slicer/Slicer/pull/8634))
* Fix broken links to the PolySeg paper ([PR-8639](https://github.com/Slicer/Slicer/pull/8639))
* Remove warning section for libtirpc GSS/Kerberos symbol lookup error ([PR-8652](https://github.com/Slicer/Slicer/pull/8652))
* Add dedicated GOVERNANCE document and reference it from the about page ([PR-8656](https://github.com/Slicer/Slicer/pull/8656))
* Reference "Code of Conduct" in Governance section and Update contribution processes ([PR-8661](https://github.com/Slicer/Slicer/pull/8661))
* Support GitHub-style alerts in documentation and improve CONTRIBUTING document formatting ([PR-8662](https://github.com/Slicer/Slicer/pull/8662))
* Fix segmentation oversampling snippet in script repository ([PR-8679](https://github.com/Slicer/Slicer/pull/8679))
* Add Fedora 37+ launch troubleshooting ([PR-7114](https://github.com/Slicer/Slicer/pull/7114))
* Add top-level "Extensions" page ([PR-8453](https://github.com/Slicer/Slicer/pull/8453))
* Warn about uncommon volume format options ([PR-8756](https://github.com/Slicer/Slicer/pull/8756))
* Add "Slicer integration in hospital/PACS context" to DICOM module docs ([PR-8786](https://github.com/Slicer/Slicer/pull/8786))
* Document the new .vp.json volume property file format ([PR-8791](https://github.com/Slicer/Slicer/pull/8791))

#------------------------------------------------------------------------------
# Style

* Remove obsolete Qt4 code ([PR-8322](https://github.com/Slicer/Slicer/pull/8322))
* Remove executable permission from non-script text files ([PR-8540](https://github.com/Slicer/Slicer/pull/8540))
* Consistent formatting and indentation of C++ sources ([PR-7603](https://github.com/Slicer/Slicer/pull/7603))
* Update .git-blame-ignore-revs with recent style and compatibility commits ([PR-8566](https://github.com/Slicer/Slicer/pull/8566))
* Explain static_cast use in Qt event handling ([PR-8563](https://github.com/Slicer/Slicer/pull/8563))
* Normalize qualifier order ([PR-8586](https://github.com/Slicer/Slicer/pull/8586))
* Normalize insertion of braces after control statements ([PR-8671](https://github.com/Slicer/Slicer/pull/8671))
* Update to use .hxx instead of .txx for tooling ([PR-8741](https://github.com/Slicer/Slicer/pull/8741))

#------------------------------------------------------------------------------
# Compilation

* Update python-cmake-buildsystem anticipating python version update ([PR-8165](https://github.com/Slicer/Slicer/pull/8165))
* Move classes from Modules/Loadable/Markups/MRML to Libs/MRML/Core ([PR-8155](https://github.com/Slicer/Slicer/pull/8155))
* Update VTK backporting fix to support building on Linux with clang ([PR-8183](https://github.com/Slicer/Slicer/pull/8183))
* Ensure setting `run_ctest_with_upload` to `FALSE` skips package upload ([PR-8170](https://github.com/Slicer/Slicer/pull/8170))
* Improve compatibility with ITK_LEGACY_REMOVE flag  ([PR-8105](https://github.com/Slicer/Slicer/pull/8105))
* Use std::thread instead of deprecated ITK threading functions ([PR-8194](https://github.com/Slicer/Slicer/pull/8194))
* Update BRAINSTools to fix macOS build ([PR-8197](https://github.com/Slicer/Slicer/pull/8197))
* Fix Windows build errors by explicitly including `Windows.h` ([PR-8196](https://github.com/Slicer/Slicer/pull/8196))
* Update external project to support externally built TBB libraries ([PR-8202](https://github.com/Slicer/Slicer/pull/8202))
* Fix -Winconsistent-missing-override in `vtkMRMLMarkupsROINode` ([PR-8218](https://github.com/Slicer/Slicer/pull/8218))
* Improve system Qt detection on Debian usr-merge and multiarch systems ([PR-8111](https://github.com/Slicer/Slicer/pull/8111))
* Fix Windows build error by explicitly including Windows.h ([PR-8292](https://github.com/Slicer/Slicer/pull/8292))
* Exclude dependabot and pre-commit pull requests from changelog ([PR-8293](https://github.com/Slicer/Slicer/pull/8293))
* Make vtkSlicerTerminologiesModuleLogic API backward compatible ([PR-8326](https://github.com/Slicer/Slicer/pull/8326))
* Fix warning due to missing return path ([PR-8340](https://github.com/Slicer/Slicer/pull/8340))
* Update ITK to 5.4.3 ([PR-8339](https://github.com/Slicer/Slicer/pull/8339))
* Update build-system to support forcing extension revision ([PR-6378](https://github.com/Slicer/Slicer/pull/6378))
* Make build fail with meaningful error message with CMake 4 ([PR-8383](https://github.com/Slicer/Slicer/pull/8383))
* Update LandmarkRegistration module to latest ([PR-8390](https://github.com/Slicer/Slicer/pull/8390))
* Update vtkAddon to fix wrapping error reported when using VTK 9.5 ([PR-8429](https://github.com/Slicer/Slicer/pull/8429))
* Update CTK to fix build when using VTK 9.5 ([PR-8431](https://github.com/Slicer/Slicer/pull/8431))
* Add documentation for building Slicer on Ubuntu 24.04, remove obsolete instructions for Ubuntu 20.04 ([PR-8444](https://github.com/Slicer/Slicer/pull/8444))
* Update python-cmake-buildsystem anticipating python version update ([PR-8454](https://github.com/Slicer/Slicer/pull/8454))
* Update python packages to latest ([PR-8455](https://github.com/Slicer/Slicer/pull/8455))
* Modernize integration of VTK build with Python site-packages ([PR-8457](https://github.com/Slicer/Slicer/pull/8457))
* Remove unused Qt includes in vtkMRMLSequenceStorageNode.cxx ([PR-8462](https://github.com/Slicer/Slicer/pull/8462))
* Remove unused logic includes from CropVolume module ([PR-8465](https://github.com/Slicer/Slicer/pull/8465))
* Update python-cmake-buildsystem anticipating python version update ([PR-8467](https://github.com/Slicer/Slicer/pull/8467))
* Move unreferenced node cleanup methods from MRMLLogic to MRMLScene  ([PR-8470](https://github.com/Slicer/Slicer/pull/8470))
* Move vtkSlicerCLIModuleLogic from Base/QTCLI to Base/Logic ([PR-8464](https://github.com/Slicer/Slicer/pull/8464))
* Remove obsolete includes from vtkSlicerApplicationLogic ([PR-8476](https://github.com/Slicer/Slicer/pull/8476))
* Fix macOS build removing obsolete VTK wrapping of qSlicerBaseQTCLI ([PR-8475](https://github.com/Slicer/Slicer/pull/8475))
* Update python-cmake-buildsystem anticipating python version update ([PR-8479](https://github.com/Slicer/Slicer/pull/8479))
* Make vtkSlicerTerminologiesModuleLogic API backward compatible ([PR-8484](https://github.com/Slicer/Slicer/pull/8484))
* Update teem to fix windows build ([PR-8503](https://github.com/Slicer/Slicer/pull/8503))
* Update RapidJSON to latest revision ([PR-8502](https://github.com/Slicer/Slicer/pull/8502))
* Update minimum required CMake version from 3.16.3 to 3.20.6 ([PR-8501](https://github.com/Slicer/Slicer/pull/8501))
* Fix configuration on Windows by updating RapidJSON project installation ([PR-8508](https://github.com/Slicer/Slicer/pull/8508))
* Fix unsigned comparison & unused variable compiler warnings ([PR-8497](https://github.com/Slicer/Slicer/pull/8497))
* Fix deprecated declarations related to vtkStdString ([PR-8509](https://github.com/Slicer/Slicer/pull/8509))
* OpenSSL 1.1.1w is needed to fix missing include ([PR-8504](https://github.com/Slicer/Slicer/pull/8504))
* Fix OpenSSL 1.1.1w build on macOS with non-system zlib ([PR-8513](https://github.com/Slicer/Slicer/pull/8513))
* Fix unused variable warning in qMRMLSortFilterColorProxyModel ([PR-8510](https://github.com/Slicer/Slicer/pull/8510))
* Update JsonCpp to skip installation of object files ([PR-8517](https://github.com/Slicer/Slicer/pull/8517))
* Replace WIN32 with _WIN32 in VTK and ITK-related code ([PR-8521](https://github.com/Slicer/Slicer/pull/8521))
* Update SimpleITK to 2.5.2 and corresponding dependencies ([PR-8522](https://github.com/Slicer/Slicer/pull/8522))
* Fix return type of extraPythonScriptProcessedArgumentsCount property ([PR-8523](https://github.com/Slicer/Slicer/pull/8523))
* Update MultiVolumeExplorer version for excluding Qt4 support ([PR-8528](https://github.com/Slicer/Slicer/pull/8528))
* Update BRAINSTools to fix CMake warning due to version mismatch ([PR-8529](https://github.com/Slicer/Slicer/pull/8529))
* Ensure correct handling of maximum representable double values ([PR-8550](https://github.com/Slicer/Slicer/pull/8550))
* Remove redundant Slicer_HAVE_QT5 definitions ([PR-8554](https://github.com/Slicer/Slicer/pull/8554))
* QObject must be listed first in multiple inheritance ([PR-8556](https://github.com/Slicer/Slicer/pull/8556))
* Replace `fabs` with `std::abs` for consistency in types ([PR-8551](https://github.com/Slicer/Slicer/pull/8551))
* `showViewContextMenuActionsForItem` as `override` ([PR-8553](https://github.com/Slicer/Slicer/pull/8553))
* Refactor QDir assignment to use setPath for consistency ([PR-8558](https://github.com/Slicer/Slicer/pull/8558))
*  Fix variable name closet->closest ([PR-8560](https://github.com/Slicer/Slicer/pull/8560))
* Revert removal of redundant Slicer_HAVE_QT5 definitions ([PR-8562](https://github.com/Slicer/Slicer/pull/8562))
* Remove obsolete Qt version checks related to Qt4 ([PR-8570](https://github.com/Slicer/Slicer/pull/8570))
* Update CTK with PythonQt wrapping support for Qt 5.15 ([PR-8572](https://github.com/Slicer/Slicer/pull/8572))
* signed vs unsigned compiler warning ([PR-8574](https://github.com/Slicer/Slicer/pull/8574))
* Ensure `isPythonDisabled` is defined regardless of Python support ([PR-8577](https://github.com/Slicer/Slicer/pull/8577))
* Prefer c++11 range for to Qt macros ([PR-8580](https://github.com/Slicer/Slicer/pull/8580))
* Update bzip2 from 1.0.8 to 1.1.0 to resolve CMake deprecation issues ([PR-8595](https://github.com/Slicer/Slicer/pull/8595))
* Update LibArchive from 3.6.1 to 3.8.1 to resolve CMake deprecation issues ([PR-8594](https://github.com/Slicer/Slicer/pull/8594))
* Switch from zlib 1.2.3 to maintained zlib-ng 2.2.4 fork ([PR-8597](https://github.com/Slicer/Slicer/pull/8597))
* Update VTK with vtkAxisActor2D tick and label position fix ([PR-8636](https://github.com/Slicer/Slicer/pull/8636))
* Update CTKAppLauncherLib and CTKAPPLAUNCHER ([PR-8629](https://github.com/Slicer/Slicer/pull/8629))
* Always enable CLI support and remove Slicer_BUILD_CLI_SUPPORT option ([PR-8633](https://github.com/Slicer/Slicer/pull/8633))
* Fix Windows build error in debug mode due to python312_d.lib ([PR-8651](https://github.com/Slicer/Slicer/pull/8651))
* Replace deprecated use of TestBigEndian CMake module ([PR-8650](https://github.com/Slicer/Slicer/pull/8650))
* Remove unneeded setting of WORDS_BIGENDIAN/WORDS_LITTLEENDIAN macros ([PR-8653](https://github.com/Slicer/Slicer/pull/8653))
* Fix linux build errors ([PR-8665](https://github.com/Slicer/Slicer/pull/8665))
* Fix pattern for excluding bots from auto-generated changelog ([PR-8673](https://github.com/Slicer/Slicer/pull/8673))
* Update VTK to 9.5.1 ([PR-8683](https://github.com/Slicer/Slicer/pull/8683))
* Ensure BUILD_JOB_SERVER_AWARE is set for external projects ([PR-8691](https://github.com/Slicer/Slicer/pull/8691))
* Set BUILD_JOB_SERVER_AWARE for extension ExternalProject on CMake ≥ 3.28 ([PR-8702](https://github.com/Slicer/Slicer/pull/8702))
* Fix quoting of BUILD_JOB_SERVER_AWARE in extension ExternalProject ([PR-8704](https://github.com/Slicer/Slicer/pull/8704))
* Update VTK to 9.5.2 ([PR-8733](https://github.com/Slicer/Slicer/pull/8733))
* Enable building with CMake 4 ([PR-8740](https://github.com/Slicer/Slicer/pull/8740))
* Fix compiler warnings unused variables/missing enumerations ([PR-8743](https://github.com/Slicer/Slicer/pull/8743))
* Update FindVcvars from v1.8 to v1.12 ([PR-8744](https://github.com/Slicer/Slicer/pull/8744))
* Update CTK and align MOC include names with Qt AUTOMOC convention ([PR-8813](https://github.com/Slicer/Slicer/pull/8813))
* Qt AUTOGEN migration: enable AUTOUIC, AUTORCC, AUTOMOC across Slicer ([PR-8814](https://github.com/Slicer/Slicer/pull/8814))
* Update CTK to modernize PythonQt integration ([PR-8817](https://github.com/Slicer/Slicer/pull/8817))
* Fix AUTOUIC include dir for multi-config generators ([PR-8818](https://github.com/Slicer/Slicer/pull/8818))
* Update CTK to fix PythonQt build ensuring Qt DIR is passed ([PR-8824](https://github.com/Slicer/Slicer/pull/8824))
* Add support for Visual Studio 2026 ([PR-8742](https://github.com/Slicer/Slicer/pull/8742))
* Update CTK to include changes for Qt5/Qt6 compatibility ([PR-8833](https://github.com/Slicer/Slicer/pull/8833))
* Reduce threshold determining use of response file with AUTOMOC ([PR-8834](https://github.com/Slicer/Slicer/pull/8834))
* Require Qt XmlPatterns only when QtTesting is enabled ([PR-8835](https://github.com/Slicer/Slicer/pull/8835))

#------------------------------------------------------------------------------
# Uncategorized

<!-- Release notes generated using configuration in .github/release.yml at v5.10.0 -->

## What's Changed
* Use subject hierarchy tree as node selector in Volumes, Volume Rendering, Segmentations, Transforms modules ([PR-8119](https://github.com/Slicer/Slicer/pull/8119))
* Remove support for obsolete OpenGL VTK backend ([PR-8249](https://github.com/Slicer/Slicer/pull/8249))
* Add support for managing and blending arbitrary number of layers in Slice viewer ([PR-8210](https://github.com/Slicer/Slicer/pull/8210))
* Store and edit terminologies in color table nodes ([PR-8112](https://github.com/Slicer/Slicer/pull/8112))
* Color table terminology fixes ([PR-8297](https://github.com/Slicer/Slicer/pull/8297))
* Add reset ambient shading options ([PR-8337](https://github.com/Slicer/Slicer/pull/8337))
* Improve histogram display in Volumes module ([PR-8342](https://github.com/Slicer/Slicer/pull/8342))
* Reduce warnings during legacy scene load ([PR-8357](https://github.com/Slicer/Slicer/pull/8357))
* Fix hardening of inverted composite transform ([PR-8365](https://github.com/Slicer/Slicer/pull/8365))
* A collection of traceback fixes in automated tests ([PR-8423](https://github.com/Slicer/Slicer/pull/8423))
* Update transforms.md ([PR-8534](https://github.com/Slicer/Slicer/pull/8534))
* Improvements to default node usage across different node creation methods ([PR-8420](https://github.com/Slicer/Slicer/pull/8420))
* Volume sequence IO 5D ([PR-8391](https://github.com/Slicer/Slicer/pull/8391))

## New Contributors
* @sadhana-r made their first contribution ([PR-8171](https://github.com/Slicer/Slicer/pull/8171))
* @sbelsk made their first contribution ([PR-8179](https://github.com/Slicer/Slicer/pull/8179))
* @chime167 made their first contribution ([PR-8166](https://github.com/Slicer/Slicer/pull/8166))
* @tom-osika made their first contribution ([PR-8199](https://github.com/Slicer/Slicer/pull/8199))
* @nlbucki made their first contribution ([PR-8313](https://github.com/Slicer/Slicer/pull/8313))
* @AlexyPellegrini made their first contribution ([PR-8238](https://github.com/Slicer/Slicer/pull/8238))
* @SebGoll made their first contribution ([PR-8390](https://github.com/Slicer/Slicer/pull/8390))
* @PereGinebra made their first contribution ([PR-8401](https://github.com/Slicer/Slicer/pull/8401))
* @finetjul made their first contribution ([PR-8445](https://github.com/Slicer/Slicer/pull/8445))
* @bramton made their first contribution ([PR-8511](https://github.com/Slicer/Slicer/pull/8511))
* @kovalev0 made their first contribution ([PR-8610](https://github.com/Slicer/Slicer/pull/8610))
* @petk made their first contribution ([PR-8650](https://github.com/Slicer/Slicer/pull/8650))
* @deepakri201 made their first contribution ([PR-8605](https://github.com/Slicer/Slicer/pull/8605))
* @ruffsl made their first contribution ([PR-8681](https://github.com/Slicer/Slicer/pull/8681))
* @Villafruela made their first contribution ([PR-7114](https://github.com/Slicer/Slicer/pull/7114))
* @ThomasKierski made their first contribution ([PR-8763](https://github.com/Slicer/Slicer/pull/8763))

**Full Changelog**: https://github.com/Slicer/Slicer/compare/v5.8.1...v5.10.0

#------------------------------------------------------------------------------
# slicerbot

* Update Slicer.crt CA bundle ([PR-8207](https://github.com/Slicer/Slicer/pull/8207))
* Update Slicer.crt CA bundle ([PR-8400](https://github.com/Slicer/Slicer/pull/8400))
* Update Slicer.crt CA bundle ([PR-8485](https://github.com/Slicer/Slicer/pull/8485))
* Update Slicer.crt CA bundle ([PR-8539](https://github.com/Slicer/Slicer/pull/8539))

#------------------------------------------------------------------------------
# slicer-app


#------------------------------------------------------------------------------
# dependabot



## Extensions

### Extensions added
* SlicerHeadCTDeid
  - URL: https://github.com/payabvashlab/SlicerHeadCTDeid
  - Category: Utilities
  - Tier: 1
* ClassAnnotation
  - URL: https://github.com/lorenaromeo/SlicerClassAnnotation.git
  - Category: Utilities
  - Tier: 3
* SlicerTelemetry
* DenseCorrespondenceAnalysis
  - URL: https://github.com/SlicerMorph/SlicerDenseCorrespondenceAnalysis.git
  - Category: SlicerMorph
  - Tier: 3
* ModalityConverter
  - URL: https://github.com/ciroraggio/SlicerModalityConverter.git
  - Category: Image Synthesis
  - Tier: 3
* CADSWholeBodyCTSeg
  - URL: https://github.com/murong-xu/SlicerCADSWholeBodyCTSeg
  - Category: Segmentation
  - Tier: 1
* SlicerOpenLIFU
  - URL: https://github.com/OpenwaterHealth/SlicerOpenLIFU.git
  - Category: Utilities
  - Tier: 1
* LayerDisplayableManager
  - URL: https://github.com/KitwareMedical/SlicerLayerDisplayableManager
  - Category: Developer Tools
  - Tier: 5
* DBSCoalignment
  - URL: https://github.com/IVarha/SlicerDBSCoalignment.git
  - Category: Netstim
  - Tier: 1
* UpperAirwaySegmentator
  - URL: https://github.com/capenaka/SlicerUpperAirwaySegmentator
  - Category: Segmentation
  - Tier: 1
* IGSpineDeformity
  - URL: https://github.com/SenonETS/SlicerIGSpineDeformity.git
  - Category: IGT
* SPECTRecon
  - URL: https://github.com/PyTomography/SlicerSPECTRecon.git
  - Category: Tomographic Reconstruction
* ASLtoolkit
  - URL: https://github.com/LOAMRI/Slicer-ASLtoolkit.git
  - Category: Neuroimaging
* AnatomyCarve
  - URL: https://github.com/andrey-titov/SlicerAnatomyCarve.git
  - Category: Rendering
  - Tier: 1
* SlicerANTsPy
  - URL: https://github.com/SlicerMorph/SlicerANTsPy.git
  - Category: Registration
  - Tier: 3
* SlicerMultiverSeg
  - URL: https://github.com/dalcalab/SlicerMultiverSeg
  - Category: Segmentation
  - Tier: 3
* NeuroStrip
  - URL: https://github.com/dyollb/SlicerNeuroStrip
  - Category: Segmentation
  - Tier: 1
* Trame
* RadioembolizationDosimetry
  - URL: https://github.com/4burakfe/SlicerRadioembolizationDosimetry
  - Category: Nuclear Medicine
  - Tier: 1
* SlicerOrbitSurgerySim
  - URL: https://github.com/chz31/SlicerOrbitSurgerySim
  - Category: Planning
  - Tier: 3
* nnInteractiveSlicer
* EVARSim
  - URL: https://github.com/rwic/SlicerEVARSim
  - Category: Modeling
  - Tier: 1

### Extensions renamed
* SlicerNNInteractive -> nnInteractive
* nnInteractive -> NNInteractive
* SlicerTelemetry -> Telemetry
* SlicerDTIALPS -> DTI-ALPS
* Trame -> SlicerTrame
* nnInteractiveSlicer -> SlicerNNInteractive

### Extensions removed
* SlicerWMA
