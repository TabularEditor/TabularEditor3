# Creating your first Analysis Services Model

**Applies to:** &#10060;<del>Desktop Edition</del>, &#10004;Standard Edition, &#10004;Enterprise Edition

This page walks you through the process of creating a new Analysis Services tabular model from scratch using Tabular Editor 3.

```eval_rst
.. important::
    Tabular Editor 3 Standard Edition is limited to `SQL Server Standard Edition <https://docs.microsoft.com/en-us/analysis-services/analysis-services-features-supported-by-the-editions-of-sql-server-2016?view=asallproducts-allversions#tabular-models>`__ and `Azure Analysis Services Basic Tier <https://docs.microsoft.com/en-us/azure/analysis-services/analysis-services-overview#basic-tier>`__. Note that certain modelling features are not supported at these tiers.

    Tabular Editor 3 Desktop Edition does not have any support for Analysis Services tabular models.
    
    `More information </editions.html>`
```

##### Creating a new model

- From the File menu, choose New > Model... or hit `CTRL+N` 

```eval_rst
.. image:: https://user-images.githubusercontent.com/8976200/116813646-02a6fc80-ab55-11eb-89b0-8909b768ce7e.png
  :width: 400
```

- Provide a name for your model or use the default value. Then, choose the compatibility level depending on which version of Analysis Services you are targetting. Your options are the following:
  - 1200 (Works with SQL Server 2016 or newer, and Azure Analysis Services)
  - 1400 (Works with SQL Server 2017 or newer, and Azure Analysis Services)
  - 1500 (Works with SQL Server 2019 or Azure Analysis Services)
- For the best development experience, check the "Use workspace database" option. This requires that you have an instance of Analysis Services available on which your workspace database will be deployed. This could be a local or a remote instance of SQL Server Analysis Services or it could be an instance of Azure Analysis Services. When you click OK, you will be prompted to enter the connection string for the Analysis Services instance in which you want the workspace database created.

```eval_rst
.. note::
    With a workspace database, you can validate Power Query (M expressions) and import table schema from Power Query expressions. You can also refresh and query data in the workspace database, making it easier to debug and test your DAX expressions.
```
