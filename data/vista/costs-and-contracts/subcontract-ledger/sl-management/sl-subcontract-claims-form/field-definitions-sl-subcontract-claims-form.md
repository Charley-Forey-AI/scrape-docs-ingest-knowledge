---
title: "Field Definitions: SL Subcontract Claims Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form/field-definitions-sl-subcontract-claims-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form/field-definitions-sl-subcontract-claims-form"
---

# Field Definitions: SL Subcontract Claims Form

The following is a list of field descriptions for the SL
 Subcontract Claims form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## JCCo

The JCCo field on the SL Subcontract Claims form.

This field defaults the active company specified in the Company field on the main menu.
Enter the JC company by which to filter subcontracts.
 Entry in this field requires that you also enter a job in the Job field. If you do not enter a Job, the system disables job filtering and displays a ** JOB FILTERING DISABLED ** message.

## Job

The Job field on the SL Subcontract Claims form.

This field defaults the Active Job specified in the Change Active Information form (accessed from the Main Menu by selecting View > Change Active Info.)
Enter the JC company by which to filter subcontracts or press F4 to select from a list of valid jobs for the specified Job Cost company.
 Entry in this field requires that you also enter a JC company in the JCCo field. If you do not enter a JC company, the system disables job filtering and displays a ** JOB FILTERING DISABLED ** message.
Once you've entered the JCCo and Job, the system displays only subcontract claims for that company and job.

## Subcontract

The Subcontract field on the SL Subcontract Claims form.
Enter a subcontract number or press F4 to select
 one from a list. You can only select existing subcontracts that have not been closed.
 Subcontract are closed using the [SL Close
 ](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-maintenance/about-the-sl-close-form) form.
You cannot use this field to create a new
 subcontract. If you want to create a new subcontract, press F5 in this
 field. This will launch the SL Subcontract Entry batch process, which can be used to create
 new subcontracts.

## Claim No

The Claim No field on the SL Subcontract Claims form.
Enter the claim number. The claim number can be a number up to 10 digits long, and you can have several claims on a single subcontract.
You can also press F4 to select an existing claim from a list. Only claims on the selected subcontract will display in the list.
Note: When a new claim is created, the system will automatically add all of the existing subcontract items to the claim. You can see the subcontract items using the Items tab on this form.

## Notes

The Notes tab on the SL Subcontract Claims form.
Use this field to enter notes on the claim.

### Spelling Check / Add Standard Note

To spell check the text in this field, click the Spelling icon on the toolbar or
 select Tools > Spelling.
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

For additional information about subcontract claims, see [About Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims).

## Description

The Description field on the SL Subcontract Claims form, Info tab.
Enter a description of the claim. The description can be up to 60 characters long.

## Claim Date

The Claim Date field on the SL Subcontract Claims form, Info tab.
Enter the claim date. This field auto-populates with the current date when you create a new claim.

## Received Claim Date

The Received Claim Date field on the SL Subcontract Claims form, Info tab.
Enter the date the claim was received. By default, this field populates with the current date when a new claim is created.

## Claim Status

The Claim Status field on the SL Subcontract Claims form, Info tab.
Select the claim status:

- Pending - This status defaults for all claims when they are first entered. You will only change from this status when the claim is certified or denied.

- Denied - Select this status if the subcontract claim was denied.

- Certified - Select this status if the claim has been certified. For claims being sent to AP Transaction Entry, you must select this status prior to running the update to AP Transaction Entry. Otherwise, the claim will not be available for selection in the SL Claim Update to AP Trans form (accessed by selecting FileUpdate to AP Transaction Entry). For claims being sent to AP Unapproved Invoice Entry, you can only select this status once you have approved the claim via the AP unapproved invoice process.

Note: This option is disabled if the Claim Approval Required check box on the SL
 Subcontract Entry Detail form was selected when the subcontract was created. It is enabled once the claim is approved in the AP module.

## Invoice Number/Invoice Date/Invoice Description

The Invoice Number/Invoice Date/Invoice Description fields on the SL Subcontract Claims form, Info tab.
Use these fields to enter the AP invoice information. When the claim is sent to AP, the information entered in these fields will populate on the invoice.
For example the Invoice Number
 will populate in the AP Reference field on the AP Transaction
 Entry form when the claim is sent to AP.
When creating a new claim, the Invoice Date
 field will populate with the current date.

## Due Date

