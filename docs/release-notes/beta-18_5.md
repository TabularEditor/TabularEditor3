- Download [Tabular Editor 3 BETA-18.5](https://cdn.tabulareditor.com/files/TabularEditor.3.BETA-18.5.x86.msi)
- Download [Tabular Editor 3 BETA-18.5 (64 bit)](https://cdn.tabulareditor.com/files/TabularEditor.3.BETA-18.5.x64.msi)
- [All releases](https://docs.tabulareditor.com/projects/te3/en/latest/downloads.html)

## New features in BETA-18.5:

- The Search dialog (CTRL+F) now supports searching the entire model. When this option is selected in the dropdown, another dropdown appears that lets you choose which object properties to search. There are also options for regular expressions, backslash expressions and also [Dynamic LINQ search, similar to Tabular Editor 2.x](https://docs.tabulareditor.com/Advanced-Filtering-of-the-Explorer-Tree.html) (Dynamic LINQ can also be enabled by entering `:` as the first character in the "Find what" field). Search results are displayed in a separate window, and double-clicking on an item in the search results window will take you directly to that item, highlighting the relevant property in the property grid:

![image](https://user-images.githubusercontent.com/30911111/119983803-edd94f80-bfc0-11eb-91cb-aee084e0c83d.png)

- Added support for DAX date literal syntax `dt"2021-05-27"`
- Updated TOM to version 19.21.0

## Bugfixes and minor updates in BETA-18.5:

- Added multiline string editor for table SourceExpressions
- Ensure relationship names are not regenerated when cutting and pasting
- Added BPA support for the `it` keyword in FixExpressions, see https://github.com/otykier/TabularEditor/issues/846
- Improved behavior of Find/Replace window when switching between documents/UI elements
- Fixed a bug with the precedence order of the NOT keyword, see https://github.com/TabularEditor/TabularEditor3/issues/5.
