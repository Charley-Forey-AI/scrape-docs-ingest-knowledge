---
title: "Cash Management Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/accounting/cash-management-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/accounting/cash-management-features"
---

# Cash Management Features

Vista 2021 R1 delivers on user-requested Cash Management enhancements, fixes, and other improvements.

## Allow Resetting AP/PR Beginning Check Numbers by CM Account

You can now override the standard defaulting process for beginning check numbers (printed in AP or PR) by CM account.
The standard default procedure for check printing bases the default on the highest check number in the system, which includes manually entered check numbers. If a manual check has been issued using an arbitrary high number, that number plus one becomes the default for each check run.
To allow overriding the standard default, a new Beginning Check # field was added to the CM Accounts form. If a value is entered in this field, the system uses the value to default the beginning check number when printing checks (via AP Check Print or PR Check Print) for the specified CM account. Once you complete a check run, the system then updates this field based on the last check number used.
If you clear the checks (that is, you select the Clear Existing Check #s (Number can be reused.) option in the selected print form), the system clears the check numbers and sets the Beginning Check # field in CM Accounts back to the number specified before you printed the checks
Note: If you leave the Beginning Check # field blank for a CM account, the system uses the standard default procedure.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