The Due Date field on the SL Subcontract Claims form, Info tab.
Enter the due date of the claim.
This field will default based on the invoice
 date entered on the claim (SL Subcontract Claims> Info tab> Due Date field)
 and the payment terms entered on the subcontract (SL Subcontract Entry> Info tab in the
 upper portion of the form> Pay Terms field). Payment terms are
 created and maintained using the [ HQ Payment Terms ](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form) form.
Currently this field is only supplemental information. The value in this field is not sent to the AP module or used in any standard reports.

## Certified Date

The Certified Date field on the SL Subcontract Claims form, Info tab.
Use this field to enter the date the claim was
 certified. When you certify the claim and change the Claim Status field to Certified, this
 field is enabled and it will populate with the current date.

## Approved Retention / Certified Retention

The Approved Retention / Certified Retention field on the SL Subcontract Claims form, Info tab.
The title of this field displays as Approved Retention for U.S. and Canadian companies, and as Certified Retention for Australian companies.
This field displays the calculated retention on the claim. You can also use this field to manually change the retention on the entire claim. The system redistributes the amount that you manually enter in this field to the subcontract items included on the claim. For more information, see [About Calculating and Distributing Claim Retention](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/about-calculating-and-distributing-claim-retention).
Note: Once you send a claim to Accounts Payable (AP Transaction
 Entry or AP Unapproved Invoice Entry), this field is
 disabled.

## SL Item

The SL Item field on the SL Subcontract Claims form, Items tab.
This field displays the subcontract item number.
You can also use this field to add an existing
 subcontract item to the claim. Press F4 in this field to see a list of items
 on the subcontract.
When you create a new claim in the SL Subcontract Claims form, all of the existing items on the subcontract are automatically added to the Items tab. For example, this can be done monthly or as work is completed and more needs to be invoiced. The system tracks the claim amounts on each subcontract item, regardless of which claim was billed.
Use the Items tab to delete any subcontract items that do not apply to the claim. This can only be done before the claim is sent to the AP module.
If you add a subcontract item to the subcontract after the claim has been created (for example a change order creates a new item on the subcontract), the new subcontract item will not be on the claim.
There are several ways to add the new subcontract item to a claim. You cannot add an item to a claim after it has been sent to the AP module.

- Use the Update Items button - Use the Update
 Items button on the SL Subcontract Claims form to add the new
 subcontract item to the claim. This only applies if the claim has not been sent to
 the AP module (either AP Transaction Entry or AP Unapproved Invoice Entry). Once the
 claim is sent to AP, the Items tab is disabled and you cannot add new items to the
 claim.

- Manual entry - Use the Items tab to manually add a subcontract item to a claim.

- Create a new claim - You can also have multiple claims associated with a single subcontract. This means that rather than adding the new subcontract item to an existing claim, you can also create a new claim for the new subcontract item.
To create a new claim, open the SL Subcontract Claims form and create a new claim for the subcontract. When you create the new claim, all of the existing items on the subcontract will be added to the claim.
This field is disabled once the claim has been sent
 to the AP module using the File > Update to
 AP Transaction Entry, or File > Update to
 AP Unapproved Invoice Entry.

This field is disabled once the claim
 has been sent to the AP module using the File > Update to AP Transaction Entry, or File > Update to AP Unapproved Invoice Entry.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)Claims - Overview

Related information

- [Process Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)

- [SL Subcontract Claims Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form)

## Invoice Line Description

The Invoice Line Description field on the SL Subcontract Claims form, Items tab.
When the claim is sent to the AP module, the text in this field will be used as the description of the invoice line item.
For example if the claim is sent to AP
 Transaction Entry, this field will populate in the Description field in the lower portion of
 the form.
This field is disabled once the claim has been
 sent to the AP module using the File > Update to AP
 Transaction Entry, or File > Update to AP
 Unapproved Invoice Entry.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)Claims - Overview

## % Claim to Date

The % Claim to Date field on the SL Subcontract Claims form, Items tab.
Enter the total percentage to date on the
 claim and the system will automatically populate the remaining columns on the Items tab
 with the calculated values.
If there are no previous claims on the
 subcontract item, the system will populate the Items tab columns based on the amount of the
 change entered in this field. For example if you change the value in this field from 0% to
 25%, the Claim To
 Date Amount and Claim Amount fields will populate with a
 value that is 25% of the subcontract item total.
