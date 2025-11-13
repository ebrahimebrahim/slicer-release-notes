#------------------------------------------------------------------------------
# Improvements

* Define a window icon for all windows  by @jamesobutler in https://github.com/Slicer/Slicer/pull/8186
* Support specifying extension contributors as CMake list by @sbelsk in https://github.com/Slicer/Slicer/pull/8175
* Update BRAINSTools from 2024-05-31 to 2024-11-09 by @jcfr in https://github.com/Slicer/Slicer/pull/8191
* Make NSIS Windows installer prettier with application branding  by @jamesobutler in https://github.com/Slicer/Slicer/pull/8192
* Centralize retrieval of Markups Moving attributes in display node by @jadh4v in https://github.com/Slicer/Slicer/pull/8173
* Add `ctkColorPickerButton` support with `QColor` in `parameterNodeWrapper` by @sjh26 in https://github.com/Slicer/Slicer/pull/8195
* Generalize internal `qt_root_dir` path by @RafaelPalomar in https://github.com/Slicer/Slicer/pull/8219
* Update vtkAddon by @jcfr in https://github.com/Slicer/Slicer/pull/8227
* Warn when setting volume node with invalid vtkImageData by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/8178
* Add support for additional NumPy types in `slicer.util.updateTableFromArray` by @jadh4v in https://github.com/Slicer/Slicer/pull/8180
* Mark SlicerLogic UpdateBlendLayers() & UpdateFractions() helpers as static by @jcfr in https://github.com/Slicer/Slicer/pull/8234
* Update vtkAddon anticipating update to VTK >= 9.4 by @jcfr in https://github.com/Slicer/Slicer/pull/8239
* Consolidate SliceLogic calls to SetInterpolateTexture by @jcfr in https://github.com/Slicer/Slicer/pull/8232
* Remove support for building against VTK <= 9.1 by @jcfr in https://github.com/Slicer/Slicer/pull/8244
* Add segment visibility toggle option by @fedorov in https://github.com/Slicer/Slicer/pull/8247
* Generalize SliceLogic API introducing "Nth Layer" functions by @jcfr in https://github.com/Slicer/Slicer/pull/8277
* Make maximum file length configurable by @lassoan in https://github.com/Slicer/Slicer/pull/8245
* Generalize CompositeNode API introducing "Nth Layer" functions by @jcfr in https://github.com/Slicer/Slicer/pull/8278
* Refactor vtkMRMLSliceLogic::UpdatePipeline to use "Nth Layer" API by @jcfr in https://github.com/Slicer/Slicer/pull/8279
* Generalize CompositeNode "opacity" API introducing "Nth Layer" functions by @jcfr in https://github.com/Slicer/Slicer/pull/8280
* Add convenience methods to get/set terminology in segments by @lassoan in https://github.com/Slicer/Slicer/pull/8296
* Reduce unnecessary error reporting in segmentation SH by @cpinter in https://github.com/Slicer/Slicer/pull/8299
* Select the first suitable node by default in tree views by @lassoan in https://github.com/Slicer/Slicer/pull/8306
* Update VTK (vtkMultiVolume bounds computation fix) by @dzenanz in https://github.com/Slicer/Slicer/pull/8309
* Remove additional code handling VTK support <= 9.1 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8310
* Move singleton declaration from vtkMRMLLayoutNode constructor by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8317
* Add CopyContent methods to vtkMRMLLayoutNode and vtkMRMLSequenceBrowserNode by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8318
* Update Scene Views to use Sequences by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8303
* Add invert colors option to Volumes module by @lassoan in https://github.com/Slicer/Slicer/pull/8341
* Add option to hide missing display nodes in sequences by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8354
* Add Curved Planar Reformation (CPR) support to GeneralizedReformat by @Leengit in https://github.com/Slicer/Slicer/pull/8148
* Make all colors defined by default when setting a LUT  by @lassoan in https://github.com/Slicer/Slicer/pull/8349
* Add option to show CLI executable windows on Windows by @cutun in https://github.com/Slicer/Slicer/pull/8172
* Refactor observations in MRML nodes by @lassoan in https://github.com/Slicer/Slicer/pull/8350
* Update VTK from 9.2.20230607 to 9.4.2 by @AlexyPellegrini in https://github.com/Slicer/Slicer/pull/8238
* Include slice intersection mouse move info in tooltip by @jamesobutler in https://github.com/Slicer/Slicer/pull/8392
* Select first preferred terminology if no entry is found by @cpinter in https://github.com/Slicer/Slicer/pull/8395
* Add functions to update the contents of existing scene views by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8393
* Update CTK to add components to ctkVTKVolumePropertyWidget by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8414
* Set color picker to use basic colors tab by default by @jamesobutler in https://github.com/Slicer/Slicer/pull/8416
* Remove Slicer mention from Markups save to default display tooltip by @jamesobutler in https://github.com/Slicer/Slicer/pull/8428
* Simplify qSlicerStyle removing obsolete workaround #7418 by @cutun in https://github.com/Slicer/Slicer/pull/8376
* Make it easier to render large volumes on macOS by @lassoan in https://github.com/Slicer/Slicer/pull/8430
* Remove old deprecation warning by @jamesobutler in https://github.com/Slicer/Slicer/pull/8433
* Always show context selector in terminology navigator by @lassoan in https://github.com/Slicer/Slicer/pull/8436
* Add fast clipping shortcut for volume rendering by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8438
* Add dicom instance number in the dataProbe by @Punzo in https://github.com/Slicer/Slicer/pull/8432
* Move Markups MRML JSON helper classes to MRMLCore by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8452
* Replace deprecated imp module with importlib to support Python 3.12+ by @jcfr in https://github.com/Slicer/Slicer/pull/8459
* Replace deprecated assertRegexpMatches with assertRegex to support Python 3.12+ by @jcfr in https://github.com/Slicer/Slicer/pull/8461
* Bump docs dependencies to resolve vulnerability alerts by @jamesobutler in https://github.com/Slicer/Slicer/pull/8478
* Upgrade from python 3.9.10 to 3.12.10 by @jcfr in https://github.com/Slicer/Slicer/pull/8466
* Bump doc dependency pygments version to resolve vulnerability by @jamesobutler in https://github.com/Slicer/Slicer/pull/8482
* Replace deprecated pydicom API usage by @jamesobutler in https://github.com/Slicer/Slicer/pull/8488
* Enforce python 3.12 and newer syntax by @jamesobutler in https://github.com/Slicer/Slicer/pull/8489
* Improve tooltip for model nodes in subject hierarchy by @cpinter in https://github.com/Slicer/Slicer/pull/8425
* Bump docs dependency urllib3 to resolve vulnerability alert by @jamesobutler in https://github.com/Slicer/Slicer/pull/8495
* Update teem from r6245 to r7265 by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8500
* Update JsonCpp from 0.10.6 to 1.9.6 by @jcfr in https://github.com/Slicer/Slicer/pull/8492
* Support fixup overrides in app and extension packaging contexts by @jcfr in https://github.com/Slicer/Slicer/pull/8516
* Make JSON files in extensions translatable by @lassoan in https://github.com/Slicer/Slicer/pull/8519
* Update CTK to include PythonQt updates by @jcfr in https://github.com/Slicer/Slicer/pull/8527
* Add PET support to CreateDICOMSeries CLI by @cpinter in https://github.com/Slicer/Slicer/pull/8538
* Increase git hook maximum line length from 160 to 180 by @jcfr in https://github.com/Slicer/Slicer/pull/8545
* Add support for building against VTK version 9.5.0 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8427
* Update Python initialization to use PyConfig API by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8548
* Update SurfaceToolbox to integrate Dynamic Modeler Revolve tool by @mauigna06 in https://github.com/Slicer/Slicer/pull/8544
* Enable relative import of Slicer Python-wrapped libraries by @Thibault-Pelletier in https://github.com/Slicer/Slicer/pull/8535
* Add multi-component handling for vtkMRMLVolumePropertyNode by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8439
* Avoid changing selected volume rendering component when switching modes by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8588
* Add parameter node GUI connector for qMRMLSubjectHierarchyComboBox by @lassoan in https://github.com/Slicer/Slicer/pull/8573
* Add widget to select any node for scene views by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8607
* Set Windows registry key to use high performance graphics by @jamesobutler in https://github.com/Slicer/Slicer/pull/8643
* Add parameter node GUI connectors by @lassoan in https://github.com/Slicer/Slicer/pull/8646
* Remove unnecessary threshold preview pipeline in unused views by @jamesobutler in https://github.com/Slicer/Slicer/pull/8622
* Add line profile module by @nhjohnston in https://github.com/Slicer/Slicer/pull/8435
* Match color label title font size to legend font size by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8668
* Restore OpenGL core profile usage on Windows platform by @jamesobutler in https://github.com/Slicer/Slicer/pull/8669
* Add API to retrieve view displayable managers without Qt widgets by @jcfr in https://github.com/Slicer/Slicer/pull/8658
* Split segment editor logic by @Thibault-Pelletier in https://github.com/Slicer/Slicer/pull/8666
* Make vtkITKImageWriter more robust by @jcfr in https://github.com/Slicer/Slicer/pull/8697
* Update CompareVolumes to include optional return mapping and reuse of layout selection widget from LandmarkRegistration by @koegl in https://github.com/Slicer/Slicer/pull/8678
* Add keyboard and mouse shortcuts for Module Selector navigation by @ruffsl in https://github.com/Slicer/Slicer/pull/8681
* Decouple Base, Libs, and Modules/Loadable from app-specific paths via runtime Home/Share in vtkMRMLApplicationLogic by @AlexyPellegrini in https://github.com/Slicer/Slicer/pull/8004
* Allow reading/writing of 2 component vector volumes by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8732
* Add customizable application display name property by @jamesobutler in https://github.com/Slicer/Slicer/pull/8731
* Improve custom sample data download by @lassoan in https://github.com/Slicer/Slicer/pull/8736
* Add volume reorientation to Crop Volume module by @lassoan in https://github.com/Slicer/Slicer/pull/8737
* Make volume rendering transfer function adjustment easier by @lassoan in https://github.com/Slicer/Slicer/pull/8739
* Add TLS authentication support to DICOM Sender and Listener by @jcfr in https://github.com/Slicer/Slicer/pull/8121
* Add support for storing modeling displacement field transforms by @lassoan in https://github.com/Slicer/Slicer/pull/8757
* Segment Editor: class rename, MRML logic integration, and logging controls by @Thibault-Pelletier in https://github.com/Slicer/Slicer/pull/8746
* Save node attributes in volume and transform sequence files by @lassoan in https://github.com/Slicer/Slicer/pull/8762
* Add support for reading/writing 2 component sequence files by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8772
* Expose segment editor effect cursor functions by @ThomasKierski in https://github.com/Slicer/Slicer/pull/8763
* Propagate terminology when exporting segments to models by @cpinter in https://github.com/Slicer/Slicer/pull/8765
* Update CTKAppLauncher from 0.1.32 to 33 by @lassoan in https://github.com/Slicer/Slicer/pull/8801
* Show launcher splashscreen until Slicer is started by @lassoan in https://github.com/Slicer/Slicer/pull/8802
* Simplify Slice view removing LightBox feature by @jcfr in https://github.com/Slicer/Slicer/pull/8776
* Update CTK to include PythonQt minimizing commontk fork deltas by @jcfr in https://github.com/Slicer/Slicer/pull/8803

