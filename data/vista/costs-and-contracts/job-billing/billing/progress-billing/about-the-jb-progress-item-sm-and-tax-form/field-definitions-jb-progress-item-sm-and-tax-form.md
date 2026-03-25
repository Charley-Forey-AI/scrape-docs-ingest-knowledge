---
title: "Field Definitions: JB Progress Item SM and Tax Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-progress-item-sm-and-tax-form/field-definitions-jb-progress-item-sm-and-tax-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-progress-item-sm-and-tax-form/field-definitions-jb-progress-item-sm-and-tax-form"
---

# Field Definitions: JB Progress Item SM and Tax Form

The following is a list of field descriptions for the JB
 Progress Item SM and Tax form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Item

 Display only, all items on the contract initialized to this billing.

##  Previous SM

 This field defaults the previous stored materials total for the specified contract item. You may only override this value if the Allow Changes to Previous and Contract Amounts box is checked in JB Company Parameters.
Note: If you are using the 'auto update previous billed amounts on future bills' feature (JB Company Parameters), it is strongly suggested that you do not change this value. Changing this value may cause inaccuracies when previous amounts are updated for future billings.

##  Purchased

 Enter the total dollar value of materials purchased for this billing cycle. The amount entered here increases the Net Invoice SM field (the sum of purchased materials minus the installed materials).

##  Installed

 Enter the total dollar value of materials that have been installed during this billing cycle. The amount entered here decreases the Net Invoice SM field (the sum of purchased materials minus the installed materials).
Note: Make sure that progress has been posted to each item on this invoice for which installed material values have been entered.

##  SM Retainage %

 Enter the percentage to use for calculating stored materials retainage on this invoice. Initially defaults the retainage specified for the contract item in JC Contract Items.
Note: If you enter retainage for stored materials at the contract level (JB Progress Bill Retg Totals), any amount entered here is overridden, and will need to be re-entered.

##  SM Retg This Inv

 Defaults an amount based on total stored materials this invoice and the retainage percent entered for this item. This value may be overridden.
Note: If you enter retainage for stored materials at the contract level (via JB Progress Bill Retg Totals), any amount entered here is overridden, and will need to be re-entered.

##  Tax Code

 Enter the tax code to use for calculating taxes for this item. Initially defaults the tax code assigned to the contract item in JC Contract Items.
Note: If you post intercompany invoices (e.g., the AR company in JC Company Parameters differs from the JC/JB company), and tax is applied to an invoice (billing), the tax liability remains with the AR company. For example, if JB Co #1 posts an invoice of $1050 (includes $50 tax), AR Co #2 receives a debit of $1050 to its Receivables account, a credit of $50 to its Sales Tax Payable account, and a credit of $1000 to its Intercompany Payables account. JB Co #1 receives a debit of $1000 to its Intercompany Receivables account and a credit of $1000 to its Contract Revenue account.

##  Tax Basis

 Enter the amount on which taxes will be calculated for this item. Initially defaults as follows:

- If you do not track retainage tax separately (the Distribute Tax to Retainage box is unchecked in AR Company Parameters), defaults the total billing amount for this item (work complete plus stored materials).

 Work Complete + Stored Materials = Tax Basis

- If you track retainage tax separately (the Distribute Tax to Retainage box is checked in AR Company Parameters), this amount will exclude retainage amounts for work complete or store materials.

 (Work Complete + Stored Materials) – (WC Retg + SM Retg) = Tax Basis
Intercompany Invoices
 If you post intercompany invoices (e.g., the AR company in JC Company Parameters differs from the JC/JB company), and tax is applied to an invoice (billing), the tax liability remains with the AR company. For example, if JB Co #1 posts an invoice of $1050 (includes $50 tax), AR Co #2 receives a debit of $1050 to its Receivables account, a credit of $50 to its Sales Tax Payable account, and a credit of $1000 to its Intercompany Payables account. JB Co #1 receives a debit of $1000 to its Intercompany Receivables account and a credit of $1000 to its Contract Revenue account.

