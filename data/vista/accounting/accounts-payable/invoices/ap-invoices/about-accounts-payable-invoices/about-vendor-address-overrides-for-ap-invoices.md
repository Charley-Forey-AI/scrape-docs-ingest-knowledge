---
title: "About Vendor Address Overrides for AP Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-vendor-address-overrides-for-ap-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-vendor-address-overrides-for-ap-invoices"
---

# About Vendor Address Overrides for AP
 Invoices

To any invoice, you can assign a name and address that is
 different than what is found in the vendor's record.
When entering invoices, whether using the AP
 Transaction Entry, AP Recurring Invoices, or AP Unapproved Invoice Entry form, you can use the
 fields on the Address Overrides tab to do a one-time override to the vendor's payment address
 as defined in the AP Vendors form. Each override address generates a separate check during the
 payment process.
This is most commonly used with a temporary vendor so that the same
 temporary vendor can be reused for multiple invoices.
Note: If you need to store all invoice data for each
 temporary vendor, set up each vendor separately instead of using the same temporary
 vendor.
There are two options for overriding the payment
 address:
The first option (available in the AP Transaction Entry and AP Unapproved
 Invoice Entry forms only) is to select the Override Payment Address checkbox and
 manually enter an override address and/or vendor name in the corresponding fields.
The second option is to enter an additional
 address sequence number in the Address Seq # field. In order to use this
 option, the vendor must have at least one additional address defined on the Add'l Addresses
 tab in the AP Vendors form. Additionally, the Address Type field for the additional address
 record must be set to either 1-Payment or 0-Both. For more
 information, see [Assigning Additional Addresses to Vendors](/en/vista/vista/accounting/accounts-payable/vendors/about-additional-vendor-addresses).
Note: Address sequences can also be entered for purchase
 orders in PO. If you enter a PO line in this form, the PO’s address sequence (and its
 associated address information) will default for the invoice here if no override address or
 address sequence is specified for the invoice.
Regardless of the manner in which an override
 address is defined for an invoice, the specified address prints on all checks generated from
 the invoice unless it is overridden in the AP Payment Workfile form.

Related concepts

- [About Temporary Vendors](/en/vista/vista/accounting/accounts-payable/vendors/about-temporary-vendors)

- [AP Vendors Form](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form)

- [AP Payment Workfile Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-workfile-form)
