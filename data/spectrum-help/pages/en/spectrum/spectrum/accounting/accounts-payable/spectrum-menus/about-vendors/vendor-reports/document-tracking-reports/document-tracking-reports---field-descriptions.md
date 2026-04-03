---
title: "Document Tracking Reports - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-reports/document-tracking-reports/document-tracking-reports---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-reports/document-tracking-reports/document-tracking-reports---field-descriptions"
---

# Document Tracking Reports - Field Descriptions

Use this table for reference when completing the fields on this screen.
FieldsDescriptions
Selections This icon in Spectrum indicates you can select more than one value.

VendorWhen the report is accessed from the Vendor Info Bar, this field defaults to the current vendor.
JobIf you don't want all jobs included, select one or more.
Subcontract #If you don't want all subcontracts included, select one or more.
Actions - Enter an action code. To review action types, select the dropdown arrow.
Actions include 'Open' Recurring items, but if the Final renewal flag is selected for an item in the [Subcontract Document Tracking](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/utilities-overview/purge-unposted-vendor-invoices/subcontract-document-tracking) screen, items will NOT be considered 'open' unless the expiration date is <blank>.

1 Print on tracking item exception reportWhen this report is printed.
If sub-tier vendor item tracking is being used, these reports will include exception items triggered by Action #1 and the sub-tier items will be listed under the associated subcontract.
Additional lines will appear on the report for recurring tracking items for Vendors, Subcontracts, and Sub-Tier Vendors, excluding Subcontracts that are flagged for 'Final renewal'.

2 Warning messageDuring Vendor Invoice Entry, Manual Check Entry, Manual Credit Card Payment Entry, Subcontract Billing Entry, Subcontract Change Order Entry, and Change Request Subcontract Pricing Entry.
If sub-tier vendor item tracking is being used, warnings for the sub-tier vendors will display for the associated subcontract.
Open Recurring items flagged for a warning will include a hyperlink that opens the Job Compliance Tracking page.

3 Put new invoices on hold statusDuring Invoice Entry and Subcontract Billing Entry.
Items may be set to 'on hold' if even one recurring date triggers this action for the vendor, subcontract or any associated sub-tier vendor.

4 Don't allow checks to be selectedDuring Check Selection and Manual Check Entry.
Payment will be disallowed even if one recurring date triggers this action for the vendor, subcontract or any associated sub-tier vendor.

5 Print on check distribution action reportDuring regular check printing.
Additional lines will appear on the report for each recurring iteration of the tracking item that is currently open for Vendors, Subcontracts, and Sub-Tier Vendors.

6 Print lien releaseDuring regular check printing and with Lien Release Form.
7 Display in Subcontract KioskWhen the My Subcontract Manager screen is opened it will display alerts for "warnings" (triggered by action #7) for recurring Yes/No documents.
Select exception report?
Use this checkbox to print a document tracking report by exception. The exception report is the default report if no Saved Selection is present.

Expiration dateEnter the expiration date.
Include items triggered by expiration date?Select to include any items with a date trigger.
Include items triggered by completion status?Select to include any items with a completion status trigger.
Include items triggered with every payment?Select to include any items with an every payment trigger.
Completion statusChoose which document types to include on the report.
Subcontract statusChoose one or more subcontract statuses to include on the report.
Select distribution report?
Select to print a document tracking report by check distribution; additional trigger selections and completion status options are enabled to allow you to further customize your report results.

Check dateEnter the check date or press Enter to select the default of the current Accounts Payable processing date.
Include items triggered by expiration date?Select to include any items with a date trigger.
Include items triggered by completion status?Select to include any items with a completion status trigger.
Include items triggered with every payment? Select to include any items with an every payment trigger.
