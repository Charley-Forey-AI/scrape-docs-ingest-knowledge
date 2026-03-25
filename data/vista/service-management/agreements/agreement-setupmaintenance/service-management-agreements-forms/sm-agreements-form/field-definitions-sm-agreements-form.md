---
title: "Field Definitions: SM Agreements Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form/field-definitions-sm-agreements-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form/field-definitions-sm-agreements-form"
---

# Field Definitions: SM Agreements Form

The following is a list of field descriptions for the SM
 Agreements form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Agreement

Enter a number to represent this agreement or
 enter N, New, or + to have
 the system automatically assign the next sequential number available (based on highest
 existing agreement numbers).
Note: If you manually assign a number, be aware that the system uses the highest existing number to determine the next available number when using the auto-numbering functionality.

## Revision

Displays the current agreement revision, showing the term and revision status. The revision represents changes to the agreement as a whole (i.e. original agreement, amendments, renewals). You can select different revisions to view, but you cannot edit the revision term or status.
When you add a new agreement, this field automatically defaults a status of Quote. Other statuses are applied by the system based on the agreement activity. The statuses applied are as follows:

- Quote - Not activated. In addition to the original quote, this status will also be applied to amendments and renewals when they are first initiated, as well as to agreements or renewals that have been deactivated (see [Deactivating an Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-activation--deactivation-form) for more information).

- Active - This status is applied to any revision (agreement, amendment, or renewal) that has been activated.

- Terminated - This status is applied to any revision that is manually terminated or terminated by activation of an amendment.

- Expired - This status is assigned to all agreements that have expired (i.e. passed their expiration date).

## Description

Enter a description for this agreement, up to 60 characters.
Note: Once you activate the agreement, this field is disabled and cannot be edited. The system will maintain this description through all amendment and renewal revisions of this agreement.

## Alt Agreement

