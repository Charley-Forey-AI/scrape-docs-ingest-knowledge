---
title: "Tracking Subcontract Compliance | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/tracking-subcontract-compliance"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/tracking-subcontract-compliance"
---

# Tracking Subcontract Compliance

You can track subcontract compliance using SL Compliance.
Compliance codes are set up in HQ Compliance Codes. You can then add them to subcontracts in SL Compliance so that you can track whether the subcontractor/supplier complies with the codes.
There are two types of compliance codes you can set up: yes/no codes or date codes. You will track compliance differently, depending on the type of code in use.

- Yes/No - When using a yes/no code for tracking compliance, you will select the Complied checkbox to indicate when the subcontractor is in compliance and use the Receive Date field to enter the date you received the compliance information.

- Date - When using a date code for tracking compliance, you will enter the compliance expiration date in the Exp Date field and use the Receive Date field to enter the date you received the compliance information. As long as the current date is equal to or less than the expiration date, the subcontractor is in compliance.

 For more information about adding compliance codes to a subcontract, see [Add Compliance Codes to a Subcontract](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/add-compliance-codes-to-a-subcontract).

## Associating Compliance Codes with Specific Invoices

If you are tracking compliance, and want to associate a compliance code to a specific invoice, enter the invoice's AP reference number in the AP Ref field. This allows you to pay future subcontract invoices that are in compliance, while blocking payment for non-compliant items by associated them with a specific AP invoice. If you do not enter an AP reference number for specific compliance codes, the system applies compliance to all invoices.

## Verifying Compliance in AP

If you are verifying compliance in AP, select the Verify checkbox for each applicable code in SL Compliance. The system reviews the codes when you run the AP Payment Preview with Compliance report or when you edit the subcontract in SL Worksheet. If one or more of the codes are not in compliance, the report displays the non-compliant subcontracts, while the SL Worksheet will display a warning in red. If you are verifying compliance for a yes/no code, the warning displays if you have not selected the Complied checkbox for the code in SL Compliance. If you are verifying compliance for a date code, the system compares the Exp Date field in SL Compliance against the invoice date for the AP transaction. If the invoice date is more recent than the expiration date, the warning displays.
Note: The way the system enforces compliance is dependent on settings in AP Company Parameters. The system may prevent payments related to non-compliant subcontracts, or it may display warnings, but allow payment to occur. For more information, see [Vendor Compliance Tracking](/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking).

Related information

- [SL Compliance Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/sl-compliance-form)

- [SL Worksheet Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)

- [HQ Compliance Codes Form](/en/vista/vista/administration/headquarters/compliance-setup/hq-compliance-codes-form)
