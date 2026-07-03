# Improvements

* Improves Extrude tool and Revolve tool from Dynamic Modeler by @mauigna06 in https://github.com/Slicer/Slicer/pull/8816
* Update ITK to v5.4.5 by @dzenanz in https://github.com/Slicer/Slicer/pull/8862
* Update BRAINSTools from 2024-11-09 to 2025-11-10 by @dzenanz in https://github.com/Slicer/Slicer/pull/8860
* Disable ITKv4 legacy classes and interfaces by @dzenanz in https://github.com/Slicer/Slicer/pull/8898
* Enable ITKv4 legacy for Rigid3D and BSplineDeformable transforms by @dzenanz in https://github.com/Slicer/Slicer/pull/8911
* Transform-related cleanup and improvements by @dzenanz in https://github.com/Slicer/Slicer/pull/8917
* Get image data extent using accessor instead of direct member by @jamesobutler in https://github.com/Slicer/Slicer/pull/8925
* Allow volume rendering of non-linearly transformed volumes by @lassoan in https://github.com/Slicer/Slicer/pull/8929
* Expose material properties in Segmentation module GUI by @lassoan in https://github.com/Slicer/Slicer/pull/8782
* Make transform visualization 2D glyphs thickness and arrow tip length editable on GUI by @lassoan in https://github.com/Slicer/Slicer/pull/8931
* Support 2D transforms by converting to 3D during reading by @dzenanz in https://github.com/Slicer/Slicer/pull/8842
* Make 2D circle glyph resolution adjustable for transform display by @lassoan in https://github.com/Slicer/Slicer/pull/8934
* Add "Flip normal" action to plane node by @lassoan in https://github.com/Slicer/Slicer/pull/8794
* Replace deprecated AddActor2D/RemoveActor2D usage by @jamesobutler in https://github.com/Slicer/Slicer/pull/8944
* Add position status column to qSlicerSimpleMarkupsWidget by @lassoan in https://github.com/Slicer/Slicer/pull/8955
* Remove support for building against VTK <= 9.3 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8972
* Remove support for Qt versions < 5.15 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8977
* Add view node flag to disable Markups occlusion checking by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8979
* Refactor Visual DICOM Browser UI for large databases by @Punzo in https://github.com/Slicer/Slicer/pull/8866
* Show number of control points in SH tooltip of markup nodes by @cpinter in https://github.com/Slicer/Slicer/pull/8915
* Disable Brotli support in CURL configuration by @ruffsl in https://github.com/Slicer/Slicer/pull/9007
* Make Teem a private dependency by @AlexyPellegrini in https://github.com/Slicer/Slicer/pull/9030
* Improve labels and tooltips for Scene Views dialog by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/9006
* Update CTKAppLauncher from 0.1.33 to 0.1.34 by @lassoan in https://github.com/Slicer/Slicer/pull/9033
* Scroll to newly added segment in the segment editor by @Punzo in https://github.com/Slicer/Slicer/pull/9042
* Remove layout node assert impacting tests in debug mode by @jamesobutler in https://github.com/Slicer/Slicer/pull/9035
* Add JSON schema for additional extension metadata by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/9057
* Add support for building against VTK version 9.6.0 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8928
* Add refresh functionality to visual DICOM browser and UI by @Punzo in https://github.com/Slicer/Slicer/pull/9070
* Add directional glyphs to curve and line nodes by @Punzo in https://github.com/Slicer/Slicer/pull/9066
* Add support for additional extension metadata by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/9040
* Set application icon to SlicerApp-Real.exe executable by @jamesobutler in https://github.com/Slicer/Slicer/pull/8987
* Enable Zlib support in DCMTK build by @fedorov in https://github.com/Slicer/Slicer/pull/9107
* Separate SampleData category name and title by @lassoan in https://github.com/Slicer/Slicer/pull/9096
* Pin transitive dependencies in python-dicom-requirements by @fedorov in https://github.com/Slicer/Slicer/pull/9132
* Add auto-trim of file cache at application startup by @lassoan in https://github.com/Slicer/Slicer/pull/9115
* Allow Slicer_USE_QtTesting=ON with Qt 6 builds by @hjmjohnson in https://github.com/Slicer/Slicer/pull/9138
* Add application icon for linux by @lassoan in https://github.com/Slicer/Slicer/pull/9196
* Add support for 2D special cases of MatrixOffsetTransform by @dzenanz in https://github.com/Slicer/Slicer/pull/9204
* Gray out visibility icon of SH item under hidden parent by @lassoan in https://github.com/Slicer/Slicer/pull/9195
* Deprecate fcsv file format by @lassoan in https://github.com/Slicer/Slicer/pull/9192
* Keep markup placement preview visible when slice view moves or zooms by @lassoan in https://github.com/Slicer/Slicer/pull/9189
* Add unique Slicerrc file for custom apps with ability to turn off by @jamesobutler in https://github.com/Slicer/Slicer/pull/9240

