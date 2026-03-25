---
title: "Field Definitions: IN Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form/field-definitions-in-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form/field-definitions-in-company-parameters-form"
---

# Field Definitions: IN Company Parameters Form

The following is a list of field descriptions for the IN
 Company Parameters form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  IN Company

 Enter the IN company (must be a valid HQ Company) in which Inventory processing will occur.

##  GL Co#

 Specify the GL company to update when materials are bought, sold, or transferred from this location.

##  Journal

 Specify the journal to update when posting adjustments, transfers, or production entries in Inventory.

##  Burdened Unit Cost - include AP Misc Amt and Tax

The Burdened Unit Cost–Include AP Misc Amt and Tax checkbox in the IN Company Parameters form.
Check this box if you want unit costs for stocked materials to include tax and miscellaneous amounts (for example, freight) that have been posted in AP. The system uses this 'burdened unit cost' to update both last and average unit cost for the material and posts these costs to the Inventory GL Account.
If unchecked, tax and freight costs are not included in the unit cost of a material, but are tracked separately. Freight costs are posted to the specified "Misc GL Account,” with overrides by location (IN Locations) or location/category (IN Location Category Override). Tax amounts are posted to the company "Tax GL Account", with overrides by location.

##  Misc GL Account

 Specify the GL expense account to debit with miscellaneous amounts posted in AP. Must be an active GL Account with a subledger type of ‘I’ (Inventory) or null.
Note: If you are using burdened cost, and you enter freight amounts on AP invoices with the "Inc" flag set to N, the freight amounts will be credited to this account to offset the charge to inventory. When the freight bill is entered, it will be debited to this same account.

##  Tax GL Account

 Specify the GL expense account to debit for sales tax when posting transactions in AP. Must be an active GL Account with a subledger type of ‘I’ (Inventory) or null.

##  Audit Options

The audit options determine when new records of changes are added to the HQ Master Audit (HQMA) database table. For example, if you change a setting on the company parameters form, the system creates a new record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. See [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more information about viewing audit records in the HQMA table.
The list below details the audit options.

- Company Parameters – Company
 Parameters will always be checked. Any changes made to the IN Company Parameters
 program will be tracked in the Master Audit file.

- Locations - Check this box to
 record changes to Inventory locations in the Location Master, Location Groups,
 Location Company Overrides, Location Category Overrides, and Location
 Company/Category Overrides.

- Materials - Check this box to
 record changes to material information in IN Materials and IN Material U/Ms. This
 does not include system updates to material quantities and unit costs (i.e. On Hand,
 On Order, Allocated, etc.).

- Bill of Materials - Check this box
 to record changes made in IN Bill of Materials and IN Bill of Materials Override.

- Material Orders – Check this box to
 record changes made to material orders and material order items in IN Material Order
 Entry. Does not include updates posted via material order 'confirmation' or 'close'
 batches.

##  Auto Generate MO#s

 Check this box to have the system
 automatically generate material order numbers. When a material order is entered, the system
 will generate a material order number based on the Last Used MO # (specified below).
 Leave this box unchecked if you:

- do not want to auto generate material order numbers

-  use alpha/numeric material order numbers

- use the Project Management module and have elected to use the Project/Seq option for generating MO numbers.

##  Last Used MO#

 This field is only applicable if you checked
 the Auto Generate
 MO#s box above.
 When setting up Inventory, specify a starting material order number, up to 10 digits. When entering material orders, the system assigns material order numbers sequentially based on this number.
 After the initial setup, this field is automatically updated by the system each time a material order number is generated, and should not need editing. This field is NOT updated by manually assigned material order numbers.

## Attach batch reports to HQ Batch Control

Check this box if the batch reports should be attached to the batch record that displays in the [HQ Batch Control](/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form) form.
 The reports are stored using the Attachment Storage Location and Subdirectory Structure parameters defined in DM Attachment Options.

- The system will attempt to export batch reports before posting the batch. If the export is successful, it will then post the batch. However, if errors occur for any batch report, the system will display an error message and abort the posting process. You will need to correct the error before you can revalidate and post the batch.

- Because you can secure audit reports (in VA Report Security), access to attachments generated through this process is restricted to HQ Batch Control. If you have secured the HQ Batch Control form, users will only be able to access batch reports if they have access to HQ Batch Control. Unlike regular attachments, indexes are not created for batch report attachments and you cannot access them using DM Attachment Search.

## GL Month Close validation check for IN transactions posted after monthly reconciliation

GL Month Close Validation Check for IN Transactions Posted after Monthly Reconciliation checkbox on the Info tab of the IN Company Parameters form.
Select this box to validate that transactions have not been posted after monthly reconciliation when GL Month End Close is run.

Related information

- [IN Company Parameters Form](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form)

- [About Pricing Options](/en/vista/vista/job-resources/inventory/setup--maintenance/company/about-pricing-options)

- [About the GL Month End Close Form](/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-month-end-close-form)

##  Valuation Method

The Valuation Method field on the IN Company Parameters form, Add'l Info tab.
Select the valuation method to use for monthly reconciliation.

- 0-As posted – Month-end value set equal to beginning value plus sum of net activity posted throughout the month. No correcting entries will be made.

- 1-Average Cost – Month-end value calculated using beginning value and monthly average cost. Monthly average cost calculated based on the ‘posted’ costs of all ‘ins’.

- 2-FIFO (First In First Out) – Month-end value calculated based on actual dates and costs, outgoing inventory relieved from oldest to newest stock on hand.

- 3-LIFO (Last In First Out) – Month-end value calculated based on actual dates and costs, outgoing inventory relieved from newest to oldest stock on hand.

- 4-Standard Cost – Month-end value calculated based on ending ‘quantity on hand’ times current standard unit cost. Should match ‘posted’ ending value unless standard cost has been changed during the month.

The valuation method determines how the system captures beginning, ending, and summarized transaction activity by month, as well as how it makes adjusting entries to correct inventory values when "ins" and "outs" are not posted in sequence.

##  Cost Method

The Cost Method field on the IN Company Parameters form, Add'l Info tab.

Indicate the cost method to use for relieving inventory when materials are sold, transferred, or produced.

- 1-Average Cost – Relieve inventory using the material's average unit cost at the time of transfer, usage, or sale. Purchases and other increases to stock are valued at their actual cost (may include freight and tax if the ‘burdened unit cost’ option is selected below).

- 2-Last Cost – Relieve inventory using the material's last unit cost at the time of transfer, usage, or sale. Purchases and other increases to stock are valued at their actual cost (may include freight and tax if the ‘burdened unit cost' option is selected below.)