#------------------------------------------------------------------------------
# Performance

* Improve sequence node storage performance for simple nodes by @jcfr in https://github.com/Slicer/Slicer/pull/8696

#------------------------------------------------------------------------------
# Fixes

* Fix duplicated registration of Markups node in tests by @jcfr in https://github.com/Slicer/Slicer/pull/8187
* Fix typo in Grow From Seeds help text by @chime167 in https://github.com/Slicer/Slicer/pull/8166
* Add cleanup to SegmentEditorEffect by @tom-osika in https://github.com/Slicer/Slicer/pull/8199
* Fix saving into .mrb with long node names by @lassoan in https://github.com/Slicer/Slicer/pull/8214
* Avoid additional error message in DICOMReaders.py by @jcfr in https://github.com/Slicer/Slicer/pull/8215
* Fix scene loading warning message by @jcfr in https://github.com/Slicer/Slicer/pull/8216
* Fix crash in vtkSlicerApplicationLogic destructor by @lassoan in https://github.com/Slicer/Slicer/pull/8213
* Add missing newlines and fix  indentation in `PrintSelf` by @jcfr in https://github.com/Slicer/Slicer/pull/8235
* Do not load DWMRI volumes as sequences by @pieper in https://github.com/Slicer/Slicer/pull/8242
* Fix py_UtilTest on Windows by @lassoan in https://github.com/Slicer/Slicer/pull/8252
* Fix crash in SystemTools::RemoveADirectory by @lassoan in https://github.com/Slicer/Slicer/pull/8250
* Ensure blend pipeline is updated when setting operation Add or Subtract by @jcfr in https://github.com/Slicer/Slicer/pull/8233
* Avoid unnecessary error message in UpdateAddSubOperation by @jcfr in https://github.com/Slicer/Slicer/pull/8257
* Fix core IO manager initialization by @jcfr in https://github.com/Slicer/Slicer/pull/8287
* Fix qSlicerTransformsModuleWidgetTest by @lassoan in https://github.com/Slicer/Slicer/pull/8291
* Fix DICOM scene export by @cpinter in https://github.com/Slicer/Slicer/pull/8300
* Show the currently selected volume rendering preset name by @lassoan in https://github.com/Slicer/Slicer/pull/8305
* Fix 3D view bounds computation with multivolume rendering by @lassoan in https://github.com/Slicer/Slicer/pull/8314
* Fix crash in multivolume rendering by @lassoan in https://github.com/Slicer/Slicer/pull/8315
* Fix failing py_nomainwindow_* tests by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8331
* Fix invalid scene view indexing by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8332
* Call Modified if segment display properties changed during copy by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8344
* Fixing writing empty color names into ctbl format by @lassoan in https://github.com/Slicer/Slicer/pull/8348
* Fix excessive qMRMLSceneViewMenu::resetMenu calls by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8358
* Fix crash in vtkSlicerTerminologiesModuleLogic by @lassoan in https://github.com/Slicer/Slicer/pull/8361
* Update CTK to fix `ctkDICOMDatabase::fileValue` for non-cached files by @jcfr in https://github.com/Slicer/Slicer/pull/8371
* Disable logging of VTK deprecation warnings during Python autocompletion by @jcfr in https://github.com/Slicer/Slicer/pull/8372
* Update CTK to ensure robust Python auto-completion anticipating VTK 9.4 by @jcfr in https://github.com/Slicer/Slicer/pull/8380
* Fix crash when entering into Transforms module by @lassoan in https://github.com/Slicer/Slicer/pull/8388
* Adjust the FieldOfView to match the aspect ratio of the slice dimensions. by @Punzo in https://github.com/Slicer/Slicer/pull/8370
* Fix vtkMRMLMarkupsLineNode::GetLineStartPosition crash for empty node by @lassoan in https://github.com/Slicer/Slicer/pull/8412
* Fix volume rendering clipping for volumes with negative scalar by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8403
* Fix editing color list in picker widget by @jamesobutler in https://github.com/Slicer/Slicer/pull/8417
* Fix editing of segment color by @lassoan in https://github.com/Slicer/Slicer/pull/8424
* Restore fallback DICOM SEG upload with alternative storescu config by @PereGinebra in https://github.com/Slicer/Slicer/pull/8401
* Fix incorrect expected warnings in vtkMRMLAnnotationSceneTest by @jamesobutler in https://github.com/Slicer/Slicer/pull/8437
* Do not attempt to import obsolete qSlicerBaseQTCLIPython module by @jcfr in https://github.com/Slicer/Slicer/pull/8480
* Avoid invalid default when retrieving active place node class name by @jcfr in https://github.com/Slicer/Slicer/pull/8487
* Make color table csv file reading more robust by @lassoan in https://github.com/Slicer/Slicer/pull/8472
* Update CTK to improve ctkAxesWidget styling and support CMake 4+ by @jcfr in https://github.com/Slicer/Slicer/pull/8493
* Fix invalid typing usage in parameter node following pyupgrade by @jamesobutler in https://github.com/Slicer/Slicer/pull/8494
* Ensure deepcopy is propagated in vtkMRMLSequenceBrowserNode::CopyContent by @jcfr in https://github.com/Slicer/Slicer/pull/8515
* Fix runtime loading of JsonCpp library from build tree on Windows by @jcfr in https://github.com/Slicer/Slicer/pull/8532
* Prevent WindowLevelPreset duplication in volume display node by @lassoan in https://github.com/Slicer/Slicer/pull/8542
* Incorrect number of arguments given when weightAdjustment was desired. by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8552
* Fix reordering of subject hierarchy nodes by @lassoan in https://github.com/Slicer/Slicer/pull/8422
* Fix incorrect QDir assignment introduced during refactoring by @jcfr in https://github.com/Slicer/Slicer/pull/8581
* Fix improper Python initialization causing inconsistent interpreter state by @jcfr in https://github.com/Slicer/Slicer/pull/8582
* Select first component when RGBA volume rendering is selected by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8587
* Fix crashes caused by range-based loops over temporary Qt containers by @jcfr in https://github.com/Slicer/Slicer/pull/8589
* Add missing return from WriteVolumePropertyNode by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8592
* Add krb5-gssapi-stub to avoid GSSAPI runtime linkage issues on Linux by @jcfr in https://github.com/Slicer/Slicer/pull/8598
* Fix qMRMLNodeAttributeTableViewTest reintroducing empty QString init by @jcfr in https://github.com/Slicer/Slicer/pull/8602
* Fix system git invocation in GSSAPI stub builds and generalize executable wrapper by @jcfr in https://github.com/Slicer/Slicer/pull/8613
* Update CompareVolumes to fix Hot Link selection issue by @koegl in https://github.com/Slicer/Slicer/pull/8614
* Fix invalid node type in GetViewNodeClasses() by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8615
* Make node type labels translatable by @mhdiop in https://github.com/Slicer/Slicer/pull/8091
* Fix removal of dash characters from exported segmentation filename by @lassoan in https://github.com/Slicer/Slicer/pull/8617
* Replace u8‑prefixed unit suffix literals with narrow strings by @kovalev0 in https://github.com/Slicer/Slicer/pull/8610
* Avoid cursor jump on edit in extension LineEdit by @shai-ikko in https://github.com/Slicer/Slicer/pull/8621
* Initialize environment from launcher before Python to fix macOS startup by @jcfr in https://github.com/Slicer/Slicer/pull/8632
* Fix empty volume display histogram group box by @jamesobutler in https://github.com/Slicer/Slicer/pull/8630
* Ensure MRMLApplicationLogic is initialized in all modules, fix Colors by @jcfr in https://github.com/Slicer/Slicer/pull/8644
* Fix Windows graphics preference not set when installing app with admin privileges by @jamesobutler in https://github.com/Slicer/Slicer/pull/8645
* Drop unneeded nsl and nis dependencies to resolve libtirpc symbol error by @jcfr in https://github.com/Slicer/Slicer/pull/8649
* Restore https download on macOS fixing packaging of SSL python modules by @jcfr in https://github.com/Slicer/Slicer/pull/8654
* Fix traceback using line profile on 2D image by @nhjohnston in https://github.com/Slicer/Slicer/pull/8657
* Fix not returning GUI tag after connection by @nhjohnston in https://github.com/Slicer/Slicer/pull/8667
* Update CTK to ensure VTK views are always up-to-date by @jcfr in https://github.com/Slicer/Slicer/pull/8672
* Show all referenced series as checkboxes in DICOM popup by @deepakri201 in https://github.com/Slicer/Slicer/pull/8605
* Fix VTK errors drawing line profile plot with undefined points by @nhjohnston in https://github.com/Slicer/Slicer/pull/8677
* Fixed hidden slice edges kept appearing in 3D views by @lassoan in https://github.com/Slicer/Slicer/pull/8684
* Fix automatic conversion of annotation nodes by @lassoan in https://github.com/Slicer/Slicer/pull/8686
* Fix py_nomainwindow_test_slicer_parameter_node_wrapper_guis test by @lassoan in https://github.com/Slicer/Slicer/pull/8687
* Improve scene view storage and conversion, fix model visibility issues by @lassoan in https://github.com/Slicer/Slicer/pull/8693
* Suppress unnecessary warning for hidden subject hierarchy items by @jamesobutler in https://github.com/Slicer/Slicer/pull/8695
* Fix crash in vtkSegmentation::CollapseBinaryLabelmaps by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8700
* Prevent crash on SH reparent without displayable node by @lassoan in https://github.com/Slicer/Slicer/pull/8701
* Use UVW layer opacities when building the UVW blending pipeline by @jcfr in https://github.com/Slicer/Slicer/pull/8711
* Fix loading of multi-file volumes in SampleData module by @lassoan in https://github.com/Slicer/Slicer/pull/8710
* Fix ReverseAlpha compositing inverting opacities not layers by @jcfr in https://github.com/Slicer/Slicer/pull/8712
* Fix Add/Subtract compositing clobbering background input by @jcfr in https://github.com/Slicer/Slicer/pull/8709
* Update SampleData test for multi-file volume loading behavior by @jcfr in https://github.com/Slicer/Slicer/pull/8713
* Improve error reporting and fix Color module tests by @jcfr in https://github.com/Slicer/Slicer/pull/8717
* Manage correctly row deletion in qMRMLSubjectHierarchyCombobox by @achataigner in https://github.com/Slicer/Slicer/pull/8692
* Fix MIP and MinIP VolumeRendering with SSAO render pass by @Thibault-Pelletier in https://github.com/Slicer/Slicer/pull/8719
* Fix Undo/Redo in the segment editor logic by @Thibault-Pelletier in https://github.com/Slicer/Slicer/pull/8722
* Fix reading of vector volumes by @lassoan in https://github.com/Slicer/Slicer/pull/8718
* Make DICOMProcess init cooperative so TLS mixin is initialized by @jcfr in https://github.com/Slicer/Slicer/pull/8751
* Preserve `sys.path` during Slicer module discovery & add startup test by @RafaelPalomar in https://github.com/Slicer/Slicer/pull/8727
* Delete IO options when using native file dialog to prevent leak by @jcfr in https://github.com/Slicer/Slicer/pull/8753
* Fix geometry initialization from empty segmentation file by @lassoan in https://github.com/Slicer/Slicer/pull/8761
* Do not reset markups control points when reading XML attributes by @Punzo in https://github.com/Slicer/Slicer/pull/8748
* Fixed cloning of composite transforms by @lassoan in https://github.com/Slicer/Slicer/pull/8768
* Make mrb file loading more robust by @lassoan in https://github.com/Slicer/Slicer/pull/8771
* Clear existing node references before parsing new ones by @Punzo in https://github.com/Slicer/Slicer/pull/8749
* childwidgetvariables do not return an object with an empty attribute by @malbi in https://github.com/Slicer/Slicer/pull/8775
* Fix OpenGL error at startup in debug mode by @lassoan in https://github.com/Slicer/Slicer/pull/8795
* Fix loading of orientation marker and fonts by @ruffsl in https://github.com/Slicer/Slicer/pull/8800
* Ensure launcher splash-screen gets hidden on app restart by @lassoan in https://github.com/Slicer/Slicer/pull/8808
* Update CTK to fix AUTOMOC DCMTK/Python clash and chart refresh by @jcfr in https://github.com/Slicer/Slicer/pull/8823
* Fix Line Profile issues showing multiple lines by @lassoan in https://github.com/Slicer/Slicer/pull/8809
* Update VTK to include vtkSurfaceNets3D fix for orientation consistency by @jcfr in https://github.com/Slicer/Slicer/pull/8831

