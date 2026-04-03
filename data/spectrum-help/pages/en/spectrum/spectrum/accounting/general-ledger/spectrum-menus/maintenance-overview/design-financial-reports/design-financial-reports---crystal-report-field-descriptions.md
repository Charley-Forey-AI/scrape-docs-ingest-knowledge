---
title: "Design Financial Reports - Crystal Report Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/design-financial-reports/design-financial-reports---crystal-report-field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/design-financial-reports/design-financial-reports---crystal-report-field-descriptions"
---

# Design Financial Reports - Crystal Report Field Descriptions

Use the table below for reference when completing the fields for Crystal Report format.
FieldsDescriptions
Main Properties
Include page footers?

- Select to print footers at the bottom of the report.

- If you select this checkbox, the Page Footer button displays. Click it to open the [Financial Report Page Footer](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/design-financial-reports/design-financial-reports---crystal-report-field-descriptions/financial-report-page-footer) window.

Departmental reporting?Select this checkbox if your GL was originally set up to use Departments. The Department start and end position fields become available.
Department start/end positionWhen defining departmental reports, determine the position of the departmental code within G/L account codes.
The length of the department code is defined on the [General Ledger Installation - Properties](/en/spectrum/spectrum/accounting/general-ledger/general-ledger-installation-overview/general-ledger-installation---properties) screen.

- If the length is only one character, then the starting and ending positions are both "1".

- If the department code length is three characters, then the starting position is "1" and the ending position is "3".

 This function may still be used in a company with no department codes. If you still want a report based on the final two digits of the account code, determine the position within the account code of these two digits.
For four-digit accounts, the start position is "3" and the end position is "4".

Cost center reporting?Select this checkbox if your GL was originally set up to use Cost Centers.
