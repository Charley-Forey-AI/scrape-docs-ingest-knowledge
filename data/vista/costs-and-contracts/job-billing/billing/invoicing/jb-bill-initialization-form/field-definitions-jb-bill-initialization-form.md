---
title: "Field Definitions: JB Bill Initialization Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-bill-initialization-form/field-definitions-jb-bill-initialization-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-bill-initialization-form/field-definitions-jb-bill-initialization-form"
---

# Field Definitions: JB Bill Initialization Form

The following is a list of field descriptions for the JB Bill
 Initialization form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Bill Month

 Enter the bill month to assign to all initialized billings (progress and/or T&M). This month determines which costs initialize for the billing.

## Initialize Option

 This option determines the type of billing you will be generating, as well as how items are initialized based on bill type (as defined in JC Contract Items).

- P-Progress (P) Items Only – Select this option to generate progress billings only. The system will initialize only those items with bill type of ‘P’ (Progress), and calculate values based on percent complete. All T&M-specific fields are disabled when this option is selected.

- B-Progress (P) and Both (B) Items – Initialize (B) Items as T&M – Select this option to generate both progress and T&M billings. The system will initialize items with a bill type of ‘P’ or ‘B’ (Both). Values for items with a bill type of ‘P’ will be calculated based on percent complete. Items with a bill type of ‘B’ will be initialized as T&M, with values based on T&M calculations using Job Cost detail. You might typically use this option when the contract is a ‘Progress’ type, but you have T&M change orders that will be included in AIA reporting. When this option is selected, all fields are enabled, including those specific to T&M billings.

- X-Progress (P) and Both (B) Items – Initialize (B) Items as Progress – Select this option to generate progress billings. The system will initialize items with a bill type of ‘P’ or ‘B’ as Progress. Values for both types will be calculated based on percent complete. When this option is selected, all T&M-specific fields are disabled.

- T-T&M (T) Items Only – Select this option to generate T&M billings only. The system will initialize only those items with a ‘T&M’ bill type, with values based on T&M calculations using Job Cost detail. You might typically use this option for straight T&M billing with no AIA reporting. When this option is used, Progress-specific fields are disabled.

### About the Initialize As $0.00 option

