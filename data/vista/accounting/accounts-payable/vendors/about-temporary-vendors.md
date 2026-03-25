---
title: "About Temporary Vendors | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/vendors/about-temporary-vendors"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/vendors/about-temporary-vendors"
---

# About Temporary Vendors

Use the AP Vendors form to create records for vendors you
 don't intent to use for very long.
To mark a vendor as temporary, select the Temporary checkbox on the Info tab.
Note: When you select the Temporary checkbox, all of the
 fields in AP Vendors become optional for the vendor, with the exception of the 1099
 fields (United States users),and the T5 fields (Canada users) on the Add'l Info tab.
 These fields are disabled, as you would not need to report this information for
 temporary vendors; however, the AP Transaction Entry form does allow you to enter this
 information for temporary vendors, if necessary.
If you
 are using temporary vendors, how you set them up may depend on whether or not you are
 required to keep their associated data.
If you need to keep data for temporary vendors, even
 for a short period of time, you need to set each temporary vendor up separately. This
 allows the system to track transaction data the same as for a regular vendor. When you
 want to purge the temporary vendor from the system, check the Paid Transactions and
 Temporary Vendors box when using the AP Purge form.
If you do not need to keep data for temporary vendors, you can set up a single vendor number (such as 999) for all temporary vendors. Although you are not required to enter the vendor name, you will be required to enter a sort name because the system uses the sort name whenever alphabetical sorting is used, such as on reports and lookups (F4). You could use TEMP VENDOR as the sort name so that it is easily identified.
When posting transactions for temporary vendors using the same vendor number, use the Address Override Info tab in the AP Transaction Entry form to enter each vendor’s name and address. This not only allows you to identify the vendor for each transaction, but also directs the system to print a separate check for each vendor, even though the same vendor number is used.

Related information

- [AP Vendors Form](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form)

- [AP Transaction Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form)

- [AP Purge Form](/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/ap-maintenance-forms/ap-purge-form)
