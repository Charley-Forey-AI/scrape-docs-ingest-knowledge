---
title: "PO Receipt Expense Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipt-expense-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipt-expense-initialize-form"
---

# PO Receipt Expense Initialize Form

Use this form to define whether you will update GL accounts and subledgers when receiving goods on purchase orders.

You can access this form by selecting File > Initialize Expenses on Receipt from PO Company Parameters.

- Update GL/Subledgers on Receipt - This option is used in conjunction with the ability in PO to accrue 'received' items as actual units and costs. When this option is selected, GL accounts and subledgers are updated whenever goods are received on purchase orders (flagged for receiving) in PO Receipts Entry. If not selected, GL accounts and subledgers are not updated when receiving goods in PO.

- Interface Levels - The JC Interface, EM Interface, IN Interface, and GL Expense Interface Level fields are used to specify what information will be updated to GL and at what level. If you are updating GL expenses, you will also need to define the Summary or Detail GL description, as well as the Accrual Account. The Accrual Account is used to indicate which GL account will be credited when Job, Equipment, Inventory, Expense, and SM Work Order PO transactions are interfaced to GL. This account must be designated if using these options, and must have a subledger code of “P” (Payables) or null.Note: If you using the Service Management module (SM), the GL Expense Interface option specified here will also be used to determine the level of detail when updating Cost and WIP accounts for work completed purchase lines (type 5-Purchase).

- Initialize a Batch - Once you have made the necessary changes, select Initialize Batch. The system initializes all PO items flagged for receiving that have differing Received and Invoiced values, and display them in the Detail Preview grid. If the Update GL/Subledgers on Receipt checkbox was previously selected and you deselect it, the update backs out the units and cost from JC, EM, and/or IN, and reverses the GL distributions. If the Update GL/Subledgers on Receipt box was previously unselected and you selet it, GL is updated with the expense, as are JC, EM, and/or IN, and the AP Accrual Account is credited. Previously processed records are not updated.Note: If you wish to clean up your POs before making the change, you can clear the entries and cancel the batch, update your POs accordingly, then rerun the initialization process in this form. However, before you cancel/clear the batch, it is suggested that you access the Batch Process form (File menu), validate the batch, and print the audit lists. You can then clear the batch from within the Batch Process form, or exit the form and clear the batch using the Cancel and Clear button.

- Cancel and Clear Batch - Select File > Cancel Batch to cancel and clear the batch. All purchase order items listed in the Detail Preview grid are cleared from the batch, the batch is canceled, and the PO Receipt Expense Initialize form closes.

- PO Item Distribution - The PO item distribution feature allows you to distribute PO items into multiple lines when they are received. When expensing receipts using the PO Receipt Expense Initialize form, the PO item distribution lines are used as the basis for the expenses.Note: Even if you do not use the item distribution feature, when you create a PO item, the system automatically creates a single PO item line that is identical to the PO item, which is then used to expense the receipt. For more information about the PO Item Distribution feature, see [PO Item Distribution Overview](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-item-distribution-overview).
