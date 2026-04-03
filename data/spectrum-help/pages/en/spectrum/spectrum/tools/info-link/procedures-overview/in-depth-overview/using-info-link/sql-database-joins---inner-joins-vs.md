---
title: "SQL Database Joins - Inner Joins vs. Outer Joins | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/sql-database-joins---inner-joins-vs.-outer-joins"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/sql-database-joins---inner-joins-vs.-outer-joins"
---

# SQL Database Joins - Inner Joins vs. Outer Joins

When creating queries or reports with more than one table, it is important to understand the various types of database joins. The following sections discuss the specifics of inner joins and outer joins.

## Inner Joins

Most programs default to an inner join when two tables are connected. Normally when you join a detailed table to a master table, an inner join is the correct type of join. The values that connect the two tables together must be in both tables. To illustrate, if you had a job number without phases set up, the query would not select any data for that job.
Note: To find records in a table that do not have corresponding records in another table, use the Access Query Wizard to create a Find Unmatched Query.
Another example of this type of join is the Open Invoice to the Customer Master. Additionally, one-to-one relationships use this join type. For example: the P/R Employee Master Files 1, 2 and 3.

## Outer Joins

Use outer joins to include all of the records from one table and records from
 another table only where the joined columns match. A perfect example is the Job Cost
 History file. This table contains posted details from many different modules. Let us say
 that you want to create a report showing all job cost transactions and information
 specific to the vendor or employee for A/P and P/R transactions. A record originating in
 the A/P module will have a vendor code associated with it, but no employee code. A
 record from the P/R module will be exactly the opposite — an employee code, but no
 vendor code.
If you were using Microsoft Access in this scenario, Access would automatically create the joins when these three tables are added in the query window. (All of the joins would default as inner joins.)
If you ran this query, it would return a no data message. Access would attempt to find job cost transactions that have a vendor code matching the A/P Vendor Master file and an employee code matching the P/R Employee Master file. Obviously, there are no transactions that have both pieces of data.
Consider changing the join properties as follows. To access the Join Properties dialog box, right-click on the join line between the tables and select Join Properties. Set the join between the JC Transaction History file and the A/P Vendor Master File to include ALL records from JC Transaction History and only matching records from the A/P Vendor Master file. Change the join between the other two files to match. Include ALL records in the JC Transaction History.
Include only matching records in the P/R Employee Master file.
As you can see, this process changes the appearance of the join line from a simple line to an arrow. The arrow points from the table from which you are selecting ALL records and points to the table selecting only matching records.
Not only does the query retrieve records that have a vendor code or an employee code, but also records that don't have either code. The query selects ALL records from the JC Transaction History file and grabs the matching data from the other two tables. For the unmatched transactions, it simply leaves the Vendor_Name and Employee_Name fields blank.
The same join properties and settings are available in Excel. To modify/change the join properties in Excel, double-click the join line. A dialog box similar to the one used in Access appears, and you will be prompted to enter the desired join type.
The join properties in Crystal Reports differs from Excel and Access in that it differentiates between left and right outer joins, and includes additional join property choices. Once you have selected the tables for your report, click the Database pull-down menu and select Visual Linking Expert. The tables appear with the standard inner joins automatically inserted. Click the link you wish to modify, and then click the Options button at the bottom of the screen. The following screen will appear:
The SQL join types are listed in the bottom right-hand corner. The Equal join is the same as the Inner join. The Left Outer and Right Outer joins are synonymous with Outer joins. Crystal reports simply makes a distinction as to the physical placement of one table to another in the Visual Linking Expert. For more information about the remaining join types listed here, or more detailed information about the inner and outer join types, see the Crystal Reports Help files. These files contain strong, clear definitions of the different join types.