# Performance

* Fixes performance issues for DICOM import in Qt6 by @Punzo in https://github.com/Slicer/Slicer/pull/8982
* Optimize update of 3D segmentation display manager by @Punzo in https://github.com/Slicer/Slicer/pull/9031

# Fixes

* Branding text in the installer was being ignored by @dzenanz in https://github.com/Slicer/Slicer/pull/8858
* Fix log10 display of inverted color tables by @lassoan in https://github.com/Slicer/Slicer/pull/8884
* Fix a test assuming that the extension manager is enabled by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/8888
* Fix module finder with Qt6 by @lassoan in https://github.com/Slicer/Slicer/pull/8903
* Fix View Controller module crash with virtual reality view by @lassoan in https://github.com/Slicer/Slicer/pull/8900
* Fix Capture toolbar in incorrect location at startup  by @jamesobutler in https://github.com/Slicer/Slicer/pull/8936
* Fix crash in ExportSegmentsToColorTableNode by @lassoan in https://github.com/Slicer/Slicer/pull/8942
* Fix last used control point number not reset when list reset by @jamesobutler in https://github.com/Slicer/Slicer/pull/8970
* Remove orphan points from ROI and plane cut tools of Dynamic Modeler by @lassoan in https://github.com/Slicer/Slicer/pull/8971
* Fix Qt6 data dialog description shift-change by @codeling in https://github.com/Slicer/Slicer/pull/8978
* Fix invalid segment iterator in vtkSegmentation::ReorderSegments by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8981
* Update VTK with virtual reality fixes by @lassoan in https://github.com/Slicer/Slicer/pull/8984
* Fix correct vtkErrorMacro message return by @benediktjohannes in https://github.com/Slicer/Slicer/pull/8997
* Fix table copy/paste failure when system clipboard is unavailable by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/9025
* Fix copy-paste error in oversampling fuzzy membership function by @mhalle in https://github.com/Slicer/Slicer/pull/9045
* Fix inability to create multiple scene views by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/9059
* Fix VTK observer leak in parameterNodeWrapper connectGui/disconnectGui by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/9063
* Disable touch events on macOS Qt6 to fix stuck 3D rotation by @pieper in https://github.com/Slicer/Slicer/pull/9069
* Fix markup control point coordinates not updating in table by @mhalle in https://github.com/Slicer/Slicer/pull/9047
* Fix operator precedence in time unit display coefficients by @mhalle in https://github.com/Slicer/Slicer/pull/9046
* Fix effective range computation in volume property node widget by @lassoan in https://github.com/Slicer/Slicer/pull/9080
* Fix python errors when the application path has special characters by @lassoan in https://github.com/Slicer/Slicer/pull/9032
* Fix static curl link failures by @hjmjohnson in https://github.com/Slicer/Slicer/pull/9095
* Fix typo in dicom thumbnail size label by @benediktjohannes in https://github.com/Slicer/Slicer/pull/8964
* Add missing Superclass::setup() calls in 13 module widgets by @mhalle in https://github.com/Slicer/Slicer/pull/9044
* Fix failing extension description tests by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/9112
* Guard null SegmentationNode in qMRMLSegmentEditorWidget by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/9134
* Resolve QtTesting install library name from imported target by @hjmjohnson in https://github.com/Slicer/Slicer/pull/9137
* Restore removed slicer.util._executePythonModule by @lassoan in https://github.com/Slicer/Slicer/pull/9141
* Fix SampleData module by @lassoan in https://github.com/Slicer/Slicer/pull/9150
* Fix GetFileNameWithoutExtension() failing when called with no arguments by @jamesobutler in https://github.com/Slicer/Slicer/pull/9152
* Fix Extension Wizard module creation by @cpinter in https://github.com/Slicer/Slicer/pull/9178
* Fix Qt geometry warning when showing terminology selector by @lassoan in https://github.com/Slicer/Slicer/pull/9197
* Reset view action metadata when opening SH widget context menu by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/9205
* Clicking visibility icon does not change item selection by @cpinter in https://github.com/Slicer/Slicer/pull/9198
* Prevent loss of volume rendering opacity transfer function points by @lassoan in https://github.com/Slicer/Slicer/pull/9186
* Disable default VTK render window keyboard shortcuts by @lassoan in https://github.com/Slicer/Slicer/pull/9194
* Fix segment metadata off-by-one when loading DICOM Labelmap SEG by @fedorov in https://github.com/Slicer/Slicer/pull/9163
* Show folder opacity before visibility toggle by @vacaslistradas in https://github.com/Slicer/Slicer/pull/9200
* Fix crash when selecting active scalars for several model nodes at once by @lassoan in https://github.com/Slicer/Slicer/pull/9169
* Fix unwanted markup measurements by @lassoan in https://github.com/Slicer/Slicer/pull/9216
* Fixed missing openjp2 shared library by @lassoan in https://github.com/Slicer/Slicer/pull/9227
* Fix missing openjp2 shared library in macOS package by @lassoan in https://github.com/Slicer/Slicer/pull/9228
* Restore slicer.util Python console imports by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/9220
* Fix std::regex crash in volume rendering (Qt WebEngine symbol interposition) by @RafaelPalomar in https://github.com/Slicer/Slicer/pull/9231
* Hide 3D angle line when fewer than 2 points by @lassoan in https://github.com/Slicer/Slicer/pull/9215
* Fix terminology selector opening with empty content on repeated opens by @xskere in https://github.com/Slicer/Slicer/pull/9223
* Fix qMRMLNodeComboBox::nodeAddedByUser emitted twice by @dparikh79 in https://github.com/Slicer/Slicer/pull/9158
* Fix crash loading table with unsupported schema column type by @mauigna06 in https://github.com/Slicer/Slicer/pull/9238
* Fix duplicate Opacity slider for segments in subject hierarchy by @lassoan in https://github.com/Slicer/Slicer/pull/9243
* Disable FP exception trapping for ModelMaker/MergeModels tests on macOS by @RafaelPalomar in https://github.com/Slicer/Slicer/pull/9241
* Fix incorrect sync of 2D colormap to rendering colormap by @ajallphin in https://github.com/Slicer/Slicer/pull/9250
* Fix crash exporting series with no local files by @sjh26 in https://github.com/Slicer/Slicer/pull/9251

