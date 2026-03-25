---
title: "Set up Master/Sub Vendor Level Validation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/check-for-unique-ap-reference-numbers/set-up-mastersub-vendor-level-validation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/check-for-unique-ap-reference-numbers/set-up-mastersub-vendor-level-validation"
---

# Set up Master/Sub Vendor Level Validation

If you are using the master vendor/sub vendor feature, you can
 set up validation for AP reference numbers to ensure accurate control over which vendors are
 included.
There are two ways to set up validation for AP reference
 numbers when using the Master/Sub Vendor feature: by company and by vendor.The following describes both options

1. To set up master/sub vendor
 level validation by company (only use if ALL vendors are set up as master vendors or
 sub vendors):

1.  In the AP Company Parameters form, set the
 Check for unique APRef drop-down to 3-By Master Vendor & Co
 or 4-By Master Vendor,
 X-Co.

1. In the AP Vendors form, Info tab, enter the
 master vendor for each sub vendor in the Master Vendor field.

1. In the AP Vendors form, Add'l Info tab, set the
 Override Unique APRef Level  drop-down to 0– No Override.

1. To set up master/sub vendor level validation by vendor:

1. In the AP Company Parameters form, set the
 Check for unique APRef drop-down to 1-By Vendor & Co or
 2-By Vendor,
 X-Co.

1. In the AP Vendors form, Info tab, use the
 Master Vendor
 field to enter the master vendor for each sub vendor in the master/sub vendor
 group.

1. In the AP Vendors form, Add'l Info tab, set the
 Override Unique APRef Level drop-down for each master vendor
 and sub vendor to 3-By Master
 Vendor & Co or 4-By Master Vendor, X-Co (depending on the company level). Make
 sure that each vendor in the master/sub vendor group is assigned the same
 option.

1. For all other vendors not set up as a master or
 sub vendor, set the Override Unique APRef Level
 drop-down (in AP Vendors) to 0-
 No Override.

Related information

- [AP Vendors Form](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form)