#------------------------------------------------------------------------------
# Documentation

* Fix links to slicer doxygen in the developer guide by @sadhana-r in https://github.com/Slicer/Slicer/pull/8171
* Dynamically generate links to slicer doxygen based on ReadTheDocs version by @sadhana-r in https://github.com/Slicer/Slicer/pull/8176
* Fix various broken documentation links in developer guide by @sbelsk in https://github.com/Slicer/Slicer/pull/8179
* Add documentation for help menu by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/8169
* Update Transforms module API documentation adding missing Doxygen links by @jcfr in https://github.com/Slicer/Slicer/pull/8185
* Update vtkMRMLSliceCompositeNode and vtkMRMLSliceLogic to use doxygen grouping markers by @jcfr in https://github.com/Slicer/Slicer/pull/8231
* Update BlendPipeline comment to correctly depict pipeline by @jcfr in https://github.com/Slicer/Slicer/pull/8236
* Remove obsolete comment from vtkMRMLSliceLogic::UpdatePipeline by @jcfr in https://github.com/Slicer/Slicer/pull/8237
* Improve or add comments in vtkMRMLSliceLogic::UpdatePipeline by @jcfr in https://github.com/Slicer/Slicer/pull/8243
* Add ambient shadows section to documentation by @lassoan in https://github.com/Slicer/Slicer/pull/8304
* Update model maker documentation by @nlbucki in https://github.com/Slicer/Slicer/pull/8313
* Moved 2 modules to match application module selector by @robertf in https://github.com/Slicer/Slicer/pull/8335
* Remove link to wiki from list of modules by @robertf in https://github.com/Slicer/Slicer/pull/8338
* Update build instructions to warn users about CMake 4 incompatibility by @lassoan in https://github.com/Slicer/Slicer/pull/8381
* Fix VTK coding conventions dead link by @finetjul in https://github.com/Slicer/Slicer/pull/8445
* Fix entry in "Script repository / Segmentations" by @bramton in https://github.com/Slicer/Slicer/pull/8511
* Add DOI and dynamic citation count badges for Slicer reference paper by @mauigna06 in https://github.com/Slicer/Slicer/pull/8561
* Fix build instructions updating Qt installer URLS for macOS and Linux by @jcfr in https://github.com/Slicer/Slicer/pull/8593
* Add Ubuntu 25.04 build instructions and GSS/Kerberos workaround by @Punzo in https://github.com/Slicer/Slicer/pull/8634
* Fix broken links to the PolySeg paper by @cpinter in https://github.com/Slicer/Slicer/pull/8639
* Remove warning section for libtirpc GSS/Kerberos symbol lookup error by @Punzo in https://github.com/Slicer/Slicer/pull/8652
* Add dedicated GOVERNANCE document and reference it from the about page by @jcfr in https://github.com/Slicer/Slicer/pull/8656
* Reference "Code of Conduct" in Governance section and Update contribution processes by @jcfr in https://github.com/Slicer/Slicer/pull/8661
* Support GitHub-style alerts in documentation and improve CONTRIBUTING document formatting by @jcfr in https://github.com/Slicer/Slicer/pull/8662
* Fix segmentation oversampling snippet in script repository by @cpinter in https://github.com/Slicer/Slicer/pull/8679
* Add Fedora 37+ launch troubleshooting by @Villafruela in https://github.com/Slicer/Slicer/pull/7114
* Add top-level "Extensions" page by @jcfr in https://github.com/Slicer/Slicer/pull/8453
* Warn about uncommon volume format options by @pieper in https://github.com/Slicer/Slicer/pull/8756
* Add "Slicer integration in hospital/PACS context" to DICOM module docs by @jcfr in https://github.com/Slicer/Slicer/pull/8786
* Document the new .vp.json volume property file format by @lassoan in https://github.com/Slicer/Slicer/pull/8791