# Documentation

* Update issue templates for patch and release processes by @jcfr in https://github.com/Slicer/Slicer/pull/8838
* Revise Visual Studio installation instructions for Windows by @lassoan in https://github.com/Slicer/Slicer/pull/8851
* Add recent SlicerMorph funding sources to about.md by @lassoan in https://github.com/Slicer/Slicer/pull/8894
* Add recent SlicerHeart funding by @lassoan in https://github.com/Slicer/Slicer/pull/8899
* Add CHOP Frontier Program funding information by @lassoan in https://github.com/Slicer/Slicer/pull/8913
* Update supported operating system versions by @jamesobutler in https://github.com/Slicer/Slicer/pull/8933
* fix inconsistencies between documentation and code by @fedorov in https://github.com/Slicer/Slicer/pull/9008
* Add macOS (Silicon) Qt6 build recipe by @isabelfrolick in https://github.com/Slicer/Slicer/pull/9011
* Add Qt6 Linux build instructions with tabbed Qt5/Qt6 layout by @RafaelPalomar in https://github.com/Slicer/Slicer/pull/9084
* Fix spelling error in image segmentation guide by @hjmjohnson in https://github.com/Slicer/Slicer/pull/9098
* Fix typo in MRML overview documentation by @anthonyylee in https://github.com/Slicer/Slicer/pull/9116
* Add two commercial products in the about documentation page by @cpinter in https://github.com/Slicer/Slicer/pull/9168
* Fix elongation and flatness definitions in segment statistics by @gliu2 in https://github.com/Slicer/Slicer/pull/9177
* Do not show "Edit on GitHub" link for special documentation pages by @lassoan in https://github.com/Slicer/Slicer/pull/9188

# Compilation

