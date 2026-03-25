---
title: "Field Definitions: PO Receipt Expense Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipt-expense-initialize-form/field-definitions-po-receipt-expense-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipt-expense-initialize-form/field-definitions-po-receipt-expense-initialize-form"
---

# Field Definitions: PO Receipt Expense Initialize Form

The following is a list of field descriptions for the PO
 PO Receipt Expense Initialize form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Update GL/Subledgers on Receipt

Check this box to have GL accounts and subledgers updated when receiving goods on purchase orders (in PO Receipts Entry). When selected, JC Interface, EM Interface, IN Interface, and GL Expense Interface Level fields are enabled, and you must define what information will be updated to GL and at what level
Do not check this box if GL accounts and subledgers will not be updated when receiving goods on purchase orders.
Note: If you elect to use this option, and you have existing receipts, when you click the Create Batch button, the Detail Preview grid is populated with all existing PO items that are marked for receiving and have a difference between what has been received and what has been invoiced (dollars and units).
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipt-expense-initialize-form)PO Receipt Expense Initialize
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## JC Interface Level

- Detail - If this option is selected, one GL/Subledger entry will be created for each Job PO transaction in a batch.

- None - If this option is selected, no GL/Subledger update for Job PO transactions will occur.

[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipt-expense-initialize-form)PO Receipt Expense Initialize
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## EM Interface Level

- Detail - If this option is selected, one GL/Subledger entry will be created for each Equipment PO transactions in a batch.

- None - If this option is selected, no GL/Subledger update for Equipment PO transactions will occur.

[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipt-expense-initialize-form)PO Receipt Expense Initialize
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## IN Interface Level

- Detail - If this option is selected, one GL/Subledger entry will be created for each Inventory PO transactions in a batch.

- None - If this option is selected, no GL/Subledger update for Inventory PO transactions will occur.

[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipt-expense-initialize-form)PO Receipt Expense Initialize
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## GL Expense Interface Level

Select one of the options below to indicate
 how GL is to be updated when PO expense entries are posted.

- Summary - If this option is selected, Expense PO
 entries will be summarized and one GL/Subledger entry will be posted for each unique
 GL account. Enter the description that will be used for each of these transactions in
 the Summary
 GL Description field below.

- Detail - If this option is selected, one
 GL/Subledger entry will be created for each Expense PO transactions in a batch. Use
 the "Select Available Items for Detail Level GL Descriptions” box to define the
 detail description that will be used for these entries. None - If this option is
 selected, no GL/Subledger update for Expense PO transactions will occur. When this
 option is selected, the “In Use” checkbox is not selected on PO Company Parameters,
 and the GL Expense Interface Level cannot be changed on that form.

Note: The interface level selected here will also be used
 when updating Cost and WIP accounts for work completed purchase lines (type 5-Purchase) on
 SM work orders.
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipt-expense-initialize-form)PO Receipt Expense Initialize
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Summary GL Description

Used for 'Summary' GL Expense Interface Level.
Enter the description you want used each time a summarized Expense PO entry is interfaced to GL. Up to 60 characters allowed.

[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipt-expense-initialize-form)PO Receipt Expense Initialize
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Detail Level GL Description

Using the selection box to the right, indicate the fields you want included as part of the GL transaction description each time a detailed expense PO entry is interfaced to GL. Available fields are:

- Vendor#

- Sort Name

- Receiver#

- Receipt Date

- PO#

- PO Item

- Trans#

Items will be added to the description in the order they are selected. To remove an item from the description, unselect the item. When the GL entry is made, the system pulls the data from each of the fields and creates the description from the information.

[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipt-expense-initialize-form)PO Receipt Expense Initialize
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters

## Accrual Account

Specify the accrual account to be updated when Job, Equipment, Inventory, and Expense PO transactions are interfaced to GL. This account will also be updated when receiving materials (via PO Receipts Entry) that were purchased for an SM work order.
Note: The GL account specified here must be set up GL Chart of Accounts with a subledger type of “P” or null.
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipt-expense-initialize-form)PO Receipt Expense Initialize
[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company Parameters
