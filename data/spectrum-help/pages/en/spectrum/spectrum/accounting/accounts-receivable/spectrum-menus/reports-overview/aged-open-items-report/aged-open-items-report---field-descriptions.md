---
title: "Aged Open Items Report - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/reports-overview/aged-open-items-report/aged-open-items-report---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/reports-overview/aged-open-items-report/aged-open-items-report---field-descriptions"
---

# Aged Open Items Report - Field Descriptions

Use this table for reference when completing the fields on this screen.
FieldDescription
FormatSelect Detailed report to print an aging report, or select Summary report to print a summarized aging report.
The detailed Aged Open Items Report displays each individual invoice and payment (including company contact name); the summary report prints only one summarized line per customer or job.

Sort bySelect Customer code to sort this report by customer code, select Job to sort this report by job, or select Customer alpha to sort this report alphabetically.
Minor sortSelect By date to perform a secondary sort of this report by date, or select By transaction # to perform a secondary sort of this report by transaction number.
SelectionsEnter the job number, work order number, customer type, salesperson code and project manager you want to include on the report, or press Enter to include ALL on the report.
The current customer code defaults in the Customer field. If the report has a saved template, the application applies those saved settings and then sets this field to the current customer code.

G/L divisionEnter the G/L division code(s) you want to include on this report, or press Enter to print all G/L division codes.
If you select a specific G/L division code, when you press Enter to exit this field, the Show G/L Divisional Portion window displays. Use this window to specify whether to use the selected G/L divisional code each time the Aged Open Items Report is run.
If one or more codes are entered, any invoices that were distributed to sales G/L codes with the matching division codes are selected. If the invoice is distributed to divisions other than those selected, an asterisk displays on the report.

Minimum balanceThe default is a minimum current balance of minus $99,999,999 (including retention), causing all customers to appear in the report, regardless of balance. If only customers who have a positive balance should appear in the report, enter the desired minimum balance here.
Minimum days overdueEnter 1 to 120 to print only for overdue customers. If only customers with overdue balances are desired, enter the number of days past due before a customer is to be included on the report.
For example, if you request all customers with at least 30 days past due, only customers who have any open item(s) of at least 30 days appear in the report. The report contains all open invoices for the customer, not just those invoices past due. A customer with one 10-day overdue item would not be included on the report. If left blank, all customers appear in the report.

Period end dateEnter the date to use for this aging report, or press Enter to print through the current Accounts Receivable processing date. A search window is available for viewing the calendar.

- If the Include paid invoices checkbox is not selected, the invoice date is used. The report does not include transactions that have dates later than the date entered here.

- If the Include paid invoices checkbox is selected, the General Ledger date is used, rather than the invoice date.

Include paid invoices?Select if this report is being printed as of a prior period end date. When this option is selected, the report shows invoices that were open as of the period end date, regardless of whether they were subsequently paid.
Include job totals?Select to include job totals on the A/R Aged Open Items Report. This checkbox is enabled only when the Customer code or Customer alpha sort by option is selected.
Include customer totals?Select to include customer totals on the A/R Aged Open Items Report. This checkbox is enabled only when one of the following conditions is met:

- The Job sort option is selected.

- The Summary report format option is selected, and the Job sort option is selected.

Show G/L divisional portion of open balance only?This checkbox is enabled only if a General Ledger division code is entered in the G/L division field.
If this checkbox is selected, the divisional amounts display and the asterisks indicate that other divisions are excluded from the invoice total.
Deselect to include all of the G/L divisions on the report. An asterisk prints on the report indicating that more than one division is associated with the invoice(s) and all the divisional amounts have been included.

Include work order number?Appears only if the Work Order module is enabled.
Select to include work order numbers in the report.
Disabled if the Summary format is selected.

Include invoice-specific notes?Select if you want to include invoice-specific notes on the report.
CurrencyIf Multi-Currency processing is being used, the Aged Open Items Report can be translated into an alternate currency. Enter a valid non-reporting currency. The report includes only invoices assigned to print in the specified currency.
At the end of each accounting period, GAAP requires that receivables held in a non-reporting currency be revalued using the month-end FX rate. The Controller should run the Aged Open Items Report by currency, revalue it into the reporting currency, and make the appropriate reversing journal entry.

Translate to local currency?Displays only if a valid non-reporting currency has been specified in the Currency field.
Select to run the report using the local currency.
