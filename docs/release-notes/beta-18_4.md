# Tabular Editor 3 BETA-18.4 Release Notes

- Download [Tabular Editor 3 BETA-18.4](https://cdn.tabulareditor.com/files/TabularEditor.3.BETA-18.4.x86.msi)
- Download [Tabular Editor 3 BETA-18.4 (64 bit)](https://cdn.tabulareditor.com/files/TabularEditor.3.BETA-18.4.x64.msi)

## New features in BETA-18.4:

- Tabular Editor 3 will now store (encrypted) credentials for data sources in the personal .tmuo file. This is ideal when using a workspace database, as you can then specify a set of credentials different from those defined in the Model.bim file. If you're using version control, make sure to ignore the .tmuo extension. Even though the credentials in the file are encrypted with the Windows user key, the idea is that each developer can have their own .tmuo file containing credentials and preferences that apply only for them, and therefore this file should not be included in version control.
- Tabular Editor 3 now prompts for credentials that are going to be overwritten during a deployment operation, so you no longer have to set the credentials through another tool after deployment. Please note that Power Query data sources will always have their credentials wiped during a deployment operation, so credentials for these types of data sources must be entered upon every deployment.
- Upon creating a new model, you will now have the option to connect to a workspace database immediately (recommended).

## Bugfixes in BETA-18.4:

- Fixed an issue with keyboard shortcuts and certain actions (Undo/Redo, etc.) not always being enabled when switching the focus between different editors.
- Find/replace dialog now has a minimum size to avoid scrollbars.

## Bugfixes in BETA-18.3:

- Improved semantic analyzer performance on large models (regression in BETA-18.x)
- Queuing a data refresh operation should no longer freeze the UI
- Keyboard buttons (left/right arrows and F2 for rename) may now again be used to navigate the Tabular Explorer tree

## Bugfixes in BETA-18.2:

- The DAX parser now correctly recognizes object names containing double quotes (see issue #22).

## New features in BETA-18.1:

- Update Table Schema from Power Query sources (see below)

## Bugfixes in BETA-18.1:

- Tabular Editor will now remember skin settings between upgrades
- Fixed a bug with lineage tags causing crashes when copying Calculated Tables or Calculation Group Tables
- Fixed a false error on the COALESCE and COMBINEVALUES DAX functions
- Included Microsoft.AnalysisServices.dll in the distribution, which should ensure that Tabular Editor can properly import/export VPAX files
- Tabular Editor will now automatically reestablish connection to AS for data refresh purposes

## Update Table Schema from Power Query sources

A new release of the Tabular Editor 3 beta is here. And I'm really excited about this one, for one particular reason: 

For the first time ever, Tabular Editor can now detect schema changes on Power Query data sources and partitions. And not just for relational data sources, but for ANY Power Query expression that can be evaluated by your Analysis Services engine. "How on earth is that even possible?!?", you might be thinking. Well, pay close attention to that last sentence: "ANY Power Query expression that can be evaluated by your Analysis Services engine".

A little known fact about the Analysis Services engine is that it is actually a transactional system. This means that we can start a transaction against a database that is already deployed on Analysis Services, make some metadata changes, refresh some data, query some data and then finally roll back the transaction, leaving the database in the original state as if we didn't even touch it at all.

So, in order to detect schema changes for Power Query partitions, Tabular Editor 3 will now add a hidden, temporary table to the model, populate that table using the M-function [`Table.Schema`](https://docs.microsoft.com/en-us/powerquery-m/table-schema) on the source query that we want to detect the schema for. Then, that temporary table is refreshed on the server (using the credentials that are already present on the server to access the data source) - this refresh only takes a split second, thanks to query folding happening inside the M engine. Finally, Tabular Editor will query the table to read the schema, before rolling back the entire transaction. The result:

![image](https://github.com/TabularEditor/TabularEditor3/blob/master/media/update%20schema.gif?raw=true)

The only caveat is of course that Tabular Editor 3 has to be connected to an instance of Analysis Services, but it doesn't matter whether or not the model you're working with holds any data - as long as the credentials to the data sources are stored in AS (and AS can actually access the data source). This technique is particularly useful if you use Tabular Editor 3's [workspace mode](https://docs.tabulareditor.com/Workspace-Database.html).

In addition to detecting column names and data types, Tabular Editor 3 will also let you update the Description property from the source (if present). On SQL Server sources, this would be the MS_Description extended property. If a column is renamed in the source, it will show up in the Apply Schema Changes dialog as a column import and a column remove. However, as shown in the GIF above, if you Ctrl+Right Click on these two schema changes, you can combine them as a single "rename source column" schema change. The advantage of this approach, is that Tabular Editor 3 will automatically fix up any DAX expressions that reference the renamed column.

### Limitations in this release:

- The schema compare option is only available for Power Query partitions while Tabular Editor is connected to an instance of Analysis Services
- Schema compare while offline will only be available for Legacy (Provider) partitions, similar to Tabular Editor 2.X. However, this functionality is not included in BETA-18.1, as I am initially looking for feedback on schema compare for Power Query partitions. Both this feature and the Import Tables Wizard will be available in the next beta release.
- This feature can be used on a Power BI Desktop model as well, but keep in mind that adding/modifying/deleting columns on a table is not among the [supported modeling operations for External Tools](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-external-tools#data-modeling-operations). Also, be aware that Power BI Desktop may be caching metadata for certain types of data sources, so you may have to run a refresh within Power BI Desktop before Tabular Editor can pick up the schema changes.
