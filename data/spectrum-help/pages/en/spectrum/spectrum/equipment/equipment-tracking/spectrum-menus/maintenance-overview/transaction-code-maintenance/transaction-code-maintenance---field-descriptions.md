---
title: "Transaction Code Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-tracking/spectrum-menus/maintenance-overview/transaction-code-maintenance/transaction-code-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-tracking/spectrum-menus/maintenance-overview/transaction-code-maintenance/transaction-code-maintenance---field-descriptions"
---

# Transaction Code Maintenance - Field Descriptions

Use this table for reference when completing the fields in
 the screen.
FieldDescription
Transaction codeSelect the transaction code from the drop-down menu.
DescriptionEnter the description for this transaction code or press Enter to accept the default description.
Deployment typeThis selection defaults based on the Direct Cost setting and defaults to Job Cost when adding a new code. The direct cost specifies whether or not this transaction code is for job cost.
Processing
Create inventory and equipment stand-by transactions?This flag ensures that a transaction will be sent to either the equipment or inventory systems as a cost transaction with General Ledger effects (in the equipment case, the transaction must also meet the minimum billing requirements). If the checkbox is clear, then the transaction WILL NOT be sent to either the equipment or inventory systems, but will be saved in the Equipment Tracking system as a history transaction (for example, setting the equipment status to 'repair' but no transaction is sent to the equipment system).
If the Direct cost checkbox is selected and this checkbox is left blank, then transactions recorded in Equipment Transaction Entry will not be updated to Job Cost. These transactions will not require entry of a phase and cost type, but these fields may be completed, if desired, for Equipment Tracking Inquiry purposes.

Add inventory markup on Job Requisitions?This checkbox is only enabled if the Deployment type is set to Job cost and the Create inventory and equipment stand-by transactions checkbox is selected. Select this checkbox to enter the G/L accounts that should be used for small tools, inventory, and equipment markups.
Equipment G/L account
Inventory G/L account
Small tools G/L account
Use the available drop-down arrows to select the G/L debit account codes you want to use for the current transaction. (Options listed here may vary based on your company's licensed modules.)
