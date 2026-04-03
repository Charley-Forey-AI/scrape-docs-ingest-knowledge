---
title: "Statements - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/reports-overview/statements/statements---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/reports-overview/statements/statements---field-descriptions"
---

# Statements - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field
Description

Customer
The current customer code will default in this field. If the report has a saved template, the software will apply those saved settings and then set this field to the current customer code.

Customer type
Enter the customer for which to print a statement, or press Enter to accept the software default of ALL.

Minimum balance
The default is a minimum balance of one cent. To print only statements for customers who have positive outstanding balances, press Enter to accept the default. To print statements for customers who have zero balances or credit balances, enter the desired minimum balance here.

Period end date
Enter the desired period end date, or press Enter to print through the current Accounts Receivable processing date. The period end date is used to age the customer's account at the bottom of the statement. It is also used as a cut-off date so that invoices dated after the period end date will not appear on the customer's statement.

# days grace
If only statements for customers with overdue balances are desired, enter the number of days past due before printing a statement. For example, if the operator requests all customers with at least "30" days past due, only customers who have any open item(s) of at least 30 days will print. When the statement is printed, it will contain all open invoices for the customer, not just those invoices past due. A customer with one 10-day overdue item will not receive a statement. If this field is left blank, all statements will print.

Cost group
If the cost center feature is enabled in the Enterprise Installation screen, enter a cost group in this field. When a cost group or cost center is specified, the report will show only invoices assigned to that cost group/cost center. When the operator specifies a cost center, Spectrum verifies that the operator has permission to access that cost center before proceeding.

Items to include
Select the option button that corresponds to the items you want to include on this statement. Open only items include invoices and other transactions that are not yet fully applied or all items, which will include everything still in the open item file shown in the Customers screen, even if paid in full.

Sort by
Select Customer to sort statements by customer, or select Job to sort by job number.

Format
Select the report format to print.

- Standard Use this option to view the customer statements with current balances.

- Past due Use this option to view the customer statements with past due balances.

Saved Selections
All report starting screens offer a Saved Selections bar and Save Current button that can be used to remember saved user selections the next time this report is accessed. Whenever the Saved Selections bar is available, the Date Calculator feature is also available for date, fiscal year, and fiscal period fields.
Buttons
Save Current
Located in the Saved Selections bar, click this button after you have made your report selections if you think you want to save them for future use. A widow opens that allows you to enter a name for the report "template" that you are saving, and you can set this template as your default. Additional settings allow you to share this template with other operators or to assign it as a system-wide default (thereby ensuring that everyone is seeing the same items).
Preview
After making your report selections, click this button to preview the report in PDF format. From here you can review the information and then print, save or email the file to someone else.
Export
Click this button to open the Export Report window. Here you can choose a report format (including PDF, RPT, RTF, CSV, and XLS), designate a name for the report (or accept the default name) and decide if you want the report to include auto-generated bookmarks.
My Reports
Use the My Reports window to add and maintain any custom Crystal reports. This feature can then be used in conjunction with the report filters feature to set the default report to a custom report.