- 3-Standard Cost – All ‘ins’ and ‘outs’ to inventory are valued at the material's standard unit cost. Purchases and other increases to stock post the difference between standard and actual costs into a Cost Variance GL Account.

Note: You may override the Cost Method defined for a company by location in the IN Locations form or by location/category in the IN Location Category Override form. The system will only use the cost method defined here if the Cost Method for a location is set to No Override.

## Pricing Option: Customer Sales

Select the method that be used to calculate the unit price when selling materials to customers in Material Sales. See [Pricing Options](/en/vista/vista/job-resources/inventory/setup--maintenance/company/about-pricing-options) for an overview of the pricing options.

- 1-Average Cost Plus Markup

- 2-Last Cost Plus Markup

- 3-Standard Cost Plus Markup

- 4-Standard Price Less Discount

Note: If a markup/discount rate is specified for the customer in [ AR Customers ](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form), that rate will be used in the calculation of the unit price. If no rate is specified at the customer level, then the Customer Markup/Discount Rate specified for the material in [IN Location Materials ](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form) is used.

##  Pricing Option: Job Sales

 Select the method that will be used to calculate the unit price when selling materials to
 jobs in Material Sales. See [ Pricing Options ](/en/vista/vista/job-resources/inventory/setup--maintenance/company/about-pricing-options)for an
 overview of the pricing options.

- 1-Average Cost Plus Markup

- 2-Last Cost Plus Markup

- 3-Standard Cost Plus Markup

- 4-Standard Price Less Discount

Note: If a markup/discount rate is specified for the job in
 [JC Jobs ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form), that rate will be used in the calculation of the
 unit price. If no rate is specified at the job level, then the Job Markup/Discount Rate
 specified for the material in [IN Location Materials ](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form) is used.

