# Creating your first Analysis Services Model

**Applies to:** &#10060;<del>Desktop Edition</del>, &#10004;Business Edition, &#10004;Enterprise Edition

This page walks you through the process of creating a new Analysis Services tabular model from scratch using Tabular Editor 3.

```eval_rst
.. important::
    Tabular Editor 3 Business Edition is limited to `SQL Server Standard Edition <https://docs.microsoft.com/en-us/analysis-services/analysis-services-features-supported-by-the-editions-of-sql-server-2016?view=asallproducts-allversions#tabular-models>`__ and `Azure Analysis Services Basic Tier <https://docs.microsoft.com/en-us/azure/analysis-services/analysis-services-overview#basic-tier>`__. Note that certain modelling features are not supported at these tiers.

    Tabular Editor 3 Desktop Edition does not have any support for Analysis Services tabular models.
    
    `More information </editions.md>`__.
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

Once your model is created, the next step is to add a data source and some tables.

#### Adding a data source and tables

Before you can import data to your tabular model, you have to set up one or more data sources. Locate the TOM Explorer, right-click on the "Data Sources" folder and choose "Create". For a model that uses compatibility level 1400 or higher, we have two options: Legacy and Power Query data sources. To learn more about th differences between these two types of data sources, [consult the Microsoft Analysis Services blog](https://docs.microsoft.com/en-us/archive/blogs/analysisservices/using-legacy-data-sources-in-tabular-1400).

```eval_rst
.. image:: https://user-images.githubusercontent.com/8976200/124598010-72db4280-de64-11eb-818a-e5793f061185.png
  :width: 400
```

In this example, we will create a Power Query data source, which we will use to import a few tables from a SQL Server relational database. Once the data source is created, hit F2 to rename it and configure the data source using the Propery Grid as seen in the screenshot below:

```eval_rst
.. image:: https://user-images.githubusercontent.com/8976200/124599856-71ab1500-de66-11eb-8ede-3a6272872734.png
  :width: 400
```

In our example, we set the following properties:

| Property | Value |
|---|---|
| Name | `AdventureWorks` |
| Protocol | `tds` |
| Database | `AdventureWorksDW2017` |
| Server | `localhost` |
| AuthenticationKind | `ServiceAccount` |

Hit Save (Ctrl+S). You will be prompted to provide a path and file name for the Model.bim file which will hold the model metadata that you have created so far. You may also save the model as a folder structure instead (File > Save to folder...), which is recommended if you plan to integrate your model metadata into a version controlled environment. If you are using a Workspace Database, Tabular Editor 3 will also synchronize the metadata to the connected instance of Analysis Services.

Next, add a new table to the model by right-clicking on the "Tables" folder and choosing "Create > Table" (you can also hit Alt+5). Give the table a name, in our example `Internet Sales`. Expand the table, locate the partition on the table and provide the following M query as the partition expression, in order to populate the table with data:

```M
let
    Source = #"AdventureWorks",
    Data = Source{[Schema="dbo",Item="FactInternetSales"]}[Data]
in
    Data
```

This assumes that the relational SQL Server database contains a table named "FactInternetSales" within the "dbo" schema.

```eval_rst
.. image:: https://user-images.githubusercontent.com/8976200/124601212-dd41b200-de67-11eb-9720-3890d7d746ba.png
  :width: 600
```

Next, right-click on the newly created table and choose "Update table schema...". This allows Tabular Editor to automatically populate the table columns based on the partition query.

```eval_rst
.. note::
    If you are not using a Workspace Database, this operation is only available in Tabular Editor version 3.1.0 or newer.
```

```eval_rst
.. image:: https://user-images.githubusercontent.com/8976200/124601333-0104f800-de68-11eb-94f7-654c9e8ff206.png
  :width: 650
```

Hit "OK" to add the columns to the table. Hit Save again (Ctrl+S). If you are using a Workspace Database, you may refresh the table on the server and browse the data in the table once the refresh operation is complete. To do so, right-click the table and choose "Refresh table > Automatic (table)". Wait for the operation on the "Data Refresh" tab to complete, then right-click the table and choose "Preview" (you can do so from the TOM Explorer as well), to view the actual data within the table:

```eval_rst
.. image:: https://user-images.githubusercontent.com/8976200/124602234-f0a14d00-de68-11eb-8886-dc7e0d255f9a.png
  :width: 650
```

If the table you imported is a dimension table, we recommend setting the "Key" property of the primary key column on the table, to "true". This makes it easier to define relationships between this and other tables, as we shall see later.

Repeat this process for any table you wish to import to your Tabular model. You don't have to refresh the data in each table one by one - instead, you can run the refresh operation at the model level.

#### Defining relationships

Once you have imported a number of tables, the easiest way to define the relationships between them with Tabular Editor 3, is to create a new diagram. Choose "File > New > Diagram". Then, multi-select and drag the tables into the diagram view or right-click on the tables and choose "Add to diagram":

```eval_rst
.. image:: https://user-images.githubusercontent.com/8976200/124602823-8a68fa00-de69-11eb-9332-09ad42c4f1b3.png
  :width: 350
```

To create a relationship between two tables, locate the foreign key column on the fact table and "drag" that column to the primary key column on the dimension table. Hit "OK" to confirm the relationship settings in the dialog that appears.

```eval_rst
.. image:: https://user-images.githubusercontent.com/8976200/124604764-8f2ead80-de6b-11eb-88d0-c9cebbca57d0.png
  :width: 450
```

Close the diagram view (no need to save it, as you can always reconstruct the diagram later). Hit Ctrl+S once again to save the model. Now it's time to add some business logic. If you're using a Workspace Database, now is a good time to execute a refresh (automatic or calculate) at the model level, to ensure that the supporting structures for the relationships are created on the server, thus bringing the model into a queryable state.

#### Adding measures

Select one of the tables in the TOM Explorer and hit Alt+1 (or choose Create > New Measure) to add a measure to that table. Give the measure a name and provide a DAX expression for the measure.

```eval_rst
.. image:: https://user-images.githubusercontent.com/8976200/124605349-19771180-de6c-11eb-94be-7baf8b5e0ee9.png
  :width: 450
```

Hit Ctrl+S to save the model metadata.

If you're using a Workspace Database, you can now test your new measure directly inside Tabular Editor 3. The easiest way to test it is by using a Pivot Grid. Choose File > New > Pivot Grid, then drag the newly created measure from the TOM Explorer into the grid. You can also drag columns and hierarchies from the TOM Explorer into the Filter, Row or Column area of the Pivot Grid, to slice your measure by different dimension attributes:

```eval_rst
.. image:: https://user-images.githubusercontent.com/8976200/124605906-ae7a0a80-de6c-11eb-985d-6fd580ed81d1.png
  :width: 300
```

If you didn't use a Workspace Database, you will have to deploy your model to an instance of Analysis Services, before you can perform data refreshes and query the model.

#### Deploying the data model

To deploy the model metadata to any instance of Analysis Services, click on the "Model" menu and choose "Deploy...". This brings up the Tabular Editor 3 Deployment Wizard which is similar to the Deployment Wizard of Tabular Editor 2.X. Follow the instructions on the various pages of the wizard, to deploy the model metadata to an instance of Analysis Services. You can also use the Deployment Wizard to generate a TMSL/XMLA script, that can be handed over to an Analysis Services server administrator for manual deployment.

```eval_rst
.. image:: https://user-images.githubusercontent.com/8976200/124607262-f5b4cb00-de6d-11eb-8139-4f74b5ae19bf.png
  :width: 450
```

To refresh and test the deployed database, you can use the standard management and client tools provided by Microsoft, or you can use another instance of Tabular Editor 3 (assuming you have administrative access on the instance of Analysis Services where the deployed model resides).

The paragraph above provides a good reason for using the Workspace Database approach described above. When connected to a workspace database, you will be able to perform all development operations, including data refresh and testing of business logic within the same instance of Tabular Editor 3, without having to rely on other tools.