If there are previous claims on the
 subcontract, the system will populate the Items tab columns based on the increase from the
 previous claim amount. For example if you change the value in this field from 25% to 50%,
 the Claim to Date
 Amount field will populate with a value that is 50% of the subcontract item
 total, and the Claim Amount field will populate with a value that is 25% of the
 subcontract item total.
This field is disabled once the claim has been
 sent to the AP module using the File > Update to AP
 Transaction Entry, or File > Update to AP
 Unapproved Invoice Entry.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)Claims - Overview

## Claim To Date Units

The Claim To Date Units field on the SL Subcontract Claims form, Items tab.
This field displays the % claim to date amount
 multiplied by the current units.
You can also enter the total units to date on
 the claim and the system will automatically populate the remaining columns on the Items tab
 with the calculated values.
Note: This field is only enabled on units based subcontract
 items - LS does not display in the Unit of Measure(UM) field.
If there are no previous claims on the subcontract item, the system will populate the Items tab columns based on the amount of the change entered in this field. For example if you change the value in this field from 0 to 100 units, the
 Claim To Date Amount
 field will populate with the new claim amount of 100 units multiplied by the unit cost, and the
 Claim Units
 field will display the current claim, which is 100 units.
If there have been previous claims on the subcontract item, the system will populate the Items tab columns based on the amount of the change entered in this field. For example if you change the value in this field from 100 to 500 units, the
 Claim to Date Amount
 field will populate with 500 units multiplied by the unit cost, and the
 Claim Units
 field will display 400 units (the increase of 400 units on the new claim).
Show Units/ Hide Units button
Use the Show Units / Hide Units button at the bottom of the form to display/hide this field.
This field is disabled once the claim has been
 sent to the AP module using the File > Update to AP
 Transaction Entry , or File > Update to AP
 Unapproved Invoice Entry.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)Claims - Overview

## Claim To Date Amount

The Claim To Date Amount field on the SL Subcontract Claims form, Items tab.
This field displays the calculated claim to date amount (claim to date units X current unit cost).
If you change the value in this field, the system will recalculate the other columns on the tab.
For example if you increase the value in this
 field from $4,925 to $5,000, the system will recalculate the % Claim to Date
 field, and the Claim Amount field will increase by $75. If the subcontract item is units
 based, the system will also recalculate the Claim to Date Units and Claim Units
 fields.
This field is disabled once the claim has been
 sent to the AP module using the File > Update to AP
 Transaction Entry, or File > Update to AP
 Unapproved Invoice Entry.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)Claims - Overview

## Claim Units

The Claim Units field on the SL Subcontract Claims form, Items tab.
This field displays the units associated with
 the current claim ((% Claim To Date X current units on claim) - units on previous claims).
If you change the units in this field, the
 system will recalculate the other fields on the Items tab. For example if you change the
 units in this field from 100 to 200, the system Claim to Date Units will increase to
 reflect the additional 100 units, and recalculate the % Claim to Date, Claim to Date
 Amount, and Claim Amount fields.
Show Units/ Hide Units button
Use the Show Units / Hide Units button at the bottom of the form to display/hide this field.
This field is disabled once the claim has been
 sent to the AP module using the File > Update to AP
 Transaction Entry, or File > Update to AP
 Unapproved Invoice Entry.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)Claims - Overview

## Claim Amount

The Claim Amount field on the SL Subcontract Claims form, Items tab.
Use this field to enter the amount of the current claim (claim units X current unit cost).
If you change the value in this field, the
 system will recalculate the remaining fields on the Items tab.
If the claim amount exceeded the current
 subcontract amount, the Allow Exceeded Claim Entry box on the SL
 Company Parameters form determines how validation will be applied to the form. [More](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/about-the-sl-company-parameters-form/field-definitions-sl-company-parameters-form#ID-0005c44a--en)
This field is disabled once the claim has been
 sent to the AP module using File > Update to AP
 Transaction Entry, or File > Update to AP
 Unapproved Invoice Entry.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)Claims - Overview

## Certified Amount / Approve Amount

The Certified Amount / Approve Amount field on the SL Subcontract Claims form, Items tab.
The title of this field is Certified Amount for Australian companies and Approve Amount for U.S. and Canadian companies.
Use this field to enter the certified /
 approved amount. When this claim is sent to AP, this is the invoice item amount. By default
 this field will populate with a calculated amount based on the Claim Amount
 field.
