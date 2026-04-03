---
title: "Cost Transaction Entry - View AP - Vendor field descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/cost-transaction-entry---view-ap---vendor-field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/cost-transaction-entry---view-ap---vendor-field-descriptions"
---

# Cost Transaction Entry - View AP - Vendor field descriptions

When AP – Vendoris selected as the source for this
 transaction, the vendor code field appears.
This screen tracks multi-company cost transactions from the Equipment company, for improved
 inquiry (drill-back to cost history details) and for consistency with other equipment
 transaction entries.
Fields
Descriptions

Equipment code
Enter or select the equipment code, which is from the designated company. Entry is not allowed if the equipment's status is Retired.
Note: To change the Company field, press the Backtab or down arrow key
 after entering the equipment code.

Description

Cost category
Enter the cost category code. A lookup window is available for viewing valid cost category codes.

Company
If the Multi-company checkbox is selected in Equipment Control Installation, the company code displays. If the equipment is in a different company, press the Backtab or down arrow key to access this field and change the company code.

Vendor
The vendor code displays based on the code selected on the main screen (and can be from the current company only).

Invoice #
Enter the invoice number (optional).

Invoice date

Amount
Enter the transaction amount.

G/L debit
The default debit G/L account code from Cost Category File Maintenance displays. Enter to accept the default, or enter the desired account for this transaction. The account description will display. Entry is required in this field. Select the Equipment cost option in the G/L Master File MaintenanceDirect cost option group in order to display this information.
Note: Data entry is prevented if the General Ledger account code
 status is Not
 Used. A warning message displays if the General Ledger account
 code status is Inactive.
Click on this field to search for G/L accounts. If no restrictions are found for the vendor cost category, the search window will allow you to search across all G/L accounts. If restrictions are found for the cost category, you will only be able to search G/L accounts for the designated cost category.

G/L credit
Enter the credit G/L account code for this transaction. The account description will display. Entry is required in this field. Select the No direct cost option in the G/L Master File MaintenanceDirect cost option group in order to display this information.
Note: Data entry is prevented if the General Ledger account code
 status is Not
 Used. A warning message displays if the General Ledger account
 code status is Inactive.

Eq work order
Enter the equipment work order number associated with this line item, or
 double-click on this field or press F4 to select from a list
 of available equipment work order numbers. If a closed equipment work order
 number is entered into this field, a message displays but does not disallow
 further data entry.
This field displays only if the Cost Category File Maintenance screen's Data entry radio group is set to Optional or Require equipment work order.
Note: Because it is possible to enter equipment codes that were
 set up in other companies, when a company other than the current company is
 specified in the Company field, a search window is available to view work
 orders stored in that other company. If Preventive Maintenance is not
 present in that other company, then this field does not display.

Remark
Information recorded in this field is stored in the Equipment Cost History file when updated. Remarks will auto-repeat until you exit the screen.

Cost category description
The description defaults based on the cost category entered earlier.

Other info
The vendor name displays.

Related information

- [Transaction Entry by Accounts Payable - Cost Center Information](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/transaction-entry-by-accounts-payable---cost-center-information)
