---
title: "Field Definitions: SL Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/about-the-sl-company-parameters-form/field-definitions-sl-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/about-the-sl-company-parameters-form/field-definitions-sl-company-parameters-form"
---

# Field Definitions: SL Company Parameters Form

The following is a list of field descriptions for the SL
 Company Parameters form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## SL Company

Enter a valid company number. This company must be set up in HQ Company Setup before it can be set up here.

## Audit Options

The audit options determine when new records of changes are added to the HQ Master Audit (HQMA) database table. For example, if you change a setting on the company parameters form, the system creates a new record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. See [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more information about viewing audit records in the HQMA table.
The following lists and describes the audit options.

- Company Parameters – This audit option is display only, and is always checked. Any changes made to the SL Company Parameters form are tracked in the Master Audit file.

- SL Entry/Change Orders – SL Subcontract Entry (header and items), SL Change Order Entry

Note: Audit records are not written to HQMA for subcontracts/SL change orders purged via SL Purge.

- SL Compliance – Select this box to record additions, deletions, and changes made to compliance codes using the SL Compliance form, as well as compliance codes initialized to a subcontract based on the job’s default compliance group, or added/deleted via AP Vendor Compliance.

Note: Audit records will not be generated for compliance code changes due to purging subcontracts.
Note: When setting up a company, the entry of invalid data in certain fields causes a warning; however, entries are allowed and the record can be saved. This primarily applies to (but it not limited to) required data such as the “interface to” companies and journals, since it is sometimes necessary to set up the company information before setting up the data being requested.

## Enforce Catch Up

The selection in this box only applies to the
 claims process.
Check this box if you want the system to
 calculate the approved retention defaults on claims using an alternative method when
 creating claims in the [SL
 Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form) form.
When this box is checked, the system will
 calculate retention based on the average retention rate on all of the subcontract items on
 the claim. The system will then apply this average rate to the total current claim amount
 to determine the retention amount, which it will then assign to each subcontract item
 included on the claim.
This can have an affect on the following:

- The default approved retention
 calculated on the entire claim (SL Subcontract Claims> Info tab> Approved
 Retention field)

- The default approved retention assigned
 to each subcontract item included on the claim (SL Subcontract Claims> Items
 tab> Approved Retention field)

The calculated retention percentage is an
 average, not a weighted average.
Click [here](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims) for
 an overview on the claims process. For more information on claim retention calculations,
 see [About Claim Retention Calculations](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/about-the-sl-company-parameters-form/field-definitions-sl-company-parameters-form#ID-0003e71d--en).

### About Claim Retention Calculations

Each subcontract item on the claim is given equal
 weight, regardless of the total subcontract item amount, or the amount of the current
 claim. See the diagram below for an example.

WC Retention % on Item
Total Subcontract Item Amount
Current Claim
Approved Amount

Item #1
10%
$100,000
$15,000

Item #2
5%
$1,500,00
$375,000

Calculated Retention %
7.5%

Example #1 - Multiple subcontract items with
 different retention percentages
If there are several items on the claim with different retention percentages and the approved amount on those claim items is different, the average calculated retention percentage will be applied to the entire claim amount and then assigned to each subcontract item on the claim.
In the diagram below, the system calculates retention by applying the 7.5% to the entire claim amount ($390,000), and it comes up with $29,250 for the retention on the claim. When the system assigns this value to specific subcontract items on the claim, Item #2 is calculated using the default WC retention % on the subcontract item (in this case %5), and the remaining amount is assigned to Item #1.

WC Retention % on Item
Total Subcontract Item Amount
 Current Approved Claim Amount
Calculated Retention on Items
% Approved Retention

Item #1
10%
$100,000
$15,000
$10,500 (29250-18,750)
70% (10,500/15,000)

Item #2
5%
$1,500,000
$375,000
$18,750 (5% X 375,000)
5%
* The 5% is the default work complete retention percentage on the subcontract item

Totals
7.5%
$1,600,000
$390,000
$29,250
7.5%

If the Enforce Catchup box is
 not checked
Retention is calculated at the item level, not at
 the claim level. The diagram below outlines the retention amounts if the
 Enforce Catchup box is not checked.

WC Retention % on Item
Total Subcontract Item Amount
 Current Approved Claim Amount
Calculated Retention on Items
% Approved Retention

Item #1
10%
$100,000
$15,000
$1,500
10%

Item #2
5%
$1,500,000
$375,000
$18,750
5%

Totals
7.5%
$1,600,000
$390,000
$20,250

If the approved claim amount on Item #1 is not large enough to cover the remaining retention, the remaining retention is added to Item #2.

WC Retention % on Item
Total Subcontract Item Amount
 Current Approved Claim Amount
Calculated Retention on Items
% Approved Retention

Item #1
10%
$100,000
$15,000
$15,000 (entire amount of the claim)
100%

Item #2
5%
$1,500,000
$750,000
$43, 375 ((5% X 750,000)+ amount carried over from Item #1)
5.65%

Totals
7.5%
$1,600,000
$765,000
$57,375
7.5%

Example #2 - A claim item with 0%
 retention
The diagram below outlines how the system will
 calculate retention if you have an item on the claim that has a work complete retention
 percentage of 0.

WC Retention % on Item
Total Subcontract Item Amount
 Current Approved Claim Amount
Calculated Retention on Items
% Approved Retention

Item #1
10%
$100,000
$15,000
$15,000
100%

Item #2
0%
$1,500,000
$450,000
0
0

Totals
10%
$1,600,000
$465,000
$15,000

The system calculates a 10% average retention on the claim, and then applies it to the total current approved claim amount, not just to the claim that should include retention. This means that the calculated retention on the claim is $46,500 ($465,000 X 10%). Since this amount is larger than the approved claim amount on Item #1 (the only item that includes a work complete retention percentage), the entire approved claim amount on Item #1 is retained.
The $15,000 calculated retention on the claim is
 larger than the 10% X $100,000. This means you will also see a (-$5,000 in the Retainage
 Remaining total at the top of the form under the Claim Number field.
The setting in this box only determines the default
 approved retention on the claim and claim items. If the calculated approved retention is
 incorrect, you can manually change it using the Approved Retention field on the Info
 tab on the [SL Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form) form.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)SL Claims - Overview

## Attach batch reports to HQ Batch Control

Check this box if the batch reports should be attached to the batch record that displays in the [HQ Batch Control](/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form) form.
 The reports are stored using the Attachment Storage Location and Subdirectory Structure parameters defined in DM Attachment Options.

- The system will attempt to export batch reports before posting the batch. If the export is successful, it will then post the batch. However, if errors occur for any batch report, the system will display an error message and abort the posting process. You will need to correct the error before you can revalidate and post the batch.

- Because you can secure audit reports (in VA Report Security), access to attachments generated through this process is restricted to HQ Batch Control. If you have secured the HQ Batch Control form, users will only be able to access batch reports if they have access to HQ Batch Control. Unlike regular attachments, indexes are not created for batch report attachments and you cannot access them using DM Attachment Search.

## Allow Exceeded Claim Entry

The Allow Exceeded Claim Entry checkbox on the SL Company Parameters form.

Select this checkbox to allow entering a claim amount (in SL Subcontract Claims) that is greater than the current subcontract amount.
Leave this checkbox unselected if claim amounts should not exceed the current subcontract amount. If you enter a claim amount that exceeds the current subcontract amount, an error displays; you must change the amount in order to save the record.
Tip: You can see the current contract amount in the Subcontract Detail section of the SL Subcontract Claims form.

Note: You can enter claims that exceed the current subcontract amount by:

- entering a claim amount for a subcontract item that is greater than the current subcontract amount

- overriding the approved amount for a subcontract item (which defaults from the item's claim amount) with a value that is greater than the current subcontract amount. The approved amount is the amount that is sent to the AP module.

- entering multiple claims for a subcontract that total more than the current subcontract amount. The system only validates that the Claim Amount field is less than the current subcontract amount, not the Claim To Date Amount field.

## Enforce Phase/CT Estimate Limit

Enforce Phase/CT Estimate Limit checkbox on the Info tab of the SL Company Parameters form.
Select one of the following options from the drop-down list related to limiting SL entry:
No Limit Enforcement - No restrictions will be made to subcontract
 entry when a job phase and cost type would go over budget
Warning Only - Users will only receive warnings for subcontract
 entry that would cause a job phase and cost type to go over budget
Prevent Post/Interface - Users will be prevented from posting a
 subcontract when it would push the estimate associated with the phase and cost type over
 budget
