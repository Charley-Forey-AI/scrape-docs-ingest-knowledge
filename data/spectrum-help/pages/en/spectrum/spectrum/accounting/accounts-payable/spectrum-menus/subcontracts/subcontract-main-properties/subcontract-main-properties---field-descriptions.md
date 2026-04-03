---
title: "Subcontract Main Properties - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-main-properties/subcontract-main-properties---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-main-properties/subcontract-main-properties---field-descriptions"
---

# Subcontract Main Properties - Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields/ButtonsDescriptions
 Header fields
 Vendor The vendor code entered must already be set up in the vendor file. The vendor's full name will display.
When adding a new subcontract, if Vendor Document Tracking is enabled for the selected vendor, any warning triggers will display in the action window.

 Subcontract # It is recommended that the job number be used as the subcontract number for most vendors.Important: If your instance of Spectrum is integrated with another application (ProjectSight, for example) you may find it necessary to use a different numbering convention that doesn't conflict with the requirements of that application.If you need further guidance, consult your implementation team.

 Job classification
 Job # The job number entered must already be set up in Job Cost > Job File Maintenance.
 Phase The system will use the phase code entered here as the default in A/P Vendor Invoice Entry and Change Order Entry.Note: Data entry is prevented if the phase status is set to Complete, and a warning displays if the status is set to Inactive.
 Cost Center Information If cost centers are being used, Spectrum verifies the operator has authorization for the phase-specific cost center, if any. Spectrum compares the cost center specified in the phase file with cost centers in the operator's assigned cost center scheme, and if the cost center is not present, then that phase may not be edited.

 Cost type The system will use the cost type entered here as the default during invoice entry and change order entry. The default cost type entered here must be a valid cost type for the default phase. A search window is available for viewing valid cost types.
 Contract details
 Contract type Enter the type of contract used for this subcontractor's work. For example, electrical, plumbing, roof, and more. This contract type will print on the Subcontract File Listing. (This may be different than the contract type set up with the customer in Job File Maintenance).
 Insurance Use the drop-down menu to select the appropriate vendor insurance certificate option. If No is selected, a warning will be triggered in Vendor Invoice Entry.
 Date sent Enter the date the subcontract was sent, or double-click to select a date from the Date Change window. This date is used in conjunction with the [Subcontract Change Order Log](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-financial-summary/subcontract-change-order-log).
 Date issued Enter the date the subcontract was issued.
 Contact Use this field to enter a contact associated with the subcontract.
 Unit price contract? Select this checkbox if this subcontract should use unit pricing. [Subcontract Phase Details - Unit Price](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-phase-details---unit-price)
 Comment Comments entered here are printed on the [Subcontract File Listing](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-reports/subcontract-file-listing).
Subcontract contacts - displays one row for every contact set up for the current vendor code
Add
Edit
These buttons allow you to Add/Edit contacts if you have permission for New/Edit Subcontract even if you do not have security for New/Edit Vendor.
The Add Contact button opens the Search Contacts window where you can search/select a contact from the list or add a "New" contact within the window. If an existing contact is selected, it is automatically associated with the Vendor and the Job.

Assign to JobSelect a row that is not currently showing a "Yes" in the Assigned to job column, and then click Save to commit the contact to the job. Conversely, you can unassign a contact from a job by selecting a row that is currently showing "Yes" and clicking this button.
StatusSelect the status type that you want to assign to the current subcontract. The status for the newly-entered subcontracts defaults as Active.

- Active - invoice entry is allowed.

- Inactive - a warning message displays during invoice entry.

- Complete - a warning message displays and the application prevents entering invoices for this subcontract.

Logon?The Logon? column indicates whether the contact has a Spectrum logon (and if present, whether it is Active or Inactive). Spectrum logons are required for non-Spectrum users to access the Subcontract Kiosk.
