---
title: "Field Definitions: JC Field Ticket Add Costs Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/jc-field-ticket-add-costs/field-definitions-jc-field-ticket-add-costs-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/jc-field-ticket-add-costs/field-definitions-jc-field-ticket-add-costs-form"
---

# Field Definitions: JC Field Ticket Add Costs Form

The following is a list of field descriptions for the JC Field
 Ticket Add Costs form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Contract

The Contract field on the JC Field Ticket Add Costs form.
This field is disabled when you access this form via the JC Field Tickets form, and defaults the contract associated with the selected field ticket.
Enter the contract associated with the field ticket you want to work with. Press F4 for list of valid contracts.

## Mth

The Mth field on the JC Field Ticket Add Costs form.
Enter the month to include and press Return. The grid displays all costs posted to the contract in the specified month.Note: To further filter records in the grid, you can enter the transaction type to include in the Type field.

## Type

The Type field on the JC Field Ticket Add Costs form.
Enter the transaction type to include or press F4 to select from a list of valid transaction types. The grid refreshes to show only those transactions of the specified type.
Transaction types may apply to multiple sources. Therefore, if you want to see only costs associated with a specific source, leave the Type field blank and use the grid filter to show only costs for the specified source. The following shows the transaction types associated with each source.
SourceTrans Type
AP EntryAP, RU
AR ReceiptJC
EMRevEM, RU
IN MatlOrdMO, RU
JC CostAdjAP, CA, EM, IC, JC, MO, MS, PR,
 RU
JC MatUseIN, MI, RU
MS TicketsMS, RU
PR EntryPR, RU
SM WorkOrdAP, EM, IN, JC, MI, PR

## Show ticketed costs only

The Show ticketed costs only checkbox on the JC Field Ticket Add Costs form.
Select this checkbox only if you want to remove costs from the specified field ticket. The system automatically refreshes the grid to show only ticketed cost detail.
Do not select this checkbox if you are adding costs to the specified field ticket.

## Field Ticket

The Show ticketed costs only checkbox on the JC Field Ticket Add Costs form.
Enter the field ticket number. This will be either the field ticket to which you are adding costs or the field ticket from which to remove costs. Press F4 for a list of valid field tickets for the specified contract.

## Include

The Include checkbox on the JC Field Ticket Add Costs form.
Select this checkbox for each cost detail entry to add or remove for the specified field ticket.Note: You can select all items in the grid at once by clicking Check All (above the grid). You can also highlight several items in the grid (consecutively or randomly), which toggles the Check All button to Check Selected. Then select Check Selected.