* Enable CMP0071 NEW behavior for extension builds by @sjh26 in https://github.com/Slicer/Slicer/pull/8845
* Update minimum required CMAKE_OSX_DEPLOYMENT_TARGET to 14.0 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8850
* Update python packages to latest by @jamesobutler in https://github.com/Slicer/Slicer/pull/8844
* Fix crash when setting none display in SH combobox with no scene by @cpinter in https://github.com/Slicer/Slicer/pull/8853
* Support building with ITK legacy support ON/OFF by @dzenanz in https://github.com/Slicer/Slicer/pull/8841
* Update vtkAddon to fix build error by @lassoan in https://github.com/Slicer/Slicer/pull/8873
* Replace deprecated QRegExp usage by @lassoan in https://github.com/Slicer/Slicer/pull/8875
* Update CTK to fix Qt6 errors by @lassoan in https://github.com/Slicer/Slicer/pull/8901
* Fix QT_PLUGINS_DIR detection using qmake by @hubutui in https://github.com/Slicer/Slicer/pull/8910
* Include the iostream header where cout/cerr used by @jamesobutler in https://github.com/Slicer/Slicer/pull/8927
* Switch building SimpleITK from source to using pre-built Whl by @jamesobutler in https://github.com/Slicer/Slicer/pull/8923
* Remove deprecated vtkVectorOperators by @jamesobutler in https://github.com/Slicer/Slicer/pull/8926
* Remove unused SimpleITK shared build option by @jamesobutler in https://github.com/Slicer/Slicer/pull/8932
* Update CTK with fix to build with Qt 6.10 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8938
* Update CTK with Qt6 pythonqt wrapping fixes by @jamesobutler in https://github.com/Slicer/Slicer/pull/8940
* Update LibFFI to v3.5.2 based version by @jamesobutler in https://github.com/Slicer/Slicer/pull/8939
* Fix LibFFI build error on macOS and Linux by @jamesobutler in https://github.com/Slicer/Slicer/pull/8943
* Update DCMTK version to 3.7.0 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8946
* Update DCMTK to 3.7.0+ commit with binary seg fix by @jamesobutler in https://github.com/Slicer/Slicer/pull/8948
* Remove handling of old OpenSSL 1.0.x with Qt <5.12 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8950
* Enforce Qt 5.15 minimum across all platforms  by @jamesobutler in https://github.com/Slicer/Slicer/pull/8949
* Fix TBB install not found during Linux build by @jamesobutler in https://github.com/Slicer/Slicer/pull/8951
* Update cURL version to 8.17.0 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8959
* Skip PIC flag passed to MSVC by @jamesobutler in https://github.com/Slicer/Slicer/pull/8957
* Update urllib3 version to latest 2.6.3 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8966
* Update urllib3 version to latest 2.6.3 in doc requirement by @jamesobutler in https://github.com/Slicer/Slicer/pull/8968
* Fix sqlite linker failure by @jamesobutler in https://github.com/Slicer/Slicer/pull/8969
* Update DCMTK to 3.7.0++ commit with additional binary seg fix by @fedorov in https://github.com/Slicer/Slicer/pull/8988
* Add option for IDImageIO support in CMake configuration by @Punzo in https://github.com/Slicer/Slicer/pull/9023
* Unify the use of generated Export.h files in Base and MRML libs by @AlexyPellegrini in https://github.com/Slicer/Slicer/pull/9036
* Update VTK to 9.6.1 by @jamesobutler in https://github.com/Slicer/Slicer/pull/9087
* Fix CTKAppLauncherLib add-qt6-support commit hash by @codeling in https://github.com/Slicer/Slicer/pull/9067
* Update CompareVolumes with refresh optimization by @jamesobutler in https://github.com/Slicer/Slicer/pull/9086
* Fix Qt6 MOC incomplete type errors by @RafaelPalomar in https://github.com/Slicer/Slicer/pull/9083
* Update Slicer cert creation with non-archived mozilla repo by @heitbaum in https://github.com/Slicer/Slicer/pull/8973
* Update CTK to latest (3b3f9eff) by @hjmjohnson in https://github.com/Slicer/Slicer/pull/9097
* Update ITK to 5.4.6 by @jamesobutler in https://github.com/Slicer/Slicer/pull/9125
* Update CTK with PythonQt crash fix by @jamesobutler in https://github.com/Slicer/Slicer/pull/9128
* Update VTK to 9.6.2 by @jamesobutler in https://github.com/Slicer/Slicer/pull/9166
* Update python packages to latest by @jamesobutler in https://github.com/Slicer/Slicer/pull/9161
* Update CTK to latest version by @lassoan in https://github.com/Slicer/Slicer/pull/9202
* Update CTK with Qt 6.11 build support by @jamesobutler in https://github.com/Slicer/Slicer/pull/9212
* Raise minimum CMake floor to 3.28 and remove dead version-conditional code by @hjmjohnson in https://github.com/Slicer/Slicer/pull/9210
* Update docs dependencies to resolve security advisories by @jamesobutler in https://github.com/Slicer/Slicer/pull/9222
* Add missing itkImageRegionIteratorWithIndex.h includes by @hjmjohnson in https://github.com/Slicer/Slicer/pull/9219
* Add MSVC compatibility check when using Qt 5 by @jamesobutler in https://github.com/Slicer/Slicer/pull/9221
* Update FindVcvars with support for old toolsets in newer VS by @jamesobutler in https://github.com/Slicer/Slicer/pull/9206
* Add Meta AR video passthrough by @lassoan in https://github.com/Slicer/Slicer/pull/9249