When initializing progress items (options P, B, or X), contract items with the Initialize As $0.00 box checked (in JC Contract Items) will be initialized with bill units/dollars set to 0.00. If using option B, this flag is ignored on items being processed as T&M. You might typically use this feature for contract items that have been over billed (for example, mobilization, and equipment movement). For more details, see [Initialize as $0.00 Option](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form/field-definitions-jc-contract-items-form#ID-000178b9--en)

##  Initialize By

- Process Group - Select this radio button to initialize billings by process group. Billings are generated for all contracts that are assigned the specified process group.
 For T&M billings, if there are customers (without contracts) assigned to the process group, those billings are processed first, using the template assigned to the customer (in the process group). Customer billings will include a bill header and lines, but no JC detail.

- Contract Range - Select this radio button to initialize billings by contract. Billings are generated for all contracts in the specified range.

##  Processing Group

 If initializing by process group, entry in this field is required.
 Enter the processing group (from JB Processing Group) to restrict invoice initialization by. Billings are generated for all eligible contracts assigned this processing group.
 For T&M billings, if there are customers (without contracts) assigned to the process group, those billings are processed first, using the template assigned to the customer (in the process group). Customer billings include a bill header and lines, but no JC detail. (You will typically use these types of billings for monthly maintenance or other non-job related billings.)

##  Beginning/Ending Contract

 If initializing by contract range, entry in these fields is required.
 Enter the beginning and ending in a range of contracts (from JC Contracts) to initialize. If initializing a single contract, enter the same number in both fields.

##  Restrict by Item Bill Group

 Check this box to restrict the initialization of contract items by bill group. When checked, only contract items with a bill group (assigned in JC Contract Items) matching the one specified in the Item Bill Group field are initialized.
 Leave this box unchecked to initialize all contract items, regardless of bill group.

##  Item Bill Group

 Enter the bill group (as defined in JB Bill Groups) to restrict item initialization by. All contract items assigned a bill group (in JC Contract Items) matching the bill group specified here are initialized to the billing.

##  Add Separate Invoice Per Item Bill Group

This box is enabled when you select either option B or T from the [Initialize Option](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-bill-initialization-form/field-definitions-jb-bill-initialization-form#ID-000149cd--en) drop-down.
 Check this box to generate a separate invoice for each unique bill group.
 Leave this box unchecked to initialize multiple bill groups to a single invoice.

##  Invoice Date

 Specify the invoice date for all initialized billings. This field initially defaults to the current date.

## Ticketed Cost Option

The Ticketed Cost Options drop-down (unlabeled) on the JB Bill Initialization form.
This field is enabled only when the Initialize Option drop-down is set to B-Progress (P) and Both (B) Items – Initialize (B) Items as T&M or T-T&M (T) Items Only.
Specify whether to include cost detail associated with field tickets that are approved for initialized billings.

- Y - Include Ticketed Costs - Select this option to include cost detail associated with approved field tickets, as well as cost detail not associated with field tickets. For cost detail records associated with field tickets, initialization includes only those records where the associated field ticket(s) were approved on or before the specified Approval Cutoff Date. If no approval cutoff date is specified, initialization includes all records associated with approved field tickets, regardless of their approval date.
For cost detail records not associated with field tickets, the system uses the dates in the T&M Job Cost Detail Transaction Range section to determine cost detail to include.

- N - Exclude Ticketed Costs - Select this option to exclude cost detail associated with field tickets and only initialize cost detail not associated with field tickets. When selected, the Approval Cutoff Date field is disabled.

- O - Ticketed Costs Only - Select this option to include only cost detail associated with approved field tickets and exclude costs not associated with field tickets. If an Approval Cutoff Date is specified, initialization includes cost detail with field ticket(s) that were approved on or before the specified approval cutoff date. If no approval cutoff date is specified, initialization includes all cost detail records with approved field tickets, regardless of their approval date. In addition, all fields in the T&M Job Cost Detail Transaction Range section are disabled.

## Approval Cutoff Date

The Approval Cutoff Date field on the JB Bill
 Initialization form.
This field is enabled only when:

- the Initialize Option drop-down is set to B-Progress
 (P) and Both (B) Items – Initialize (B) Items as T&M or T-T&M
 (T) Items Only,
and

- the Ticketed Cost Options drop-down is set to Y-Include Ticketed Costs or O-Ticketed Costs Only

Enter the approval cutoff date for field tickets to include during bill initialization. Initialization will only include cost detail records that are associated with field tickets approved on or before this date.
If you leave this field blank, initialization includes all cost detail records associated with approved field tickets, regardless of the field ticket approval date.Note: The cost detail date range and cutoff months specified in the T & M Job Cost Detail Transaction Range section are used only for cost detail not associated with field tickets. For cost detail records associated with field tickets, the system uses the Approval Cutoff Date to determine which records to include. This ensures that all costs associated with a single ticket number are billed together, since they cannot be billed separately.

##  Cost Detail Beginning/Ending Date

The Cost Detail Beginning/Ending Date fields on the JB Bill Initialization form.
 These fields are enabled for Initialize Option T (T&M only) or B (Progress and T&M), but apply to T&M items only. However, if the Ticketed Cost Option drop-down is set to O-Ticketed Costs Only, these fields are disabled.
 Enter the beginning and ending date in the range of dates from which you want costs pulled from Job Cost for initialization. If left blank, all available costs are included on the billing.

##  Cost Detail Cutoff Month

The Cost Detail Cutoff Month field on the JB Bill Initialization form.
 This field is enabled for Initialize Option T (T&M only) or B (Progress and T&M), but applies to T&M items only. However, if the Ticketed Cost Option drop-down is set to O-Ticketed Costs Only, these fields are disabled.
 Enter the month through which to pull costs from JC when invoices are generated. If left blank, all available costs will be included on the billing.

##  Use Different Labor Cutoff Date

The Use Different Labor Cutoff Date checkbox on the JB Bill Initialization form.
 This checkbox is enabled for Initialize Option T (T&M only) or B (Progress and T&M), but applies to T&M items only. However, if the Ticketed Cost Option drop-down is set to O-Ticketed Costs Only, these fields are disabled.
 Check this box to use a different cutoff date (than the Cost Detail Cutoff Date) for pulling in labor-type job cost detail. Use the Labor Cutoff Date field to specify the date through which to pull labor-type cost detail.
 Leave this box unchecked if labor-type job cost detail is pulled based on the Cost Detail Cutoff Date.

##  Labor Cutoff Date

The Labor Cutoff Date field on the JB Bill Initialization form.
 This field is enabled for Initialize Option T (T&M only) or B (Progress and T&M), but applies to T&M items only. However, if the Ticketed Cost Option drop-down is set to O-Ticketed Costs Only, these fields are disabled.
 Enter the date through which to pull labor-type costs from JC when invoices are generated. If left blank, all available labor-type costs will be included on the billing.

##  Change Orders Thru

 Specify the date through which to initialize change orders on this billing. All change orders dated on or before this date are included on initialized billings.
Note: For Progress Billings, once billings are initialized, review all change orders for each billing in JB Prog Bill Chg Order Items (Change Orders button in JB Progress Billings) to ensure that all appropriate change orders have been included.

##  Assign Invoice Numbers

 Check this box to have the system automatically assign invoice numbers during initialization. The system assigns invoice numbers sequentially based on the Last Invoice # field in JB Company Parameters or AR Company Parameters, depending on whether you selected Job Billing or Accounts Receivable as the Last Invoice Option in JB Company Parameters.
 Leave this box unchecked to assign invoice numbers to billings manually (in JB Progress Billing or JB T&M Bill Edit).

##  Beginning/Ending Bill Date

 This field applies to Progress billings only; it is disabled for Initialize Option T (T&M only).
 Specify the beginning and ending bill date for this group of progress billings. (Note: These dates are informational only and do not control the data included when initializing billings. For example, you might use these dates to identify the range this billing covers.)

## Ready for Review

The Ready for Review checkbox on the JB Bill Initialization form.
This field is enabled only if you selected the Use Review and Approval Workflow checkbox in JB Company Parameters.
Select this checkbox to set the Ready for Review checkbox as selected in JB Progress Billing and/or JB T&M Bill Edit for all billings created during the initialization process. You can override the setting as needed for individual billings.

Clear this checkbox if you want to individually mark billings as "ready for review" in JB Progress Billings and/or JB T&M Bill Edit after the initialization process is complete.
