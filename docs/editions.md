# Tabular Editor 3 Editions

## Supported Data Modelling Scenarios

The main difference between the various editions of Tabular Editor 3, is which types of tabular data modelling scenarios they support. To understand this difference, consider that Analysis Services (Tabular) exists in a number of different "flavors":

- Power BI Desktop
- Power BI Premium through the XMLA Endpoint (Premium Per User or **Premium/Embedded Capacity gen1/gen2**)
- **Power BI Report Server**
- SQL Server (2016+) Analysis Services (Developer, Standard, **Enterprise editions**)
- Azure Analysis Services (Developer, Basic, **Standard tiers**)

We consider the highlighted "flavors" of Analysis Services to be Enterprise-Tier, and as such, these may only be used with Tabular Editor 3 Enterprise Edition. Please refer to the matrix below for the full overview of supported scenarios:

|Scenario / Edition|Desktop|Standard|Enterprise
|---|---|---|---|
|External Tool for Power BI Desktop|&#10004;|&#10004;|&#10004;|
|Load/save model metadata to disk*|&#10060;|&#10004;|&#10004;|
|Workspace Mode†|&#10060;|&#10004;|&#10004;|
|Power BI Premium Per User|&#10060;|&#10004;|&#10004;|
|SQL Server Developer Edition|&#10060;|&#10004;‡|&#10004;|
|SQL Server Standard Edition|&#10060;|&#10004;|&#10004;|
|SQL Server Enterprise Edition|&#10060;|&#10060;|&#10004;|
|Azure AS Developer Tier|&#10060;|&#10004;‡|&#10004;|
|Azure AS Basic Tier|&#10060;|&#10004;|&#10004;|
|Azure AS Standard Tier|&#10060;|&#10060;|&#10004;|
|Power BI Report Server|&#10060;|&#10060;|&#10004;|
|Power BI Premium Capacity (P SKUs)|&#10060;|&#10060;|&#10004;|
|Power BI Embedded Capacity (A/EM SKUs)|&#10060;|&#10060;|&#10004;|

\***Note:** Supported file formats are: **.pbit** (Power BI Template), **.bim** (Analysis Services model metadata), **.vpax** (VertiPaq Analyzer) and **database.json** (Tabular Editor folder structure).

†**Note:** Workspace Mode allows Tabular Editor 3 to simultaneously save model metadata to disk and synchronize a database on any of the editions of Analysis Services supported by the Tabular Editor 3 edition purchased.

‡**Note:** Enterprise Edition is required if the Analysis Services data model contains perspectives or tables with multiple partitions.

## Modelling Restrictions for non-Power BI models

Specifically for Analysis Services (not Power BI) data models, we restrict a few data modelling operations inside Tabular Editor 3 as well, corresponding to the restrictions on Azure Analysis Services Basic Tier and SQL Server Analysis Services Standard Edition:

|Modelling Feature / Edition|Standard|Enterprise
|---|---|---|
|Perspectives|&#10060;|&#10004;|
|Multiple partitions|&#10060;|&#10004;|

There are no other feature differences between the Tabular Editor 3 editions, than the ones listed above. 

## Modelling Restrictions for Power BI models

There are no feature differences across the Tabular Editor 3 editions for Power BI data models.

```eval_rst
.. note::
    Please keep in mind that Power BI Desktop `currently does not support all Data Modelling operations <https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-external-tools#data-modeling-operations>`__. For this reason, Tabular Editor 3 by default blocks operations that are not supported by Power BI Desktop. However, this restriction can be removed under Tools > Preferences > Power BI.
```

## Personal vs. Transferable licenses

Our Desktop Edition and Standard Editions uses a personal licensing model. This means, that a user receives their own personal License Key, which can not be shared or transferred to other users. When a user no longer requires the product, their subscription should be cancelled to avoid recurring payments.

Our Enterprise Edition uses a transferable licensing model. This means, that multiple users can share the same license key. Each license holds a number of "seats" up to the purchased quantity. Once a user activates their installation of Tabular Editor 3, they will occupy a seat in the license. When a user no longer requires the product, <a href="mailto:support@tabulareditor.com?subject=Transferable%20License%20Rotation">contact support</a> in order to free the seat for another user.

## Enterprise Edition Volume Discounts

Our Enterprise Edition is priced in tiers, according to the following table (similar discount rates apply to monthly commitment):

|Tier|Yearly price per seat|
|---|---|
|First 5 seats|$950.00 USD|
|Next 6-10 seats|$900.00 USD|
|Next 11-20 seats|$850.00 USD|
|Next 21-50 seats|$800.00 USD|
|Seats 51 and above|$750.00 USD|

As an example, if you need 12 seats, the price breaks down as follow:

```
Seats 1-5:    5 x 950.00 = $  4,750.00
Seats 6-10:   5 x 900.00 = $  4,500.00
Seats 11-12:  2 x 850.00 = $  1,700.00
--------------------------------------
Total                      $ 10,950.00
======================================
```

If you require more than 100 seats, please <a href="mailto:sales@tabulareditor.com">contact sales</a> for a quote.