# Style

* Fix multiple typing errors by @benediktjohannes in https://github.com/Slicer/Slicer/pull/8996
* Fix codespell errors by @lassoan in https://github.com/Slicer/Slicer/pull/9061
* Prefer declaring CMake min max required versions as variables by @jhlegarreta in https://github.com/Slicer/Slicer/pull/8375
* Fix typos in the CreateDICOMSeries GUI by @lassoan in https://github.com/Slicer/Slicer/pull/9103

# Uncategorized

* Fix missing closed surface segment statistics if segmentation node is transformed by @lassoan in https://github.com/Slicer/Slicer/pull/8854
* Trivial fixes to prepare Qt6 compatibility by @lassoan in https://github.com/Slicer/Slicer/pull/8868
* More Qt6 preparation commits by @lassoan in https://github.com/Slicer/Slicer/pull/8874
* Add Qt6 support by @lassoan in https://github.com/Slicer/Slicer/pull/8893
* Fix test failures with Qt6 by @lassoan in https://github.com/Slicer/Slicer/pull/8919
* Fix mention of SWIG required external project and update to deep copy PushVolumeToSlicer by @jamesobutler in https://github.com/Slicer/Slicer/pull/8930
* Additional Qt 6 compatibility fixes by @jamesobutler in https://github.com/Slicer/Slicer/pull/8935
* Qt6 packaging and startup fixes by @jamesobutler in https://github.com/Slicer/Slicer/pull/8937
* Build oneTBB from source and update to 2022.3.0 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8945
* Qt6 additional version fixes for Qt 6.8 support by @jamesobutler in https://github.com/Slicer/Slicer/pull/8956
* Switch to official XZ project repository and update to v5.8.2 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8958
* Switch sqlite-amalgamation repo to more maintained version and update to version 3.51.2. by @jamesobutler in https://github.com/Slicer/Slicer/pull/8965
* Crash closing application after fill between slices by @xriobe in https://github.com/Slicer/Slicer/pull/8998
* Update reference link for fast grow-cut method by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/9058
* Fix translation related errors by @lassoan in https://github.com/Slicer/Slicer/pull/9104
* Improve python package installation utilities by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/9010
* Add DICOM SEG/PM/SR/M3D plugins to Slicer core by @fedorov in https://github.com/Slicer/Slicer/pull/9114
* Fix dcmqi binary lookup by @fedorov in https://github.com/Slicer/Slicer/pull/9136
* Fix CacheManager startup warning by @lassoan in https://github.com/Slicer/Slicer/pull/9159
* Fix test failures by @lassoan in https://github.com/Slicer/Slicer/pull/9162
* Add dcmtk JPEG2000 support by @lassoan in https://github.com/Slicer/Slicer/pull/9099
* Minor code fixes by @lassoan in https://github.com/Slicer/Slicer/pull/9213
* Fix private storable node saving by @lassoan in https://github.com/Slicer/Slicer/pull/9236
* Fix atlastests by @lassoan in https://github.com/Slicer/Slicer/pull/9235
* Add option for logarithmic color mapping by @ajallphin in https://github.com/Slicer/Slicer/pull/9016
* Fix SubjectHierarchyFoldersTest1, vtkMRMLMarkupsStorageNodeTest2, vtkMRMLVolumePropertyNodeTest1 by @lassoan in https://github.com/Slicer/Slicer/pull/9242

# slicerbot

* Update Slicer.crt CA bundle by @slicerbot in https://github.com/Slicer/Slicer/pull/9102
* Update Slicer.crt CA bundle by @slicerbot in https://github.com/Slicer/Slicer/pull/9111
* Update Slicer.crt CA bundle by @slicerbot in https://github.com/Slicer/Slicer/pull/9237

# dependabot

* None

# slicer-app

* None
