---
title: "Field Definitions: AP Recurring Invoice Posting Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoice-posting-form/field-definitions-ap-recurring-invoice-posting-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoice-posting-form/field-definitions-ap-recurring-invoice-posting-form"
---

# Field Definitions: AP Recurring Invoice Posting Form

The following is a list of field descriptions for the AP Recurring Invoice Posting form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Restrict By Frequency

 Check this box if you want to restrict by frequency code. Use the frequency code options box to the right of this field to select the frequency codes you want included in the selection process.
 Do not check this box if the want to include all frequency codes in the selection process.

## Restrict By Vendor

Check this box if you want to restrict by vendor. Use the Vendor field to the right of this field to select the vendor.

## Vendor

 Specify the vendor (from AP Vendors) whose
 recurring invoices you want to process.

## Restrict By Invoice

 Check this box if you want to restrict which of a vendor’s recurring invoices to process. Use the Beginning and Ending Invoice fields to specify the range of invoices. This field is disabled until a valid vendor has been entered in the Vendor field.
 Do not check this box if you want to include all of a vendor’s recurring invoices.

## Invoice Date

This field initially defaults the current date. Accept the default, or specify which date you want to appear as the Invoice Date on all of the recurring invoices. This date does not apply to “once a month” invoices that have an Invoice Day specified.
When you have entered all of the selection criteria, click the Update button to add the entries to the batch. When done, the selected invoices appear in the grid at the bottom of the screen, the selection options are cleared, and you can make new selections.
Note: To delete an invoice from the grid, highlight the
 invoice and press the Delete key (keyboard). Once you answer OK to the "1 invoice was
 deleted from the AP Header Batch File" message, the invoice is cleared from the grid. To
 delete all invoices from the batch, click the Post button to bring up the AP Batch Process
 form, and click the Clear Batch button.
When you have finished adding all invoices you want to process to the batch, click the Post button to post the batch. The AP Batch Process form is opened, and you can process the batch as normal.