#------------------------------------------------------------------------------
# Style

* Remove obsolete Qt4 code by @jamesobutler in https://github.com/Slicer/Slicer/pull/8322
* Remove executable permission from non-script text files by @jcfr in https://github.com/Slicer/Slicer/pull/8540
* Consistent formatting and indentation of C++ sources by @jcfr in https://github.com/Slicer/Slicer/pull/7603
* Update .git-blame-ignore-revs with recent style and compatibility commits by @jcfr in https://github.com/Slicer/Slicer/pull/8566
* Explain static_cast use in Qt event handling by @lassoan in https://github.com/Slicer/Slicer/pull/8563
* Normalize qualifier order by @jcfr in https://github.com/Slicer/Slicer/pull/8586
* Normalize insertion of braces after control statements by @jcfr in https://github.com/Slicer/Slicer/pull/8671
* Update to use .hxx instead of .txx for tooling by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8741

#------------------------------------------------------------------------------
# Compilation

* Update python-cmake-buildsystem anticipating python version update by @jcfr in https://github.com/Slicer/Slicer/pull/8165
* Move classes from Modules/Loadable/Markups/MRML to Libs/MRML/Core by @jcfr in https://github.com/Slicer/Slicer/pull/8155
* Update VTK backporting fix to support building on Linux with clang by @jcfr in https://github.com/Slicer/Slicer/pull/8183
* Ensure setting `run_ctest_with_upload` to `FALSE` skips package upload by @jadh4v in https://github.com/Slicer/Slicer/pull/8170
* Improve compatibility with ITK_LEGACY_REMOVE flag  by @dzenanz in https://github.com/Slicer/Slicer/pull/8105
* Use std::thread instead of deprecated ITK threading functions by @dzenanz in https://github.com/Slicer/Slicer/pull/8194
* Update BRAINSTools to fix macOS build by @jcfr in https://github.com/Slicer/Slicer/pull/8197
* Fix Windows build errors by explicitly including `Windows.h` by @dzenanz in https://github.com/Slicer/Slicer/pull/8196
* Update external project to support externally built TBB libraries by @jcfr in https://github.com/Slicer/Slicer/pull/8202
* Fix -Winconsistent-missing-override in `vtkMRMLMarkupsROINode` by @jcfr in https://github.com/Slicer/Slicer/pull/8218
* Improve system Qt detection on Debian usr-merge and multiarch systems by @RafaelPalomar in https://github.com/Slicer/Slicer/pull/8111
* Fix Windows build error by explicitly including Windows.h by @jamesobutler in https://github.com/Slicer/Slicer/pull/8292
* Exclude dependabot and pre-commit pull requests from changelog by @jcfr in https://github.com/Slicer/Slicer/pull/8293
* Make vtkSlicerTerminologiesModuleLogic API backward compatible by @lassoan in https://github.com/Slicer/Slicer/pull/8326
* Fix warning due to missing return path by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8340
* Update ITK to 5.4.3 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8339
* Update build-system to support forcing extension revision by @jcfr in https://github.com/Slicer/Slicer/pull/6378
* Make build fail with meaningful error message with CMake 4 by @lassoan in https://github.com/Slicer/Slicer/pull/8383
* Update LandmarkRegistration module to latest by @SebGoll in https://github.com/Slicer/Slicer/pull/8390
* Update vtkAddon to fix wrapping error reported when using VTK 9.5 by @jcfr in https://github.com/Slicer/Slicer/pull/8429
* Update CTK to fix build when using VTK 9.5 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8431
* Add documentation for building Slicer on Ubuntu 24.04, remove obsolete instructions for Ubuntu 20.04 by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8444
* Update python-cmake-buildsystem anticipating python version update by @jcfr in https://github.com/Slicer/Slicer/pull/8454
* Update python packages to latest by @jcfr in https://github.com/Slicer/Slicer/pull/8455
* Modernize integration of VTK build with Python site-packages by @jcfr in https://github.com/Slicer/Slicer/pull/8457
* Remove unused Qt includes in vtkMRMLSequenceStorageNode.cxx by @jcfr in https://github.com/Slicer/Slicer/pull/8462
* Remove unused logic includes from CropVolume module by @jcfr in https://github.com/Slicer/Slicer/pull/8465
* Update python-cmake-buildsystem anticipating python version update by @jcfr in https://github.com/Slicer/Slicer/pull/8467
* Move unreferenced node cleanup methods from MRMLLogic to MRMLScene  by @jcfr in https://github.com/Slicer/Slicer/pull/8470
* Move vtkSlicerCLIModuleLogic from Base/QTCLI to Base/Logic by @jcfr in https://github.com/Slicer/Slicer/pull/8464
* Remove obsolete includes from vtkSlicerApplicationLogic by @jcfr in https://github.com/Slicer/Slicer/pull/8476
* Fix macOS build removing obsolete VTK wrapping of qSlicerBaseQTCLI by @jcfr in https://github.com/Slicer/Slicer/pull/8475
* Update python-cmake-buildsystem anticipating python version update by @jcfr in https://github.com/Slicer/Slicer/pull/8479
* Make vtkSlicerTerminologiesModuleLogic API backward compatible by @lassoan in https://github.com/Slicer/Slicer/pull/8484
* Update teem to fix windows build by @jcfr in https://github.com/Slicer/Slicer/pull/8503
* Update RapidJSON to latest revision by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8502
* Update minimum required CMake version from 3.16.3 to 3.20.6 by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8501
* Fix configuration on Windows by updating RapidJSON project installation by @jcfr in https://github.com/Slicer/Slicer/pull/8508
* Fix unsigned comparison & unused variable compiler warnings by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8497
* Fix deprecated declarations related to vtkStdString by @jcfr in https://github.com/Slicer/Slicer/pull/8509
* OpenSSL 1.1.1w is needed to fix missing include by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8504
* Fix OpenSSL 1.1.1w build on macOS with non-system zlib by @jcfr in https://github.com/Slicer/Slicer/pull/8513
* Fix unused variable warning in qMRMLSortFilterColorProxyModel by @jcfr in https://github.com/Slicer/Slicer/pull/8510
* Update JsonCpp to skip installation of object files by @jcfr in https://github.com/Slicer/Slicer/pull/8517
* Replace WIN32 with _WIN32 in VTK and ITK-related code by @Thibault-Pelletier in https://github.com/Slicer/Slicer/pull/8521
* Update SimpleITK to 2.5.2 and corresponding dependencies by @jamesobutler in https://github.com/Slicer/Slicer/pull/8522
* Fix return type of extraPythonScriptProcessedArgumentsCount property by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8523
* Update MultiVolumeExplorer version for excluding Qt4 support by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8528
* Update BRAINSTools to fix CMake warning due to version mismatch by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8529
* Ensure correct handling of maximum representable double values by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8550
* Remove redundant Slicer_HAVE_QT5 definitions by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8554
* QObject must be listed first in multiple inheritance by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8556
* Replace `fabs` with `std::abs` for consistency in types by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8551
* `showViewContextMenuActionsForItem` as `override` by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8553
* Refactor QDir assignment to use setPath for consistency by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8558
*  Fix variable name closet->closest by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8560
* Revert removal of redundant Slicer_HAVE_QT5 definitions by @jcfr in https://github.com/Slicer/Slicer/pull/8562
* Remove obsolete Qt version checks related to Qt4 by @jcfr in https://github.com/Slicer/Slicer/pull/8570
* Update CTK with PythonQt wrapping support for Qt 5.15 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8572
* signed vs unsigned compiler warning by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8574
* Ensure `isPythonDisabled` is defined regardless of Python support by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8577
* Prefer c++11 range for to Qt macros by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8580
* Update bzip2 from 1.0.8 to 1.1.0 to resolve CMake deprecation issues by @jamesobutler in https://github.com/Slicer/Slicer/pull/8595
* Update LibArchive from 3.6.1 to 3.8.1 to resolve CMake deprecation issues by @jcfr in https://github.com/Slicer/Slicer/pull/8594
* Switch from zlib 1.2.3 to maintained zlib-ng 2.2.4 fork by @jcfr in https://github.com/Slicer/Slicer/pull/8597
* Update VTK with vtkAxisActor2D tick and label position fix by @jamesobutler in https://github.com/Slicer/Slicer/pull/8636
* Update CTKAppLauncherLib and CTKAPPLAUNCHER by @jcfr in https://github.com/Slicer/Slicer/pull/8629
* Always enable CLI support and remove Slicer_BUILD_CLI_SUPPORT option by @AlexyPellegrini in https://github.com/Slicer/Slicer/pull/8633
* Fix Windows build error in debug mode due to python312_d.lib by @lassoan in https://github.com/Slicer/Slicer/pull/8651
* Replace deprecated use of TestBigEndian CMake module by @petk in https://github.com/Slicer/Slicer/pull/8650
* Remove unneeded setting of WORDS_BIGENDIAN/WORDS_LITTLEENDIAN macros by @jcfr in https://github.com/Slicer/Slicer/pull/8653
* Fix linux build errors by @lassoan in https://github.com/Slicer/Slicer/pull/8665
* Fix pattern for excluding bots from auto-generated changelog by @jcfr in https://github.com/Slicer/Slicer/pull/8673
* Update VTK to 9.5.1 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8683
* Ensure BUILD_JOB_SERVER_AWARE is set for external projects by @jcfr in https://github.com/Slicer/Slicer/pull/8691
* Set BUILD_JOB_SERVER_AWARE for extension ExternalProject on CMake ≥ 3.28 by @jcfr in https://github.com/Slicer/Slicer/pull/8702
* Fix quoting of BUILD_JOB_SERVER_AWARE in extension ExternalProject by @jcfr in https://github.com/Slicer/Slicer/pull/8704
* Update VTK to 9.5.2 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8733
* Enable building with CMake 4 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8740
* Fix compiler warnings unused variables/missing enumerations by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8743
* Update FindVcvars from v1.8 to v1.12 by @jcfr in https://github.com/Slicer/Slicer/pull/8744
* Update CTK and align MOC include names with Qt AUTOMOC convention by @jcfr in https://github.com/Slicer/Slicer/pull/8813
* Qt AUTOGEN migration: enable AUTOUIC, AUTORCC, AUTOMOC across Slicer by @jcfr in https://github.com/Slicer/Slicer/pull/8814
* Update CTK to modernize PythonQt integration by @jcfr in https://github.com/Slicer/Slicer/pull/8817
* Fix AUTOUIC include dir for multi-config generators by @jcfr in https://github.com/Slicer/Slicer/pull/8818
* Update CTK to fix PythonQt build ensuring Qt DIR is passed by @jcfr in https://github.com/Slicer/Slicer/pull/8824
* Add support for Visual Studio 2026 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8742
* Update CTK to include changes for Qt5/Qt6 compatibility by @jcfr in https://github.com/Slicer/Slicer/pull/8833
* Reduce threshold determining use of response file with AUTOMOC by @jcfr in https://github.com/Slicer/Slicer/pull/8834
* Require Qt XmlPatterns only when QtTesting is enabled by @jcfr in https://github.com/Slicer/Slicer/pull/8835

