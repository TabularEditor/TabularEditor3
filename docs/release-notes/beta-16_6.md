# Tabular Editor 3 BETA-16.6 Release Notes

- Download [Tabular Editor 3 BETA-16.6](https://cdn.tabulareditor.com/files/TabularEditor.3.BETA-16.6.x86.msi)
- Download [Tabular Editor 3 BETA-16.6 (64 bit)](https://cdn.tabulareditor.com/files/TabularEditor.3.BETA-16.6.x64.msi)

## Updates in BETA-16.6:

- Fixed an issue with the "Group By Columns" collection editor's Add-button.
- Changed the default Compatibility Level for new Power BI Datasets to 1560.
- Allow creation of new table-level objects (measures, columns, hierarchies) when the currently selected object is a table-level object itself.

## Updates in BETA-16.5:

- Installer should now correctly register Tabular Editor 3 as an external tool for Power BI Desktop
- Added the "-nosplash" CLI option, which is used when Power BI Desktop launches Tabular Editor 3, as the splash screen could sometimes cause Tabular Editor 3 to become "hidden" behind Power BI Desktop. After upgrading Tabular Editor 3, make sure you restart Power BI Desktop.
- Download links now uses our Azure CDN which is where we will host Tabular Editor 3 binaries going forward. The following URLs always point to the latest version of Tabular Editor 3:
  - https://cdn.tabulareditor.com/files/latest/TabularEditor.3.x86.msi
  - https://cdn.tabulareditor.com/files/latest/TabularEditor.3.x64.msi

## Updates in BETA-16.4:

A rather big list of bug fixes and minor improvements incoming:

### General improvements:
- Name of .pbix file is now used as the database name when saving a .pbix model as a .bim/folder structure.
- Added x64 support (both x64 and x86 builds are targeting "Any CPU", but the latter has the "Prefer32Bits" flag set)
- Installer has been updated. It's now using WiX, which ensures that the registry and local app data folder are neatly cleaned when the product is uninstalled. In addition, it looks better :-)
- Macro recorder now supports recording of most (all?) model changes that can be done through the UI
- Added support for multi-column scalar predicates, which is a new DAX syntax that was added recently. Tabular Editor tries to guess which version of Analysis Services is used based on the model metadata, but since this is not always possible (e.g. when working offline), you can override how Tabular Editor treats multi-column scalar predicate table filter expressions under Tools > Preferences > DAX Editor > General > Semantic Engine Features).
- Updated TOM to version 19.18.0.

### Usability improvements:
- Increased the "hitbox" of the expand/collapse arrow in TOM Explorer increased (see [this comment](https://github.com/TabularEditor3/PublicPreview/issues/81#issuecomment-789637586))
- Double-clicking the icon next to an object in the TOM Explorer now brings the DAX Expression Editor into view.

### Bug fixes:
- Fixed DAX semantic analyzer issue, which would cause "ghost" error messages in certain expressions
- Fixed issue #75 
- Fixed issue #77
- Fixed issue #84
- Fixed a number of crashes based on telemetry. @**Everyone**: Keep sending those error reports when an exception occurs, and please provide descriptions - they are invaluable when trying to figure out what went wrong! Thanks!

## Updates in BETA-16.3:

- "Custom Actions" have been renamed to "Macros".
  - There's a new window that lets you manage all macros currently defined. Edit an existing macro by doubleclicking on an item.
  - Once a C# script is saved as a macro, the document will update the macro on subsequent saves (Ctrl+S). Use File > Save As... if you need to save the script as a file.
  - Macros can have identical names. They are distinguished internally using an auto-assigned ID.
  - Fixed an issue that prevented a macro from being saved
- The Window menu now also contains a "New" submenu, containing the same menu items as "File > New"
- Inactive toolbars and menus are now hidden by default, to reduce UI cluttering (can be changed in Tools > Preferences > User Interface).
- Fixed a DAX parser bug that caused `GENERATESERIES` to provide a table with a wrongly-named column, possibly related to #61
- Fix for issue #74 (EndBatch() called before BeginBatch() crash)
- Added warning and refresh of local TOM tree upon save to DB, if changes were made to the deployed model metadata outside of Tabular Editor


## Updates in BETA-16.2:

- Table Preview can now auto-refresh similar to DAX queries/pivot grids (see issue #73)
- Fixed a bug that would prevent Table Preview from showing a calculated table that had not been refreshed
- DAX script support for creating calculated columns and calculated tables
- DAX scripts can now be partially executed (see issue #69). 4 buttons should light up on the "DAX Script" toolbar, when editing a DAX script. These buttons have the following shortcuts:
  - `F5` will apply the full script.
  - `Shift+F5` will apply the full script and also sync the connected database.
  - `F8` will apply only the current selection.
  - `Shift+F8` will apply the current selection and sync the connected database.
- Added a watermark to the diagram view to guide users on how to add tables to the diagram (see issue #76)
- Background Best Practice Analysis should no longer freeze the UI (see issue #79)
- Toolbar buttons/context menu options for ignoring rules/objects on the Best Practice Analyzer view, should now work correctly
- The "please wait" form should no longer overlap any dialogs being spawned from a C# script
- Various bug fixes (possibly related to issue #74)

## Updates in BETA-16.1:

- Measures now use a "calculator" icon, to better align the experience with Power BI Desktop. Calculation Item icons have also been changed slightly, so that they are distinguishable from measures.
- Key columns are now shown in **bold**
- Added "Define Measure" and "Inline Measure" refactoring options
- Improved auto-complete behaviour around DEFINE / EVALUATE statements of DAX queries. For example, autocomplete can now also suggest measures, columns and tables defined inside the query.
- Auto-complete now also suggests measures for the Name parameter of functions such as SUMMARIZECOLUMNS, ADDCOLUMNS, etc., completing both the Name and the Expression parameter at once: 
![autocomplete names](https://user-images.githubusercontent.com/8976200/107629428-66aada80-6c62-11eb-91e4-d5528947840a.gif)
- Revisited #42.
- Deployment Wizard now stores deployment preferences (destination + options) to the .tmuo file sitting next to the Model.bim or Database.json file on disk. This makes it easier to perform deployments when switching between different models, if each model is always deployed to the same destination.
- Updated TOM to 19.16.3. Should fix issue #63.
- Fixed issue #64.
- Fixed a bug with model files appearing in the "Recent Files" menu.

## Updates in BETA-16.0:

- Deployment Wizard updated. Also fixes issue #42 and #43.
- Support for DEFINE COLUMN and TABLE syntax in DAX queries
- The File menu now has a "Recent Files" and a "Recent Tabular Models" submenu. The former holds references to the 10 most recent DAX scripts, model diagrams, DAX queries and C# scripts that were saved/opened. The latter holds references to the 10 most recent model files (bim / pbit / folder).
- Fixed #67 
- Fixed #66 