---
title: "Set up Credit Services with Comdata | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments/set-up-credit-services-with-comdata"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments/set-up-credit-services-with-comdata"
---

# Set up Credit Services with Comdata

To use credit card services, you must set up the provider you
 are using. This page covers setting up credit card service provider information for
 Comdata.
You must have specific pieces of information provided by Comdata.

1. In the VA Site Settings form, Comdata FTP Settings section, enter the connection information provided by Comdata in the

 URL,

 Port,

 User ID, and

 Password fields.

1. In the AP Company Parameters form, on the Payment Services tab, select 1-Comdata from the Credit Service drop-down.The system enables the fields in the Comdata section.

1. In the CM Acct field, enter the CM account or press

 F4 to select from a list.This account provides a contra account to credit when you initialize credit card payments through the specified credit services vendor.
Note: You must specify an account that exclusively tracks credit
 card service payments. This account must be different from the

 CM
 Account # field on the Subledgers tab.

1. If you want to override the connection information set in the VA Site Setting form, enter that connection information in the

 URL,

 Port,

 User ID, and

 Password fields.

1. Enter your Comdata account code, customer ID, and code word in the

 Account Code,

 Customer ID, and

 Code Word fields, respectively.

1. (Optional) In the

 Location Code field, press F4 to look up available AP Invoice Header fields. This maps up to 10 characters to the Location field of the PS20 Payment Request file.

1. (Optional) In the

 Inv Comments field, press

 F4 to look up available AP Invoice Header fields. This maps up to 60 characters to the Comments field of the PS20 Payment Request file.

1. Save the record.

 You are now set up to pay vendor invoices by credit
 card using Comdata.
 For each vendor that you will pay by credit card,
 you must set the default payment method to Credit Service in the AP Vendors form. For more
 information, see [Set the Vendor's Payment Method: U.S. and Canada](/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-payment-methods/set-the-vendors-payment-method-u.s.-and-canada) or [Set the Vendor's Payment Method: Australia](/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-payment-methods/set-the-vendors-payment-method-australia).

Related information

- [Credit Card Payments](/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments)

- [AP Company Parameters Form](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form)
