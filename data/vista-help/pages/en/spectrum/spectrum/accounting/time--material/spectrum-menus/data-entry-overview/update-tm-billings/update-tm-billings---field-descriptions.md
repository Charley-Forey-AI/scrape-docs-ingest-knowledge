---
title: "Update T+M Billings - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/update-tm-billings/update-tm-billings---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/update-tm-billings/update-tm-billings---field-descriptions"
---

# Update T+M Billings - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Build List of Billings to Update

Job A/R invoice batch
The Build List of Billings to
 Update window displays first. Enter the job number and the
 batch code identifying the Accounts Receivable invoice to be reversed. After
 clicking OK, the
 list builds, and the Update T+M Billings to Invoice
 Entry screen displays all selected billings in progress.

Grid

Job Job name
The job code and name display. Spectrum sorts first by Job, then by Billing #.

Customer Customer name
The Customer code and name display. If no customer has been assigned, you will
 need to assign a customer to the job in Job Cost > Job Main Properties. For further information, click the Help link from that
 screen in Spectrum.

Billing #
The billing number displays. If the billing number exceeds 999, the billing number will automatically be converted to the alpha equivalent (Example: A00 = 1000).

Billing total
If the billing method = A/R invoice, the billing total including add-ons, fees, and sales tax displays.
If the billing method = Change request, the billing total will be calculated before sales tax and VAT.

Invoice date
The Invoice date currently stored for this billing displays. Click the arrow
 to select a date from the Date Change window. This
 date must be within the Time + Material minimum and maximum Processing
 dates.
If the Invoice date must be in
 G/L period checkbox is selected in the Accounts
 Receivable Installation screen, any date within the T+M
 minimum/maximum date range can be entered, but the G/L date must be in the
 same fiscal period as the date.
If the billing method = Change request, this field will be skipped.

G/L date
The General Ledger date currently stored for this billing displays. Click the arrow to select a date from the Date Change window. This date must be within the Time + Material minimum and maximum processing dates.
If the Invoice date must be in
 G/L period checkbox is selected in the Accounts
 Receivable Installation screen, any date within the T+M
 minimum/maximum date range can be entered, but the G/L date must be in the
 same fiscal period as the Invoice date. If you enter an Invoice date in a different
 period, Spectrum requires this field to be changed to that period as
 well.
If the billing method = Change request, this field will be skipped.

Update?
Select this box to select the line and update the billing to Accounts Receivable.
You cannot select this checkbox if:

- There is no primary customer designated in Job Main Properties.

- A customer is assigned, but there is no corresponding A/R contract.

- Either the Invoice or G/L date are outside the allowed range.

Contract #
The corresponding contract number displays.

Price type
The corresponding price type displays:

- Time + Material

- Cost-plus

- Unit price

- Fixed price

Change request
If the billing method from the T+M Job Billing Setup
 screen is 'Change request', enter a change request # in this field to add a
 detail row with a blank billing item on the Billing
 tab. Change requests with a status of 'Executed', 'Approved', or 'Reverse'
 will be disallowed.
The change request cannot be changed if it has been attached to a change order, change request has been transferred to a draw request, or is non-cost reimbursable.
If the billing method = A/R invoice or no billing method is stored, this field will be skipped.

Billing method
The billing method from the T+M Job Billing Setup
 screen displays in this field. If no billing method is stored, 'A/R invoice'
 will display by default.