You cannot invoice a claim if there is a 0 in
 this field - for example when you select File > Update to AP
 Transaction Entry, a claim will not display in the selection form if the approved amount is
 0.
Note: If the approve amount does not equal the claim amount,
 you must enter an explanation in the Notes field on the Items tab.
This field is disabled once the claim has been
 sent to the AP module using the File > Update to AP
 Transaction Entry, or File > Update to AP
 Unapproved Invoice Entry.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)Claims - Overview

## Approved Retainage / Certified Retainage / Approved HoldBack

The Approved Retainage / Certified Retainage / Approved HoldBack field in SL Subcontract Claims, Items tab.
The title of this field differs depending on the country. For U.S. companies, the title is Approved Retainage; for Australian companies, Certified Retainage; and for Canadian companies, Approved HoldBack.
When you open this form, this field is initially hidden from the grid. You can display the field by clicking the Show Retention/HoldBack button. However, once you close the form, the field reverts back to hidden.
You can use this field to change the retention on each subcontract item on the claim.
Important: When creating a new claim, do not enter a value
 in this field until the approved retention displays in the Approved Retention /
 Certified Retention field on the Info tab of the SL Subcontract Claims
 form.
Once you enter amounts for
 subcontract items, the system automatically calculates the
 retention based on the Work Complete Retention % entered for each
 subcontract item in (SL Subcontract Entry (Info tab, Items section).
This means that you can ignore this field if the following is true:

- You entered a value in the Work Complete Retention % field in SL Subcontract Entry for all subcontract
 items that require retention;

- The retention on the claim is always based on that percentage.

For more information about retention calculation, see [About Calculating and Distributing Claim Retention](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/about-calculating-and-distributing-claim-retention) .
Click the links below for more information about subcontract claims.
[About Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims)
[Process Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)

## Certified Units / Approve Units

The Certified Units / Approve Units field on the SL Subcontract Claims form, Items tab.
The title of this field is Certified Units for Australian companies and Approve Units for U.S. and Canadian companies.
When you open this form, this field is initially hidden from the grid. You can display the field by clicking the Show Units button. However, once you close the form, the field reverts back to hidden.
Use this field to enter the certified /
 approved units. By default this field will populate with a calculated amount based on the
 Claim
 Amount field.
If you change the value in this field, the
 Certified Amount
 / Approve Amount will be recalculated based on the Certified Units / Approve
 Units. When this claim is sent to AP, the Certified Amount / Approve
 Amount is the invoice item amount.
Note: If the approve units does not equal the claim units,
 you must enter an explanation in the Notes  field on the Items tab.
This field is disabled once the claim has been
 sent to the AP module using the File > Update to AP
 Transaction Entry, or File > Update to AP
 Unapproved Invoice Entry.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)Claims - Overview

## Plus GST / Tax Amount

The Plus GST / Tax Amount field on the SL Subcontract Claims form, Items tab.
The title of this field differs depending on the country. For Australian companies, the title is Plus GST. For U.S. and Canadian companies, the title is Tax Amount.
When you open this form, this field is initially hidden from the grid. You can display the field by clicking the Show Tax button. However, once you close the form, the field reverts back to hidden.
This field displays the calculated tax amount.
The calculated amount depends on the selection
 in the Tax Basis is
 net of retainage box on the Audit Options tab of the AP Company Parameters form.

- If selected, the tax amount will be the approved amount less the
 approved retention amount.

- If not selected, the tax amount will be the approved amount. Note: This field is only enabled if there is a tax type
 and tax code associated with the subcontract item.

This field is disabled once the claim has been
 sent to the AP module using the File > Update to AP
 Transaction Entry, or File > Update to AP
 Unapproved Invoice Entry.
For more information about subcontract claims, see [About Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims).

## Notes

The Notes field on the SL Subcontract Claims form, Items tab.
This is a required field when either of the following conditions occurs:

- Approve Units does not equal
 Claim
 Units

- Approve Amount does not equal
 Claim
 Amount

Double click in this field if you have to enter a lot of text. This will open the Grid Notes form.
This field is disabled once the claim has been
 sent to the AP module using the File > Update to AP
 Transaction Entry, or File > Update to AP
 Unapproved Invoice Entry.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)Claims - Overview

## Sequence

