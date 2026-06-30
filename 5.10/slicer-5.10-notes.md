<!-- Release notes generated using configuration in .github/release.yml at v5.10.0 -->

## What's Changed
* COMP: Update python-cmake-buildsystem anticipating python version update by @jcfr in https://github.com/Slicer/Slicer/pull/8165
* DOC: Fix links to slicer doxygen in the developer guide by @sadhana-r in https://github.com/Slicer/Slicer/pull/8171
* DOC: Dynamically generate links to slicer doxygen based on ReadTheDocs version by @sadhana-r in https://github.com/Slicer/Slicer/pull/8176
* DOC: Fix various broken documentation links in developer guide by @sbelsk in https://github.com/Slicer/Slicer/pull/8179
* DOC: Add documentation for help menu by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/8169
* COMP: Move classes from Modules/Loadable/Markups/MRML to Libs/MRML/Core by @jcfr in https://github.com/Slicer/Slicer/pull/8155
* COMP: Update VTK backporting fix to support building on Linux with clang by @jcfr in https://github.com/Slicer/Slicer/pull/8183
* DOC: Update Transforms module API documentation adding missing Doxygen links by @jcfr in https://github.com/Slicer/Slicer/pull/8185
* ENH: Define a window icon for all windows  by @jamesobutler in https://github.com/Slicer/Slicer/pull/8186
* BUG: Fix duplicated registration of Markups node in tests by @jcfr in https://github.com/Slicer/Slicer/pull/8187
* BUG: Fix typo in Grow From Seeds help text by @chime167 in https://github.com/Slicer/Slicer/pull/8166
* COMP: Ensure setting `run_ctest_with_upload` to `FALSE` skips package upload by @jadh4v in https://github.com/Slicer/Slicer/pull/8170
* ENH: Support specifying extension contributors as CMake list by @sbelsk in https://github.com/Slicer/Slicer/pull/8175
* ENH: Update BRAINSTools from 2024-05-31 to 2024-11-09 by @jcfr in https://github.com/Slicer/Slicer/pull/8191
* COMP: Improve compatibility with ITK_LEGACY_REMOVE flag  by @dzenanz in https://github.com/Slicer/Slicer/pull/8105
* COMP: Use std::thread instead of deprecated ITK threading functions by @dzenanz in https://github.com/Slicer/Slicer/pull/8194
* COMP: Update BRAINSTools to fix macOS build by @jcfr in https://github.com/Slicer/Slicer/pull/8197
* COMP: Fix Windows build errors by explicitly including `Windows.h` by @dzenanz in https://github.com/Slicer/Slicer/pull/8196
* ENH: Make NSIS Windows installer prettier with application branding  by @jamesobutler in https://github.com/Slicer/Slicer/pull/8192
* ENH: Centralize retrieval of Markups Moving attributes in display node by @jadh4v in https://github.com/Slicer/Slicer/pull/8173
* COMP: Update external project to support externally built TBB libraries by @jcfr in https://github.com/Slicer/Slicer/pull/8202
* Use subject hierarchy tree as node selector in Volumes, Volume Rendering, Segmentations, Transforms modules by @lassoan in https://github.com/Slicer/Slicer/pull/8119
* Update Slicer.crt CA bundle by @slicerbot in https://github.com/Slicer/Slicer/pull/8207
* BUG: Add cleanup to SegmentEditorEffect by @tom-osika in https://github.com/Slicer/Slicer/pull/8199
* BUG: Fix saving into .mrb with long node names by @lassoan in https://github.com/Slicer/Slicer/pull/8214
* BUG: Avoid additional error message in DICOMReaders.py by @jcfr in https://github.com/Slicer/Slicer/pull/8215
* BUG: Fix scene loading warning message by @jcfr in https://github.com/Slicer/Slicer/pull/8216
* COMP: Fix -Winconsistent-missing-override in `vtkMRMLMarkupsROINode` by @jcfr in https://github.com/Slicer/Slicer/pull/8218
* COMP: Improve system Qt detection on Debian usr-merge and multiarch systems by @RafaelPalomar in https://github.com/Slicer/Slicer/pull/8111
* ENH: Add `ctkColorPickerButton` support with `QColor` in `parameterNodeWrapper` by @sjh26 in https://github.com/Slicer/Slicer/pull/8195
* ENH: Generalize internal `qt_root_dir` path by @RafaelPalomar in https://github.com/Slicer/Slicer/pull/8219
* BUG: Fix crash in vtkSlicerApplicationLogic destructor by @lassoan in https://github.com/Slicer/Slicer/pull/8213
* ENH: Update vtkAddon by @jcfr in https://github.com/Slicer/Slicer/pull/8227
* ENH: Warn when setting volume node with invalid vtkImageData by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/8178
* ENH: Add support for additional NumPy types in `slicer.util.updateTableFromArray` by @jadh4v in https://github.com/Slicer/Slicer/pull/8180
* DOC: Update vtkMRMLSliceCompositeNode and vtkMRMLSliceLogic to use doxygen grouping markers by @jcfr in https://github.com/Slicer/Slicer/pull/8231
* BUG: Add missing newlines and fix  indentation in `PrintSelf` by @jcfr in https://github.com/Slicer/Slicer/pull/8235
* ENH: Mark SlicerLogic UpdateBlendLayers() & UpdateFractions() helpers as static by @jcfr in https://github.com/Slicer/Slicer/pull/8234
* DOC: Update BlendPipeline comment to correctly depict pipeline by @jcfr in https://github.com/Slicer/Slicer/pull/8236
* DOC: Remove obsolete comment from vtkMRMLSliceLogic::UpdatePipeline by @jcfr in https://github.com/Slicer/Slicer/pull/8237
* ENH: Update vtkAddon anticipating update to VTK >= 9.4 by @jcfr in https://github.com/Slicer/Slicer/pull/8239
* ENH: Consolidate SliceLogic calls to SetInterpolateTexture by @jcfr in https://github.com/Slicer/Slicer/pull/8232
* DOC: Improve or add comments in vtkMRMLSliceLogic::UpdatePipeline by @jcfr in https://github.com/Slicer/Slicer/pull/8243
* ENH: Remove support for building against VTK <= 9.1 by @jcfr in https://github.com/Slicer/Slicer/pull/8244
* BUG: Do not load DWMRI volumes as sequences by @pieper in https://github.com/Slicer/Slicer/pull/8242
* ENH: Add segment visibility toggle option by @fedorov in https://github.com/Slicer/Slicer/pull/8247
* Remove support for obsolete OpenGL VTK backend by @jcfr in https://github.com/Slicer/Slicer/pull/8249
* BUG: Fix py_UtilTest on Windows by @lassoan in https://github.com/Slicer/Slicer/pull/8252
* BUG: Fix crash in SystemTools::RemoveADirectory by @lassoan in https://github.com/Slicer/Slicer/pull/8250
* BUG: Ensure blend pipeline is updated when setting operation Add or Subtract by @jcfr in https://github.com/Slicer/Slicer/pull/8233
* BUG: Avoid unnecessary error message in UpdateAddSubOperation by @jcfr in https://github.com/Slicer/Slicer/pull/8257
* ENH: Generalize SliceLogic API introducing "Nth Layer" functions by @jcfr in https://github.com/Slicer/Slicer/pull/8277
* ENH: Make maximum file length configurable by @lassoan in https://github.com/Slicer/Slicer/pull/8245
* ENH: Generalize CompositeNode API introducing "Nth Layer" functions by @jcfr in https://github.com/Slicer/Slicer/pull/8278
* ENH: Refactor vtkMRMLSliceLogic::UpdatePipeline to use "Nth Layer" API by @jcfr in https://github.com/Slicer/Slicer/pull/8279
* ENH: Generalize CompositeNode "opacity" API introducing "Nth Layer" functions by @jcfr in https://github.com/Slicer/Slicer/pull/8280
* Add support for managing and blending arbitrary number of layers in Slice viewer by @jcfr in https://github.com/Slicer/Slicer/pull/8210
* BUG: Fix core IO manager initialization by @jcfr in https://github.com/Slicer/Slicer/pull/8287
* COMP: Fix Windows build error by explicitly including Windows.h by @jamesobutler in https://github.com/Slicer/Slicer/pull/8292
* Store and edit terminologies in color table nodes by @cpinter in https://github.com/Slicer/Slicer/pull/8112
* BUG: Fix qSlicerTransformsModuleWidgetTest by @lassoan in https://github.com/Slicer/Slicer/pull/8291
* COMP: Exclude dependabot and pre-commit pull requests from changelog by @jcfr in https://github.com/Slicer/Slicer/pull/8293
* ENH: Add convenience methods to get/set terminology in segments by @lassoan in https://github.com/Slicer/Slicer/pull/8296
* BUG: Fix DICOM scene export by @cpinter in https://github.com/Slicer/Slicer/pull/8300
* ENH: Reduce unnecessary error reporting in segmentation SH by @cpinter in https://github.com/Slicer/Slicer/pull/8299
* DOC: Add ambient shadows section to documentation by @lassoan in https://github.com/Slicer/Slicer/pull/8304
* Color table terminology fixes by @lassoan in https://github.com/Slicer/Slicer/pull/8297
* ENH: Select the first suitable node by default in tree views by @lassoan in https://github.com/Slicer/Slicer/pull/8306
* BUG: Show the currently selected volume rendering preset name by @lassoan in https://github.com/Slicer/Slicer/pull/8305
* ENH: Update VTK (vtkMultiVolume bounds computation fix) by @dzenanz in https://github.com/Slicer/Slicer/pull/8309
* ENH: Remove additional code handling VTK support <= 9.1 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8310
* BUG: Fix 3D view bounds computation with multivolume rendering by @lassoan in https://github.com/Slicer/Slicer/pull/8314
* BUG: Fix crash in multivolume rendering by @lassoan in https://github.com/Slicer/Slicer/pull/8315
* DOC: Update model maker documentation by @nlbucki in https://github.com/Slicer/Slicer/pull/8313
* ENH: Move singleton declaration from vtkMRMLLayoutNode constructor by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8317
* ENH: Add CopyContent methods to vtkMRMLLayoutNode and vtkMRMLSequenceBrowserNode by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8318
* STYLE: Remove obsolete Qt4 code by @jamesobutler in https://github.com/Slicer/Slicer/pull/8322
* ENH: Update Scene Views to use Sequences by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8303
* COMP: Make vtkSlicerTerminologiesModuleLogic API backward compatible by @lassoan in https://github.com/Slicer/Slicer/pull/8326
* BUG: Fix failing py_nomainwindow_* tests by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8331
* BUG: Fix invalid scene view indexing by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8332
* DOC: Moved 2 modules to match application module selector by @robertf in https://github.com/Slicer/Slicer/pull/8335
* Add reset ambient shading options by @lassoan in https://github.com/Slicer/Slicer/pull/8337
* DOC: Remove link to wiki from list of modules by @robertf in https://github.com/Slicer/Slicer/pull/8338
* COMP: Fix warning due to missing return path by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8340
* ENH: Add invert colors option to Volumes module by @lassoan in https://github.com/Slicer/Slicer/pull/8341
* Improve histogram display in Volumes module by @lassoan in https://github.com/Slicer/Slicer/pull/8342
* BUG: Call Modified if segment display properties changed during copy by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8344
* ENH: Add option to hide missing display nodes in sequences by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8354
* BUG: Fixing writing empty color names into ctbl format by @lassoan in https://github.com/Slicer/Slicer/pull/8348
* COMP: Update ITK to 5.4.3 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8339
* ENH: Add Curved Planar Reformation (CPR) support to GeneralizedReformat by @Leengit in https://github.com/Slicer/Slicer/pull/8148
* ENH: Make all colors defined by default when setting a LUT  by @lassoan in https://github.com/Slicer/Slicer/pull/8349
* ENH: Add option to show CLI executable windows on Windows by @cutun in https://github.com/Slicer/Slicer/pull/8172
* COMP: Update build-system to support forcing extension revision by @jcfr in https://github.com/Slicer/Slicer/pull/6378
* BUG: Fix excessive qMRMLSceneViewMenu::resetMenu calls by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8358
* ENH: Refactor observations in MRML nodes by @lassoan in https://github.com/Slicer/Slicer/pull/8350
* Reduce warnings during legacy scene load by @lassoan in https://github.com/Slicer/Slicer/pull/8357
* BUG: Fix crash in vtkSlicerTerminologiesModuleLogic by @lassoan in https://github.com/Slicer/Slicer/pull/8361
* Fix hardening of inverted composite transform by @lassoan in https://github.com/Slicer/Slicer/pull/8365
* BUG: Update CTK to fix `ctkDICOMDatabase::fileValue` for non-cached files by @jcfr in https://github.com/Slicer/Slicer/pull/8371
* BUG: Disable logging of VTK deprecation warnings during Python autocompletion by @jcfr in https://github.com/Slicer/Slicer/pull/8372
* BUG: Update CTK to ensure robust Python auto-completion anticipating VTK 9.4 by @jcfr in https://github.com/Slicer/Slicer/pull/8380
* ENH: Update VTK from 9.2.20230607 to 9.4.2 by @AlexyPellegrini in https://github.com/Slicer/Slicer/pull/8238
* DOC: Update build instructions to warn users about CMake 4 incompatibility by @lassoan in https://github.com/Slicer/Slicer/pull/8381
* COMP: Make build fail with meaningful error message with CMake 4 by @lassoan in https://github.com/Slicer/Slicer/pull/8383
* BUG: Fix crash when entering into Transforms module by @lassoan in https://github.com/Slicer/Slicer/pull/8388
* ENH: Include slice intersection mouse move info in tooltip by @jamesobutler in https://github.com/Slicer/Slicer/pull/8392
* ENH: Select first preferred terminology if no entry is found by @cpinter in https://github.com/Slicer/Slicer/pull/8395
* BUG: Adjust the FieldOfView to match the aspect ratio of the slice dimensions. by @Punzo in https://github.com/Slicer/Slicer/pull/8370
* Update Slicer.crt CA bundle by @slicerbot in https://github.com/Slicer/Slicer/pull/8400
* ENH: Add functions to update the contents of existing scene views by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8393
* BUG: Fix vtkMRMLMarkupsLineNode::GetLineStartPosition crash for empty node by @lassoan in https://github.com/Slicer/Slicer/pull/8412
* BUG: Fix volume rendering clipping for volumes with negative scalar by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8403
* ENH: Update CTK to add components to ctkVTKVolumePropertyWidget by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8414
* BUG: Fix editing color list in picker widget by @jamesobutler in https://github.com/Slicer/Slicer/pull/8417
* ENH: Set color picker to use basic colors tab by default by @jamesobutler in https://github.com/Slicer/Slicer/pull/8416
* COMP: Update LandmarkRegistration module to latest by @SebGoll in https://github.com/Slicer/Slicer/pull/8390
* A collection of traceback fixes in automated tests by @jamesobutler in https://github.com/Slicer/Slicer/pull/8423
* ENH: Remove Slicer mention from Markups save to default display tooltip by @jamesobutler in https://github.com/Slicer/Slicer/pull/8428
* BUG: Fix editing of segment color by @lassoan in https://github.com/Slicer/Slicer/pull/8424
* COMP: Update vtkAddon to fix wrapping error reported when using VTK 9.5 by @jcfr in https://github.com/Slicer/Slicer/pull/8429
* BUG: Restore fallback DICOM SEG upload with alternative storescu config by @PereGinebra in https://github.com/Slicer/Slicer/pull/8401
* COMP: Update CTK to fix build when using VTK 9.5 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8431
* ENH: Simplify qSlicerStyle removing obsolete workaround #7418 by @cutun in https://github.com/Slicer/Slicer/pull/8376
* ENH: Make it easier to render large volumes on macOS by @lassoan in https://github.com/Slicer/Slicer/pull/8430
* ENH: Remove old deprecation warning by @jamesobutler in https://github.com/Slicer/Slicer/pull/8433
* ENH: Always show context selector in terminology navigator by @lassoan in https://github.com/Slicer/Slicer/pull/8436
* BUG: Fix incorrect expected warnings in vtkMRMLAnnotationSceneTest by @jamesobutler in https://github.com/Slicer/Slicer/pull/8437
* DOC: Fix VTK coding conventions dead link by @finetjul in https://github.com/Slicer/Slicer/pull/8445
* COMP: Add documentation for building Slicer on Ubuntu 24.04, remove obsolete instructions for Ubuntu 20.04 by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8444
* ENH: Add fast clipping shortcut for volume rendering by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8438
* ENH: Add dicom instance number in the dataProbe by @Punzo in https://github.com/Slicer/Slicer/pull/8432
* COMP: Update python-cmake-buildsystem anticipating python version update by @jcfr in https://github.com/Slicer/Slicer/pull/8454
* COMP: Update python packages to latest by @jcfr in https://github.com/Slicer/Slicer/pull/8455
* ENH: Move Markups MRML JSON helper classes to MRMLCore by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8452
* COMP: Modernize integration of VTK build with Python site-packages by @jcfr in https://github.com/Slicer/Slicer/pull/8457
* ENH: Replace deprecated imp module with importlib to support Python 3.12+ by @jcfr in https://github.com/Slicer/Slicer/pull/8459
* ENH: Replace deprecated assertRegexpMatches with assertRegex to support Python 3.12+ by @jcfr in https://github.com/Slicer/Slicer/pull/8461
* COMP: Remove unused Qt includes in vtkMRMLSequenceStorageNode.cxx by @jcfr in https://github.com/Slicer/Slicer/pull/8462
* COMP: Remove unused logic includes from CropVolume module by @jcfr in https://github.com/Slicer/Slicer/pull/8465
* COMP: Update python-cmake-buildsystem anticipating python version update by @jcfr in https://github.com/Slicer/Slicer/pull/8467
* COMP: Move unreferenced node cleanup methods from MRMLLogic to MRMLScene  by @jcfr in https://github.com/Slicer/Slicer/pull/8470
* COMP: Move vtkSlicerCLIModuleLogic from Base/QTCLI to Base/Logic by @jcfr in https://github.com/Slicer/Slicer/pull/8464
* COMP: Remove obsolete includes from vtkSlicerApplicationLogic by @jcfr in https://github.com/Slicer/Slicer/pull/8476
* COMP: Fix macOS build removing obsolete VTK wrapping of qSlicerBaseQTCLI by @jcfr in https://github.com/Slicer/Slicer/pull/8475
* ENH: Bump docs dependencies to resolve vulnerability alerts by @jamesobutler in https://github.com/Slicer/Slicer/pull/8478
* COMP: Update python-cmake-buildsystem anticipating python version update by @jcfr in https://github.com/Slicer/Slicer/pull/8479
* BUG: Do not attempt to import obsolete qSlicerBaseQTCLIPython module by @jcfr in https://github.com/Slicer/Slicer/pull/8480
* ENH: Upgrade from python 3.9.10 to 3.12.10 by @jcfr in https://github.com/Slicer/Slicer/pull/8466
* ENH: Bump doc dependency pygments version to resolve vulnerability by @jamesobutler in https://github.com/Slicer/Slicer/pull/8482
* COMP: Make vtkSlicerTerminologiesModuleLogic API backward compatible by @lassoan in https://github.com/Slicer/Slicer/pull/8484
* Update Slicer.crt CA bundle by @slicerbot in https://github.com/Slicer/Slicer/pull/8485
* BUG: Avoid invalid default when retrieving active place node class name by @jcfr in https://github.com/Slicer/Slicer/pull/8487
* ENH: Replace deprecated pydicom API usage by @jamesobutler in https://github.com/Slicer/Slicer/pull/8488
* ENH: Enforce python 3.12 and newer syntax by @jamesobutler in https://github.com/Slicer/Slicer/pull/8489
* BUG: Make color table csv file reading more robust by @lassoan in https://github.com/Slicer/Slicer/pull/8472
* ENH: Improve tooltip for model nodes in subject hierarchy by @cpinter in https://github.com/Slicer/Slicer/pull/8425
* BUG: Update CTK to improve ctkAxesWidget styling and support CMake 4+ by @jcfr in https://github.com/Slicer/Slicer/pull/8493
* ENH: Bump docs dependency urllib3 to resolve vulnerability alert by @jamesobutler in https://github.com/Slicer/Slicer/pull/8495
* BUG: Fix invalid typing usage in parameter node following pyupgrade by @jamesobutler in https://github.com/Slicer/Slicer/pull/8494
* ENH: Update teem from r6245 to r7265 by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8500
* ENH: Update JsonCpp from 0.10.6 to 1.9.6 by @jcfr in https://github.com/Slicer/Slicer/pull/8492
* COMP: Update teem to fix windows build by @jcfr in https://github.com/Slicer/Slicer/pull/8503
* COMP: Update RapidJSON to latest revision by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8502
* COMP: Update minimum required CMake version from 3.16.3 to 3.20.6 by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8501
* COMP: Fix configuration on Windows by updating RapidJSON project installation by @jcfr in https://github.com/Slicer/Slicer/pull/8508
* COMP: Fix unsigned comparison & unused variable compiler warnings by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8497
* COMP: Fix deprecated declarations related to vtkStdString by @jcfr in https://github.com/Slicer/Slicer/pull/8509
* COMP: OpenSSL 1.1.1w is needed to fix missing include by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8504
* DOC: Fix entry in "Script repository / Segmentations" by @bramton in https://github.com/Slicer/Slicer/pull/8511
* COMP: Fix OpenSSL 1.1.1w build on macOS with non-system zlib by @jcfr in https://github.com/Slicer/Slicer/pull/8513
* BUG: Ensure deepcopy is propagated in vtkMRMLSequenceBrowserNode::CopyContent by @jcfr in https://github.com/Slicer/Slicer/pull/8515
* COMP: Fix unused variable warning in qMRMLSortFilterColorProxyModel by @jcfr in https://github.com/Slicer/Slicer/pull/8510
* COMP: Update JsonCpp to skip installation of object files by @jcfr in https://github.com/Slicer/Slicer/pull/8517
* ENH: Support fixup overrides in app and extension packaging contexts by @jcfr in https://github.com/Slicer/Slicer/pull/8516
* ENH: Make JSON files in extensions translatable by @lassoan in https://github.com/Slicer/Slicer/pull/8519
* COMP: Replace WIN32 with _WIN32 in VTK and ITK-related code by @Thibault-Pelletier in https://github.com/Slicer/Slicer/pull/8521
* COMP: Update SimpleITK to 2.5.2 and corresponding dependencies by @jamesobutler in https://github.com/Slicer/Slicer/pull/8522
* COMP: Fix return type of extraPythonScriptProcessedArgumentsCount property by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8523
* ENH: Update CTK to include PythonQt updates by @jcfr in https://github.com/Slicer/Slicer/pull/8527
* COMP: Update MultiVolumeExplorer version for excluding Qt4 support by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8528
* COMP: Update BRAINSTools to fix CMake warning due to version mismatch by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8529
* BUG: Fix runtime loading of JsonCpp library from build tree on Windows by @jcfr in https://github.com/Slicer/Slicer/pull/8532
* Update transforms.md by @lassoan in https://github.com/Slicer/Slicer/pull/8534
* Update Slicer.crt CA bundle by @slicerbot in https://github.com/Slicer/Slicer/pull/8539
* STYLE: Remove executable permission from non-script text files by @jcfr in https://github.com/Slicer/Slicer/pull/8540
* BUG: Prevent WindowLevelPreset duplication in volume display node by @lassoan in https://github.com/Slicer/Slicer/pull/8542
* ENH: Add PET support to CreateDICOMSeries CLI by @cpinter in https://github.com/Slicer/Slicer/pull/8538
* ENH: Increase git hook maximum line length from 160 to 180 by @jcfr in https://github.com/Slicer/Slicer/pull/8545
* ENH: Add support for building against VTK version 9.5.0 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8427
* STYLE: Consistent formatting and indentation of C++ sources by @jcfr in https://github.com/Slicer/Slicer/pull/7603
* COMP: Ensure correct handling of maximum representable double values by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8550
* COMP: Remove redundant Slicer_HAVE_QT5 definitions by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8554
* COMP: QObject must be listed first in multiple inheritance by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8556
* ENH: Update Python initialization to use PyConfig API by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8548
* COMP: Replace `fabs` with `std::abs` for consistency in types by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8551
* COMP: `showViewContextMenuActionsForItem` as `override` by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8553
* COMP: Refactor QDir assignment to use setPath for consistency by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8558
* COMP:  Fix variable name closet->closest by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8560
* COMP: Revert removal of redundant Slicer_HAVE_QT5 definitions by @jcfr in https://github.com/Slicer/Slicer/pull/8562
* STYLE: Update .git-blame-ignore-revs with recent style and compatibility commits by @jcfr in https://github.com/Slicer/Slicer/pull/8566
* STYLE: Explain static_cast use in Qt event handling by @lassoan in https://github.com/Slicer/Slicer/pull/8563
* DOC: Add DOI and dynamic citation count badges for Slicer reference paper by @mauigna06 in https://github.com/Slicer/Slicer/pull/8561
* BUG: Incorrect number of arguments given when weightAdjustment was desired. by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8552
* ENH: Update SurfaceToolbox to integrate Dynamic Modeler Revolve tool by @mauigna06 in https://github.com/Slicer/Slicer/pull/8544
* COMP: Remove obsolete Qt version checks related to Qt4 by @jcfr in https://github.com/Slicer/Slicer/pull/8570
* COMP: Update CTK with PythonQt wrapping support for Qt 5.15 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8572
* ENH: Enable relative import of Slicer Python-wrapped libraries by @Thibault-Pelletier in https://github.com/Slicer/Slicer/pull/8535
* BUG: Fix reordering of subject hierarchy nodes by @lassoan in https://github.com/Slicer/Slicer/pull/8422
* ENH: Add multi-component handling for vtkMRMLVolumePropertyNode by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8439
* COMP: signed vs unsigned compiler warning by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8574
* COMP: Ensure `isPythonDisabled` is defined regardless of Python support by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8577
* BUG: Fix incorrect QDir assignment introduced during refactoring by @jcfr in https://github.com/Slicer/Slicer/pull/8581
* COMP: Prefer c++11 range for to Qt macros by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8580
* BUG: Fix improper Python initialization causing inconsistent interpreter state by @jcfr in https://github.com/Slicer/Slicer/pull/8582
* STYLE: Normalize qualifier order by @jcfr in https://github.com/Slicer/Slicer/pull/8586
* BUG: Select first component when RGBA volume rendering is selected by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8587
* ENH: Avoid changing selected volume rendering component when switching modes by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8588
* BUG: Fix crashes caused by range-based loops over temporary Qt containers by @jcfr in https://github.com/Slicer/Slicer/pull/8589
* BUG: Add missing return from WriteVolumePropertyNode by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8592
* DOC: Fix build instructions updating Qt installer URLS for macOS and Linux by @jcfr in https://github.com/Slicer/Slicer/pull/8593
* COMP: Update bzip2 from 1.0.8 to 1.1.0 to resolve CMake deprecation issues by @jamesobutler in https://github.com/Slicer/Slicer/pull/8595
* COMP: Update LibArchive from 3.6.1 to 3.8.1 to resolve CMake deprecation issues by @jcfr in https://github.com/Slicer/Slicer/pull/8594
* COMP: Switch from zlib 1.2.3 to maintained zlib-ng 2.2.4 fork by @jcfr in https://github.com/Slicer/Slicer/pull/8597
* ENH: Add parameter node GUI connector for qMRMLSubjectHierarchyComboBox by @lassoan in https://github.com/Slicer/Slicer/pull/8573
* BUG: Add krb5-gssapi-stub to avoid GSSAPI runtime linkage issues on Linux by @jcfr in https://github.com/Slicer/Slicer/pull/8598
* BUG: Fix qMRMLNodeAttributeTableViewTest reintroducing empty QString init by @jcfr in https://github.com/Slicer/Slicer/pull/8602
* ENH: Add widget to select any node for scene views by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8607
* BUG: Fix system git invocation in GSSAPI stub builds and generalize executable wrapper by @jcfr in https://github.com/Slicer/Slicer/pull/8613
* BUG: Update CompareVolumes to fix Hot Link selection issue by @koegl in https://github.com/Slicer/Slicer/pull/8614
* BUG: Fix invalid node type in GetViewNodeClasses() by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8615
* BUG: Make node type labels translatable by @mhdiop in https://github.com/Slicer/Slicer/pull/8091
* BUG: Fix removal of dash characters from exported segmentation filename by @lassoan in https://github.com/Slicer/Slicer/pull/8617
* Improvements to default node usage across different node creation methods by @jamesobutler in https://github.com/Slicer/Slicer/pull/8420
* BUG: Replace u8‑prefixed unit suffix literals with narrow strings by @kovalev0 in https://github.com/Slicer/Slicer/pull/8610
* BUG: Avoid cursor jump on edit in extension LineEdit by @shai-ikko in https://github.com/Slicer/Slicer/pull/8621
* COMP: Update VTK with vtkAxisActor2D tick and label position fix by @jamesobutler in https://github.com/Slicer/Slicer/pull/8636
* COMP: Update CTKAppLauncherLib and CTKAPPLAUNCHER by @jcfr in https://github.com/Slicer/Slicer/pull/8629
* BUG: Initialize environment from launcher before Python to fix macOS startup by @jcfr in https://github.com/Slicer/Slicer/pull/8632
* DOC: Add Ubuntu 25.04 build instructions and GSS/Kerberos workaround by @Punzo in https://github.com/Slicer/Slicer/pull/8634
* BUG: Fix empty volume display histogram group box by @jamesobutler in https://github.com/Slicer/Slicer/pull/8630
* COMP: Always enable CLI support and remove Slicer_BUILD_CLI_SUPPORT option by @AlexyPellegrini in https://github.com/Slicer/Slicer/pull/8633
* DOC: Fix broken links to the PolySeg paper by @cpinter in https://github.com/Slicer/Slicer/pull/8639
* ENH: Set Windows registry key to use high performance graphics by @jamesobutler in https://github.com/Slicer/Slicer/pull/8643
* BUG: Ensure MRMLApplicationLogic is initialized in all modules, fix Colors by @jcfr in https://github.com/Slicer/Slicer/pull/8644
* ENH: Add parameter node GUI connectors by @lassoan in https://github.com/Slicer/Slicer/pull/8646
* BUG: Fix Windows graphics preference not set when installing app with admin privileges by @jamesobutler in https://github.com/Slicer/Slicer/pull/8645
* ENH: Remove unnecessary threshold preview pipeline in unused views by @jamesobutler in https://github.com/Slicer/Slicer/pull/8622
* ENH: Add line profile module by @nhjohnston in https://github.com/Slicer/Slicer/pull/8435
* BUG: Drop unneeded nsl and nis dependencies to resolve libtirpc symbol error by @jcfr in https://github.com/Slicer/Slicer/pull/8649
* COMP: Fix Windows build error in debug mode due to python312_d.lib by @lassoan in https://github.com/Slicer/Slicer/pull/8651
* DOC: Remove warning section for libtirpc GSS/Kerberos symbol lookup error by @Punzo in https://github.com/Slicer/Slicer/pull/8652
* COMP: Replace deprecated use of TestBigEndian CMake module by @petk in https://github.com/Slicer/Slicer/pull/8650
* COMP: Remove unneeded setting of WORDS_BIGENDIAN/WORDS_LITTLEENDIAN macros by @jcfr in https://github.com/Slicer/Slicer/pull/8653
* BUG: Restore https download on macOS fixing packaging of SSL python modules by @jcfr in https://github.com/Slicer/Slicer/pull/8654
* DOC: Add dedicated GOVERNANCE document and reference it from the about page by @jcfr in https://github.com/Slicer/Slicer/pull/8656
* Volume sequence IO 5D by @cpinter in https://github.com/Slicer/Slicer/pull/8391
* DOC: Reference "Code of Conduct" in Governance section and Update contribution processes by @jcfr in https://github.com/Slicer/Slicer/pull/8661
* BUG: Fix traceback using line profile on 2D image by @nhjohnston in https://github.com/Slicer/Slicer/pull/8657
* DOC: Support GitHub-style alerts in documentation and improve CONTRIBUTING document formatting by @jcfr in https://github.com/Slicer/Slicer/pull/8662
* COMP: Fix linux build errors by @lassoan in https://github.com/Slicer/Slicer/pull/8665
* ENH: Match color label title font size to legend font size by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8668
* BUG: Fix not returning GUI tag after connection by @nhjohnston in https://github.com/Slicer/Slicer/pull/8667
* ENH: Restore OpenGL core profile usage on Windows platform by @jamesobutler in https://github.com/Slicer/Slicer/pull/8669
* STYLE: Normalize insertion of braces after control statements by @jcfr in https://github.com/Slicer/Slicer/pull/8671
* BUG: Update CTK to ensure VTK views are always up-to-date by @jcfr in https://github.com/Slicer/Slicer/pull/8672
* COMP: Fix pattern for excluding bots from auto-generated changelog by @jcfr in https://github.com/Slicer/Slicer/pull/8673
* BUG: Show all referenced series as checkboxes in DICOM popup by @deepakri201 in https://github.com/Slicer/Slicer/pull/8605
* DOC: Fix segmentation oversampling snippet in script repository by @cpinter in https://github.com/Slicer/Slicer/pull/8679
* BUG: Fix VTK errors drawing line profile plot with undefined points by @nhjohnston in https://github.com/Slicer/Slicer/pull/8677
* ENH: Add API to retrieve view displayable managers without Qt widgets by @jcfr in https://github.com/Slicer/Slicer/pull/8658
* BUG: Fixed hidden slice edges kept appearing in 3D views by @lassoan in https://github.com/Slicer/Slicer/pull/8684
* BUG: Fix automatic conversion of annotation nodes by @lassoan in https://github.com/Slicer/Slicer/pull/8686
* BUG: Fix py_nomainwindow_test_slicer_parameter_node_wrapper_guis test by @lassoan in https://github.com/Slicer/Slicer/pull/8687
* COMP: Update VTK to 9.5.1 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8683
* ENH: Split segment editor logic by @Thibault-Pelletier in https://github.com/Slicer/Slicer/pull/8666
* COMP: Ensure BUILD_JOB_SERVER_AWARE is set for external projects by @jcfr in https://github.com/Slicer/Slicer/pull/8691
* PERF: Improve sequence node storage performance for simple nodes by @jcfr in https://github.com/Slicer/Slicer/pull/8696
* ENH: Make vtkITKImageWriter more robust by @jcfr in https://github.com/Slicer/Slicer/pull/8697
* BUG: Improve scene view storage and conversion, fix model visibility issues by @lassoan in https://github.com/Slicer/Slicer/pull/8693
* BUG: Suppress unnecessary warning for hidden subject hierarchy items by @jamesobutler in https://github.com/Slicer/Slicer/pull/8695
* BUG: Fix crash in vtkSegmentation::CollapseBinaryLabelmaps by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8700
* ENH: Update CompareVolumes to include optional return mapping and reuse of layout selection widget from LandmarkRegistration by @koegl in https://github.com/Slicer/Slicer/pull/8678
* ENH: Add keyboard and mouse shortcuts for Module Selector navigation by @ruffsl in https://github.com/Slicer/Slicer/pull/8681
* DOC: Add Fedora 37+ launch troubleshooting by @Villafruela in https://github.com/Slicer/Slicer/pull/7114
* COMP: Set BUILD_JOB_SERVER_AWARE for extension ExternalProject on CMake ≥ 3.28 by @jcfr in https://github.com/Slicer/Slicer/pull/8702
* DOC: Add top-level "Extensions" page by @jcfr in https://github.com/Slicer/Slicer/pull/8453
* COMP: Fix quoting of BUILD_JOB_SERVER_AWARE in extension ExternalProject by @jcfr in https://github.com/Slicer/Slicer/pull/8704
* BUG: Prevent crash on SH reparent without displayable node by @lassoan in https://github.com/Slicer/Slicer/pull/8701
* BUG: Use UVW layer opacities when building the UVW blending pipeline by @jcfr in https://github.com/Slicer/Slicer/pull/8711
* BUG: Fix loading of multi-file volumes in SampleData module by @lassoan in https://github.com/Slicer/Slicer/pull/8710
* BUG: Fix ReverseAlpha compositing inverting opacities not layers by @jcfr in https://github.com/Slicer/Slicer/pull/8712
* BUG: Fix Add/Subtract compositing clobbering background input by @jcfr in https://github.com/Slicer/Slicer/pull/8709
* BUG: Update SampleData test for multi-file volume loading behavior by @jcfr in https://github.com/Slicer/Slicer/pull/8713
* ENH: Decouple Base, Libs, and Modules/Loadable from app-specific paths via runtime Home/Share in vtkMRMLApplicationLogic by @AlexyPellegrini in https://github.com/Slicer/Slicer/pull/8004
* BUG: Improve error reporting and fix Color module tests by @jcfr in https://github.com/Slicer/Slicer/pull/8717
* BUG: Manage correctly row deletion in qMRMLSubjectHierarchyCombobox by @achataigner in https://github.com/Slicer/Slicer/pull/8692
* BUG: Fix MIP and MinIP VolumeRendering with SSAO render pass by @Thibault-Pelletier in https://github.com/Slicer/Slicer/pull/8719
* BUG: Fix Undo/Redo in the segment editor logic by @Thibault-Pelletier in https://github.com/Slicer/Slicer/pull/8722
* BUG: Fix reading of vector volumes by @lassoan in https://github.com/Slicer/Slicer/pull/8718
* ENH: Allow reading/writing of 2 component vector volumes by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8732
* ENH: Add customizable application display name property by @jamesobutler in https://github.com/Slicer/Slicer/pull/8731
* COMP: Update VTK to 9.5.2 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8733
* ENH: Improve custom sample data download by @lassoan in https://github.com/Slicer/Slicer/pull/8736
* ENH: Add volume reorientation to Crop Volume module by @lassoan in https://github.com/Slicer/Slicer/pull/8737
* COMP: Enable building with CMake 4 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8740
* ENH: Make volume rendering transfer function adjustment easier by @lassoan in https://github.com/Slicer/Slicer/pull/8739
* COMP: Fix compiler warnings unused variables/missing enumerations by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8743
* ENH: Add TLS authentication support to DICOM Sender and Listener by @jcfr in https://github.com/Slicer/Slicer/pull/8121
* COMP: Update FindVcvars from v1.8 to v1.12 by @jcfr in https://github.com/Slicer/Slicer/pull/8744
* STYLE: Update to use .hxx instead of .txx for tooling by @hjmjohnson in https://github.com/Slicer/Slicer/pull/8741
* BUG: Make DICOMProcess init cooperative so TLS mixin is initialized by @jcfr in https://github.com/Slicer/Slicer/pull/8751
* BUG: Preserve `sys.path` during Slicer module discovery & add startup test by @RafaelPalomar in https://github.com/Slicer/Slicer/pull/8727
* BUG: Delete IO options when using native file dialog to prevent leak by @jcfr in https://github.com/Slicer/Slicer/pull/8753
* DOC: Warn about uncommon volume format options by @pieper in https://github.com/Slicer/Slicer/pull/8756
* ENH: Add support for storing modeling displacement field transforms by @lassoan in https://github.com/Slicer/Slicer/pull/8757
* ENH: Segment Editor: class rename, MRML logic integration, and logging controls by @Thibault-Pelletier in https://github.com/Slicer/Slicer/pull/8746
* BUG: Fix geometry initialization from empty segmentation file by @lassoan in https://github.com/Slicer/Slicer/pull/8761
* BUG: Do not reset markups control points when reading XML attributes by @Punzo in https://github.com/Slicer/Slicer/pull/8748
* BUG: Fixed cloning of composite transforms by @lassoan in https://github.com/Slicer/Slicer/pull/8768
* ENH: Save node attributes in volume and transform sequence files by @lassoan in https://github.com/Slicer/Slicer/pull/8762
* BUG: Make mrb file loading more robust by @lassoan in https://github.com/Slicer/Slicer/pull/8771
* BUG: Clear existing node references before parsing new ones by @Punzo in https://github.com/Slicer/Slicer/pull/8749
* ENH: Add support for reading/writing 2 component sequence files by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8772
* BUG: childwidgetvariables do not return an object with an empty attribute by @malbi in https://github.com/Slicer/Slicer/pull/8775
* ENH: Expose segment editor effect cursor functions by @ThomasKierski in https://github.com/Slicer/Slicer/pull/8763
* DOC: Add "Slicer integration in hospital/PACS context" to DICOM module docs by @jcfr in https://github.com/Slicer/Slicer/pull/8786
* ENH: Propagate terminology when exporting segments to models by @cpinter in https://github.com/Slicer/Slicer/pull/8765
* DOC: Document the new .vp.json volume property file format by @lassoan in https://github.com/Slicer/Slicer/pull/8791
* BUG: Fix OpenGL error at startup in debug mode by @lassoan in https://github.com/Slicer/Slicer/pull/8795
* ENH: Update CTKAppLauncher from 0.1.32 to 33 by @lassoan in https://github.com/Slicer/Slicer/pull/8801
* ENH: Show launcher splashscreen until Slicer is started by @lassoan in https://github.com/Slicer/Slicer/pull/8802
* ENH: Simplify Slice view removing LightBox feature by @jcfr in https://github.com/Slicer/Slicer/pull/8776
* ENH: Update CTK to include PythonQt minimizing commontk fork deltas by @jcfr in https://github.com/Slicer/Slicer/pull/8803
* BUG: Fix loading of orientation marker and fonts by @ruffsl in https://github.com/Slicer/Slicer/pull/8800
* BUG: Ensure launcher splash-screen gets hidden on app restart by @lassoan in https://github.com/Slicer/Slicer/pull/8808
* COMP: Update CTK and align MOC include names with Qt AUTOMOC convention by @jcfr in https://github.com/Slicer/Slicer/pull/8813
* COMP: Qt AUTOGEN migration: enable AUTOUIC, AUTORCC, AUTOMOC across Slicer by @jcfr in https://github.com/Slicer/Slicer/pull/8814
* COMP: Update CTK to modernize PythonQt integration by @jcfr in https://github.com/Slicer/Slicer/pull/8817
* COMP: Fix AUTOUIC include dir for multi-config generators by @jcfr in https://github.com/Slicer/Slicer/pull/8818
* BUG: Update CTK to fix AUTOMOC DCMTK/Python clash and chart refresh by @jcfr in https://github.com/Slicer/Slicer/pull/8823
* COMP: Update CTK to fix PythonQt build ensuring Qt DIR is passed by @jcfr in https://github.com/Slicer/Slicer/pull/8824
* COMP: Add support for Visual Studio 2026 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8742
* BUG: Fix Line Profile issues showing multiple lines by @lassoan in https://github.com/Slicer/Slicer/pull/8809
* BUG: Update VTK to include vtkSurfaceNets3D fix for orientation consistency by @jcfr in https://github.com/Slicer/Slicer/pull/8831
* COMP: Update CTK to include changes for Qt5/Qt6 compatibility by @jcfr in https://github.com/Slicer/Slicer/pull/8833
* COMP: Reduce threshold determining use of response file with AUTOMOC by @jcfr in https://github.com/Slicer/Slicer/pull/8834
* COMP: Require Qt XmlPatterns only when QtTesting is enabled by @jcfr in https://github.com/Slicer/Slicer/pull/8835

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
