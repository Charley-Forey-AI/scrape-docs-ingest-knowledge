---
title: "Design Financial Reports - Standard Report Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/design-financial-reports/design-financial-reports---standard-report-field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/design-financial-reports/design-financial-reports---standard-report-field-descriptions"
---

# Design Financial Reports - Standard Report Field Descriptions

Use the table below for reference when completing the fields for Standard Report format.
FieldsDescriptions
Main properties
Maximum columnsEnter the maximum width for each column in this report - any number from 80 to 132.
Standard column headingsStandard headings are the names of the fields in Spectrum from which the information is being taken.

- Select Yes to use standard (system-generated) column headings on this report.

- Select No to customize column headings.

- Select Both to use a combination of standard and customized column headings.

If you select No or Both, the Column Heading button becomes available.

Column HeadingClick to open the [Non-Standard Column Heading](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/design-financial-reports/design-financial-reports---standard-report-field-descriptions/non-standard-column-heading) window.
Include page footers?

- Select to print footers at the bottom of the report.

- If you select this checkbox, the Page Footer button displays. Click it to open the [Financial Report Page Footer](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/design-financial-reports/design-financial-reports---crystal-report-field-descriptions/financial-report-page-footer) window.

Departmental reporting?Select this checkbox if your GL was originally set up to use Departments. The Department start and end position fields become available.
When you print a departmental financial report, the G/L account description shown on the report is associated with the G/L code of the last department included.

Department start/end positionWhen defining departmental reports, determine the position of the departmental code within G/L account codes.
The length of the department code is defined on the [General Ledger Installation - Properties](/en/spectrum/spectrum/accounting/general-ledger/general-ledger-installation-overview/general-ledger-installation---properties) screen.

- If the length is only one character, then the starting and ending positions are both "1".

- If the department code length is three characters, then the starting position is "1" and the ending position is "3".

 This function may still be used in a company with no department codes. If you still want a report based on the final two digits of the account code, determine the position within the account code of these two digits.
For four-digit accounts, the start position is "3" and the end position is "4".

Cost center reporting?Select this checkbox if your GL was originally set up to use Cost Centers.

Non-Crystal page headings

- For each of the nine heading fields, enter both the row and column on the report where you want each heading to display.

- Headings can appear on rows one, two, or three.

- If you don't want to print a heading field on the report, leave the field blank by pressing Enter without typing a number.

- Under Row, enter the row (1–3) to print the heading field on.

- Under Column, indicate the horizontal position in which the heading field should print.

- You can enter a specific column number, or enter Left justified, Right justified, or Centered.

For the report components that follow, enter the row and column numbers to indicate the element's print position.
Run date

- The date you run the report.

- If the run date should print on the standard report, allow 14 characters.

- Format is MM/DD/YY.

Run time

- The time stamp of when you run the report.

- If the time stamp should print on the standard report, allow 14 characters.

- Format is TIME: XX:XX:XX.

Dept name
Company name

- If the company name should print on the report, allow 30 characters.

- The name prints as entered in the Spectrum Company Installation screen.

Report titleIf the title should print on the report, allow for a maximum length of 30 characters.
Per end date

- The period end date.

- If you want the period end date to appear on the standard report, allow 25 characters.

- Format is PERIOD END DATE: MM/DD/YY.

Page number

- The report screen number.

- If you want the screen number to print on the standard report, allow 10 characters.

- Format is screen: XXXX.

Report ID

- If you want to display the report ID, allow 10 characters.

- Format is RPT ID: XX.
