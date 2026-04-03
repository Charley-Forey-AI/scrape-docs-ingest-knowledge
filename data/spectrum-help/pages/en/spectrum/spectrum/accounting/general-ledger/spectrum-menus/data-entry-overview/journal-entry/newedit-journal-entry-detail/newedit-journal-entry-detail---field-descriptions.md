---
title: "New/Edit Journal Entry Detail - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/data-entry-overview/journal-entry/newedit-journal-entry-detail/newedit-journal-entry-detail---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/data-entry-overview/journal-entry/newedit-journal-entry-detail/newedit-journal-entry-detail---field-descriptions"
---

# New/Edit Journal Entry Detail - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Journal entry # Year Period Current balance
The journal entry number, fiscal year, fiscal period number, and running balance associated with the transaction date display.

Details

G/L account
Enter a valid G/L account for this journal entry. This field disallows entry of a Not used account. The account description displays to the right of the code.

Reference
This field defaults from the previous line.

Debit Credit
Enter the debit and credit amounts for the journal entry. These fields do not accept negative values.
The Credit field disables if the Debit field has a non-zero value.

Job distribution
The distribution fields vary depending on whether the G/L account code is a Direct job cost, Direct equipment cost, or Direct work order cost.
If the G/L account code is a Direct job cost, enter the following fields:

- Job: Enter a job number. This field allows entry of a 'Completed' job and provides a warning if an 'Inactive' job is entered. The job number will default from the previous line if you enter multiple detail lines. If the job number is changed, the Phase, Cost type, and Cost center fields must be re-validated before the you can save and exit this window.

- Phase: Enter a phase number. The Phase and Cost type fields disallow entry of a 'Completed' phase, and provide a warning if an 'Inactive' phase/cost type is entered. The phase list in the master job will automatically be used to create a phase in the sub-job if it does not already exist in the sub-job list.

- Cost type: Enter a cost type such as Labor, Materials, Burden, Equipment, and so on.

Equipment distribution
If the G/L account code is a Direct equipment cost, enter the following fields:

- Equipment: Enter an equipment code. This field disallows the entry of a 'Retired' equipment code, and provides a warning if an 'Inactive' code is entered. The Equipment code will default from the previous line if you enter multiple detail lines.

- Cost category: Enter a cost category in this field. This field displays only if the Department field is set to use a department that is Direct cost = Equipment code. When adding a new part used, Spectrum will verify that the assigned G/L account is not restricted for this cost category code. If the G/L account is restricted, an error message appears and you will not be able to proceed.
Note: When the Preventive Maintenance
 installation option, Require maintenance work orders
 for all maintenance work, is selected, you cannot enter
 an equipment code directly, and must go to the Preventive
 Maintenance > Maintenance Work
 Order screen to select a piece of equipment from
 there.

Work order distribution
If the G/L account code is a Direct work order cost, enter the following fields:

- Work order: Enter a
 work order. This field will disallow entry of a work order with a
 'Completed' status or a 'Job' work order. The Work order number will
 default from the previous line if the Operator enters multiple detail
 lines. If the Work order number is changed, the rest of the
 distribution fields must be re-validated before the Operator can save
 and exit this window.Note: If the work order
 dispatch status is set to 'proposed' entry will be
 disallowed.

- Eq. work order:
 Enter an equipment work order. If a closed work order is entered, a
 warning displays, but does not prevent further data entry. This field
 displays only if the Cost category field contains a cost category that is
 set to require an equipment work order number. Entry of an equipment
 work order is optional. This setting is maintained in the Equipment Control > Cost Category Field Maintenance screen's Data entry field. Please refer to the Equipment
 Control Help file for more details.

- Site equipment:
 Enter a site equipment code. Entry of a valid equipment code will be
 required if the Work Order installation option
 Require equipment
 code for work order transactions? is selected. The Site
 equipment code defaults from the previous line if you enter multiple
 detail lines.

- Component: This
 field will only be enabled if any components are set up for the
 designated piece of equipment, or the Work Order installation > Require component
 code for work order transactions checkbox is selected. The component will default from
 the previous line if the Operator enters multiple detail lines.

- Contract: This field
 is disabled if the Service Contract module is unavailable, or no
 contract exists in the SC module for the equipment/component
 combination. If a contract is specified in the work order header, this
 contract will default if valid for the equipment/component, and you
 will be disallowed from assigning a different contract # on the work
 order. If a contract is not specified in the work order header, you
 can enter any combination of contracts or a blank contract in the work
 order detail. If the Work Order installation
 option for Require
 equipment code for work order transactions? is not
 selected, you can enter a valid contract # without assigning an
 equipment code. The contract will default from the previous line if
 you enter multiple detail lines and no contract is specified in the
 work order header.

- Sell price: This
 field is optional. The Sell price defaults to the Debit amount (cost)
 for Time + Material work orders, and defaults to 0.0 for Flat rate
 work orders, but you may override the price.
