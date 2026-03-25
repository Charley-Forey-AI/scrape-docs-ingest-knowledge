---
title: "SL Subcontract Claims Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form"
---

# SL Subcontract Claims Form

Use this form to enter, track, and certify subcontractor claims.
Claim amounts are entered on subcontract items and then sent to the AP module (AP Transaction Entry or AP Unapproved Invoice Entry).
The The JCCo and Job fields allow you to filter the subcontract claims displayed to only those applicable to the specified company and job. The system automatically defaults the active JCCo and Job (based on settings defined via the Main Menu), but you may override the defaults as needed. If you clear one or both of the fields, job filtering is disabled and a ** JOB FILTERING DISABLED ** message displays to the right of the Job field.
 Once you enter or select a subcontract and claim number, the informational section (accessed by selecting the down arrow below the claim number) shows information about the subcontract and claim, including original and current contract amounts, retainage withheld, previous claimed amounts, approved retention, and claim amounts.
If the subcontract is out of compliance (indicated by the red "Out of Compliance" message displayed to the right of the Subcontract number), you can review the assigned compliance codes and update their status as needed by selecting the SL Compliance button (which opens the SL Compliance Detail form). For more information, see [SL Compliance Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/sl-compliance-form).
The Invoice Details and Payment Details sections of the form show display-only information about the subcontract claim invoice and invoice/retainage payments (respectively).

## Items

Use the Items tab to enter the claim amounts on the subcontract items. When a new claim is created, the system automatically populates all of the existing subcontract items on this tab.
If you add items to a subcontract after you have create a claim, you can add those items to the claim by selecting the Update Items button. When selected, the system auto-adds all new subcontract items to the claim. However, this only applies if you have not sent the subcontract claim to Accounts Payable.
The fields on the Items tab are locked if either of the following is true:

- The claim has already been sent to the AP module (AP Transaction Entry or AP Unapproved Invoice Entry). If you need to change a claim that has been sent to the AP module, you need to delete the generated invoice in the AP module. This will enable the fields on the Items tab on the SL Subcontract Claims form.

- The Certified option in the Claim Status field on the Info tab of the SL Subcontract Claims form has been selected.

The Show Units, Show Totals, Show Retainage, and Show Tax buttons (bottom of form) allow you display/hide specific fields on the Items tab. Once you select a "show" button, additional fields display on the Items tab related to the button you selected (for example, Show Units will display additional "units" fields). It addition, the "show" button changes to a "hide" button, so that you can hide the additional fields if needed.

## Distribute Item Retainage

The Distribute Item Retainage button (labeled Distribute Item Retention for Australian companies and Distribute Item Holdback for Canadian companies) allows you to calculate and distribute item retention for a subcontract claim.
 When you select this button, the system calculates and distributes item retention based on the Work Completed Retainage % specified (in SL Subcontract Entry) for each subcontract item included on the claim. You can view the retention distribution by selecting the Show Retainage button.
If Item level retention has caused the 'Max Retention Limit has been exceeded' message (shown in red) to appear, selecting the Distribute Item Retainage button recalculates retention for each subcontract item based on the subcontract's Approved Retention amount and clears the message.
Note: If you set the maximum retention level for a subcontract to 0% or 0$ (in SL Subcontract Entry, Maximum Retention Settings/PBA tab), and Item level retention has caused the 'Max Retention Limit has been exceeded' message (shown in red) to appear, selecting the Distribute Item Retainage button clears the message and sets the retainage amount to 0.00 for each subcontract item.

For more information about distributing item retainage, see [About Calculating and Distributing Claim Retention](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/about-calculating-and-distributing-claim-retention).

## Unapproved Change Orders

Use this tab to manually add an unapproved item to the claim, for example a subcontract change order (SCO) that was created in the PM module and has not been interfaced with the SL module.
You can enter a claim amount but not an approved amount, which means any amounts entered on this tab will not generate invoice items when the claim is sent to the AP module.

Related information

- [Send a claim to AP Transaction Entry](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/send-a-claim-to-ap-transaction-entry)

- [Send a claim to AP Unapproved Invoice Entry](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/send-a-claim-to-ap-unapproved-invoice-entry)

- [Approved Retention / Certified Retention](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form/field-definitions-sl-subcontract-claims-form#ID-0003ed69--en)

- [Process Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)
