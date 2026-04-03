---
title: "Vendor Document Tracking - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-document-tracking/vendor-document-tracking---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-document-tracking/vendor-document-tracking---field-descriptions"
---

# Vendor Document Tracking - Field Descriptions

The table below is provided as a reference when completing the New Vendor Document Tracking Item window; note that some fields may be unavailable depending on your setup.
Fields/Buttons
Descriptions

Tracking item
The tracking item code, description, and related message text assigned to the selected tracking item in [Document Tracking Item Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance) display.

Trigger basis
Select the trigger basis that you want to use for this tracking item. Your selection will determine if additional fields need to be completed, and only those fields that pertain to the trigger basis will display. For example, if you set a tracking item up as 'Recurring', you will then see an 'Interval type' field and a 'Number of weeks or months per interval' field.
Note: When the trigger basis is set to 'Every payment' the Document Tracking Action option to 'Display in Subcontract Kiosk' will be unavailable.

Expiration date
The Expiration date is used in conjunction with the date trigger; the date trigger will not do anything until the Expiration date has passed. This is most often used for Insurance Certificates; if the date passes and you don't have a new certificate, you can set the software to stop all payments to the vendor.
Document tracking items with a blank expiration date will be considered 'Open'.

Action completed?
This checkbox is used to track whether someone has done something. An example is "have we run a credit check on this sub?" After you have completed this action, it gets noted and you can move forward.

Comment
Enter any comments that you want to include for the current tracking code.

Entry operator Entry date
The current operator and system date display in these fields.

Actions
Select the checkboxes corresponding to the action you want to apply to the current code. For example, if you are adding a Lien Release code, you would want to select the checkbox that reads Print lien release during check printing option.
Action #6 - Print lien release during check printing--is not available unless the trigger basis is set to 'Every payment'.
If you are unsure which actions you want to select for this tracking item,
 click the Action Help button to open a window that explains the specifics of
 each action.

Buttons

Subs
Click this button to go to the [Subcontract Document Tracking](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/utilities-overview/purge-unposted-vendor-invoices/subcontract-document-tracking) screen.

Items
Click this button to go to the [Document Tracking Item Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance) screen.

Job Compliance
If Job Compliance Tracking is being used, select an item code and click the 'Job compliance' hyperlink to launch a new tab displaying the related details.

Action Help
If you are unsure which actions you want to select for this tracking item, click the Action Help button to open a window that explains the specifics of each action.
