---
title: "Subcontract Ledger | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger"
---

# Subcontract Ledger

The Subcontract Ledger (SL) module works with other accounting modules to monitor the progress of subcontracts.
You can create subcontracts in the SL module or create them in the PM module and interface them with the SL module using the PM Interface form.
The SL module interacts with Accounts Payable (AP) to provide the invoicing and payments to the subcontractor, and with Job Cost (JC) to track committed costs. Change orders, backcharges, and compliance tracking are also included in the processing of subcontracts in this module.

## Subcontract Numbers

Generally subcontract numbers are in one of the following formats:

- A combination of Job and Vendor numbers. For example, you might use the first six digits of the Job number and a six-digit Vendor number.

- A combination of Job and Sequence numbers.

No matter which format you use, you should be consistent.

## Auto-Generated Subcontract Numbers

When you create a subcontract in the PM module (via PM Subcontracts or PM Subcontract Detail), you can have the system automatically assign it a number (using the settings in PM Company Parameters, Subcontract Parameters tab).
Note: You can only generate subcontract numbers automatically in the PM module; manual entry is still required in the SL Subcontract Entry form. It is recommended that manually entered numbers use the same format as defined for auto-numbering in PM Company Parameters.

Manually entered subcontract numbers are validated against both SL and PM to ensure duplicate numbers are not used

## Committed Costs and Units

Subcontract costs are updated to Job Cost as committed costs for the job. The total value of a subcontract (including any change orders and backcharges) impacts the Total and Remaining Committed Costs. As invoices are posted to the subcontract through the AP module, the Remaining Committed Costs are reduced. This figure is recalculated to be the remaining dollar amount or units multiplied by the current unit cost.
Note: When you add an item to a subcontract, the system sends the tax rate amount to the committed cost fields in JC. If the tax rate amount changes, the system will not update the committed cost amounts. When relieving committed costs through AP, the system will relieve the original tax rate amount from the committed cost, but will use the current tax rate on the AP invoice

## Updating Units to Job Cost

Changes to the Total and Remaining Committed Costs always update to the JCCP (JC Cost by Period) file, but how units are updated depends on the unit of measure assigned to the job, phase, and JC cost type.If the subcontract item's unit of measure matches the JC unit of measure, the units are accumulated in JCCP. If the subcontract item's unit of measure does not match, no units update will occur. For more information, see Costs by Period.
The system makes entries to the JCCD (JC Cost Detail) file whenever changes are made to the Total and Remaining Committed Costs. Units are expressed in the unit of measure assigned to the item. For more information, see Transaction Detail.

## Add-Ons

Add-ons are used to handle additions and deductions to subcontracts that should be separated from other subcontract items, such as bonds, dues, and liquidated damages. To facilitate the use of add-ons, set up the various add-ons that your company uses in the SL Add-ons form. The type of add-on (percent or amount) determines how the add-on is calculated when entered in the SL Subcontract Entry form.

Related information

- [Types of Subcontract Items](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/types-of-subcontract-items)

- [Using the SL Worksheet](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/using-the-sl-worksheet)

- [About Subcontract Backcharges](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-backcharges)

- [About Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims)

- [Subcontract and Job Cost Files Impacted by SL Posting](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/subcontract-and-job-cost-files-impacted-by-sl-posting)

- [About Multi-Company Processing](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-multi-company-processing)
