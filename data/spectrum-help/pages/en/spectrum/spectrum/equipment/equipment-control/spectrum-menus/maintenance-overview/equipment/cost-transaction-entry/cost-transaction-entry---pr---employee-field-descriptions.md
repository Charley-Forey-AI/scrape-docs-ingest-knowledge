---
title: "Cost Transaction Entry - PR - Employee field descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/cost-transaction-entry---pr---employee-field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/cost-transaction-entry---pr---employee-field-descriptions"
---

# Cost Transaction Entry - PR - Employee field descriptions

When PR – Cost is selected as the source for this
 transaction, the employee code field appears.
This screen tracks multi-company cost transactions from the Equipment company, for improved
 inquiry (drill-back to cost history details) and for consistency with other equipment
 transaction entries.

- Only certain operators will have permission to enter Payroll-type transactions. If an Operator is not authorized to enter payroll transactions, the PR-Cost button will be hidden and this screen will be unavailable.

- When updating Payroll Cost transactions, the software looks to the Payroll burden type setting in the [Equipment Control Installation – Properties](/en/spectrum/spectrum/equipment/equipment-control/equipment-control-installation-overview/equipment-control-installation--properties) screen in the current employee's company.

- If Document Imaging is being used, any images stored for this screen are saved in the EC cabinet, by default.

Fields
Descriptions

Equipment code
 Enter or select the equipment code, which is from the designated company.
When updating Payroll Cost transactions, the software looks to the Payroll burden type setting in the [Equipment Control Installation – Properties](/en/spectrum/spectrum/equipment/equipment-control/equipment-control-installation-overview/equipment-control-installation--properties) screen in the current employee's company.
Note: To change the Company field, press the Backtab or down arrow
 key after entering the equipment code.

Description

Cost category
Enter the cost category code.

Company
If the Multi-company checkbox is selected in Equipment Control Installation, the company code displays. If the equipment is in a different company, press the Backtab or down arrow key to access this field and change the company code.

Employee code
Select an employee code.

Check #
Enter the employee check number. (Optional)

Hours
Enter the transaction hours. (Optional)

Gross rate
The gross pay displays. Press Enter to accept this default calculation or enter a different transaction amount. The default gross pay amount is computed as the hours multiplied by the rate.

Amount
Press Enter to accept the calculated default amount or enter a new amount. The amount is computed as the quantity multiplied by the rate.

G/L debit
The default debit G/L account code from Cost Category File Maintenance displays. Enter to accept the default, or enter the desired account for this transaction. The account description will display. Entry is required. Select the Equipment cost option in the G/L Master File MaintenanceDirect cost option group in order to display this information.
Click on this field to search for G/L accounts. If no restrictions are found for the employee cost category, the search window will allow you to search across all G/L accounts. If restrictions are found for the cost category, you will only be able to search G/L accounts for the designated cost category.

G/L credit
Enter the credit G/L account code for this transaction. The account description will display. Entry is required. Select the No direct cost option in the G/L Master File MaintenanceDirect cost option group in order to display this information.

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
The employee name displays.

Related information

- [Cost Transaction Entry by Payroll - Cost Center Information](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/cost-transaction-entry-by-payroll---cost-center-information)
