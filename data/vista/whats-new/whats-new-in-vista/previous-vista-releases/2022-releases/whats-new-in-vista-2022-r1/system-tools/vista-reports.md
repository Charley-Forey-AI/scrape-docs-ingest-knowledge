---
title: "Vista Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r1/system-tools/vista-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r1/system-tools/vista-reports"
---

# Vista Reports

The following discusses new reports, as well as updates made to existing standard reports for the 2022 R1 release.

## A note about security

 When new reports are added, their default security level is set to None, even for users who have Full Access to Vista. When reviewing new reports for this release, determine who should have access to which reports. Add or change security as needed in VA Report Security. Make sure to include any Audit and Distribution reports as permission to access the related batch forms does not automatically give permission to access the audit/distribution reports. You can locate audit/distribution reports in VA Report Security using the Filter bar. Enter Audit in the Type column, and the grid will restrict the list of reports to only audit and distribution reports.
For a list of report defects fixed in this release, click [here](https://support.viewpoint.com/s/browse-cases-and-issues?tabset-d4f10=2) to go to the Track Cases/Issues page of the Viewpoint Customer Portal. Use the filter options to select your product and module. Then in the Fixed In Version field, select this version.

## Accounting

The Vista 2022 R1 release affects reports in the Accounts Payable module. There are no new or changed reports for the Accounts Receivable, Cash Management, or General Ledger modules.
Table 1. Changed ReportsReportReport IDDescription
AP Check Print - AvidXchange1293In conjunction with the transition to Aatrix for year-end reporting, this report was removed from the Reports menu, as it is no longer being used.

AP Vendor Compliance67Added a new Show only Codes that are not in compliance? parameter to report. When selected, the report displays only those codes with which the vendor is not currently in compliance. If not selected (default), the report shows all compliance codes for the vendor, regardless of compliance status.

United States
AP 1099 Dividend Print Form Copy B1In conjunction with the transition to Aatrix for year-end reporting, the following reports were removed from the Reports menu, as they are no longer being used.

AP 1099 Dividend Print Form Copy C2
AP 1099 Interest Print Form Copy B3
AP 1099 Interest Print Form Copy B4
AP 1099 Miscellaneous Print Form Copy B5
AP 1099 Miscellaneous Print Form Copy B6
 AP 1099 NEC Print Form Copy B 1331
AP 1099 NEC Print Form Copy B1332

## Costs and Contracts

The Vista 2022 R1 release affects reports in the Job Billing, Job Cost, and Purchase Order modules. There are no new or changed reports for the PreConstruction or Subcontract Ledger modules.
Table 2. Changed ReportsReportReport IDDescription
JB Progress Invoice448If you use multi-level tax codes, these reports now allow breaking them out into their individual components (such as GST and PST). To enable this functionality, the following changes were made:

- Added a new Print Detail for Tax This Invoice parameter that when selected, prints a breakout (on applicable invoices) of the single-level codes associated with the multi-level code and their amounts.

- Removed the Plus Sales Tax line in the Totals section and added two new lines: Plus Previous Tax and Plus Tax This Invoice.

If you do not select the Print Detail for Tax This Invoice parameter, the report prints the previous tax amount in the Plus Previous Tax line, and the tax amount for the current invoice in the Plus Tax This Invoice line.
If you select the Print Detail for Tax This Invoice parameter, the report prints a Plus Tax This Invoice line for each single-level tax code in use by a contract item on the invoice, as well as a separate line for each of the single-level members of any multi-level tax codes.
Total Tax: 1,785.00
Plus Tax This Invoice (GST): 1,050.00
Plus Tax This Invoice (PST): 735.00
In addition, as part of this functionality, a new vHQTXHistory table was added to track the single-level tax codes and amounts that make up each of the multi-level tax codes. This table is populated when you initialize bills via JB Initialization, as well as when you update a bill item in JB Progress Bill.
Note: For legacy invoices (created prior to this release), no tax detail data is available in the system for display. For any such invoice, a single summary value for the current tax amount appears in place of tax details in the totals section, along with an indicator of the unavailability of tax details for that particular invoice.

JB Progress Invoice with Units450

## HR and Payroll

The Vista 2022 R1 release affects reports in the Human Resources and Payroll modules.
Table 3. Changed ReportsReportReport IDDescription
PR Department Costs (Pre 6.11 version)1294In conjunction with the transition to Aatrix for year-end reporting, these reports were removed from the Reports menu, as they are no longer being used.
PR Department Costs by Expense Month (Pre 6.11 version)1295
United States
PR W2 Employee Run862In conjunction with the transition to Aatrix for year-end reporting, these reports were removed from the Reports menu, as they are no longer being used.
 PR W2 Employee Run Attach863
PR W2 Local Order866
PR W2 State Order868

Canada
PR Canada T4 Summary1062In conjunction with the transition to Aatrix for year-end reporting, these reports were removed from the Reports menu, as they are no longer being used.
PR Canada T4 Slip1066
PR Canada T4 Slip No Form1109
PR T4 Reconciliation Report1151
