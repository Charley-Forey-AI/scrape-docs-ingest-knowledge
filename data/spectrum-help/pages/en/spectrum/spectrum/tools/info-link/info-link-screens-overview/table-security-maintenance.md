---
title: "Table Security Maintenance | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/info-link/info-link-screens-overview/table-security-maintenance"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/info-link/info-link-screens-overview/table-security-maintenance"
---

# Table Security Maintenance

Use this screen to build a list of Spectrum data tables (or views) that can be accessed with Info-Link.
You can assign security categories and levels to each table or view.
Each operator whose security level is greater than or equal to the security level for the table can access the information in the table.
If un-updated entries are present, the status line above the list box indicates security changes are pending. Select Update Database to apply current settings.
Fields/ButtonsDescriptions
Table/view categoryLeave this field blank to view all tables available for Info-Link.
Enter the category code for the tables you wish to add or change. The user security needs to match the category code entered here.
Ordinarily, table categories have the same initials as the module (for example, JC for Job Cost, PR for Payroll). You may edit them if you want - for example, you might have several different categories for different job cost tables.
The only requirements are that they match the table categories defined in Table Security Maintenance and each table or view be assigned to only one category.
Partial table nameApplicable only after you have created a list of tables.Press Enter to view all of the defined tables, or enter a partial table name.

Table/view nameEnter the desired table or view name, or use the dropdown list to display a search window that shows all available tables and views and their associated descriptions. Table names ending in “_MC” allow access to all rows for all companies whereas other tables normally only allow access to the operator’s current company (as determined by the first three letters of the operator ID).
Table categoryDisplays the same table category as entered above.
Read access levelEnter a number 1 through 9 to define the security level for this table. If the level is less than or equal to the level defined for an operator, the operator will be able to view the information contained in that database table.
Write access levelAssign level 0 to all users who should not write to the table, regardless of their security setup.
Most if not all Operators use Info-Link only for reading information in the application; they don’t use it to write to database tables.
If an Operator should have write permission, enter a number 1 through 9 to define the security level to be used for this user when writing to tables. If the security level defined for a table is equal to or greater than what you assign here, the user will be able to write to the table.

ListingSelect to display the Table Security Report starting screen.
