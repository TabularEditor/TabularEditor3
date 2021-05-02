# Creating your first Power BI dataset

**Applies to:** &#10060;<del>Desktop Edition</del>, &#10004;Standard Edition, &#10004;Enterprise Edition

This page walks you through the process of creating a new Power BI dataset from scratch using Tabular Editor 3.

```eval_rst
.. important::
    Tabular Editor 3 Standard Edition is limited to <a href="https://docs.microsoft.com/en-us/power-bi/admin/service-premium-per-user-faq">Power BI Premium Per User</a>. For Power BI Premium or Embedded capacity, you must upgrade to Tabular Editor 3 Enterprise Edition. In either case, the Power BI workspace in which the dataset is to be deployed, must have its <a href="https://docs.microsoft.com/en-us/power-bi/admin/service-premium-connect-tools#enable-xmla-read-write">XMLA read/write endpoint enabled</a>.

    Tabular Editor 3 Desktop Edition does not have any support for Power BI datasets.
```

1. From the File menu, choose New > Model... or hit `CTRL+N`

![image](https://user-images.githubusercontent.com/8976200/116811596-860f2080-ab4a-11eb-917b-20501c1b52ef.png)

- Provide a name for your model or use the default value. Then, set the compatibility level to "1560 (Power BI Dataset)".
- For the best development experience, check the "Use workspace database" option. This requires that you have a development workspace available in Power BI, with XMLA read/write enabled.