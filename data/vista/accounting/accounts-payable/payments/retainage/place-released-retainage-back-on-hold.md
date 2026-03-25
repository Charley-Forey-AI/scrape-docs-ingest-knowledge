---
title: "Place Released Retainage Back on Hold | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/retainage/place-released-retainage-back-on-hold"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/retainage/place-released-retainage-back-on-hold"
---

# Place Released Retainage Back on Hold

You can put previously released retainage back on hold using AP Released Retainage. Use this option when the retainage was released in error or the wrong amount was released.
The title of the AP Release Retainage form changes to AP Release Retention for
 Australian companies and AP Release Holdback for Canadian companies. On this page,
 we use only the name AP Release Retainage. In addition, references to "retainage"
 across this page mean "retention" or "holdback."
The following video demonstrates placing released retainage back
 on hold.
Note: You must use a browser on your local computer to view this video, and not a browser in the cloud. If you are currently using a cloud-based browser, copy this page's URL and paste it into a web browser on your local computer.

To place released retainage back on hold:

1. From the main menu, select Accounts Payable > Programs > AP Release Retainage.The Batch Selection form displays.

1. Open a batch using one of the following methods:

- Select Create a new batch and enter the batch month in the Batch Month field.

- Select Use an existing batch and select the appropriate batch from the Unposted Batches grid.Note: If you select this option, you must use a batch that does not contain transactions for releasing retainage. The system does not allow mixing "release retainage" transactions with "place released retainage on hold" transactions in the same batch.

1. Select OK.The AP Release Retainage form displays.

1. To initialize previously released retainage transactions to the grid:

1. Select the arrow by the Selection Criteria for Release Hold heading to expand the section.

1. Use the selection criteria options to restrict the released retainage transactions pulled into the batch. See the F1 help on individual fields for more information.

1. In the Release Options section, select the Put previously released back on hold? checkbox.

1. In the Original Release Date field, enter the retainage release date by which to restrict transactions added to the batch.

1. Select Fill Grid.The system populates the grid with all previously released retainage transactions meeting the selected criteria, and sets the Type field for each transaction to 1-Undo Release. In addition, it sets the Amount field to the exact amount of the previously released retainage. This amount cannot be changed.

1. To manually add transactions to the grid:

1. In the Batch Seq field, enter +, N, or New to create a new record.

1. In the Type field, select 1-Undo Release.

1. In the Expense Month field, enter the expense month for the original AP transaction (the posted month of the original transaction for which retainage was withheld.)

1. Use the Transaction and Line fields to specify the transaction and line to place back on hold.

1. The Amount field defaults the exact amount of the previously released retainage. This amount cannot be changed.

1. [Process the batch](/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/batch-processing/process-a-batch#task-8952--en__task-8952).

The system places the specified release amounts back on
 hold and updates the GL accounts as applicable. You can then release the held amounts
 later as needed.Note:If you release retainage and split it for payment, but you put the retainage back on hold without paying any of the split, the batch posting action to put the retainage back on hold will automatically remove the split.

For more information about how the system handles the GL
 updates, see [Updates to GL for Retainage](/en/vista/vista/accounting/accounts-payable/payments/retainage/about-updates-to-gl-for-retainage).

Related information

- [AP Release Retainage/Retention/Holdback Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-release-retainageretentionholdback-form)

- [About Retainage](/en/vista/vista/accounting/accounts-payable/payments/retainage/about-retainage)

- [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice)