##  Pricing Option: Inventory Sales

 Select the method that will be used to calculate the unit price when selling materials to inventory locations in Material Sales or when Usage Option is set to Sales. See [ Pricing Options ](/en/vista/vista/job-resources/inventory/setup--maintenance/company/about-pricing-options)for an overview of the pricing options.

- 1-Average Cost Plus Markup

- 2-Last Cost Plus Markup

- 3-Standard Cost Plus Markup

- 4-Standard Price Less Discount

Note: Uses the Inventory Markup/Discount Rate specified for the material in [IN Location Materials ](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form).

##  Pricing Option: Equip Sales

 Select the method that will be used to calculate the unit price when selling materials to equipment in Material Sales. See [ Pricing Options ](/en/vista/vista/job-resources/inventory/setup--maintenance/company/about-pricing-options)for an overview of the pricing options.

- 1-Average Cost Plus Markup

- 2-Last Cost Plus Markup

- 3-Standard Cost Plus Markup

- 4-Standard Price Less Discount

Note: Uses the Equipment Markup/Discount Rate specified for the material in [IN Location Materials ](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form).

## Pricing Option: Service Sales

 Select the method that will be used to calculate the unit price for stocked materials used on a service work order (in SM Work Orders). See [Pricing Options](/en/vista/vista/job-resources/inventory/setup--maintenance/company/about-pricing-options) for an overview of pricing options.

- 1-Average Cost Plus Markup

- 2-Last Cost Plus Markup

- 3-Standard Cost Plus Markup

- 4-Standard Price Less Discount

When entering work completed Inventory lines (in SM Work Orders), the system will use the last, average, or standard unit cost or unit price defined for the location/material in IN Location Materials (depending on the pricing option selected here), along with the Service Markup/Discount rate specified for the location (also in IN Location Materials) to determine the Cost Rate for the work completed line.

##  Usage Option

 Indicate how component materials are handled during production posting when the source location of the component material is different than the production location of the finished good.
Sale - Select this option if component materials will be “sold” to the production location. Unit price will be determined by the Pricing Option specified for Inventory.
Transfer - Select this option if component materials will be “transferred” to the production location. Value will be determined by the Cost Method specified above.

##  Allow Unit Cost Overrides

 Check this box to allow overrides to a material’s unit cost when posting sales, transfers, or production usage.
 Do not check this box if overrides to a material’s unit cost are not allowed.

## Display warning if Qty On Hand is negative

Check this box to display a warning when the sale, transfer, or usage of a material causes the 'on hand' quantity at the specified location to be exceeded. The message will indicate that the transaction will result in a negative “on hand” quantity. Entry will still be allowed.
Leave this box unchecked to suppress the "negative quantity" warning when entering sales, transfers, or usage of a materials that exceed the 'on hand' quantity at the specified location.
Note: The setting defined here does not control the
 "negative on-hand quantity" warning displayed in MS Ticket Entry when the quantity
 specified for material will exceed the on-hand quantity for a location; to provide a
 warning on MS tickets, check the Display warning if Qty On Hand is negative in MS
 Ticket Entry box in IN Location Materials.

##  Allow GL Account Overrides

 Check this box to allow overrides to the Inventory account when entering Inventory transactions in PO Entry, AP Transaction Entry, AP Recurring Invoices, and AP Unapproved Invoice Entry.
 Do not check this box if not allowing overrides to the Inventory account when entering Inventory transactions in AP and PO.
Note: It is suggested that this option remain unchecked to ensure that Inventory and General Ledger stay in balance on Inventory accounts.

## GL Adjustments Interface Level

Specify the GL Adjustments interface level.

- None - If selected, no update to GL will occur. This option is typically only used during initial setup.

- Detail - If selected, one GL entry will be made for each inventory transaction. Use the “Select Available Items for Detail Level GL Description” box below to define the detail description that will be used for these entries.

- Summary - If selected, entries will be summarized and one entry will be posted for each unique GL account. Use the “Summary GL Description” field below to enter the description that will be used for these transactions.

Note: The interface level selected here will also be used
 when updating Cost and WIP accounts for work completed inventory lines (type 4-Inventory)
 on SM work orders; however, the update will only occur if the IN interface
 box is checked in SM Company Parameters.