#------------------------------------------------------------------------------
# Uncategorized

<!-- Release notes generated using configuration in .github/release.yml at v5.10.0 -->

## What's Changed
* Use subject hierarchy tree as node selector in Volumes, Volume Rendering, Segmentations, Transforms modules by @lassoan in https://github.com/Slicer/Slicer/pull/8119
* Remove support for obsolete OpenGL VTK backend by @jcfr in https://github.com/Slicer/Slicer/pull/8249
* Add support for managing and blending arbitrary number of layers in Slice viewer by @jcfr in https://github.com/Slicer/Slicer/pull/8210
* Store and edit terminologies in color table nodes by @cpinter in https://github.com/Slicer/Slicer/pull/8112
* Color table terminology fixes by @lassoan in https://github.com/Slicer/Slicer/pull/8297
* Add reset ambient shading options by @lassoan in https://github.com/Slicer/Slicer/pull/8337
* Improve histogram display in Volumes module by @lassoan in https://github.com/Slicer/Slicer/pull/8342
* Reduce warnings during legacy scene load by @lassoan in https://github.com/Slicer/Slicer/pull/8357
* Fix hardening of inverted composite transform by @lassoan in https://github.com/Slicer/Slicer/pull/8365
* A collection of traceback fixes in automated tests by @jamesobutler in https://github.com/Slicer/Slicer/pull/8423
* Update transforms.md by @lassoan in https://github.com/Slicer/Slicer/pull/8534
* Improvements to default node usage across different node creation methods by @jamesobutler in https://github.com/Slicer/Slicer/pull/8420
* Volume sequence IO 5D by @cpinter in https://github.com/Slicer/Slicer/pull/8391

