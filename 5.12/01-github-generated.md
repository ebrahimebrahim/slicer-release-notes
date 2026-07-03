<!-- Release notes generated using configuration in .github/release.yml at v5.12.0 -->

## What's Changed
* DOC: Update issue templates for patch and release processes by @jcfr in https://github.com/Slicer/Slicer/pull/8838
* COMP: Enable CMP0071 NEW behavior for extension builds by @sjh26 in https://github.com/Slicer/Slicer/pull/8845
* COMP: Update minimum required CMAKE_OSX_DEPLOYMENT_TARGET to 14.0 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8850
* COMP: Update python packages to latest by @jamesobutler in https://github.com/Slicer/Slicer/pull/8844
* DOC: Revise Visual Studio installation instructions for Windows by @lassoan in https://github.com/Slicer/Slicer/pull/8851
* ENH: Improves Extrude tool and Revolve tool from Dynamic Modeler by @mauigna06 in https://github.com/Slicer/Slicer/pull/8816
* Fix missing closed surface segment statistics if segmentation node is transformed by @lassoan in https://github.com/Slicer/Slicer/pull/8854
* COMP: Fix crash when setting none display in SH combobox with no scene by @cpinter in https://github.com/Slicer/Slicer/pull/8853
* BUG: Branding text in the installer was being ignored by @dzenanz in https://github.com/Slicer/Slicer/pull/8858
* COMP: Support building with ITK legacy support ON/OFF by @dzenanz in https://github.com/Slicer/Slicer/pull/8841
* ENH: Update ITK to v5.4.5 by @dzenanz in https://github.com/Slicer/Slicer/pull/8862
* ENH: Update BRAINSTools from 2024-11-09 to 2025-11-10 by @dzenanz in https://github.com/Slicer/Slicer/pull/8860
* Trivial fixes to prepare Qt6 compatibility by @lassoan in https://github.com/Slicer/Slicer/pull/8868
* COMP: Update vtkAddon to fix build error by @lassoan in https://github.com/Slicer/Slicer/pull/8873
* More Qt6 preparation commits by @lassoan in https://github.com/Slicer/Slicer/pull/8874
* COMP: Replace deprecated QRegExp usage by @lassoan in https://github.com/Slicer/Slicer/pull/8875
* BUG: Fix log10 display of inverted color tables by @lassoan in https://github.com/Slicer/Slicer/pull/8884
* BUG: Fix a test assuming that the extension manager is enabled by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/8888
* Add Qt6 support by @lassoan in https://github.com/Slicer/Slicer/pull/8893
* DOC: Add recent SlicerMorph funding sources to about.md by @lassoan in https://github.com/Slicer/Slicer/pull/8894
* DOC: Add recent SlicerHeart funding by @lassoan in https://github.com/Slicer/Slicer/pull/8899
* COMP: Update CTK to fix Qt6 errors by @lassoan in https://github.com/Slicer/Slicer/pull/8901
* ENH: Disable ITKv4 legacy classes and interfaces by @dzenanz in https://github.com/Slicer/Slicer/pull/8898
* ENH: Enable ITKv4 legacy for Rigid3D and BSplineDeformable transforms by @dzenanz in https://github.com/Slicer/Slicer/pull/8911
* DOC: Add CHOP Frontier Program funding information by @lassoan in https://github.com/Slicer/Slicer/pull/8913
* COMP: Fix QT_PLUGINS_DIR detection using qmake by @hubutui in https://github.com/Slicer/Slicer/pull/8910
* BUG: Fix module finder with Qt6 by @lassoan in https://github.com/Slicer/Slicer/pull/8903
* BUG: Fix View Controller module crash with virtual reality view by @lassoan in https://github.com/Slicer/Slicer/pull/8900
* ENH: Transform-related cleanup and improvements by @dzenanz in https://github.com/Slicer/Slicer/pull/8917
* COMP: Include the iostream header where cout/cerr used by @jamesobutler in https://github.com/Slicer/Slicer/pull/8927
* COMP: Switch building SimpleITK from source to using pre-built Whl by @jamesobutler in https://github.com/Slicer/Slicer/pull/8923
* COMP: Remove deprecated vtkVectorOperators by @jamesobutler in https://github.com/Slicer/Slicer/pull/8926
* Fix test failures with Qt6 by @lassoan in https://github.com/Slicer/Slicer/pull/8919
* ENH: Get image data extent using accessor instead of direct member by @jamesobutler in https://github.com/Slicer/Slicer/pull/8925
* ENH: Allow volume rendering of non-linearly transformed volumes by @lassoan in https://github.com/Slicer/Slicer/pull/8929
* ENH: Expose material properties in Segmentation module GUI by @lassoan in https://github.com/Slicer/Slicer/pull/8782
* ENH: Make transform visualization 2D glyphs thickness and arrow tip length editable on GUI by @lassoan in https://github.com/Slicer/Slicer/pull/8931
* Fix mention of SWIG required external project and update to deep copy PushVolumeToSlicer by @jamesobutler in https://github.com/Slicer/Slicer/pull/8930
* DOC: Update supported operating system versions by @jamesobutler in https://github.com/Slicer/Slicer/pull/8933
* COMP: Remove unused SimpleITK shared build option by @jamesobutler in https://github.com/Slicer/Slicer/pull/8932
* ENH: Support 2D transforms by converting to 3D during reading by @dzenanz in https://github.com/Slicer/Slicer/pull/8842
* Additional Qt 6 compatibility fixes by @jamesobutler in https://github.com/Slicer/Slicer/pull/8935
* ENH: Make 2D circle glyph resolution adjustable for transform display by @lassoan in https://github.com/Slicer/Slicer/pull/8934
* COMP: Update CTK with fix to build with Qt 6.10 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8938
* BUG: Fix Capture toolbar in incorrect location at startup  by @jamesobutler in https://github.com/Slicer/Slicer/pull/8936
* Qt6 packaging and startup fixes by @jamesobutler in https://github.com/Slicer/Slicer/pull/8937
* COMP: Update CTK with Qt6 pythonqt wrapping fixes by @jamesobutler in https://github.com/Slicer/Slicer/pull/8940
* COMP: Update LibFFI to v3.5.2 based version by @jamesobutler in https://github.com/Slicer/Slicer/pull/8939
* ENH: Add "Flip normal" action to plane node by @lassoan in https://github.com/Slicer/Slicer/pull/8794
* COMP: Fix LibFFI build error on macOS and Linux by @jamesobutler in https://github.com/Slicer/Slicer/pull/8943
* COMP: Update DCMTK version to 3.7.0 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8946
* Build oneTBB from source and update to 2022.3.0 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8945
* ENH: Replace deprecated AddActor2D/RemoveActor2D usage by @jamesobutler in https://github.com/Slicer/Slicer/pull/8944
* COMP: Update DCMTK to 3.7.0+ commit with binary seg fix by @jamesobutler in https://github.com/Slicer/Slicer/pull/8948
* COMP: Remove handling of old OpenSSL 1.0.x with Qt <5.12 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8950
* COMP: Enforce Qt 5.15 minimum across all platforms  by @jamesobutler in https://github.com/Slicer/Slicer/pull/8949
* COMP: Fix TBB install not found during Linux build by @jamesobutler in https://github.com/Slicer/Slicer/pull/8951
* BUG: Fix crash in ExportSegmentsToColorTableNode by @lassoan in https://github.com/Slicer/Slicer/pull/8942
* ENH: Add position status column to qSlicerSimpleMarkupsWidget by @lassoan in https://github.com/Slicer/Slicer/pull/8955
* Qt6 additional version fixes for Qt 6.8 support by @jamesobutler in https://github.com/Slicer/Slicer/pull/8956
* Switch to official XZ project repository and update to v5.8.2 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8958
* COMP: Update cURL version to 8.17.0 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8959
* COMP: Skip PIC flag passed to MSVC by @jamesobutler in https://github.com/Slicer/Slicer/pull/8957
* COMP: Update urllib3 version to latest 2.6.3 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8966
* Switch sqlite-amalgamation repo to more maintained version and update to version 3.51.2. by @jamesobutler in https://github.com/Slicer/Slicer/pull/8965
* COMP: Update urllib3 version to latest 2.6.3 in doc requirement by @jamesobutler in https://github.com/Slicer/Slicer/pull/8968
* COMP: Fix sqlite linker failure by @jamesobutler in https://github.com/Slicer/Slicer/pull/8969
* BUG: Fix last used control point number not reset when list reset by @jamesobutler in https://github.com/Slicer/Slicer/pull/8970
* BUG: Remove orphan points from ROI and plane cut tools of Dynamic Modeler by @lassoan in https://github.com/Slicer/Slicer/pull/8971
* ENH: Remove support for building against VTK <= 9.3 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8972
* ENH: Remove support for Qt versions < 5.15 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8977
* BUG: Fix Qt6 data dialog description shift-change by @codeling in https://github.com/Slicer/Slicer/pull/8978
* ENH: Add view node flag to disable Markups occlusion checking by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8979
* ENH: Refactor Visual DICOM Browser UI for large databases by @Punzo in https://github.com/Slicer/Slicer/pull/8866
* BUG: Fix invalid segment iterator in vtkSegmentation::ReorderSegments by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/8981
* BUG: Update VTK with virtual reality fixes by @lassoan in https://github.com/Slicer/Slicer/pull/8984
* COMP: Update DCMTK to 3.7.0++ commit with additional binary seg fix by @fedorov in https://github.com/Slicer/Slicer/pull/8988
* STYLE: Fix multiple typing errors by @benediktjohannes in https://github.com/Slicer/Slicer/pull/8996
* BUG: Fix correct vtkErrorMacro message return by @benediktjohannes in https://github.com/Slicer/Slicer/pull/8997
* ENH: Show number of control points in SH tooltip of markup nodes by @cpinter in https://github.com/Slicer/Slicer/pull/8915
* PERF: Fixes performance issues for DICOM import in Qt6 by @Punzo in https://github.com/Slicer/Slicer/pull/8982
* DOC: fix inconsistencies between documentation and code by @fedorov in https://github.com/Slicer/Slicer/pull/9008
* DOC: Add macOS (Silicon) Qt6 build recipe by @isabelfrolick in https://github.com/Slicer/Slicer/pull/9011
* ENH: Disable Brotli support in CURL configuration by @ruffsl in https://github.com/Slicer/Slicer/pull/9007
* COMP: Add option for IDImageIO support in CMake configuration by @Punzo in https://github.com/Slicer/Slicer/pull/9023
* Crash closing application after fill between slices by @xriobe in https://github.com/Slicer/Slicer/pull/8998
* PERF: Optimize update of 3D segmentation display manager by @Punzo in https://github.com/Slicer/Slicer/pull/9031
* BUG: Fix table copy/paste failure when system clipboard is unavailable by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/9025
* ENH: Make Teem a private dependency by @AlexyPellegrini in https://github.com/Slicer/Slicer/pull/9030
* ENH: Improve labels and tooltips for Scene Views dialog by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/9006
* ENH: Update CTKAppLauncher from 0.1.33 to 0.1.34 by @lassoan in https://github.com/Slicer/Slicer/pull/9033
* COMP: Unify the use of generated Export.h files in Base and MRML libs by @AlexyPellegrini in https://github.com/Slicer/Slicer/pull/9036
* ENH: Scroll to newly added segment in the segment editor by @Punzo in https://github.com/Slicer/Slicer/pull/9042
* ENH: Remove layout node assert impacting tests in debug mode by @jamesobutler in https://github.com/Slicer/Slicer/pull/9035
* ENH: Add JSON schema for additional extension metadata by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/9057
* Update reference link for fast grow-cut method by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/9058
* BUG: Fix copy-paste error in oversampling fuzzy membership function by @mhalle in https://github.com/Slicer/Slicer/pull/9045
* BUG: Fix inability to create multiple scene views by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/9059
* STYLE: Fix codespell errors by @lassoan in https://github.com/Slicer/Slicer/pull/9061
* BUG: Fix VTK observer leak in parameterNodeWrapper connectGui/disconnectGui by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/9063
* BUG: Disable touch events on macOS Qt6 to fix stuck 3D rotation by @pieper in https://github.com/Slicer/Slicer/pull/9069
* ENH: Add support for building against VTK version 9.6.0 by @jamesobutler in https://github.com/Slicer/Slicer/pull/8928
* ENH: Add refresh functionality to visual DICOM browser and UI by @Punzo in https://github.com/Slicer/Slicer/pull/9070
* ENH: Add directional glyphs to curve and line nodes by @Punzo in https://github.com/Slicer/Slicer/pull/9066
* BUG: Fix markup control point coordinates not updating in table by @mhalle in https://github.com/Slicer/Slicer/pull/9047
* BUG: Fix operator precedence in time unit display coefficients by @mhalle in https://github.com/Slicer/Slicer/pull/9046
* ENH: Add support for additional extension metadata by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/9040
* BUG: Fix effective range computation in volume property node widget by @lassoan in https://github.com/Slicer/Slicer/pull/9080
* BUG: Fix python errors when the application path has special characters by @lassoan in https://github.com/Slicer/Slicer/pull/9032
* COMP: Update VTK to 9.6.1 by @jamesobutler in https://github.com/Slicer/Slicer/pull/9087
* COMP: Fix CTKAppLauncherLib add-qt6-support commit hash by @codeling in https://github.com/Slicer/Slicer/pull/9067
* COMP: Update CompareVolumes with refresh optimization by @jamesobutler in https://github.com/Slicer/Slicer/pull/9086
* BUG: Fix static curl link failures by @hjmjohnson in https://github.com/Slicer/Slicer/pull/9095
* COMP: Fix Qt6 MOC incomplete type errors by @RafaelPalomar in https://github.com/Slicer/Slicer/pull/9083
* DOC: Add Qt6 Linux build instructions with tabbed Qt5/Qt6 layout by @RafaelPalomar in https://github.com/Slicer/Slicer/pull/9084
* DOC: Fix spelling error in image segmentation guide by @hjmjohnson in https://github.com/Slicer/Slicer/pull/9098
* ENH: Set application icon to SlicerApp-Real.exe executable by @jamesobutler in https://github.com/Slicer/Slicer/pull/8987
* STYLE: Prefer declaring CMake min max required versions as variables by @jhlegarreta in https://github.com/Slicer/Slicer/pull/8375
* COMP: Update Slicer cert creation with non-archived mozilla repo by @heitbaum in https://github.com/Slicer/Slicer/pull/8973
* BUG: Fix typo in dicom thumbnail size label by @benediktjohannes in https://github.com/Slicer/Slicer/pull/8964
* BUG: Add missing Superclass::setup() calls in 13 module widgets by @mhalle in https://github.com/Slicer/Slicer/pull/9044
* STYLE: Fix typos in the CreateDICOMSeries GUI by @lassoan in https://github.com/Slicer/Slicer/pull/9103
* Update Slicer.crt CA bundle by @slicerbot in https://github.com/Slicer/Slicer/pull/9102
* ENH: Enable Zlib support in DCMTK build by @fedorov in https://github.com/Slicer/Slicer/pull/9107
* Fix translation related errors by @lassoan in https://github.com/Slicer/Slicer/pull/9104
* ENH: Separate SampleData category name and title by @lassoan in https://github.com/Slicer/Slicer/pull/9096
* Update Slicer.crt CA bundle by @slicerbot in https://github.com/Slicer/Slicer/pull/9111
* DOC: Fix typo in MRML overview documentation by @anthonyylee in https://github.com/Slicer/Slicer/pull/9116
* Improve python package installation utilities by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/9010
* BUG: Fix failing extension description tests by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/9112
* COMP: Update CTK to latest (3b3f9eff) by @hjmjohnson in https://github.com/Slicer/Slicer/pull/9097
* COMP: Update ITK to 5.4.6 by @jamesobutler in https://github.com/Slicer/Slicer/pull/9125
* COMP: Update CTK with PythonQt crash fix by @jamesobutler in https://github.com/Slicer/Slicer/pull/9128
* Add DICOM SEG/PM/SR/M3D plugins to Slicer core by @fedorov in https://github.com/Slicer/Slicer/pull/9114
* ENH: Pin transitive dependencies in python-dicom-requirements by @fedorov in https://github.com/Slicer/Slicer/pull/9132
* BUG: Guard null SegmentationNode in qMRMLSegmentEditorWidget by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/9134
* BUG: Resolve QtTesting install library name from imported target by @hjmjohnson in https://github.com/Slicer/Slicer/pull/9137
* Fix dcmqi binary lookup by @fedorov in https://github.com/Slicer/Slicer/pull/9136
* ENH: Add auto-trim of file cache at application startup by @lassoan in https://github.com/Slicer/Slicer/pull/9115
* BUG: Restore removed slicer.util._executePythonModule by @lassoan in https://github.com/Slicer/Slicer/pull/9141
* ENH: Allow Slicer_USE_QtTesting=ON with Qt 6 builds by @hjmjohnson in https://github.com/Slicer/Slicer/pull/9138
* BUG: Fix SampleData module by @lassoan in https://github.com/Slicer/Slicer/pull/9150
* BUG: Fix GetFileNameWithoutExtension() failing when called with no arguments by @jamesobutler in https://github.com/Slicer/Slicer/pull/9152
* Fix CacheManager startup warning by @lassoan in https://github.com/Slicer/Slicer/pull/9159
* Fix test failures by @lassoan in https://github.com/Slicer/Slicer/pull/9162
* DOC: Add two commercial products in the about documentation page by @cpinter in https://github.com/Slicer/Slicer/pull/9168
* BUG: Fix Extension Wizard module creation by @cpinter in https://github.com/Slicer/Slicer/pull/9178
* COMP: Update VTK to 9.6.2 by @jamesobutler in https://github.com/Slicer/Slicer/pull/9166
* DOC: Fix elongation and flatness definitions in segment statistics by @gliu2 in https://github.com/Slicer/Slicer/pull/9177
* COMP: Update python packages to latest by @jamesobutler in https://github.com/Slicer/Slicer/pull/9161
* DOC: Do not show "Edit on GitHub" link for special documentation pages by @lassoan in https://github.com/Slicer/Slicer/pull/9188
* ENH: Add application icon for linux by @lassoan in https://github.com/Slicer/Slicer/pull/9196
* BUG: Fix Qt geometry warning when showing terminology selector by @lassoan in https://github.com/Slicer/Slicer/pull/9197
* COMP: Update CTK to latest version by @lassoan in https://github.com/Slicer/Slicer/pull/9202
* BUG: Reset view action metadata when opening SH widget context menu by @Sunderlandkyl in https://github.com/Slicer/Slicer/pull/9205
* BUG: Clicking visibility icon does not change item selection by @cpinter in https://github.com/Slicer/Slicer/pull/9198
* Add dcmtk JPEG2000 support by @lassoan in https://github.com/Slicer/Slicer/pull/9099
* ENH: Add support for 2D special cases of MatrixOffsetTransform by @dzenanz in https://github.com/Slicer/Slicer/pull/9204
* BUG: Prevent loss of volume rendering opacity transfer function points by @lassoan in https://github.com/Slicer/Slicer/pull/9186
* BUG: Disable default VTK render window keyboard shortcuts by @lassoan in https://github.com/Slicer/Slicer/pull/9194
* BUG: Fix segment metadata off-by-one when loading DICOM Labelmap SEG by @fedorov in https://github.com/Slicer/Slicer/pull/9163
* ENH: Gray out visibility icon of SH item under hidden parent by @lassoan in https://github.com/Slicer/Slicer/pull/9195
* ENH: Deprecate fcsv file format by @lassoan in https://github.com/Slicer/Slicer/pull/9192
* BUG: Show folder opacity before visibility toggle by @vacaslistradas in https://github.com/Slicer/Slicer/pull/9200
* ENH: Keep markup placement preview visible when slice view moves or zooms by @lassoan in https://github.com/Slicer/Slicer/pull/9189
* Minor code fixes by @lassoan in https://github.com/Slicer/Slicer/pull/9213
* COMP: Update CTK with Qt 6.11 build support by @jamesobutler in https://github.com/Slicer/Slicer/pull/9212
* COMP: Raise minimum CMake floor to 3.28 and remove dead version-conditional code by @hjmjohnson in https://github.com/Slicer/Slicer/pull/9210
* BUG: Fix crash when selecting active scalars for several model nodes at once by @lassoan in https://github.com/Slicer/Slicer/pull/9169
* COMP: Update docs dependencies to resolve security advisories by @jamesobutler in https://github.com/Slicer/Slicer/pull/9222
* BUG: Fix unwanted markup measurements by @lassoan in https://github.com/Slicer/Slicer/pull/9216
* BUG: Fixed missing openjp2 shared library by @lassoan in https://github.com/Slicer/Slicer/pull/9227
* COMP: Add missing itkImageRegionIteratorWithIndex.h includes by @hjmjohnson in https://github.com/Slicer/Slicer/pull/9219
* BUG: Fix missing openjp2 shared library in macOS package by @lassoan in https://github.com/Slicer/Slicer/pull/9228
* BUG: Restore slicer.util Python console imports by @ebrahimebrahim in https://github.com/Slicer/Slicer/pull/9220
* BUG: Fix std::regex crash in volume rendering (Qt WebEngine symbol interposition) by @RafaelPalomar in https://github.com/Slicer/Slicer/pull/9231
* BUG: Hide 3D angle line when fewer than 2 points by @lassoan in https://github.com/Slicer/Slicer/pull/9215
* COMP: Add MSVC compatibility check when using Qt 5 by @jamesobutler in https://github.com/Slicer/Slicer/pull/9221
* BUG: Fix terminology selector opening with empty content on repeated opens by @xskere in https://github.com/Slicer/Slicer/pull/9223
* Fix private storable node saving by @lassoan in https://github.com/Slicer/Slicer/pull/9236
* Fix atlastests by @lassoan in https://github.com/Slicer/Slicer/pull/9235
* BUG: Fix qMRMLNodeComboBox::nodeAddedByUser emitted twice by @dparikh79 in https://github.com/Slicer/Slicer/pull/9158
* COMP: Update FindVcvars with support for old toolsets in newer VS by @jamesobutler in https://github.com/Slicer/Slicer/pull/9206
* Update Slicer.crt CA bundle by @slicerbot in https://github.com/Slicer/Slicer/pull/9237
* BUG: Fix crash loading table with unsupported schema column type by @mauigna06 in https://github.com/Slicer/Slicer/pull/9238
* Add option for logarithmic color mapping by @ajallphin in https://github.com/Slicer/Slicer/pull/9016
* BUG: Fix duplicate Opacity slider for segments in subject hierarchy by @lassoan in https://github.com/Slicer/Slicer/pull/9243
* BUG: Disable FP exception trapping for ModelMaker/MergeModels tests on macOS by @RafaelPalomar in https://github.com/Slicer/Slicer/pull/9241
* Fix SubjectHierarchyFoldersTest1, vtkMRMLMarkupsStorageNodeTest2, vtkMRMLVolumePropertyNodeTest1 by @lassoan in https://github.com/Slicer/Slicer/pull/9242
* ENH: Add unique Slicerrc file for custom apps with ability to turn off by @jamesobutler in https://github.com/Slicer/Slicer/pull/9240
* COMP: Add Meta AR video passthrough by @lassoan in https://github.com/Slicer/Slicer/pull/9249
* BUG: Fix incorrect sync of 2D colormap to rendering colormap by @ajallphin in https://github.com/Slicer/Slicer/pull/9250
* BUG: Fix crash exporting series with no local files by @sjh26 in https://github.com/Slicer/Slicer/pull/9251

## New Contributors
* @codeling made their first contribution in https://github.com/Slicer/Slicer/pull/8978
* @isabelfrolick made their first contribution in https://github.com/Slicer/Slicer/pull/9011
* @mhalle made their first contribution in https://github.com/Slicer/Slicer/pull/9045
* @heitbaum made their first contribution in https://github.com/Slicer/Slicer/pull/8973
* @anthonyylee made their first contribution in https://github.com/Slicer/Slicer/pull/9116
* @gliu2 made their first contribution in https://github.com/Slicer/Slicer/pull/9177
* @vacaslistradas made their first contribution in https://github.com/Slicer/Slicer/pull/9200
* @xskere made their first contribution in https://github.com/Slicer/Slicer/pull/9223
* @dparikh79 made their first contribution in https://github.com/Slicer/Slicer/pull/9158
* @ajallphin made their first contribution in https://github.com/Slicer/Slicer/pull/9016

**Full Changelog**: https://github.com/Slicer/Slicer/compare/v5.10.0...v5.12.0
