# Creating your first Analysis Services Model

**Applies to:** &#10060;<del>Desktop Edition</del>, &#10004;Standard Edition, &#10004;Enterprise Edition

This page walks you through the process of creating a new Analysis Services tabular model from scratch using Tabular Editor 3.

```eval_rst
.. important::
    Tabular Editor 3 Standard Edition is limited to `SQL Server Standard Edition <https://docs.microsoft.com/en-us/analysis-services/analysis-services-features-supported-by-the-editions-of-sql-server-2016?view=asallproducts-allversions#tabular-models>`__ and `Azure Analysis Services Basic Tier <https://docs.microsoft.com/en-us/azure/analysis-services/analysis-services-overview#basic-tier>`__. Note that certain modelling features are not supported at these tiers.

    Tabular Editor 3 Desktop Edition does not have any support for Analysis Services tabular models.
```

##### Creating a new model

- From the File menu, choose New > Model... or hit `CTRL+N` 

![image](https://user-images.githubusercontent.com/8976200/116811279-d5545180-ab48-11eb-8060-ebc1941e60ef.png)

- Provide a name for your model or use the default value. Then, choose the compatibility level depending on which version of Analysis Services you are targetting. Your options are the following:
  - 1200 (Works with SQL Server 2016 or newer, and Azure Analysis Services)
  - 1400 (Works with SQL Server 2017 or newer, and Azure Analysis Services)
  - 1500 (Works with SQL Server 2019 or Azure Analysis Services)
- For the best development experience, check the "Use workspace database" option. This requires that you have an instance of Analysis Services available on which your workspace database will be deployed. This could be a local or a remote instance of SQL Server Analysis Services or it could be an instance of Azure Analysis Services.

