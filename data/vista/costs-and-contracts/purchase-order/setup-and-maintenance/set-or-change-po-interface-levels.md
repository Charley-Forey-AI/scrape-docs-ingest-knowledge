---
title: "Set or Change PO Interface Levels | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/set-or-change-po-interface-levels"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/set-or-change-po-interface-levels"
---

# Set or Change PO Interface Levels

You can set the JC, GL, IN, and EM interface levels for
 updating GL /Subledgers in the PO module using the PO Receipt Expense Initialize
 form.

The Update GL/Sub-Ledgers on Receipt section in the PO Company Parameters form
 indicates whether the system is updating GL accounts and subledgers when you enter and
 post receipts using PO Receipts Entry or PO Initialize Receipts. With the exception
 of the GL Expense Interface group box, the system disables the fields in this
 section and you can only change the settings via the PO Receipt Expense Initialize
 form. You can toggle the radio button options in the GL Expense Interface group box
 on this form if you selected either the Summary or Detail level in PO Receipt
 Expense Initialize. You cannot change the interface options directly on this form,
 as it might adversely affect long-standing, open purchase orders.
The
 following instructions discuss how to set or change PO interface
 levels.

1. Open PO Company Parameters (Purchase Orders > Programs > PO Company Parameters).

1. In the PO Company field, enter the PO company or press
 F4 to select from a list of valid PO companies.

1. Select File > Initialize Expenses on Receipt. This opens the Batch Selection form.The Batch Selection form displays.

1. In the Do you want
 to field, select either the Create a new
 batch or Use an existing batch
 option.

1. If you selected to
 create a new batch, enter the batch month in the Batch
 Month field. If you selected to use an existing batch, select
 the batch from the list of Unposted Batches.

1. Select OK.The PO Receipt Expense Initialize form displays.

1. Select the
 Update GL/Sub-Ledgers on Receipt checkbox to enable
 the interface level settings (if not already selected).

1. Set the JC, IN, EM, and GL interface levels accordingly.For more information about each interface level/option, see the F1
 Help.

1. For the GL Expense
 Interface Level, set the interface descriptions as appropriate:

- If you set the GL Expense Interface Level option
 to Summary, use the Summary GL Description field to
 enter the description to use each time a summarized expense purchase order
 is interfaced to GL.

- If you set the GL Expense Interface Level option
 to Detail, use the Detail Level GL Description selection box to select the
 fields you want included in the GL transaction description each time a
 detailed expense purchase order is interfaced to GL.Field names are added
 to the description in the order that you select them from the selection
 box. For more information, refer to the [F1 help](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form/field-definitions-po-company-parameters-form#ID-0002fc1f--en) for this field.

1. In the
 Accrual Account field, enter the accrual account for
 updating when the system interfaces Job, Equipment, Inventory, and Expense
 purchase order transactions to GL.

1. Select Initialize Batch.A "batch initialized" message displays.

1. SelectFile > Batch Process.

 A message displays indicating that PO was updated with the
 new settings. Once you close the message, you are returned to the PO Company Parameters
 form.