The Sequence field on the SL Subcontract Claims form, Unapproved Change Orders tab.
Use this field to distinguish each item on the tab. This field will automatically populate with the next sequence available number when you add a new item to the tab.
You can also enter a '+' in this field and the system will automatically create a new item and assign it the next available sequence number.
Click the links below for more information about subcontract claims.
[SL Subcontract Claims Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form)
[Process Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)

## Sub Reference

The Sub Reference field on the SL Subcontract Claims form, Unapproved Change Orders tab.
Use this field to enter the subcontract reference number - for example the subcontract change order number.
Click the links below for more information about subcontract claims.
[SL Subcontract Claims Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form)
[Process Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)

## Description

The Description field on the SL Subcontract Claims form, Unapproved Change Orders tab.
Use this field to enter a description of the variation. The description can be up to 60 characters long.
Click the links below for more information about subcontract claims.
[SL Subcontract Claims Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form)
[Process Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)

## Claim Units

The Claim Units field on the SL Subcontract Claims form, Unapproved Change Orders tab.
Use this field to enter the claim units of the unapproved variation. The claim units entered in this field will not be included on the invoice when the claim is sent to the AP module.
Click the links below for more information about subcontract claims.
[SL Subcontract Claims Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form)
[Process Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)

## Claim Amount

The Claim Amount field on the SL Subcontract Claims form, Unapproved Change Orders tab.
Use this field to enter a claim amount. The claim amount entered in this field will not be included on the invoice when the claim is sent to the AP module.
Click the links below for more information about subcontract claims.
[SL Subcontract Claims Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form)
[Process Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)

## Notes

The Notes field on the SL Subcontract Claims form, Unapproved Change Orders tab.
Use this field to enter notes on the unapproved variation.
Double click on this field if you need to enter a lot of text. This will open the Grid Notes form.

### Spell Check / Add Standard Note

To spell check the text in this field, click the Spelling icon on the toolbar or
 select Tools > Spelling.
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

Click the links below for more information about subcontract claims.
[SL Subcontract Claims Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form)
[Process Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)

## Subcontract Details Section

The Subcontract Details and Claim Details sections
at the top of the Subcontract Claims form display subcontract and claim totals.

- Original Contract - This field displays the original amount on the subcontract.

- Variations - This field displays the Current Contract less the Original Contract fields.

- Current Contract - This field displays the original amount +/- any changes to the subcontract - for example subcontract change orders created in the PM module and interfaced using the PM Interface form, or any change orders created and posted using SL Change Order Entry.

- Retention Allowance- This field displays the allowable retention on the subcontract and it does not include taxes. This field is calculated based on the retention percentage set up on each subcontract item (SL Subcontract Entry> Info tab in the lower portion of the form> Work Completed Retainage % field). If maximum retention was set up on the subcontract (SL Subcontract Entry> Maximum Retention Settings tab), this field in calculated in the following way:

- Percent of
 Subcontract
 - If the maximum retention is set up to be a percentage
 of the subcontract, this field displays the current contract amount *
 maximum retention percentage (SL Subcontract EntryMaximum Retention
 Settings tab
 % of Subcontract
 field).

- Maximum Amount - If the maximum retention is set up to be a percentage of the subcontract, this field displays the maximum retention amount set up on the subcontract (SL Subcontract EntryMaximum Retention Settings tabRetention Amount field).

Note: If maximum retention is notset up on the subcontract,
 retention that has been released, or released and paid is not
 included in the Retention Allowance field.

- Retention
 Withheld - This field displays the retention on the current
 claim plus the retention on previous claims.

- Retention
 Remaining - This field displays Retention
 Allowance - Retention Withheld.

- Retention/
 Retainage Still on Hold - This field displays the
 retention/retainage withheld less the amount that has been released. For
 example if you are withholding $6,000 and release $1,000 of that $6,000,
 this field will display $5,000 as the retention that is still be withheld.
 This field does not include GST.
Claim Details section

- Previous
 Contract, Previous Claimed,
 Previous Certified/Previous Approved, Previous
 Certified Retention / Previous Approved Retention - These
 totals include all claims with a prior claim date.

- Contract
 This Claim, This Claim, Amount
 Certified / Amount Approved, Certified
 Retention/ Approved Retention - These totals include all
 subcontract items on the claim.

- To Date
 Claimed, To Date Certified / To Date
 Approved, To Date Certified Retainage / To
 Date Approved Retainage - These totals include previous
 claims and the current claim.
