# Tabular Editor 3 Editions

## Supported Data Modelling Scenarios

The main difference between the various editions of Tabular Editor 3, is which types of tabular data modelling scenarios they support. To understand this difference, consider that Analysis Services (Tabular) exists in a number of different "flavors":

- Power BI Desktop
- Power BI Premium through the XMLA Endpoint (Premium Per User or **Premium/Embedded Capacity gen1/gen2**)
- **Power BI Report Server**
- SQL Server (2016+) Analysis Services (Developer, Standard, **Enterprise editions**)
- Azure Analysis Services (Developer, Basic, **Standard tiers**)

We consider the highlighted "flavors" of Analysis Services to be Enterprise-Tier, and as such, these may only be used with Tabular Editor 3 Enterprise Edition. Please refer to the matrix below for the full overview of supported scenarios:

|Scenario|Desktop Edition|Standard Edition|Enterprise Edition
|---|---|---|---|
|Use Tabular Editor 3 as an External Tool for Power BI Desktop|&#10004;|&#10004;|&#10004;|
|Load/save model metadata to disk*|&#10060;|&#10004;|&#10004;|
|Power BI Premium Per User workspaces|&#10060;|&#10004;|&#10004;|
|SQL Server Analysis Services Developer Edition|&#10060;|&#10004;\*\*|&#10004;|
|SQL Server Analysis Services Standard Edition|&#10060;|&#10004;|&#10004;|
|SQL Server Analysis Services Enterprise Edition|&#10060;|&#10060;|&#10004;|
|Azure Analysis Services Developer Tier|&#10060;|&#10004;\*\*|&#10004;|
|Azure Analysis Services Basic Tier|&#10060;|&#10004;|&#10004;|
|Azure Analysis Services Standard Tier|&#10060;|&#10060;|&#10004;|
|Power BI Report Server|&#10060;|&#10060;|&#10004;|
|Power BI Premium Capacity Workspaces (P SKUs)|&#10060;|&#10060;|&#10004;|
|Power BI Embedded Workspaces (A/EM SKUs)|&#10060;|&#10060;|&#10004;|

\***Note:** Supported file formats are: **.pbit** (Power BI Template), **.bim** (Analysis Services model metadata), **.vpax** (VertiPaq Analyzer) and **database.json** (Tabular Editor folder structure).

\*\***Note:** Enterprise Edition is required if the Analysis Services data model contains perspectives or tables with multiple partitions.

Specifically for Analysis Services (not Power BI) data models, we restrict a few data modelling operations inside Tabular Editor 3 as well, corresponding to the restrictions on Azure Analysis Services Basic Tier and SQL Server Analysis Services Standard Edition:

|Feature|Standard Edition|Enterprise Edition
|---|---|---|
|Perspectives|&#10060;|&#10004;|
|Multiple partitions|&#10060;|&#10004;|

There are no other feature differences between the Tabular Editor 3 editions, than the ones listed above. 

```eval_rst
.. note::
    Please keep in mind that Power BI Desktop `currently does not support all Data Modelling operations <https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-external-tools#data-modeling-operations>`__. For this reason, Tabular Editor 3 by default blocks operations that are not supported by Power BI Desktop. However, this restriction can be removed under Tools > Preferences > Power BI.
```