##  Tax Amount

 This field defaults the tax amount for this item based on the tax basis and the specified tax code. You may override this value if necessary, but be aware that the tax basis and rate will not be updated to reflect the change.
Note: If you post intercompany invoices (e.g., the AR company in JC Company Parameters differs from the JC/JB company), and tax is applied to an invoice (billing), the tax liability remains with the AR company. For example, if JB Co #1 posts an invoice of $1050 (includes $50 tax), AR Co #2 receives a debit of $1050 to its Receivables account, a credit of $50 to its Sales Tax Payable account, and a credit of $1000 to its Intercompany Payables account. JB Co #1 receives a debit of $1000 to its Intercompany Receivables account and a credit of $1000 to its Contract Revenue account.

##  Total Retainage

 This field displays only when you are tracking retainage tax separately (i.e., Distribute Tax to Retainage box is checked in AR Company Parameters).
 Display only, the total retainage (work complete and stored materials) for the billing item. Since you are calculating/tracking retainage tax separately, this amount is excluded from the item’s tax basis.

## Retainage Tax

Enter the retainage tax amount. Initially defaults the calculated retainage tax for the billing item ([work complete retainage + stored materials retainage] x tax rate).
NOTE: For countries tracking Provincial Sales Tax (PST) and/or Goods & Services Tax (GST), such as Canada and Australia, retainage tax amounts will be broken out and updated to the appropriate GST/PST retainage tax payable accounts (as defined in HQ Tax Codes). The PST and GST amounts (included in tax basis) will be updated to the appropriate tax payable accounts.
ADD’L NOTE: If you are not tracking retainage tax separately (i.e. the Distribute Tax to Retainage option is unchecked in AR Company Parameters), both work complete and stored materials retainage will be included in the tax basis. However, the system will break out the amounts and update the appropriate GST/PST tax payable accounts.

##  Previous WC Retainage

 This field defaults the previous work complete retainage total for this contract item. You may only override this value if the Allow Changes to Previous and Contract Amounts box is checked in JB Company Parameters.
Note: If you are using the 'auto update previous billed amounts on future bills' feature (JB Company Parameters), it is strongly suggested that you do NOT change this value. Changing this value may cause inaccuracies when previous amounts are updated for future billings.

##  Previous SM Retainage

 This field defaults the total of previous stored materials retainage for this contract item. You may only override this value if the Allow Changes to Previous and Contract Amounts box is checked in JB Company Parameters.
Note: If you are using the 'auto update previous billed amounts on future bills' feature (JB Company Parameters), it is strongly suggested that you do NOT change this value. Changing this value may cause inaccuracies when previous amounts are updated for future billings.

##  Previous Released Retainage

 This field defaults the total of previously released retainage for the contract item. You may only override this value if the Allow Changes to Previous and Contract Amounts box is checked in JB Company Parameters.
Note: If you are using the 'auto update previous billed amounts on future bills' feature (JB Company Parameters), it is strongly suggested that you do NOT change this value. Changing this value may cause inaccuracies when previous amounts are updated for future billings.

## Contract Item Notes

Use this field to enter any miscellaneous notes about this contract item. The space allowance is virtually unlimited.

- Notes entered here apply only to this contract item; they do not
 apply to the bill item to which this contract item is associated. Notes intended for the
 progress bill item should be entered on the Items tab.

-  Notes entered for this contract item in JC Contract Items or PM
 Contract Items will update this field; likewise, notes entered for a contract item here
 will be updated for the contract item in JC Contract Item and PM Contract Items. Add a Standard Note
Standard notes allow you to insert
 frequently used text into some fields in the application. This text is created and
 maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the
 field, right click the mouse while focus is in the field and select Standard
 Notes from the shortcut menu, which opens the Standard Note Copy
 window. Then enter the standard note to copy (or select from F4 lookup) and click
 OK. The system inserts the selected note into the field.
Spelling Check
 Click the Spelling icon on the toolbar
 or select Tools > Spelling
  to spell check the text in this field.
