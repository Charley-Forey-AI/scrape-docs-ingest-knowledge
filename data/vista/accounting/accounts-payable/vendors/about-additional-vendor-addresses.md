---
title: "About Additional Vendor Addresses | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/vendors/about-additional-vendor-addresses"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/vendors/about-additional-vendor-addresses"
---

# About Additional Vendor Addresses

What to know when assigning additional addresses to vendors
 using the Addtl Addresses tab in the AP Vendors form.
In addition to the main payment and purchase addresses that you enter on the Info tab, a vendor may have additional addresses used for paying invoices or purchase orders. This form allows you to set up each additional vendor address and define whether the address is a 'payment' or 'purchase order' address, or whether it can be used for either.
For each additional address you set up, an address sequence is assigned. The address sequence uniquely identifies the additional address for the vendor and is used when entering transactions (in AP Transaction Entry, AP Recurring Invoices, AP Unapproved Invoices, or PO Purchase Order Entry) to indicate which address will be used to override the main payment or purchase order address.
Note: (U.S.) you can use one of these addresses when printing
 1099s, if you need to send the 1099 to an address other than the payment address specified
 for the vendor on the Info tab of the AP Vendors form. See [Setting Vendors Subject to
 1099 Reporting](/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-reporting/set-vendors-subject-to-1099-reporting-united-states) for more information.

## Updating Additional Address for Sub Vendors

When you set up an additional address for a master vendor, a message
 displays asking if sub vendor addresses should be updated. If you click
 Yes, the system automatically sets up the newly added address for the sub
 vendor. If the address sequence of the new address already exists for the
 sub vendor, the system adds the address using the next available sequential
 number.

Only addresses set as 1-Payment or
 0-Both in the Address Type field can be updated to sub vendors.
