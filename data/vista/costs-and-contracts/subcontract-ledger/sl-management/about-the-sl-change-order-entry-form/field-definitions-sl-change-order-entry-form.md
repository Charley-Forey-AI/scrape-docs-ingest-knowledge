---
title: "Field Definitions: SL Change Order Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-change-order-entry-form/field-definitions-sl-change-order-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-change-order-entry-form/field-definitions-sl-change-order-entry-form"
---

# Field Definitions: SL Change Order Entry Form

The following is a list of field descriptions for the SL
 Change Order Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Sequence #

 If this is a new batch, this field automatically defaults to “New.” The system assigns sequence numbers, so accept the default.
 If this is an existing batch, enter the sequence number to work on, or, enter “New” to add a new sequence to the batch.
 To pull an existing change order transaction into the batch, select “Add Transaction” from the File menu to access the Add Transaction to Batch form.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-change-order-entry-form)SL Change Order Entry

## Action

The Action drop-down on multiple forms throughout Vista.
When entering new records, this field defaults to A (Add) and cannot be accessed.
For existing records, select the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all related module files. (The delete functions in the toolbar and Records menu only delete the entry from the batch.

## Subcontract

Enter the subcontract that requires a change order. The system disables this field when you are editing or deleting a previously posted change order.
Note: When the subcontract change order batch is posted, PM Subcontract Detail (PMSL database table) is updated for the change order record if the SL batch month and transaction are found in PMSL.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-change-order-entry-form)SL Change Order Entry

## Item#

Enter the subcontract item (regular, change
 order, or add-on) that the change order applies to or press F4 to select a one from a list.
 This field is disabled when you are editing or deleting a previously posted change
 order.
If you enter a subcontract item number that
 does not already exist on the subcontract, a message will appear asking if you would like
 to create it. Click Yes and the [SL Add Item](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-add-item-form) form
 will display.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-change-order-entry-form)SL Change Order Entry

## Sub CO#

 Enter the subcontract change order number, up to 6 digits. This number is used to determine which subcontract change orders are included in “The net change by previously authorized Subcontract Change Orders was.....” line of the SL Change Order report. When printing this subcontract, all subcontract change orders with a number less than the one entered here will be included in that amount.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-change-order-entry-form)SL Change Order Entry

## Approved CO

Enter the approved change order number. This number represents the owner’s change order number.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-change-order-entry-form)SL Change Order Entry

## Date

Enter the date for this change order, or, accept the current date default. This is the month the change order units and dollars will be added to committed costs.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-change-order-entry-form)SL Change Order Entry

## Description

Enter a description of the change order. The value in this field can be up to 60 characters long.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-change-order-entry-form)SL Change Order Entry

## Change to Current: Units

 Enter the number of units that this change order affects the original units by. If subtracting from the original units for the subcontract item, enter as a negative amount (for example, –150.000).

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-change-order-entry-form)SL Change Order Entry

## Change to Current: Unit Cost

This field is only enabled if the subcontract item is added on the fly using SL Item Add, and the unit of measure is not LS (lump sum). Otherwise, the field is disabled and changes to the unit cost cannot be made.
Enter the unit cost of the new item.
Once the change order is saved, the resulting calculations are displayed in the fields in the lower section of the form.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-change-order-entry-form)SL Change Order Entry

## Change to Current: Total Cost / Add-on Amt

The label of this form displays depending on the item type specified. The two label options are discussed below.
Total Cost
 This label displays for LS (lump sum) items only. Specify the amount by which this change order affects the original total cost of the subcontract.
Once the change order is saved, the resulting calculations are displayed in the fields in the lower section of the form.
Add-on Amount
This label displays for add-on items only. Specify the amount by which this change order affects the original add-on amount. If the original add-on amount is a negative amount, a negative amount will add to the total, while a positive amount will subtract from the total.
For example:
Original Add-on Amount:
–200.00
–200.00

Change to Current Add-on Amount:
–150.00
150.00

New Add-on Amount:
–350.00
–50.00

Once the change order is saved, the resulting calculations are displayed in the fields in the lower section of the form.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-change-order-entry-form)SL Change Order Entry
