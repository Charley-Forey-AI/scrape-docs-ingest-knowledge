---
title: "User Security Maintenance | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/info-link/info-link-screens-overview/user-security-maintenance"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/tools/info-link/info-link-screens-overview/user-security-maintenance"
---

# User Security Maintenance

User Security Maintenance is used to set security levels for operators with access to Spectrum information from Info-Link.
If un-updated entries are present, the status line above the list box indicates security changes are pending. Select Update Database to apply current settings. Select Listing to generate a listing of all established operator security levels.
When a user initiates a query, Info-Link requires entry in the company and operator ID fields. The system then searches the tables defined in [Table Security Maintenance](/en/spectrum/spectrum/tools/info-link/info-link-screens-overview/table-security-maintenance) and builds a list of all the tables the user can access.
Normally the write access levels are 0, meaning that users cannot write to the database.
Fields/ButtonsDescriptions
CompanyEnter the company code for this user. The company code must be the same as the Spectrum company code.
Database userEnter an identification code to grant this user access to Info-Link. Once you create a username, Info-Link creates a corresponding username in SQL Server by appending this username to the company ID.
PasswordEnter a password that is 10 - 24 characters. All Info-Link user passwords are encrypted and whenever records are added or modified, the records automatically store the password.
For security purposes, the password displays as asterisks on the screen. Note that the company / division code and operator ID re-display in the lower portion of the screen.
To change the user's Info-Link password, enter a new one.

Table categoryOrdinarily, table categories have the same initials as the module (for example, JC for Job Cost, PR for Payroll). You may edit them if you want.
The only requirement is that they match the table categories defined in Table Security Maintenance.
Enter the 8-character table category code. This should match at least one category defined in Table Security Maintenance.
Read access level (1-9)Enter a number 1 through 9 to define the security level to be used for this user when reading tables. If the level is less than or equal to the level defined for a table, the user will be able to view the information contained in that database table.
Write access level (1-9)Assign level 1.
Most if not all Operators use Info-Link only for reading information in the application; they don’t use it to write to database tables.
If an Operator should have write permission, enter a number higher than 1 to define the security level to be used for this user when writing to tables. If the security level defined for a table is equal to or greater than what you assign here, the user will be able to write to the table.

ListingSelect to display the User Security Report starting screen.
Update DatabaseDisplays when there are pending changes to be applied. Select to update all records and return to the main screen.