Enter an alternate agreement identification number for this agreement, up to 30 characters. This will typically be the number used by your customer to track this agreement. The field is information only, and can be used for reporting purposes.
Note: This field is disabled when the agreement has a status of Terminated or Expired. For information on status, see the [Revision](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form/field-definitions-sm-agreements-form#ID-00041125--en) F1 help.

## Agreement Type

Enter the agreement type for this agreement.
 Must be an active agreement type. Press F4 for a list of valid agreement
 types.
The agreement type specified here will determine the department to which costs and revenue are posted.
Entry in this field is not required when first setting up the agreement. However, you must assign an agreement type before you can activate the agreement.
Note: Once you activate an agreement, this field is disabled and cannot be edited.

## Customer

Enter the SM customer to which this agreement
 applies. Must be an active customer. Press F4 for a list of valid SM customers.
Note: Once you activate an agreement, this field is disabled and cannot be edited.
Note: Once you activate an agreement, this field can only be changed by changing the customer in [SM Service Sites](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form).

## Customer PO

Enter the PO number (provided by the customer) for this agreement. Up to 30 characters allowed.
The purchase order number specified here will default automatically on all preventative maintenance work orders generated for this agreement. May be overridden at the work order scope level (in SM Work Orders).

## Effective Date

Enter the date on which this agreement became or will become effective.
Note: Once you activate an agreement, this field is disabled and cannot be edited.

## Start Date

Start Date field of the Info tab on the SM Agreements form.
Enter the start date for an agreement version beginning at a time later than the effective date and prior to the expiration date.
The field is disabled for any agreement that is not Revision 1 and is still in quote form; this field is completely hidden starting with Version 2 and greater.
Note: If you enter a
 start date, it becomes the new default for auto-scheduling—for both billing and
 amortization—and supersedes the date in the Effective Date field.

## Expiration Date

This field is
 enabled for expiring agreements only (i.e. Non-Expiring Agreements box is
 unchecked).
Required.
Enter the expiration date for this agreement. Must be at least one day after the specified effective date.
If you checked the Auto Renew box
 for this agreement, the system will use this date to determine renewal eligibility when
 running the agreement renewal process.
Note: Once you activate an agreement, this field is disabled and cannot be edited.

## Renew Through

This field is only enabled if the agreement
 specifies an agreement type with the Auto Renew checkbox selected (in [SM Agreement Types](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-types-form)).
Enter the date through which to renew the agreement. Date must be greater than the expiration date specified for the agreement.
Note: The auto-renewal functionality is not available for agreements at this time; however, it will be available in a future release. Currently, entering a date here allows the system to forecast labor allocations for the agreement prior to its renewal.

## Renew Markup

This field is only enabled if the agreement
 specifies an agreement type with the Auto Renew checkbox selected (in [SM Agreement Types](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-types-form)).
Enter the markup percent to apply when renewing the agreement. Entry is required if you entered a Renew Through date for the agreement.
Note: The auto-renewal functionality is not available for agreements at this time; however, it will be available in a future release.

## Rate Template

Enter the rate template to use for work performed on a work order that is not covered by agreement pricing (typically "add-on" work). Must be an active rate template.
Note: The rate template specified here will only be used for
 manually added work order scopes that reference this agreement or for work completed lines
 referencing this agreement that specify to use agreement rates (i.e. Coverage field
 is set to A-Agreement Rates).

## Budget Total

For use with Agreement Budgets.
Display only, the total budget amount for this agreement. This field is populated automatically based on the total budget amounts entered by call type/cost type category on the Budget tab.

## Est. Profit Margin

For use with Agreement Budgets.
Display only, the estimated profit margin for this agreement. This field is populated automatically based on the following:
(Agreement Price + Est. Service Revenue) – Budget Total / (Agreement Price + Est. Service Revenue)

## Est. Percent Markup

For use with Agreement Budgets.
Display only, the estimated percent of markup for this agreement. This field is populated automatically based on the following calculation:
(Agreement Price + Service Revenue – Budget) / Budget

## Agreement Price

Enter the price for this agreement. All services listed for this agreement (on the Work Schedule tab) with a pricing type of I-Included in Agreement will be covered by this price.
The agreement price is based on the term of the agreement. For example, if you enter an agreement price of $15,000 and the agreement covers a 2-year period, the customer will be charged a total of $15,000 for the entire 2-year period.
Note: Once you activate an agreement, this field is disabled and cannot be edited.

## Est. Service Revenue

Display only, the total estimated revenue for agreement services that are not included in the agreement price (i.e. have a price method other than Included in Agreement).
Note: The system calculates the estimated revenue dependent on how the price is applied for the service. For more information, see [Estimated Service Revenue](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-estimated-service-revenue).

## Billing Reduction

Enter the amount by which to reduce the remaining amount to bill. Do not enter as a negative number, as this number is already assumed negative.
The system automatically adjusts the Total Remaining accordingly based on the value entered here. For example, if the Total Remaining is 2,500.00 and you enter 500.00 in this field, the new Total Remaining will be 2,000.00.
 If the Total Remaining is 0.00 (e.g. this is an amendment that did not add additional pricing to the agreement service), but you want to reduce the remaining amount to bill by 500.00, entering 500.00 in this field will update the Total Remaining to -500.00.
Note: If the resulting Total Remaining amount is not 0.00, you will need to adjust the agreement billing schedule until the Total Remaining equals 0.00.

## Matl Tax Override

The Matl Tax Override drop-down on the SM Agreements form, Info tab.

Select the default tax type for material-related work completed lines (those assigned a material SM Cost Type) on an agreement work order. The option you select here defaults for each agreement service added to the agreement, which you can override as needed.

- Blank – Use the standard tax type defaulting behavior. For taxable material-related work completed lines, the tax type defaults as Sales. For non-taxable material-related work completed lines, the tax type defaults as blank.

- N - No Tax – Default the tax type as "blank" for material-related work completed lines.

- S - Sales Tax Only – Default the tax type for taxable material-related work completed lines as Sales (US) or VAT (AU/CA).

- U - Use Tax Only (US companies only) – Default the tax type as Use for taxable material-related work completed lines.

The option selected here is used as the Matl Tax Override default for agreement services; you may override the default at the agreement service level.
Note: If you amend or renew this agreement, the system copies this value to the new revision. You may override the value as needed.

### Changing the Matl Tax Override

If you change the Matl Tax Override value for an existing agreement with one or more agreement services, when you save the record, the system displays a message asking if you want to update existing agreement services to the new value.
 If you select Yes, the system updates the Matl Tax Override value for all agreement services to match the new value entered for the agreement. However, if you updated the agreement value to blank, when the services are updated, the system defaults the value from the call type associated with each service.
If you select No, the system leaves the Matl Tax Override value intact for each agreement service.

## Tax Option Override

The Tax Option Override drop-down on the SM Agreements form, Info tab.

This field defaults as blank. Choose one of the options listed below if you want that override to default on all services set up for this agreement.
If you set up a work order and reference the agreement on the work order scope, the work order scope defaults the Tax Option Override selected for this agreement.
If you leave this field blank, the Tax Option Override defaults as blank for all services set up for the agreement, as well as for all manually entered work order scopes that reference this agreement.

- N - Not Taxable - Do not apply taxes at the time of purchase or billing. The cost and billing tax types and tax codes default as blank, regardless of whether the SM cost type specified for the work completed line is taxable. You may override the defaults as needed.

- P - Taxable at Purchase Only - Apply taxes at the time of purchase only. If the cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope and the Cost Tax Code defaults from the service site or service center depending on the Tax Source defined for the work order scope. The billing tax type and billing tax code default as blank. If the cost type is not taxable or no cost type is specified, all tax fields default as blank. You may override as needed.

- B - Taxable at Billing Only - Apply taxes at the time of billing only. If the line's cost type is taxable, the billing tax type and billing tax code default to the Tax Type and Tax Code specified for the work order scope. The Cost Tax Type and Cost Tax Code default as blank. If the cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.

- M - Taxable at Purchase/Markup at Billing - Apply taxes at the time of purchase and also apply taxes to the markup amount at the time of billing. If the line's cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope and the Cost Tax Code defaults from the service site or service center depending on the Tax Source defined for the work order scope. The billing tax type and tax code default to the Tax Type and Tax Code specified for the work order scope; however, the tax basis defaults the markup amount only. If the line's cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.Note: For taxable purchases, the bill tax basis is reduced by the amount that was previously taxed at the time costs were recorded. If you did not capture taxes when recording costs, there is no credit to apply to the transaction at billing; therefore, the bill tax basis is calculated using the full billing subtotal, not just the markup.

- F - Full Tax at Purchase and Billing - Apply tax fully at time of purchase and at time of billing. If the line's cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope, and the Cost Tax Code defaults from the service site or service center, depending on the Tax Source defined for the work order scope. The billing tax type and billing tax code default to the Tax Type and Tax Code specified for the work order scope, and the tax basis defaults the full billable amount. If the line's cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.

Note: If you amend or renew this agreement, the system copies this value to the new revision. You may override the value as needed.

### Changing the Tax Option Override

If you change the Tax Option Override value for an existing agreement with one or more agreement services, when you save the record, the system displays a message asking if you want to update existing agreement services to the new value.
 If you select Yes, the system updates the Tax Option Override value for all agreement services to match the new value entered for the agreement. However, if you updated the agreement value to blank, when the services are updated, the system defaults the value from the call type associated with each service.
If you select No, the system leaves the Tax Option Override value intact for each agreement service.

## Revenue Recognition

The Revenue Recognition field on the SM Agreements form, Info tab.
If you selected the Recognize Revenue as Costs Incurred checkbox in SM Company Parameters, this field defaults to C - As Costs Incurred and is disabled.
If you did not select the Recognize Revenue as Costs Incurred checkbox in SM Company Parameters, select which option to use for recognizing revenue for this agreement:

- B - As Billed - Select this option to recognize revenue once it is billed.

- S - Amortize - Select this option to amortize revenue recognition for an agreement. When you select this option, the system allows you to set up an amortization schedule on the Amortization Schedule tab. For more information, see [Set up an Agreement Amortization Schedule
 Manually](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-amortization-schedule-setup/set-up-an-agreement-amortization-schedule-manually).

- C - As Cost Incurred - Select this option to recognize revenue as costs are incurred when posting work orders for this agreement.

Note: Once you activate the agreement, this field is disabled and cannot be changed, even when creating amendments or renewals.

## Margin

Margin field on the Info tab of the SM Agreements form.

This field is required when the Revenue Recognition type is As Costs Incurred.
Enter a mark-up percentage to apply when recognizing revenue for this agreement. During
 the revenue recognition process (in SM Revenue Recognize), the system will determine the
 revenue to recognize by applying the margin to the sum of all associated costs (that is,
 work completed lines posted to the agreement work order).
 For example, if the total cost posted for the agreement is $2,500 and the margin is 20%,
 the recognized revenue will be $3000 ($2,500.00 x 1.2 = 3,000.00).Note: The system
 won’t exceed the agreement price when calculating recognized revenue.

## Invoice Format

Enter the custom report to use for printing
 Agreement Billing invoices for this customer. Press F4 for a list of valid custom
 reports.
 Leave blank to use the Def. Agreement Inv.
 Report specified in SM Company Parameters.
Note: You can override the invoice format at the invoice level.

## Auto Schedule Trips

Auto Schedule Trips checkbox on the SM Agreements form.

Select this checkbox to automatically schedule a trip (on the SM Dispatch Board) when a PM Work Order is created.
Leave this checkbox unselected if you do not want trips auto-scheduled for this agreement.
If you have not yet set up services for the agreement, the setting here defaults for each service you add to the agreement. You can override the setting for the service as needed.
If you have already set up services for the agreement, selecting or deselecting this checkbox displays (when saving the record) asking if you want to update existing services. Select Yes to update existing services or No to update only the agreement. You will need to manually update each service accordingly.
Note: Auto-scheduled trips will default to the date and technician specified on the SM Service form.

## Separate Scope Per Service Item

The Separate Scope Per Service Item checkbox on the SM Agreements form, Info tab.
For use with the [Tasking](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling) feature.
Select this checkbox to generate a separate work order scope for each serviceable item associated with class maintenance tasks on the agreement.
Note: If you select the Separate Scope Per Service Item checkbox for an agreement and then also select the Separate Work Order checkbox for one or more agreement services, the system will generate a separate work order for each agreement service flagged for a separate work order. Remaining services will be set up on one work order with separate scopes per service item.

If you are not using the Tasking feature or do not want service items, allLeave this checkbox unselected if you want service items grouped together on the same work order scope.
For more information about this checkbox, see [Separate Scope Per Service Item](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form#ID-000410d6--en__SeparateScopesPerServiceItem).

## Call Type

Required.
Enter the call type for which to define a
 budget amount or press F4 to select from a list of valid call
 types.

## Cost Type Category

Required.
Enter L, E, M,  O, or S to specify
 the cost type category for which to define the budget amount or select the cost type
 category using the drop-down menu (accessed by clicking the down arrow). Cost type
 categories are as follows:

- L-Labor

- E-Equipment

- M-Material

- O-Other

- S-Subcontracts

## Budget Amount

Enter the budget amount for the specified call type/cost type category.

## Service Budget

Display only, the total of all agreement service cost estimates for this call type / cost type category.

## Total Remaining

The system displays an amount in this field based on the total price of the agreement (including periodic agreement services that are not being billed separately). If a billing schedule exists, this amount should be 0.00.
The Billing Reduction field (below) allows you to reduce the amount remaining to bill for the agreement; however, you can also reduce the amount to bill by entering the total amount to bill in this field.
 For example, if the defaulted Total Remaining
 is 2500.00 and you want to reduce that amount by $500, enter 2,000.00 in this field and the
 system will automatically update the Billing Reduction field by the reduction
 amount (in this case, $500).
 If the defaulted Total Remaining is 0.00
 (e.g. this is an amendment that did not add additional pricing to the agreement), but you
 want to reduce the remaining amount to bill by 500.00, enter -500.00 in this field. The
 system will update the Billing Reduction field to $500.
Note: The Total Remaining amount should always equal 0.00 when a billing schedule exists. If a billing reduction results in a Total Remaining amount that is less than or greater that 0.00, you will need to adjust the billing schedule until the Total Remaining equals 0.00.

## Service Site

Service Site field in SM Agreements, Spot Coverage tab.
Enter the service site to cover under this agreement for spot work. Must be a valid service site for the customer specified on the agreement.

## Coverage Level

Coverage Level field in SM Agreements, Spot Coverage tab.
Display only, the coverage level for the selected service site. Initially defaults as None. Once you enter coverage details in the SM Agreement Site Coverage Dtl form, the system updates this field to Coverage.

## Service

Service field on the Posted Detail tab of the SM Agreements form.
This field indicates the number associated with the service that was performed for the posted revenue.

## Source Co

Source Co field on the Posted Detail tab of the SM Agreements form.
This field indicates the source company for the posted revenue.

## Post Month

Post Month field on the Posted Detail tab of the SM Agreements form.
This field indicates the month the revenue for this particular service was posted.

## Batch Id

Batch ID field on the Posted Detail tab of the SM Agreements form.
This field indicates the batch ID for the posted revenue.

## Source

Source field on the Posted Detail tab of the SM Agreements form.
This field indicates the source of the posted revenue (SM Invoice or SM Amortize).

## Transaction Type

Transaction Type field on the Posted Detail tab of the SM Agreements form.
This field indicates the transaction type for the posted revenue.

## GLCo

GLCo field on the Posted Detail tab of the SM Agreements form.
This field indicates the general ledger company for the posted revenue.

## GL Account

GL Account field on the Posted Detail tab of the SM Agreements form.
This field indicates the general ledger account for the posted revenue.

## Deferred

Deferred flag on the Posted Detail tab of the SM Agreements form.
This flag is checked when the account is the deferred revenue account from the Deferred Revenue field of the SM Departments form.

## Debit

Debit field on the Posted Detail tab of the SM Agreements form.
A debit amount appears in this field if the posted revenue detail is a debit for this particular service.

## Credit

Credit field on the Posted Detail tab of the SM Agreements form.
A debit amount appears in this field if the posted revenue detail is a credit for this particular service.

## Revision Notes

The Revision Notes tab on the SM Agreements form.
Use this tab to enter miscellaneous notes about the selected agreement revision. The space allowance is virtually unlimited.
Notes added for a revision are specific to that revision only, meaning you can only see them when you have selected that revision. However, if notes exist for an active revision and you create an amendment, the notes are copied to the new (amendment) revision. Any further updates to notes for either revision are specific to that revision.

### Add a Standard Note

Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into this field, right click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard note to copy (or select from F4 lookup) and click OK. The system inserts the selected note into the field.

### Spelling Check

You can run a spell check on any text in a form. To run a spelling check on the text in this field, click the Spelling icon on the toolbar or select Tools > Spelling .

### Attachments

You can add attachments for an agreement revision via the Revision Notes tab or the Info tab. Attachments added for a revision are specific to that revision and are not accessible from any other revision of the agreement. In addition, attachments are not copied to new revisions when creating amendments or renewals.
To add attachments for a revision, place focus in the Revision Notes tab or the Info tab and right-click on the Attachments button () and select Add Attachments. Then add your attachment and save.
