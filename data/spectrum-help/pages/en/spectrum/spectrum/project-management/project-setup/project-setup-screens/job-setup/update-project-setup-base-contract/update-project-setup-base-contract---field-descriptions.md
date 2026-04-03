---
title: "Update Project Setup (Base Contract) - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/update-project-setup-base-contract/update-project-setup-base-contract---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/update-project-setup-base-contract/update-project-setup-base-contract---field-descriptions"
---

# Update Project Setup (Base Contract) - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Job
The job number entered in the
 Select Estimate for Update window. If the job has
 already been updated to Job Cost, a warning message displays.
Selections

Set up subcontracts in Accounts Payable?
Select this checkbox to set up
 subcontracts in Accounts Payable > Subcontracts. If more than one item in the Subcontract
 Setup has the same phase code, billing code, and vendor, the
 items will be summed when creating the subcontract. If the two items have
 different units of measure, a message will appear during the update prompting
 the user whether to convert the unit of measure to LS (lump sum).
Set up contract in Accounts Receivable?
Select this checkbox to set up a
 contract for this job in Accounts Receivable > Contracts. If this checkbox is left clear, the cursor will advance to the
 Quantity cost type to
 create field.
Set up billing detail in Accounts Receivable?
Select this checkbox to set up billing
 detail in Accounts Receivable > Contracts. For unit price jobs, if more than one item exists in the
 Billing Detail file for the same billing item, the items will be summed. If the
 unit of measure is different for these items, a message will appear during the
 update prompting whether to convert the unit of measure to LS (lump sum).
Set up job and phase estimates?
Select this checkbox in order to set
 up the Schedule of Value at a point in time after the phase estimates have been
 updated. This only applies to the Base Update (not [Change Request Setup Update](/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/change-request-setup-update)).
 If this checkbox is clear, the next two checkboxes are disabled.
Set projected costs, quantity, and hours to current estimate?
Select this checkbox to automatically
 set the projected costs, projected quantity, and projected hours when phases
 are transferred to Job Cost. Based on the Set projected costs, quantity and hours
 to current estimate when adding a phase? checkbox in the
 Job Cost Installation screen, the system will set
 projected costs, quantities, and hours equal to the current estimates as the
 phase is updated.
Include phases with no estimated cost, hours or quantity?
Select this checkbox to add all
 phases, regardless of cost, hour, or quantity value. Project Setup will only
 create phases that have a non-zero dollar value on them.
Customer
Enter the customer code for the
 Accounts Receivable contract. Entry in this field is required. Once a customer
 code has been entered, the customer name displays.
Tax code
Enter the tax code to be used for the
 Accounts Receivable contract; up to 15 characters are allowed. Once a tax code
 has been entered, the description displays. A lookup window is available for
 viewing valid sales tax codes.
Taxable
From the drop-down list select
 Yes if this is a
 taxable contract, No
 if it is not, or No
 Default if the customer's invoices are conditionally taxable and
 the decision needs to be made on an invoice-by-invoice basis.
Quantity cost type to create
Enter a valid cost type to which
 quantities should be assigned. If no cost type is desired for this quantity,
 this field can be left blank. If the cost type entered in this field does not
 exist in the Project Setup phase setup file, Spectrum will automatically create
 the cost type.
