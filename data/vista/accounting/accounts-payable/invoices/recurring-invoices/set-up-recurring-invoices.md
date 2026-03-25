---
title: "Set Up Recurring Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/set-up-recurring-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/set-up-recurring-invoices"
---

# Set Up Recurring Invoices

Use the AP Recurring Invoices form to set up recurring invoices for expenses that occur on a regular basis (rent, loans, or other fixed monthly charges).
When you set up a recurring invoice, you can:

- Assign a frequency to indicate how often the system should process the invoice.

- Set a limit amount for the invoice. Each time a transaction posts against this invoice, the system compares the amount invoiced-to-date with the limit. If the combined amount exceeds the limit, only the amount up to the limit is posted.

- Apply an expiration date to the invoice. Once the expiration date is reached, the system no longer posts transactions against the invoice.

To set up recurring invoices:

1. In the Vendor field, enter a vendor number or press F4 for a list.

1. Enter the invoice number in the Invoice field.Note: The system uses the invoice number to create the AP reference number. The number you enter is combined with a system-assigned sequence number (up to 4 digits) to create the reference number when [posting the recurring invoice](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoice-posting-form). For example, if the invoice number is 24000, then the system would create an AP reference number of 24000-1 for the first invoice, 24000-2 for the second, and so on.

1. In the Description field, enter a description for the invoice.

1. In the Pay Terms field, enter the payment terms or accept the default value which comes from the AP Vendors form.

1. In the Hold Code field, enter a hold code for this invoice, if necessary.

1. In the Frequency field, enter the frequency that indicates how often the system should post this invoice.Note: When posting recurring invoices, the system uses the frequency code to group invoices together with the same posting sequence.

1. In the Pay Control field, enter a pay control code, if necessary.Note: Pay Control codes group invoices together for payment. For example, you could assign all loan payments the same control code. Then when creating a payment batch, you could select all invoices with that pay control code.

1. Select the payment method for this invoice from the Pay Method drop-down: N-ePayments, C-Check, E-EFT, or S-Credit Service. This field initially defaults based on the Pay Method field in the AP Vendors form (Payment Method tab) for the selected vendor. For more information, see the [F1](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form/field-definitions-ap-recurring-invoices-form#ID-00006ac8--en) help.

1. In the CM Account field, enter the CM account for the invoice or accept the default value which comes from the AP Company Parameters form.

1. Select the Monthly checkbox if the invoice should only be posted once a month. If you select this checkbox, and a transaction for this invoice already exists in an expense month, the system will not generate another transaction for the same month.

1. If you want to include this transaction in 1099 totals, fill in the information in the 1099 fields. For more information, see [Prepare and Process 1099s](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/prepare-and-process-1099s).

1. Select the 1099 checkbox.The system enables the Type and Box# fields.

1. In the Type field, enter the 1099 type or press F4 to select from a list.

1. In the Box# field, press F4 to select from a list of valid boxes on the 1099 form that will be used to accumulate and print 1099 amounts.

1. If there is an expiration date for this invoice, use the Expire Date field to enter the expiration date.

1. If there is a limit for this invoice, use the Limit field to enter the limit. If you do not want to set a limit, leave this field at the 0.00 default value.

1. If you want to override the address information for the vendor, use the Address Overrides tab to enter the vendor address information to use for this invoice. For more information, see [About Vendor Address Overrides for AP
 Invoices](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-vendor-address-overrides-for-ap-invoices#ID-00003c96--en__ID-00003c96).

1. Save the record.

1. [Add detail lines to the invoice](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/enter-accounts-payable-invoices/enter-ap-invoice-lines-u.s.).

You can now create additional recurring invoice entries or [post the invoice](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoice-posting-form) to a batch.
