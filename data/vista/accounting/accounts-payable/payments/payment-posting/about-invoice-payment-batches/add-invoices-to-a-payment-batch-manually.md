---
title: "Add Invoices to a Payment Batch Manually | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-invoices-to-a-payment-batch-manually"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-invoices-to-a-payment-batch-manually"
---

# Add Invoices to a Payment Batch Manually

You can manually add invoices to a payment batch directly in the AP Payment Posting form.

 If you are tracking compliance and want to be warned of non-compliant invoices at the moment they're entered, select the appropriate option in the AP Company Parameters form. For more information, see [Vendor Compliance Tracking](/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking).

1. Open the AP Payment Posting form.

1. In the Seq # field, enter N, New, or + to have the system generate the next available sequence number.

1. From the Pay Method drop-down, select the payment method.

- N-ePayments

- C-Check

- E-EFT

- S-Credit Service

1. In the CM Acct field, enter the bank account for paying this invoice.If you selected S-Credit Service as your pay method, this CM account must match the account you entered in the CM Acct # field in the AP Company Parameters form (Payment Services tab).
If you selected either C-Check or E-EFT as your pay method, this CM account cannot be the same as the account you entered in the CM Acct # field in the AP Company Parameters form (Payment Services tab).

1. If you selected the C-Check payment method, use the Check Type field to specify whether you are using a a C-Computer check or a M-Manual check. For more information about this field, see [Check Type](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-posting-form#ID-00006343--en) field help.

1. If you are using a manual check, do the following:

1. In the CM Ref# field, enter the check number.Note: The CM Seq# field is disabled and set to 0 for all payment types.

1. In the Paid Date field, enter the check's date. If you enter a date that is not the same month and year as the batch month, the system displays a warning; however, you can still post the payment.

1. In the Vendor field, enter the vendor number or press F4 to select from a list of valid vendors.The system displays the vendor's name, address, and additional information. You may override this information as needed.

1. Save the record.

1. In the detail section of the form, use the Month field to enter the invoice month. Press F4 to see a list of months with invoices for the specified vendor.

1. In the AP Trans field, enter the invoice number or press F4 to select from a list of invoices for the specified month.Note: The CM Acct field for an invoice must match the CM account specified in the header section of the form or you will not allowed to add the invoice. If a transaction added in the grid is missing a CM account number, the system automatically assigns the CM account specified in the header.

1. Enter additional lines as needed.
