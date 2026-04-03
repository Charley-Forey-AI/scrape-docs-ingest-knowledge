---
title: "Design Financial Reports - Cost center information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/design-financial-reports/design-financial-reports---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/design-financial-reports/design-financial-reports---cost-center-information"
---

# Design Financial Reports - Cost center information

If the cost center feature is enabled in the Enterprise
 Installation screen, the Design Financial Reports screen includes the following additional
 fields: Cost center report,
 Cost center start, and Cost center end.
These fields only apply to the standard format of the Design Financials
 Report.
Field
Description

Cost center report
Select the checkbox if this is a cost center report;
 otherwise leave the checkbox clear.
Note:
 This checkbox is available only if the Department
 report checkbox is clear.

When defining cost center reports, determine the position
 of the cost center code within G/L account codes by using the Cost center start and
 Cost center end
 fields.

Cost center start
Enter the position of the first character of the portion
 of the cost center code for which this report is being created or press
 Enter to accept
 the software default of 1.
If the length is only one character, then the starting
 and ending position will both be 1.
If the department code length is three characters, then
 the starting position will be 1 and the ending position will be 3.
In a company with no cost center codes, this function may
 still be used. If you would like a report based on the final two digits of
 the account code, determine the position within the account code of these
 two digits. For four-digit accounts, the start position would be 3 and the end position
 would be 4.
When a cost center financial report is produced, the G/L
 account description shown on the report is associated with the G/L code of
 the last department included.

Cost center end
Enter the position of the last character of the portion
 of the cost center code for which this report is being created, or
 press Enter to
 accept the software default of 10.
Note:
 Spectrum confirms that the end position is equal to or
 greater than the number entered into the Cost center start
 field.

If the length is only one character, then the starting
 and ending position will both be 1.
If the department code length is three characters, then
 the starting position will be 1 and the ending position will be 3.
