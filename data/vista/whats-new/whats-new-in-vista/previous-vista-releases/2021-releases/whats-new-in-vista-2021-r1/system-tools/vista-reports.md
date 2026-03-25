---
title: "Vista Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/system-tools/vista-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/system-tools/vista-reports"
---

# Vista Reports

The following discusses new reports, as well as updates made to existing standard reports for the 2021 R1 release.

## A note about security

 When new reports are added, their default security level is set to None, even for users who have Full Access to Vista. When reviewing new reports for this release, determine who should have access to which reports. Add or change security as needed in VA Report Security. Make sure to include any Audit and Distribution reports as permission to access the related batch forms does not automatically give permission to access the audit/distribution reports. You can locate audit/distribution reports in VA Report Security using the Filter bar. Enter Audit in the Type column, and the grid will restrict the list of reports to only audit and distribution reports.

## Accounting

Table 1. New ReportsReportReport IDDescription
HR Federal Contractor VETS-42121329This new report meets all current Department of Labor (DOL) requirements and is used to export your VETS-4212 data to a CSV file for electronic submission through the VETS web-based filing system. It replaces the HR Federal Contractor Veterans Report (VETS-4212)(Report ID 1301). Most of the parameters in this new report are the consistent with those included in the old report. However, there are some differences, as noted below:

- HR Company - New parameter used to enter the HR company associated with the resources and hiring locations (if used) included in this report. Additionally, if you assigned override DUNS Number and NAICS Code identifiers by hiring location (in HR Hiring Location Setup), those values are applied to the appropriate records in the e-file. If a hiring location does not specify an override DUNS Number or NAICS Code, the system uses the identifiers assigned to the HR company in HQ Company Setup.

- VETS-assigned Company Number - Use to enter the company number assigned by the DOL. If this is the first time you have filed a VETS-4212 report, leave this field blank; you will be assigned a number to use for future filings.

- NAICS Code / DUNS Code - These parameters were excluded from this new report, as the system now populates these identifiers in the report based on the values specified for the hiring location or the company (if no hiring locations are used or if no override codes are specified for the hiring locations include in the report).

-  Parent Company - This parameter was excluded from this new report, as it was not being used.

Other changes included in this new report:

- The report now generates the appropriate "type of form" based on the records in the file as follows:

- S (Single Establishment) - Used if there are no resource records (for the specified HR company) assigned a hiring location.

- MHQ (Multiple Establishment - Headquarters) - If there is at least one resource record assigned a hiring location, one record is generated representing employees that work for the company headquarters (that is, employees not assigned a hiring location) and assigned this form type.

- MHL (Multiple Establishment - Hiring Location) - For each unique hiring location in a multiple establishment organization, a separate record is created and assigned this form type.

- The report now excludes temporary employees.

- The report now aligns with the current veteran classifications: Disabled, Armed Forces Service Medal, and Active Duty Wartime or Campaign Badge. Veteran classifications "Vietnam" and "Other Veteran" are no longer used.

HR Federal Contractor VETS Resources1330This new report serves as a companion to the HR Federal Contractor VETS-4212 report, which is used to export data for electronic filing of the VETS-4212.
You can print or review this report in Summary or Detail format:

- Summary - Shows the aggregate resource counts for each box in the VETS-4212 e-file.

- Detail - Shows the specific resources included in each aggregate count.

For multiple establishment organizations, the report shows resource counts for the company headquarters (form type Multiple Establishment - Headquarters), followed by resource counts for each hiring location (form type Multiple Establishment - Hiring Location). Clicking on the Maximum Number and Minimum Number values that appear at the end of each location section displays a list of the resources included in each count.
Note: To ensure an accurate representation of the data included in the e-file, make sure you use the same report parameter values.

Table 2. Changed ReportsReportReport IDDescription
AP Vendor Drillldown68 In conjunction with the Vendor Merge feature added in Accounts Payable, these reports now group actual (parent) and duplicate vendors together; however, you can still drill-down into each vendor's information. The only exception to this is if you run the report for a duplicate vendor. In this case, the report still displays the actual vendor, but you can only drill down into the duplicate vendor's information.
AP Vendor Payment History Drilldown73

For a list of report defects fixed in this release, click [here](https://support.viewpoint.com/s/browse-cases-and-issues?tabset-d4f10=2) to go to the Track Cases/Issues page of the Viewpoint Customer Portal. Use the filter options to select your product and module. Then in the Fixed In Version field, select this version.
