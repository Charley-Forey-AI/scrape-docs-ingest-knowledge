---
title: "Document Tracking Item Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance/document-tracking-item-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance/document-tracking-item-maintenance---field-descriptions"
---

# Document Tracking Item Maintenance - Field Descriptions

Use this table for reference when completing the fields on
 this screen.
Fields/Buttons
Descriptions

Tracking
 item code
Enter a tracking item code. For example, you might enter
 LR if you are adding a Lien Release code.

Sub-tier vendor tracking?
Select this checkbox if this item code will be subject
 to sub-tier vendor tracking; a Sub-tier? column on the main screen will display as
 'Yes'.
The software will disallow this flag to be switched once
 the code is set up. This protection is provided to assure that 'sub-tier
 vendor' tracking item codes are only used with "sub-tier" subcontract
 document tracking and that Job Compliance Tracking of sub-tier vendors is
 not compromised.
If this checkbox is selected, Action #6: Print lien release during
 check printing?, will be disabled.

Description
Enter a description for the code you just entered.

Message
 text
Enter any comments that you want to include for the
 current tracking code. Up to 250 characters are allowed.

Trigger
 basis
Select the trigger condition that you want to apply to
 the new code.
The Recurring option and interval fields are provided in
 conjunction with Job Compliance Tracking.
 This tracking item makes use of a 'Document interval' (#
 of weeks or months) between iterations, as defined in the 'Select inverval
 type' and 'Number of weeks per interval' fields. You can optionally specify
 the starting date (first document iteration) and ending date. After the
 initial iteration, the software automatically generates subsequent recurring
 entries, each with its own 'completion' flag. This functionality is also
 provided for each sub-tier vendor because different vendors may be
 responsible for a particular document (such as Certified Payroll Report) at
 different times during the progression of the job, and each sub-tier vendor
 may submit a document over a different time period.
Note:
 When the trigger basis is set to 'Every payment' the
 Document Tracking Action option to 'Display in Subcontract Kiosk' will be
 unavailable.


Action
Select the checkboxes corresponding to the actions you
 want to apply to the current code. For example, if you are adding a Lien
 Release code, you would want to select the checkbox that reads Print lien release during check
 printing option.
For each Document Tracking Action, the software
 determines whether 'open items' exist for the tracking item in context to
 the subcontract, sub-tier vendors on the subcontract, or the vendor.
If you are unsure which actions you want to select for
 this tracking item, click the Action Help button to open a window that
 explains the specifics of each action.

Action
 Help
Click this button to open the Document Tracking Actions
 window and review a list of valid action codes and descriptions of when and
 where these codes are used in Spectrum.
