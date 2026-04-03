---
title: "Aged Payables Report - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-reports/aged-payables-report/aged-payables-report---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-reports/aged-payables-report/aged-payables-report---field-descriptions"
---

# Aged Payables Report - Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

 This icon lets you know SuperSelect options are available for this field.

Allocate invoices by job?
Select this checkbox if you wish to show the job-specific balance when the invoice's distribution contains multiple jobs.
Important: When this checkbox is selected and the Summary format
 of the report is selected, the job balance information will come from the
 invoice detail lines stored in the VN_GL_DISTRIBUTION_DETAIL_MC table,
 instead of from the invoice header file.

Vendor
Vendor type
Enter the vendor code and type you want to include on this report, press Enter to include ALL vendors.

Job
When sorting this report by job number, if you have an invoice with multiple jobs in the detail lines, the invoice will only display once on the report (in the section for the last job on the invoice).

G/L division
 If one or more codes are entered, any invoices that were distributed to sales G/L codes with the matching division codes will be selected. If one or more G/L division codes are selected, and if the invoice is distributed to divisions other than those included in the total, an asterisk will display on the report.
This field is disabled when the Allocate invoices by job? checkbox is selected.

Period cut-off date
If a check was paid before the transaction and you want to include it in the report, make sure to use the actual check date and not the transaction date.

- If the Include paid invoices? checkbox is not selected, the invoice date is used for selection purposes. This report will not print transactions that have a date later than the date entered here. So, for example, if a period cut-off date of 5/31 is entered, any transactions dated later than 5/31 will not print on the report.

- If the Include paid invoices? checkbox is selected, the General Ledger date is used for selection purposes, rather than the invoice date.

Include paid invoices?
Select the checkbox to include invoices paid after the period cut-off date, for instance, if the aging is being run for a previous period. Clear the checkbox to include only unpaid invoices.
The dates used by the software for aging information are based upon the terms entered in the Vendors setup as well as the dates on all invoices. Note that "30 days past due" will only equal "30 days from the invoice date" when the customer's terms are Net Due 0 Days.
The "current" balance is the portion of the account balance which is current (not past due), the "1-30" balance is the portion of the account balance which is one to 30 days past due, and more.

Show G/L divisional portion of open balance only?
This checkbox displays only if the G/L division field is not set to ALL. Select this checkbox if you want to display partial invoice amounts for divisions only.
 If you want to include full amounts, leave this checkbox clear and an asterisk will print on the report indicating that more than one division is associated with the invoice(s). If this checkbox has been selected, the divisional amounts will display and the asterisks will indicate that other divisions are excluded from the invoice total.
Example:
For example, say you have the following two invoices:Note: Both invoices include two G/L divisions.

> Invoice A
Invoice A cont.

Division #
1
2

G/L Account
1500
2500

Amount
$300
$500

Total
$800

Invoice B
Invoice B cont.

Division #
1
3

G/L Account
1500
3500

Amount
$250
$250

Total
$500

Now say you run a report for G/L division # 1 and you leave the Show G/L divisional portion of open balance only checkbox clear. The resulting report header would display *= Other division in totals, and both Invoice A = $800* and Invoice B= $500* would appear on the report, giving a total of $1300.
If you were to run the same report for G/L division #1 and you selected the Show G/L divisional portion of open balance only checkbox, the resulting report header would display * = Other divisions total excluded, and both Invoice A = $300* and Invoice B = *$250 would appear on the report, giving a total of $550.
Finally, if you were to run the report and you opted to include ALL of the G/L divisions, your result would display both invoices for their entire amounts (Invoice A = $800, and Invoice B = $500) and no asterisks (*) would display.

Report type

- Select Detail to print the report with each invoice in detail on a separate line.

- Select Summary to print the report with a summary line for each vendor.

Primary sort by
Select Vendor code to print the report in sequence by vendor code, or select Vendor alpha to print the report in alphabetical sequence by vendor.

Secondary sort by
Select to print the report by Invoice number or Invoice date.

Cost group
If cost centers are being used in this company, enter a cost center or cost group. After specifying a cost center or cost group, the report shows only invoices assigned to that cost group/cost center.
Note: If you only have access to one cost center, this field will not display.

Tip: If you need to show the job amounts
 separately, it is recommended that you enter separate
 invoices.