##  Summary GL description - Adjustments

 This field is enabled when the Adjustments Interface Summary radio button has been selected.
 When the Summary radio button has been selected, entries are summarized and one entry is posted for each unique GL account. Use this field to enter the description used for these transactions.

##  GL Transfers Interface Level

Specify the GL Transfers interface level.
None - If selected, no update to GL will occur. This option is typically only used during initial setup.
Detail - If selected, one GL entry will be made for each inventory transaction. Use the “Select Available Items for Detail Level GL Description” box below to define the detail description that will be used for these entries.
Summary - If selected, entries will be summarized and one entry will be posted for each unique GL account. Use the “Summary GL Description” field below to enter the description that will be used for these transactions.

##  Summary GL description - Transfers

 This field is enabled when the Transfers Interface Summary radio button has been selected.
 When the Summary radio button has been selected, entries are summarized and one entry is posted for each unique GL account. Use this field to enter the description used for these transactions.

## GL Production Interface Level

Specify the GL Production interface level.

- None - If selected, no update to GL will occur. This option is typically only used during initial setup.

- Detail - If selected, one GL entry will be made for each inventory transaction. Use the “Select Available Items for Detail Level GL Description” box below to define the detail description that will be used for these entries.

- Summary - If selected, entries will be summarized and one entry will be posted for each unique GL account. Use the “Summary GL Description” field below to enter the description that will be used for these transactions.

##  Summary GL description - Production

 This field is enabled when the Production Interface Summary radio button has been selected.
 When the Summary radio button has been selected, entries are summarized and one entry is posted for each unique GL account. Use this field to enter the description used for these transactions.

##  Material Order Interface Level

Specify the Material Order interface level.
None - If selected, no update to GL will occur. This option is typically only used during initial setup.
Detail - If selected, one GL entry will be made for each inventory transaction. Use the “Select Available Items for Detail Level GL Description” box below to define the detail description that will be used for these entries.
Summary - If selected, entries will be summarized and one entry will be posted for each unique GL account. Use the “Summary GL Description” field below to enter the description that will be used for these transactions.

##  Summary GL description - Material Order

 This field is enabled when the Material Order Interface Summary radio button has been selected.
 When the Summary radio button has been selected, entries are summarized and one entry is posted for each unique GL account. Use this field to enter the description used for these transactions.

##  JC Interface Level for Material Orders

Specify the level of update to JC that will occur when posting material order confirmation entries.
None – Select this option if you do not want to update actual units or costs to JC. You will typically only use this option when initially setting up your system and entering confirmations for Material Orders whose actual costs are already reflected in JC.Batches must be validated and posted, but no transactions will be created in JC for actual units or costs.(Committed units and costs are always updated to JC.)
Detail – Select this option to update JC with one entry for each confirmation entry. The material order, item, location, material, job, phase, cost type, etc. will be recorded with each JC Cost Detail entry.
Summary – Select this option to update JC with one entry per JCCo#/Job/Phase/CostType/Material Order/UM/TaxCode/JCUM.Material order item and material-specific information will not be included in JC Detail.
NOTE:If committed costs are updated in detail, then actual costs will be also be updated in detail, unless this interface flag is set to ‘None’.

##  Document Type

The Document Type drop-down on the IN Company Parameters form, Workflow tab.
 Specify the type of document to which the workflow applies. Currently, PO-Purchase Order is the only option available.Note: You can have only one process for each document type.

Note: The workflows defined here override those defined in HQ Company Setup.

For more information about the Workflow Process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

##  Process

The Process field on the IN Company Parameters form, Workflow tab.
Enter the workflow process to perform on purchase orders or press F4 to select from a list of valid workflows. Valid workflows are those that are associated with the PO-Purchase Order document type or those that do not specify a document type.Note: When you create a workflow (in [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)), you will generally assign it to a specific document type. However, you may have generic workflows that are not associated with a specific document type (that is, the Document Type field is blank). You can assign these generic workflows to PO document types if applicable.

Note: The workflows defined here override those defined in HQ Company Setup.

##  Active

The Active checkbox on the IN Company Parameters form, Workflow tab.
Select this checkbox if this workflow should be applied when new POs are created.
For more information about the workflow process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

## Notes

The Notes field on the IN Company Parameters form, Workflow tab.
Enter any notes about the workflow.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.
