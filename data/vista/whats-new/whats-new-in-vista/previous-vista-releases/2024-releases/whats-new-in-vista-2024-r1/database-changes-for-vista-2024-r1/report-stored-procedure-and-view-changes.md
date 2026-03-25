---
title: "Report Stored Procedure and View Changes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/database-changes-for-vista-2024-r1/report-stored-procedure-and-view-changes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/database-changes-for-vista-2024-r1/report-stored-procedure-and-view-changes"
---

# Report Stored Procedure and View Changes

The following tables display all report stored procedures and/or views that have been modified or added for the Vista 2024 R1 release to improve performance or correct data display, along with the reports that are affected by this change.
Unless you have already followed instructions from previous
 release notes or Viewpoint's
 website, please copy Viewpoint's
 standard stored procedures to a new name if you have copied or modified any of the
 reports listed below. For specific instructions on copying stored procedures, see
 the [Copying Stored
 Procedures](https://support.viewpoint.com/s/knowledgedetail?c__urlname=150925535527899) document available in the Support Knowledge Base area of the
 Viewpoint Customer Portal (at [support.viewpoint.com](https://support.viewpoint.com/)). Reports can be found in the
 Vista Users section under Crystal
 Reports.
Unlike stored procedures, Viewpoint does not require customers to copy views (brv[view
 name]) for related reports used as starting points for customer-modified reports. If
 you have copied and modified any of the reports affected by view changes (listed
 below) however, you may need to open your own report in the Crystal Reports Designer
 and select Database > Verify Database.

## Stored Procedures

The following is a list of report stored procedures that were
 added or modified in this release.
Stored Procedure Name
Report Title
Report File Name
Report ID

*Added*
brptPD7APR Canada PD7A InformationPRPD7A.rpt1073
*Modified*
vrptPRCANFederalRemittancesPR Canada Federal RemittancesPRCanFederalRemittances.rpt1092

## New Report Stored Procedure Parameters

The following is a list of all new parameters for report stored procedures.
Stored Procedure
Parameter

brptPD7A@CPP2_Comp_DLCode
@CPP2_Emp_DLCode
vrptPRCANFederalRemittances@DednCPP
@DednCPP2
@DednEI
@DednFedTax
@LiabCPP
@LiabCPP2
@LiabEI
@PRCo
@PayrollProgramAccount

## Views

The following table displays all report views that were added for this release, along with affected reports.
View Name
Report Title
Report File Name
Report ID

vrvHROSHA300HR OSHA Form 300HROSHA300_Legal.rpt349
HR OSHA Form 300AHROSHA300Summary_Legal.rpt350
vrvHROSHA301HR OSHA Form 301HROSHA301Form_legal.rpt351
