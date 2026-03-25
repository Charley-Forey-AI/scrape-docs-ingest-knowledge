---
title: "Check for Unique AP Reference Numbers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/check-for-unique-ap-reference-numbers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/check-for-unique-ap-reference-numbers"
---

# Check for Unique AP Reference Numbers

Vista provides you with the
 flexibility to allow/disallow duplicate AP reference
 numbers when entering AP transactions (AP Transaction
 Entry, AP Unapproved Invoice Entry).
In both the AP Company Parameters and AP Vendors
 forms, options are provided for controlling how
 the validation process handles duplicate reference
 numbers.To set requirements
 for unique invoice numbers:

1. In the AP Company Parameters form, select the Prevent duplicate AP Reference checkbox on the Invoice Options tab.

1. Choose a default
 validation method to use for checking reference
 numbers. If you wish to override the default
 option for a vendor, you can do so in the AP
 Vendors form.The following describes how the validation
 methods function:

- 0-No Override - This option is only available in
 the AP Vendors form and indicates that an override
 is not used for the currently selected vendor. In
 this case, the option specified at the company
 level is used.

- 1-By Vendor & Co - Use this option to have
 the system check for duplicate reference numbers
 by vendor within the current company. If selected,
 and the validation process encounters a duplicate
 reference number for the specified vendor in the
 current company, a warning displays.

- 2-By Vendor X-Co - Use this option if you have
 several companies that share the same vendor file
 and you want the validation process to check all
 companies for duplicate reference numbers. If
 selected, and a duplicate reference number is
 encountered for the vendor in any of the companies
 sharing the vendor file, a warning is
 displayed.

- 3-By Master Vendor & Co - Use this option if
 you are using the master vendor/sub vendor
 feature, and you want the validation process to
 include all associated vendors within the current
 company when checking for duplicate reference
 numbers. If selected, and the system encounters a
 duplicate reference number for the master/sub
 vendor group (i.e. the master vendor and all
 assigned sub vendors) in the current company, a
 warning is displayed.

- 4-By Master Vendor X-Co - Use this option if you
 are using the master vendor/sub vendor feature and
 you have several companies sharing the same vendor
 file that should be included when checking for
 duplicate reference numbers. If selected, and the
 system encounters a duplicate reference number for
 the master/sub vendor group (i.e. the master
 vendor and all assigned sub vendors) in any of the
 companies sharing the vendor file, a warning is
 displayed.

In
 all cases, invoice entry is only allowed if the
 Prevent
 duplicate AP Reference checkbox is
 not selected. Duplicate AP references are defined
 in part by the Enable
 Case-Insensitivity on AP References
 checkbox. See this checkbox's [F1 field help](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form/field-definitions-ap-company-parameters#ID-00005b04--en) for
 further information.
Note: If you
 plan to use the 'master vendor/company' or 'master
 vendor/cross-company' methods, and you only have a
 few vendors set up using the 'master vendor/sub
 vendor' theme, it is suggested that you set these
 levels at the vendor level, and set the company
 level to either 1 or 2 (i.e. if you set the vendor
 level to 3, set the company level to 1). This way,
 the master vendor/sub vendor validation only
 occurs for those vendors designated as master
 vendors or sub vendors.
