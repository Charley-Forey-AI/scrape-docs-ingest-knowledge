---
title: "SM Agreement Profitability | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/service-management-reports/service-management-general-reports/sm-agreement-profitability"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/service-management-reports/service-management-general-reports/sm-agreement-profitability"
---

# SM Agreement Profitability

You can use the SM Agreement Profitability report by
 selecting Service Management > Reports > SM Agreement Profitability.
This report groups Cost and Billable values for work completed records per agreement into the following groups:

-  Maintenance - Work that was done per agreement terms

-  Full Coverage (Insurance) - Fully Covered work due to an existing active
 agreement

-  Add-on/Extra - Work done related to an agreement but not defined under the
 agreement

-  Other - Work completed that is not defined by any agreement, but is done in the
 date range of an existing active agreement

The starting date of the date range is determined by a combination of
 the Customer and Agreement parameters. If only the Customer is given, then the starting
 date will be the Activated Date of the very first Agreement and Revision found for that
 customer. If Agreement is given, the starting date will be the Activated Date of the
 first revision of that Agreement. The Revision parameters do not affect this starting
 date.
Dollar amounts are further grouped in to Month to Date, Quarter to Date, Year to Date, and Agreement to Date columns.
Cost amounts follow the same pattern as the Work Order Profit reports, if Actual Cost does not exist the report then looks to Projected
If an Agreement has a Budget value it will be displayed on the 'Budget' line of the report.
The Other column can be 'turned off' using the related parameter in the report launcher.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Customer (blank for all)
Select the Field Lookup button or press F4 to select the Customer or leave blank for All

Agreement (blank for all)
Click the Field Lookup
 button or press F4 to select the agreement or leave blank for
 all.

Beginning Revision
Enter beginning revision number.

Ending Revision
Enter ending revision number.

Show Non-Agreement Dollars (Other Column)
checkbox to show non-agreement dollars in the other column.
