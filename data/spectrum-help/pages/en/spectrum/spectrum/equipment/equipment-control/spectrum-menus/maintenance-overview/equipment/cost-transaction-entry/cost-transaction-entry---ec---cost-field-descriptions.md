---
title: "Cost Transaction Entry - EC - Cost Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/cost-transaction-entry---ec---cost-field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/cost-transaction-entry---ec---cost-field-descriptions"
---

# Cost Transaction Entry - EC - Cost Field Descriptions

When the EC – Cost button is clicked
 as the source for this transaction, the equipment code field appears.
If the Preventive Maintenance module is present on your system, a
 maintenance work order number prompt appears and a maintenance work order is required.
 Enter a maintenance work order number, or press F4 to select from
 a list of valid work order numbers. The system then allows entry of a valid equipment
 code number.

- Upon entry of this equipment code or maintenance work order number, the screen
 prompts for cost categories, cost amounts, and other information. Entry is not
 allowed if the equipment's status is Retired.

- Read more about [Meter Replacement](/en/spectrum/spectrum/equipment/equipment-control/troubleshooting/meter-replacement).

- If Document Imaging is being used, any images stored for this screen are saved in the EC cabinet, by default.

Fields
Descriptions

Equipment code
The equipment code displays based on the code selected on the main screen. No entry is allowed.

Description

Cost category
Enter the cost category code for this transaction. A lookup window is available for viewing valid cost category codes.
When a cost category is entered into this field, Spectrum checks the status of the code. If the cost category's status is set to Inactive, a warning displays but entry is permitted to continue.

Quantity

U/m
The unit of measure for this cost category displays, based on the UM assigned
 to the particular cost category code.
This UM will vary (for example, Gallons vs. Liters) based on the lexicon
 specified in the Company Installation screen.

Fuel/oil
Enter the fuel/oil code for this transaction. If this transaction does not involve fuel or oil, the cursor jumps past the fuel/oil code.

Rate
Press Enter to accept the default value, or enter the desired transaction rate.

Amount
The transaction total displays. Press Enter to accept the calculated default amount or enter a new amount. The amount is computed as the quantity multiplied by the rate.

G/L debit
The G/L debit account code and description default from Cost
 Category File Maintenance. Type a new G/L account or press
 Enter to
 accept this default. After the first entry, if no default exists in the
 Cost Category File Maintenance screen, the
 latest cost debit entry account code used defaults instead.
Data entry is prevented if the General Ledger account code
 status is Not
 Used. A warning message displays if the General Ledger
 account code status is Inactive.
Click on this field to
 search for G/L accounts. If no restrictions are found for the
 equipment cost category, the search window will allow you to search
 across all G/L accounts. If restrictions are found for the cost
 category, you will only be able to search G/L accounts for the
 designated cost category.
Select
 Equipment cost in the G/L Master
 File Maintenance Direct cost option group in order to
 display this information.

G/L credit
Enter the G/L credit account code for this transaction. The G/L account code description will display. Subsequent cost entries will default the latest saved cost credit G/L account added.
Select the No direct cost option in the G/L Master File Maintenance
 Direct cost option group in order to display this
 information.
Note: Data entry is prevented if the General Ledger account code
 status is Not
 Used. A warning message displays if the General Ledger
 account code status is Inactive.

Eq work order
Enter the equipment work order number associated with this line item, or select from a list of available equipment work order numbers. If a closed equipment work order number is entered into this field, a message displays but entry is allowed.
This field displays only if the Preventive Maintenance module is present and
 if the Cost Category File Maintenance screen's
 Data entry
 radio group is set to Optional or Require equipment work order.

Remark
Information recorded in this field is stored in the Equipment Cost History file when updated. Remarks will auto-repeat until you exit the screen.

Cost category description
The description defaults based on the cost category entered earlier.

Other info
When a fuel/oil code is specified, the associated description displays here.

Related information

- [Transaction Entry by Equipment Cost - Cost Center Information](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/transaction-entry-by-equipment-cost---cost-center-information)
