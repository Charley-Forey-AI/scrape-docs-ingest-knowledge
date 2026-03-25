---
title: "Vista Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/system-tools/vista-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/system-tools/vista-reports"
---

# Vista Reports

The following discusses new reports, as well as updates made to existing standard reports for the 2023 R1 release.

## A note about report security

Each new report's default security level is set to None for all users.
When reviewing new reports included with any release:

- determine which users should have access to which reports

- in the VA Report Security form, add or change access as needed

- if you happen to be granting access to batch form reports, consider also any needed access to Audit and Distribution reports, since permission to access a given batch form report does not automatically allow access to other reports.Tip: Use the Filter bar in the VA Report Security form to easily locate audit/distribution reports. In the Type column, enter Audit so the grid displays only audit and distribution reports.

## Vista client reinstall resolves report issue

You can now resolve a common Crystal Reports error containing the words `UFL` (User Function Library) and `dll` (dynamic link library) by re-installing the Vista client.

## Accounting

Table 1. Changed ReportsReportReport IDDescription
AP Spend Analysis Report – Viewpoint ePayments1316Modified this report to allow entering a range of months rather than a single year.

- Added Beginning Month and Ending Month parameters, to allow entering a range of months.

- Removed the Current Year parameter, as it is no longer needed.

- Updated the Company parameter to be a required input.

- Improved the report's error handling and messaging.

VA System Users925Modified this report to allow filtering results based on Status and License Type, enabling you to identify the NULs set up on a site.

- Added a Status: (A)ctive, (I)nactive (blank for all) parameters to allow filtering report to show only Active users or only Inactive users. If you leave this field blank, report will include all users, regardless of their status.

- Added a Licence Type (O)ffice, (P)M (blank for all) parameter to allow for filtering report to show only users with an Office license or only those with a PM license. If you leave this field blank, report will show all users, regardless of their license type.

- Added User Status and License Type fields to the report page headings to indicate user-specified input values.

- Added a Status and License Information section to the report's Detail format.

Note: If you do not filter the report by Status and/or License Type, it is suggested that you run the report in Detail format so that you can identify the status and license type for each user. The Summary format does not include User Status and License Type fields, so it is better suited for running the report with both a Status and License Type selected.

Additional changes to this report are as follows:

- Relabeled the User and User Login columns to "User Full Name" and "User Login (VP User Name)" for improved clarity and consistency

- Relabeled the User (Blank for All) and (S)ummary or (D)etail parameters to "User Name (blank for all)" and "Format: (S)ummary or (D)etail" for better clarity.
