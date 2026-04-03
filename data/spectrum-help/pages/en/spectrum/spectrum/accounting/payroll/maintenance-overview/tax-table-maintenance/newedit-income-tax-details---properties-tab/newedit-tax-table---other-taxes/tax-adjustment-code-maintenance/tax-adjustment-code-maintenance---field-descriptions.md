---
title: "Tax Adjustment Code Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/newedit-tax-table---other-taxes/tax-adjustment-code-maintenance/tax-adjustment-code-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/newedit-tax-table---other-taxes/tax-adjustment-code-maintenance/tax-adjustment-code-maintenance---field-descriptions"
---

# Tax Adjustment Code Maintenance - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Adjustment code
Enter an adjustment code and code description.

Table lookup basis
Select to base the tax on the gross income or income tax amount.

Graduated table
Select this checkbox to use the adjustment code to increase or decrease withholding.

Percentage applied to
If the graduated table option is not selected for the tax adjustment, select the amount the percentage is multiplied by: gross earnings or income tax. The lookup amount is based on the highest tax bracket that applies. The result will then be added to the 'Fixed amount' on the row.

Adjustment type
Select whether to use the adjustment code to increase or decrease withholding. Note: The Standard deduction adjustment type is used to designate tax adjustment codes set up to support state-based variable standard deduction amounts.

Annualized tax brackets
Enter the upper end of the range of earnings that appears in the tax rate table being used for entry. When the last line of the table containing the upper end of the range of earnings is reached, enter the final number as 99,999,999.99. If this limit field is left blank instead of being set to 99,999,999.99, the Check Calculation will apply the last percentage rate for all earnings (unlimited). The system will recognize this number as the final number in the table.
Note: This window will support up to 50 graduated tax table
 rows.

Annualized tax adjustment amount
Enter the base tax for the range of earnings in this row as it appears in the tax rate table being used, and the percentage that is used to calculate the additional tax based on the lower end of the range of earnings.
Note: If a particular bracket actually is 'Limit = $0.00', then
 instead of using this field to control the calculation, the Administrator
 would set the 'Fixed amount = $0.00' and the 'Percentage = 0%' in order to
 calculate 'no tax' for that bracket.

Maximum adjustment amount
Enter the annual maximum tax adjustment value for the particular tax bracket (row).
Important: Do not enter a maximum mount of blank or 0.00 because
 the system will interpret this as: no limit. Instead, enter 0.00 in both the
 Fixed amount
 and Percentage
 fields to set a zero limit.
