---
title: "Initialize Subcontracts to Worksheets | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/initialize-subcontracts-to-worksheets"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/initialize-subcontracts-to-worksheets"
---

# Initialize Subcontracts to Worksheets

Use the Initialize Worksheet feature to add a range of subcontracts to the worksheet - for example all of the subcontracts on a specific job.
You can also manually add specific subcontracts to the worksheet using the [SL Add to
 Worksheet](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/add-a-subcontract-to-a-worksheet) form. See [Using the SL Worksheet](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet) for an overview on using the SL Worksheet form.
When using the Job Billing module, invoice amounts can reflect quantities from Job Billing. See [About the SL Worksheet Initialization Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/about-the-sl-worksheet-initialization-form).

1. Open the SL Worksheet form.

1. Select File > Initialize Worksheet. This opens the SL Worksheet Initialization form.

1. Use the fields in the Job and Subcontract Selections section to select the subcontracts that should be added to the worksheet. Press F1 while in a field for detailed information about that field.

1. Use the fields in the AP Transactions Defaults section to add default information to all of the subcontracts that are being initialized. For example complete the CM Account field and this account will be selected on all of the subcontracts that are added to the worksheet. Press F1 in any field for more detailed information about that field. If a field in the AP Transaction Defaults section should default the same value each time a worksheet is initialized (for example if you always use the same pay control or CM account), you can use the Field Properties (press F3) to set a default value for that field.

1. Click Update. The SL Worksheet form displays with initialized subcontract information.Maximum Retention
If you set a maximum retention amount for the subcontract, and you exceed the maximum retention amount, the system automatically distributes the retention amount based on the distribution setting for the subcontract. For more information, see [About Subcontract Maximum Retention Amounts](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-maximum-retention-amounts).
Backcharges and add-ons
In addition to regular subcontract items, all backcharge items will be included on the worksheet, with an invoice amount of 0.00. Add-on items are also included, but the invoice amount depends on the add-on type:

- If the add-on is an “Amount” type, the invoice amount defaults to the remaining item amount (current minus invoiced).

- If the add-on is a “Percent” type, the invoice amount defaults to either the remaining Item amount or the Item’s Add-on percentage multiplied by the total invoice amount of all regular and change order items (which will not exceed the add-on’s remaining amount). The Apply Percentage to Each Invoice checkbox (SL Add-ons) determines how the percent type is calculated.

For more information on add-ons, see [About the SL Add-Ons Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-add-ons-form).[Using the SL Worksheet](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)
