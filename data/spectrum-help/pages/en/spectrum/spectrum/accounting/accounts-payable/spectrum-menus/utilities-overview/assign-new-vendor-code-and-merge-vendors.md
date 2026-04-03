---
title: "Assign New Vendor Code and Merge Vendors | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/utilities-overview/assign-new-vendor-code-and-merge-vendors"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/utilities-overview/assign-new-vendor-code-and-merge-vendors"
---

# Assign New Vendor Code and Merge Vendors

In addition to changing vendor codes, you can use this window to merge two existing vendor codes (for example, if you find that by accident the same vendor code was entered into the system more than once).
To merge codes, you can enter an existing vendor code in the New vendor code field. For convenience and clarity, whenever two existing vendor codes are specified, the entry window will prompt for whether to proceed to 'Merge Vendors' or 'Keep Separate'; this is your visual key that you are merging two vendors instead of just changing their code.

- A full system backup is recommended prior to starting the update.

- This update may not include any custom files, pre-release and new files, and non-updated data files. Confirm that all updates/postings have been performed prior to using this function and review records carefully following completion of this program.

- Perform this update only when no other users are logged into the system.

## Merging Vendors

As part of the report-and-update process, when the batch includes any vendors being merged, a special 'Search for conflicts' routine will be executed to determine whether any subcontract codes or invoice numbers are the same in both vendor accounts. If a conflict is found, a Merge Vendors Exception Listing is provided, showing the duplicate codes found. You can then decide whether to proceed with the Update or Cancel.
During the Update, any time two valid vendor codes are specified, transactions for the 'Old code' will be changed to the 'New code'. All general setup information (such as name and address, user-defined field settings and locations) assigned to the 'New code' will remain the same. Warning: If duplicate transactional records are revealed in the merge, the 'Old code' settings will be removed.
All other 'Old vendor' references, other than the duplicate transactions discussed above, will be changed to the 'New code'.

## Understanding How Data is Merged

Assuming no conflicts are found, the following section explains how data will be merged and deleted.
Vendor Master File - Certain types of data merge together, while other data is deleted:

- New Code - The update will retain all records for the 'New code' (unchanged).

- Old Code - The type of data and where it is found will determine the rule.

- Main Properties, Defaults, Locations, Payment Setup, Year-End Reporting, User-Defined Fields and Vendor Notes Pages: All information from the 'Old code' will be deleted as part of the merge.

- Contacts, Document Tracking, Document Imaging and Cost Center Pages: 'Old code' information will be changed to the 'New code' provided that a record does not already exist with the exact same keys. When duplicate keys exist, the 'Old code' data will be deleted.

Subcontract Master File - As each subcontract is unique, the system will not delete records.

- New Code - The update retains all records for the 'New code' (unchanged).

- Old Code - 'Old code' records will be switched to the 'New code' except in cases where a record with the exact same keys already exists.

Transactional Data

- New Code - The update will retain all records for the 'New code' (unchanged).

- Old Code - 'Old code' records will be switched to the 'New code' except in cases where a record with the exact same keys already exists.

Vendor and Subcontract Document Imaging - The contents of the 'old folder' in the Vendor cabinet will be merged into the 'new code' folder.

- New Code - The update will retain all records for the 'New code' (unchanged).

- Old Code - 'Old code' records will be switched to the 'New code' except in cases where a record with the exact same keys already exists.

Related information

- [Change Vendor Codes](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/utilities-overview/change-vendor-codes)
