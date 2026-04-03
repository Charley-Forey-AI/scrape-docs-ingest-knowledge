---
title: "Subcontract Document Tracking - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/utilities-overview/purge-unposted-vendor-invoices/subcontract-document-tracking/subcontract-document-tracking---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/utilities-overview/purge-unposted-vendor-invoices/subcontract-document-tracking/subcontract-document-tracking---field-descriptions"
---

# Subcontract Document Tracking - Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Tracking item
The tracking item code, description, and related message text assigned to the selected tracking item in [Document Tracking Item Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance) display.

Trigger basis
Select the trigger basis that you want to use for this tracking item.Your selection will determine if additional fields need to be completed, and only those fields that pertain to the trigger basis will display. For example, if you set a tracking item up as 'Recurring', you will then see an 'Interval type' field and a 'Number of weeks or months per interval' field.
Note: When the trigger basis is set to 'Every payment' the Document Tracking Action option to 'Display in Subcontract Kiosk' will be unavailable.

Sub-tier?
Sub-tier vendor compliance,
Open items
This column lets you know if an item was designated as a sub-tier vendor item when originally set up in [Document Tracking Item Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance).
When editing a sub-tier tracking item, a Sub-tier vendor compliance hyperlink is available to launch the Job Compliance Tracking screen, and the number of open items displays.
The open item count is the number of sub-tier vendors for this subcontract who have not closed this tracking code.
When a sub-tier row is selected, the image pane is unavailable. This is because all sub-tier documents are tracked at the sub-tier vendor level, through Job Compliance Tracking.

Expiration date
The Expiration date is used in conjunction with the date trigger. The date trigger will not do anything until the Expiration date has passed. This is most often used for Insurance Certificates--if the date passes and you don't have a new certificate, you can set the software to stop all payments to the subcontractor.
Document tracking items with a blank expiration date will be considered 'Open'.
This field does NOT display if the selected item is a sub-tier vendor item.

Final renewal?
This checkbox displays for recurring items with an 'Expiration date' to allow the Subcontract Administrator to indicate the final renewal document. For example, an annual Business License for the job location once the particular vendor is no longer at the ongoing job site. Recurring items will automatically renew unless this checkbox is selected.

Action completed?
This checkbox is used to track whether or not someone has done something. For example, "have we run a credit check on this sub?" After you have completed this action, it gets noted and you can move forward.
This field does NOT display if the selected item is a sub-tier vendor item.

Comment
Enter any comments that you want to include for the current tracking code.

Entry operator
Entry date
The current operator and system date display in these fields.

Actions
Select the checkboxes corresponding to the action you want to apply to the current code. For example, if you are adding a Lien Release code, you would want to select the checkbox that reads Print lien release during check printing option.
Note: Settings for these checkboxes default from the Item Tracking Code setup.
Action #6 - Print lien release during check printing--is not available unless the trigger basis is set to 'Every payment'.
If you are unsure which actions you want to select for this tracking item,
 click the Action Help button to open a window that explains the specifics of
 each action.

Buttons

Vendors
Click this button to go to the [Vendor Document Tracking](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-document-tracking) screen.

Items
Click this button to go to the [Document Tracking Item Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance) screen.

Lien Details
This button displays "Yes" when a lien entry is present. Click this button to open the Lien Release Details window and view the lien trade/service and legal description.

Build Items
Click this button to display the Search Tracked Vendors/Subcontracts window, select a vendor or subcontract, and when the Build Tracking Items for Subcontract prompt displays, click OK to copy the items from that vendor or subcontract (including those pertaining to sub-tier vendors).

Action Help
Click this button to open a window that explains the specifics of each action.

Job Compliance
If Job Compliance Tracking is being used, select an item code and click the 'Job compliance' hyperlink to launch a new tab displaying the related details.
