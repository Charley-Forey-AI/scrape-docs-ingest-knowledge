---
title: "Sub Vendors | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/vendors/sub-vendors"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/vendors/sub-vendors"
---

# Sub Vendors

You can link vendors together using the master vendor/sub vendor feature in Accounts Payable.
In the AP Vendors form, you can link vendors together using the master vendor/sub vendor feature. This is done by assigning a master vendor to each vendor you want designated as a sub vendor (in the Master Vendor field), according to these rules:

- you can assign a single vendor as a master vendor to multiple sub vendors

- a master vendor cannot already exist as a sub vendor for another master vendor

- vendors designated as sub vendors cannot be assigned as master vendors to other sub vendor

This feature is especially useful if you do not allow duplicate AP reference numbers and want the AP Reference validation to include all associated vendors. By setting up master and sub vendors, as well as selecting the appropriate validation option in the AP Company Parameters form (using the Check for unique APRef dropdown), you can ensure that the validation process checks the AP reference number against all vendors in the master/sub vendor group. You can also override the company validation by vendor in the AP Vendors form using the Override Unique APRef Level dropdown on the Add'l Info tab.
For example, when entering a transaction for a master vendor, the system checks the AP reference number to make sure it has not already been used by the master vendor or any of the associated sub vendors. If it has, the system displays a warning and disallows the entry. See [Checking for Unique AP Reference Numbers](/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/check-for-unique-ap-reference-numbers) for more information.