## New Contributors
* @sadhana-r made their first contribution in https://github.com/Slicer/Slicer/pull/8171
* @sbelsk made their first contribution in https://github.com/Slicer/Slicer/pull/8179
* @chime167 made their first contribution in https://github.com/Slicer/Slicer/pull/8166
* @tom-osika made their first contribution in https://github.com/Slicer/Slicer/pull/8199
* @nlbucki made their first contribution in https://github.com/Slicer/Slicer/pull/8313
* @AlexyPellegrini made their first contribution in https://github.com/Slicer/Slicer/pull/8238
* @SebGoll made their first contribution in https://github.com/Slicer/Slicer/pull/8390
* @PereGinebra made their first contribution in https://github.com/Slicer/Slicer/pull/8401
* @finetjul made their first contribution in https://github.com/Slicer/Slicer/pull/8445
* @bramton made their first contribution in https://github.com/Slicer/Slicer/pull/8511
* @kovalev0 made their first contribution in https://github.com/Slicer/Slicer/pull/8610
* @petk made their first contribution in https://github.com/Slicer/Slicer/pull/8650
* @deepakri201 made their first contribution in https://github.com/Slicer/Slicer/pull/8605
* @ruffsl made their first contribution in https://github.com/Slicer/Slicer/pull/8681
* @Villafruela made their first contribution in https://github.com/Slicer/Slicer/pull/7114
* @ThomasKierski made their first contribution in https://github.com/Slicer/Slicer/pull/8763

**Full Changelog**: https://github.com/Slicer/Slicer/compare/v5.8.1...v5.10.0

#------------------------------------------------------------------------------
# slicerbot

* Update Slicer.crt CA bundle by @slicerbot in https://github.com/Slicer/Slicer/pull/8207
* Update Slicer.crt CA bundle by @slicerbot in https://github.com/Slicer/Slicer/pull/8400
* Update Slicer.crt CA bundle by @slicerbot in https://github.com/Slicer/Slicer/pull/8485
* Update Slicer.crt CA bundle by @slicerbot in https://github.com/Slicer/Slicer/pull/8539

#------------------------------------------------------------------------------
# slicer-app


#------------------------------------------------------------------------------
# dependabot


