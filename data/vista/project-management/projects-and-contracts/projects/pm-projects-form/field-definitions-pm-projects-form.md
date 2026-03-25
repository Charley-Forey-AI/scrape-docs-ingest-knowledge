---
title: "Field Definitions: PM Projects Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form/field-definitions-pm-projects-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form/field-definitions-pm-projects-form"
---

# Field Definitions: PM Projects Form

The following is a list of field descriptions for the PM
 Projects form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Enter a project number or press F4 to select a project from a list of jobs. Up to 10 characters are allowed.
The length and format of the project number was set up when Vista was implemented. Typically, project codes have multiple parts to allow you to set up sub categories and sub-sub categories within a project.
For example, if you use multi-part project codes,
 you could set up a project with multiple buildings as follows:
Project:1025Industrial Park
Sub-project1025-1Building One
1025-2Building Two
Sub-sub project:1025-1-1Bldg 1, 1st floor
1025-1-2Bldg 1, 2nd floor

Note: Your project code format must be identical to your job code format.
If this is a new project, and the specified project number exists in the JCHJ (JC History by Job) table (because it was previously deleted), you will receive a message informing you that the number was previously used and cannot be reused until the contract is purged from contract/job history. You will then need to purge the contract/job history (in JC Contract Purge) before you can reuse the number.

[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)
[Set up a Contract](/en/vista/vista/project-management/projects-and-contracts/contracts/set-up-a-contract)

## Description

Enter a description of the job/project. You
 can enter up to 60 characters in this field.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Contract

 Enter the contract associated with the
 job/project or press F4 to select on from a list.
When creating a new job/project, this field
 defaults a contract number identical to the job number. You can accept the default or enter
 a new contract number.

## Department

This field is only enabled if the contract selected in the
 Contract field is not already set up in [PM Contracts
 ](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form).
Enter the department that the contract will be
 assigned to or press F4 to select a contract from a list. Since departments are assigned by
 contract item, the department specified here will be used as the default for the contract.
Departments are created and maintained using
 [JC Departments ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-departments-form).

##  Customer

 Enabled only if the specified contract is not
 already set up in PM Contracts.
 Indicate the customer (from the AR Customers)
 to which the specified contract applies, if applicable.

## Retainage %

This field is only enabled when the contract
 entered in the Contract field is a new contract.
Enter the retainage percent for this project.
 This is the default retainage percent that will be used on all contract items on the
 contract. This value can be changed later using the Default Retainage Percentage field on the
 Info tab of [PM Contracts ](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form).

## Start Month

Enabled only if the specified contract is not
 already set up in [PM Contracts
 ](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form).
Enter the starting month for this contract.
 This field initially defaults to the current month.

## T&M Template

Enabled only if the specified contract is not
 already set up in PM Contracts.
Enter the T&M Template (from JB T&M
 Template Setup) to use when billing the specified contract. Initially defaults the template
 specified in the ‘JB T&M Template’ field in JB Company Parameters.

## Project Manager

Use this field to assign a project manager to
 a project. This allows you to sort and filter jobs/projects by the project manager
 associated with it (for example in the PM Work Center).
Enter a project manager or press F4 to select
 one from a list.
Project Managers are created and maintained in
 [JC Project Managers ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-project-managers-form).
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Bid Number

 Enter the bid number for this job. The bid
 number can be up to 10 characters long.
This is an optional field that can be used to
 tie the job back to either an estimate code in Project Management, or a quote number in
 Material Sales.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Tax Code (Costs)

Enter the tax code that should be used as the
 default when posting sales or use tax to this project in AP, PO, and/or SL. Press
 F4
 to select a tax code from a list.
Tax codes are created and maintained using
 [HQ Tax Codes ](/en/vista/vista/administration/headquarters/tax-code-setup/about-the-hq-tax-codes-form).
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Base Tax On

Specify where to default the tax code from when entering job lines
 (for example when creating a PO item in PO Purchase Order Entry).

- J-Job - Default the tax code on the
 job/project (JC Jobs or PM Projects > Info tab> Tax Code
 field).

- V-Vendor - Default the vendor’s tax code
 (Tax
 Code field, AP Vendors).

- O-Vendor Override - Default the vendor's
 tax code (Tax
 Code field, AP Vendors). If there is not a tax code specified for the
 vendor, the system will use the job's tax code (Tax Code field, JC Jobs).

Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Liability Template

The liability method determines how payroll
 burden is assigned. Enter a liability template number or press F4 to select
 one from a list.
Liability templates are created and maintained
 using the [JC Liability Template](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-liability-template-form) form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Insurance Template

The insurance template is used when processing
 payroll on the job/project.
Enter an insurance template code or press
 F4
 to select one from a list.
Insurance templates are created and maintained
 using the [JC Insurance Template](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-insurance-template-form) form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  PR State

 This field is used as the default when
 posting timecards (PR Timecard Entry) that reference this project. This field is used by
 the Payroll module if you are using the job state for tax state, unemployment state, or
 insurance state (options in PR Company Parameters).
 Enter the state where the project is located
 or press F4 to select one from a list. State codes are created and maintained using
 the [HQ States](/en/vista/vista/administration/headquarters/region-setup/hq-states-form) form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Markup/Discount Rate

For use with the Inventory and Material Sales
 modules.
Enter the mark-up and/or discount rate that is
 used to calculate prices when posting materials to this project in Job Cost or Material
 Sales.
Material pricing calculations are based on the
 pricing option specified in [IN Company Parameters ](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form) ([More](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form/field-definitions-in-company-parameters-form#ID-000137cb--en)).
 Example: 6% is entered as .06.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Minimum Projection %

Enter the minimum percent complete needed to
 calculate a cost projection for this project/job. If the percent complete is below this
 minimum, the projected costs will be calculated at the higher of estimated or actual costs.
The value in this field is only used if a
 minimum percent complete is not set up on the phases ([JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) / [PM Project Phases](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)).
Projection minimum percentage is set up in
 several places

- [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form) / [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) - This value is only used if a
 projection minimum percentage has not been set up on the project/job or phases.

- [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form) / [JC Jobs](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form) - This value is only used if a projection
 minimum percentage has not been set up on the phases.

- [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) / [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) - This field defaults based on the
 projection minimum percentage set up using the JC Phases form.

- [JC Phases ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form) - This is the default value of the
 projection minimum percentage when new phases are added to a project/job.

Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Phases on This Job Are Locked

 Check this box to lock phases for this job so
 that only those phases/cost types assigned to this job (in JC Job Phases or JC Job Original
 Job Estimates) can be used when posting committed or actual costs in the Accounting
 modules. In addition, phase lookups for locked jobs (i.e. F4 at Phase) will use JCJP (Job
 Phases) rather than the JCPM (Phase Master).
Note: Project Management and JC Change Orders do not follow
 this rule.
 Leave this box unchecked to allow posting to
 any phase/cost type where the validated portion of the phase is set up in the phase master.
 Phase lookups will list all phases set up in JC Phases or provide options for both job
 phases or all phases.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Security Group

This field will only display if you have
 secured the 'bJob' datatype (in VA Data Security Setup) and checked the In Use flag for the
 ‘bJCJM’ (Job Master) table.
Specify the security group for this project.
 Users assigned to this security group will be allowed access to information about this job.
 Initially defaults the security group assigned in VA Secure Tables and Datatypes.

- It is important to note that in addition
 to the security group specified here, access to information about this project is
 automatically granted to the Default Security Group you specified in VA Data Security
 Setup. In addition, access may be granted to additional groups in VA Data Security
 Access.

- If you are also using data level
 security for contracts and you auto-add the contract for this project, the contract
 will not be assigned this security group. It will be assigned the default security
 group defined for ‘bContract’ in VA Data Security Setup.

## Compliance Groups: SL

If tracking compliance on subcontracts for
 this project/job, the compliance group that will be used as the default when entering
 subcontracts in [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form) or [SL Subcontract Entry](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form).
Enter a compliance group for the job or press
 F4
 to select one from a list. This default can be overridden when the subcontracts are being
 created.
Compliance groups are created and maintained
 using [HQ Compliance Groups ](/en/vista/vista/administration/headquarters/compliance-setup/about-the-hq-compliance-groups-form).
Click [here](/en/vista/vista/project-management/subcontracts/about-compliance-tracking-on-subcontracts-and-pos) for an overview on compliance.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Compliance Groups: PO

Enter a valid compliance group for this
 project/job or press F4 to select one from a list. This compliance group will be used as
 the default when entering purchase orders for this job in [PO Purchase Order Entry](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form) or [PM
 Purchase Orders](/en/vista/vista/project-management/materials/pm-purchase-orders-form). Default may be overridden.
Compliance groups are created and maintained
 using [HQ Compliance Groups ](/en/vista/vista/administration/headquarters/compliance-setup/about-the-hq-compliance-groups-form).
Click [here](/en/vista/vista/project-management/subcontracts/about-compliance-tracking-on-subcontracts-and-pos) for an overview on compliance.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Reviewer Groups: Invoice

Use this field to set up a default reviewer group for invoice lines that reference this job in [AP Unapproved Invoice Entry](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form).
For example if you create a subcontract for this job in the SL module, and then add it to a claim and send it to the AP Unapproved Invoice Entry process (using the [SL claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims) process), the invoice line items will default with this reviewer group.
 Press F4 in this field to select an active reviewer group from a list.
Reviewer groups are created and maintained using the [HQ Reviewer Groups.](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form)
Press F5 in this field to access HQ Reviewers.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

[PM Projects Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)
[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)

## Reviewer Groups: Timesheet

If you are using [timesheet entry functionality](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-timesheets), enter the timesheet reviewer
 group for this project. Press F4 for a list of active timesheet
 reviewer groups. Press F5 to access HQ Reviewer Groups.
Members of this group will review and approve timesheets that are entered for this project using PR My Timesheet Approval.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Job Phone

Enter the phone number of the project/job.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Job Fax

 Enter the fax number to use for this project.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Mail Address

Enter the mailing address for this
 job/project. The address can be up to 60 characters long.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Mail City

 Enter the city for this job/project.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Mail State

Use this field to enter the state of the
 mailing address. If the state is not in the company country (HQ Company Setup > Info tab >  Default
 Country field, you need to select a country in the Mail Country
 field.
 Enter a state or press F4 to select a
 state from a list.
States are created and maintained using the
 [HQ States ](/en/vista/vista/administration/headquarters/region-setup/hq-states-form) form.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Mail Zip

Enter the zip code for this project/job.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Mail Country

Use this field to enter the country of the
 address. This field is only necessary if the address is outside of the default country on
 the company (HQ Company Setup > Info tab > Default
 Country field).
Enter the country code for this job/project or
 press F4 to select one from a list. The selected country must be associated with
 the selected Mail
 State.
Country codes are created and maintained using the [ HQ Countries ](/en/vista/vista/administration/headquarters/region-setup/create-country-codes) form.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Mail Add'l Address

Use this field to enter additional address
 information for this job. For example, if your place of business receives its mail at a
 P.O. Box, then you might enter the P.O. Box in the Mail Address field above, and use this
 field to enter the street address.
The address information entered here is not
 used by any of the posting programs, but may be used on certain reports.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Ship Address

Enter the shipping address for this project/job. The shipping address can be up to 60 characters long.
This address is used as the shipping address on purchase orders unless overridden.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Ship City

Enter the shipping city for the project/job.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Ship State

Use this field to enter the state of the
 shipping address. If the state is not in the company country (HQ Company Setup > Info tab > Default
 Country field, you need to select a country in the Ship Country
 field.
Enter a state or press F4to select a
 state from a list.
States are created and maintained using the
 [HQ States ](/en/vista/vista/administration/headquarters/region-setup/hq-states-form) form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Ship Zip

Enter the zip code of the shipping
 address.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Ship Country

Use this field to enter the country of the
 shipping address. This field is only necessary if the address is outside of the default
 country on the company (HQ Company Setup > Info tab > Default
 Country field).
Enter a country code or press F4 to select
 one from a list. The selected country must be associated with the selected Ship State.
Country codes are created and maintained using
 the [ HQ Countries ](/en/vista/vista/administration/headquarters/region-setup/create-country-codes) form.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Ship Add'l Address

Use this field to enter additional shipping
 address information for this job. For example, if your mailing address is a P.O. Box (which
 often cannot be used as a shipping address), then you would enter the street address in the
 Ship Address field above, and use this field to enter the P.O. Box.
The address information entered here is not
 used by any of the posting programs, but may be used on certain reports.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Price Template

Enter a price template or press F4 to select
 one from a list.
Price templates are created and maintained
 using the [MS Price Templates ](/en/vista/vista/job-resources/material-sales/quotestemplates/templates/about-the-ms-price-templates-form) form. The selected template will be
 used to default prices when entering tickets in the MS module for materials purchased for
 this job/project.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Haul Tax Option

 Specify the tax option to use for haul charges.
 0=Not Taxable. Haul charges are not taxable.
 1=Taxable Using Haul Vendor. Haul charges are only taxable when using an outside vendor to haul materials.
 2=Always Taxable. Haul charges are always taxable, regardless of whether using company vehicle or outside haul vendor.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Apply Price Escalators

This field is only applicable if you are using
 the oil price escalation/de-escalation feature (HQ/MS).
Check this box to apply price escalators (set
 up in HQ Escalation Index) to this job. When checked, the MS Oil Price Escalation report
 tracks sales of applicable materials (e.g. asphalt mixes ) to this job in MS Ticket Entry
 and determines increases/decreases in pricing based on the bid index (this job’s contract
 start date) and pricing index (monthly escalation/de-escalation). Use the MS Oil Price
 Escalation report to review the resulting pricing adjustments.
Note: If a quote exists for the job in MS Quotes
 and you have checked the Apply Price Escalators flag for the quote, the system will use
 the bid index date specified on the quote instead of the job/contract start date.

Leave this box unchecked if you are not using
 the oil price escalation/de-escalation feature or if not applying price escalators to this
 job.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

[Click here for more information about the price escalation
 feature](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-escalation-index-form).

## Update Plugged Projections Automatically with Change Order Detail

Check this box to have plugged projections
 automatically updated with change order amounts at the phase/cost type level. When new
 change orders are entered using the [PM Change Orders](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form) form, the changes will update the
 projections based on the approved month on the change order.
Leave this box unchecked if plugged
 projections should not be automatically updated with change order amounts at the phase/cost
 type level.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Hours Per Man Day

 Enter the number of hours that make up a standard 'man-day' for this job. This field defaults with a 8.00.
 This value will be used when using the 'ManDays' production option in JC Cost Projections to determine 'over/under', 'remaining' and 'final' hours.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Update Units from Accounts Payable

Check this box to update actual units and unit
 cost to JCCD (JC Cost Detail) when posting AP invoices and PO receipts (if expensing
 receipts) to this job.
Leave this box unchecked if you do not want
 actual units and unit cost updated to JCCD when posting AP invoices and PO receipts to this
 job. Instead, actual units and unit cost will be set to 0.00 in JCCD. Actuals will be
 updated when posting progress in JC.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Update Units from Material Sales

Check this box to update actual units and unit
 cost to JCCD (JC Cost Detail) when posting transactions in MS (tickets and hauler
 timesheets) to this job. Defaults as checked.
Leave this box unchecked if you do not want
 actual units and unit cost updated to JCCD when posting transactions in MS to this job.
 Instead, actual units and unit cost will be set to 0.00 in JCCD. Actuals will be updated
 when posting progress in JC.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Use Default Tax Code for Subcontracts

Check this box if subcontract items should default with the tax code set up on the project/job or vendor (depending on the Base Tax On option selected on the Info tab).
This selection impacts subcontract items that are created in the following forms:

- [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)

- [PM Subcontract Detail](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)

- [SL Subcontract Entry ](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)

- [SL Add Item](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-add-item-form) (opened using [SL Change Order Entry ](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-change-order-entry-form))
If you leave this box unchecked, no tax code will default on the subcontract items.

Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

[PM Projects Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)
[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)

## Sync to ProjectSight

The Sync to ProjectSight checkbox on the PM Projects form, Add'l Info tab.
Important: Only if you have a legacy integration with ProjectSight, use this checkbox to sync records. If you have the current integration, this checkbox is *not used at this time*. For information about syncing records with the current integration, see [ProjectSight Integration with Vista](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:vista_60033).

Select this checkbox to sync this project to ProjectSight. When selected, the system sends this project to record to ProjectSight as a project.

## Structure Type

The Structure Type field on the PM Projects form, Add'l Info tab.

For use with Trimble Analytics.
Enter the structure type for this project or press F4 to select from a list of valid structure types (set up in HQ Project Structure Types).
When reporting project data in Analytics, the system uses the structure type specified here to identify and group project data in a more accurate and meaningful manner.
For more information about Analytics, see [About Viewpoint
 Analytics.](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:Analytics_000001:Analytics:Analytics)
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Exclude from Analytics

The Exclude from Analytics checkbox on the PM Projects form, Add'l Info tab.

For use with Trimble Analytics.
Select this checkbox to exclude this project from Analytics reporting. If you assigned a structure type (in the Structure Type field), the assignment will be informational only; the system will not include this project when reporting project data in Analytics.
If this project should be included in Analytics reporting, leave this checkbox unselected.
For more information about Analytics, see [About Viewpoint
 Analytics.](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:Analytics_000001:Analytics:Analytics)
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## PR Local Code

Use this field to identify the city, county, or other taxing district in which the job/project is located.
Enter a local code or press F4 to select
 one from a list. Local codes are created and maintained using the [PR Local Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-local-codes-form) form.
 If the [Use Job or Office Local for Local Tax ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form/field-definitions-pr-company-parameters-form#ID-00035bce--en) box is checked (PR Company Parameters> State/Local tab), this code will be used as a default when posting timecards ([PR Timecard Entry ](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)) that reference this job/project.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Geographic Code

Enter the geographic code for the job/project.
 The geographical code can be up to 10 characters long.
This code is currently only used by the state
 of New York for form NYS-45-CC (PR NY Quarterly Supplemental Return report).
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Certified

 For use with the Payroll module only.
 Check this box if this job is certified and should be included on Certified Payroll reports. If checked and the ‘Certified Jobs Only?’ option for the selected Certified Payroll report is set to Y, this job will be included when printing the report. However, detail included on the report is based on how the ‘Include on Certified Reports’ option is set in PR Employees.
 Leave this box unchecked if this job is not certified. Certified Payroll reports will only include this job if the ‘Certified Jobs Only?’ option for the selected Certified Payroll report is set to N (unchecked).
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

[PM Projects Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)
[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)

##  Start Date for Certifieds

 If you are including this job on certified
 payroll reports, enter the start date for certified payrolls (should be the date labor
 actually started on this job). This date will be used to calculate the week number on the
 certified payroll reports (e.g. PR Certified Payroll Transcript, PR Certified Report with
 Liabilities, etc.). This should represent the first week ending date for the job/project.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

Date Field Shortcuts

 T or t
Set the date to the current
 date.

MMDD
Four digit month and day
Enter a four digit month and
 date (MMDD) and the system will automatically add the current year.

+
The system will automatically
 set the date to tomorrow.

+5
The system will automatically
 set the date to 5 days in the future.
You can actually enter any
 value after the +, for example you can enter +7 to set the date to next
 week.

-
The system will automatically
 set the date to the previous day.

-5
The system will automatically
 set the date to 5 days in the past.
Just like with +, you can enter
 any value after the -, for example you can enter -7 to set the date to the previous week.

## Construction Type

 Construction Type drop down in the PM Projects form, PR Info tab
Used by the Payroll module for certified reporting purposes. Only required if sub-jobs for
 this project represent different types of construction (that is, distinct wage
 determinations).
Select the type for each job. The PR Certified Export - eMars report (U.S. only, ReportID 1315) will then break out your payroll data by construction type as needed, displaying the appropriate value for each employee wage-and-hour record in the Construction Type column. This meets the requirement for projects governed by multiple wage determinations (wage schedules).
Valid types are:

- B-Building

- D-Dredging

- H-Heavy

- R-Residential

- W-Highway

Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  EEO Region

Used by the Payroll module for EEO reporting
 purposes.
Enter a code, up to 8 characters, that
 identifies the region (such as county) for this job. This field is not validated, but
 allows you to print the EEO reports by region.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  SMSA Code

Use this field to identify the SMSA area in which this job is being performed.
Enter a SMSA code or press F4 to select
 one from a list.
SMSA codes are created and maintained using the [ HQ SMSA Codes ](/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-smsa-codes-forms) form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Craft Template

Use this field to select the set of craft/class pay rates to use as
 defaults when posting timecards to the project/job.
Enter a PR template code or press F4 to select
 one from a list.
Templates are created and maintained using the
 [PR Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-templates-form) form, and crafts templates are added to the
 template using the Craft Templates tab. Click [here](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-crafts-classes-and-templates) for an overview on crafts, classes, and templates.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## PR Overtime Schedule

Use this field to select the overtime schedule
 that will be used to calculate PR overtime when timecards are posted to this
 job/project.
Enter the overtime schedule or press
 F4
 to select a schedule from a list.
Overtime schedules are created and maintained
 using the [PR Overtime Schedule](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-overtime-schedule-form) form.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Rate Template

Use this field to select the fixed rate
 template that will be used when charging labor and burden to the job/project.
Enter the fixed rate template or press
 F4
 to select one from a list.
Fixed rate templates are created and
 maintained using the [JC Fixed Rate Template](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-fixed-rate-template-form) form.
The rates set up on this template will
 override the rates defined at the employee level in PR Employees. If no template is
 assigned here, rates assigned to employees will be used. If the employee’s fixed rate is
 0.00, wages will be based on actual pay rates and burden will be based on the liability
 template assigned to the job.
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## PR Leave Level

PR Leave Level field in the PM Projects form, PR Info tab
If workers on this job should earn a specific leave rate, enter the Leave Level code here. Press F4 for the PR Leave Levels Lookup from which to select a leave level.
When you process PR Auto Leave, the system compares the following two rates and uses the highest of the two in leave accrual calculations:

- the rate set for the employee in the PR Employee Leave form, or if there is not one there, the PR Leave Codes form

- the rate associated with the leave level code (as set in the PR Leave Codes form, Leave Level Overrides tab)

If the job leave rate happens to be the highest of the two, the amount of leave accrued by the employee is also based on how much they worked on the job. Note: Job-specific Leave Level overrides affect only *accruals* . These accruals cannot override limits, nor do they impact frequencies or usage.

Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

##  Use Weighted Average Overtime Rates

The Use Weighted Average Overtime Rates checkbox on the PM Projects form, PR Info
 tab.
Select this checkbox to use weighted-average overtime rates when
 applying auto overtime to timecards posted to this job. Because this option is used in
 conjunction with the Use Weighted Average Overtime Rates option in PR Craft Classes, you
 must also check this option for each craft/class to which this job applies.
Once you select this checkbox, the Average By field is enabled, and
 you must select the weighted-average overtime calculation method (Week or Day). When the
 system applies auto overtime to timecards posted to jobs, crafts, and classes for which
 both Use Weighted Average Overtime Rates options are selected, the
 system uses a weighted-average overtime rate adjustment based on the Average By calculation
 method you selected. If both options are not selected, regular overtime rates are used.
Do not select this checkbox if you are using regular overtime rates.
For more information about weighted-average overtime rates, see [Weighted Average Overtime Rates](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/weighted-average-overtime-rates).
Note: Many of the fields on the PM Projects form are also on the JC Jobs form. When you make a change to this field on the PM Projects form, the system immediately updates the same field on the JC Jobs form.

## Average By

The Average By field on the PM Projects form, PR Info tab.
This field is only enabled when you select the Use Weighted Average Overtime Rates checkbox.
Select the option to use for calculating weighted-average auto overtime:

- Week (Default) - Calculate weighted-average overtime based on the employee's weighted-average regular rate for the weekly or bi-weekly pay period.

- Day - Calculate weighted-average overtime based on the employee's weighted-average regular rate for the day.

Note: It is suggested that the option you select here be assigned to each applicable craft/class associated with this job to ensure the correct weighted-average overtime rate is used. If you set one option to Weekly and one to Day, the systems uses the daily weighted-average rate.

## Project Our Firm

The firm selected in this field overrides the
 default set up using the Our Firm field on the Info tab of the PM
 Company Parameters. Leave this field blank if you want to use the default.
Enter the firm that is designated as 'our
 firm' for this project or press F4 to select it from a list. Firms are
 created and maintained using the [PM Firms](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form) form.
Tip: The sort name can be used instead of the firm number
 when selecting firms in PM module forms. Generally the sort name is the first several
 letters of the firm name.  For example when creating a subcontract in the [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form) form for 'Bryan Electrical', you can enter the sort name 'bryan'
 in the Vendor
 field instead of the firm number '10042'. The sort name of a firm is set up
 using the Sort
 Name field on the [PM Firms](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form) form.

## Auto-Add Contract Item and Update Contract Item Amount

Check this box to automatically create
 contract items when adding phases to a project. This will also update the contract item
 amounts with estimated costs.
When checked, the following applies:

- Total estimated costs entered for all
 phases/cost types associated with a contract item will update that contract item's
 original amount.

- If you add a phase to a project and
 specify a contract item that does not exist, it will be added automatically.
 Estimated costs entered for all phases/cost types assigned to that contract item will
 update the contract item's original amount.

- If you change the contract item for an
 existing phase and the contract item does not exist, it will be added. Any estimated
 costs already set up for the phase's cost types will automatically be updated to the
 new contract item's original amount.

- If you add, delete, or change the cost
 types for a phase, contract item amount will be updated with changes.

Leave this box unchecked if you do not allow
 auto-adding contract items when adding phases or changing the contract item for an existing
 phase, and if you do not want to automatically update original contract item amounts with
 estimated costs. Original contract item amounts must be updated manually.

## Architect/Engineer: Firm

Enter the architect/engineer firm associated
 with this project or press F4 to select it from a list.
Tip: The sort name can be used instead of the firm number
 when selecting firms in PM module forms. Generally the sort name is the first several
 letters of the firm name.  For example when creating a subcontract in the [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form) form for 'Bryan Electrical', you can enter the sort name 'bryan'
 in the Vendor
 field instead of the firm number '10042'. The sort name of a firm is set up
 using the Sort
 Name field on the [PM Firms](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form) form.
Note: Once you enter the contact for the specified
 architect/engineer (in next field) and save the record, if the firm and contact do not
 already exist for the project (in PM Project Firms), they will be added. The firm/contact
 will also default as the architect/engineer firm and contact when adding or initializing
 submittals in PM Submittals - 6.5, and will be added to the 'Available Firms and Contact'
 distribution lists in several PM processing forms.

## Architect/Engineer: Contact

Specify the contact (from the architect/engineer firm designated above) for this project.
Note: Once you enter a contact and save the record, if the
 firm and contact do not already exist for the project (in PM Project Firms), they will be
 added. The firm/contact will also default as the architect/engineer firm and contact when
 adding or initializing submittals in PM Submittals - 6.5, and will be added to the
 'Available Firms and Contact' distribution lists in several PM processing forms.

## Auto-Generate Submittal Numbers using

Specify how submittal numbers will be
 generated for this project.

- P-Project— Select this option to
 generate submittal numbers automatically based on the project. When N, New, or + is
 entered, the system generates the next sequential number based on all submittal
 documents for the project.

- T-Project and Type — Select this option
 to generate submittal numbers automatically based on the project and submittal type.
 When N, New, or + is entered, the system generates the next sequential number based
 on all submittal documents for the project having the same document type (e.g. all
 submittal documents with a document type of ‘CERT’).

Use of this feature will not affect manual
 entry of submittal numbers.

## Auto-Generate Pending Change Orders using

Specify how PCO (Pending Change Order) numbers
 will be generated for this project.

- P-Project— Select this option to
 generate PCO numbers automatically based on the project. When N, New, or + is
 entered, the system generates the next sequential number based on all PCO documents
 for the project.

- T-Project and Type — Select this option
 to generate PCO numbers automatically based on the project and PCO type. When N, New,
 or + is entered, the system generates the next sequential number based on all PCO
 documents for the project having the same document type (e.g. all PCO documents with
 a document type of ‘FO’).

Use of this feature will not affect manual
 entry of PCO numbers.

## Auto-Generate Meeting Minutes using

Specify how meeting numbers will be generated for this project.

- P-Project— Select this option to generate meeting numbers automatically based on the project. When N, New, or + is entered, the system generates the next sequential number based on all meetings for the project.

- T-Project and Type — Select this option to generate meeting numbers automatically based on the project and meeting type. When N, New, or + is entered, the system generates the next sequential number based on all meetings for the project having the same document type (e.g. all meetings with a document type of ‘OWNER’).

Use of this feature will not affect meeting minute numbers that are manually entered.

## Auto Generate Request for Information Using

Specify how RFI (Request for Information)
 numbers will be generated for this project.

- P-Project— Select this option to
 generate RFI numbers automatically based on the project. When N, New, or + is
 entered, the system generates the next sequential number based on all RFI documents
 for the project.

- T-Project and Type — Select this option
 to generate RFI numbers automatically based on the project and RFI type. When N, New,
 or + is entered, the system generates the next sequential number based on all RFI
 documents for the project having the same document type (e.g. all RFI documents with
 a document type of ‘COS’).

Use of this feature will not affect manual
 entry of RFI numbers.

## Auto-Generate Request for Quote using

Specify how RFQ (Request for Quote) numbers
 will be generated for this project.

- C-Project, PCO Type, PCO — Select this
 option to generate RFQ number based on the project, PCO type, and PCO. When ‘+’ is
 entered, the system generates the next sequential number based on all RFQs for the
 project having the same PCO type and PCO number (e.g. all RFQ documents with a PCO
 Type of ‘FIELD’ and PCO number ‘100’).

- P-Project— Select this option to
 generate RFQ numbers automatically based on the project. When ‘+’ is entered, the
 system generates the next sequential number based on all RFQ documents for the
 project.

- T-Project and PCO Type — Select this
 option to generate RFQ numbers automatically based on the project and PCO type. When
 ‘+’ is entered, the system generates the next sequential number based on all RFQs for
 the project having the same PCO type (e.g. all RFQ documents with a PCO type of
 ‘FIELD’).

Use of this feature will not affect manual
 entry of RFQ numbers; however, manual entries will be considered when auto-generating RFQ
 numbers. For example, if the last number generated by the system was ‘10’, and you then
 manually entered an RFQ of ‘500’, the next number generated by the system would be ‘501’.


## Default Standard Days Due

If you are using the [Create and Send ](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature in PM, you can use the Default Standard Days Due field on the PM Info tab to designate a default number of days until due for documents created in PM.
Default Standard Days Due – This option applies to [PM Other Documents ](/en/vista/vista/project-management/issuessubmittalsother-documents/other-documents/pm-other-documents-form), [PM Request For Quote ](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview/pm-request-for-quote---6.6-form), [PM Submittals - 6.5 ](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittals---6.5-form), and [PM Transmittals ](/en/vista/vista/project-management/issuessubmittalsother-documents/transmittals/about-the-pm-transmittals-form) and is used to calculate default due dates as follows:

- PM Other Documents (Header) –Calculates the Date Due Back based on the Date Sent

- PM Request For Quote (Distribution grid) – Calculates the Date Req'd based on the Date Sent

- PM Submittals - 6.5 – Calculates the Date Due (from arch/eng) based on the To Arch/Eng date.

- PM Transmittals (Header) – Calculates the Required Return Date based on the Date Sent

- Default Request for Information Days Due – this option applies to RFI's.

- PM Request For Information (Header) – Calculates the Date Due based on the Date

Example: If the Default Days Due is 10 and you are creating a Letter of Transmittal document with a Date Sent of 07/15/12, the calculated Required Return Date will be 07/25/12.

## Default Request for Information Days Due

Enter the default 'number of days until due' that should be used on when creating RFIs. The value in this field only determines the default due back date, which can be changed when the RFI is created.
When RFIs are created in [PM Request For Information](/en/vista/vista/project-management/issuessubmittalsother-documents/rfis/about-the-pm-request-for-information-form), the Due Back field will calculate using the following formula:
Date Sent + Default RFI Days Due = Due Back
For example, if the Default Days Due is 10 and the Date Sent is 11/15/11, the calculated Date Due will be 11/25/11.

[PM Projects Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)
[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)

## Approving Firm / Approving Firm Contact

Use these fields to enter a default approving firm and contact for
 submittals and submittal packages.

- When a new submittal package is created using the [PM Submittal
 Package](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-package-form) form, the default approving firm and contact will populate in the
 Approving Firm and Approving Contact fields in the upper portion of
 the form.

- When a new submittal revision is created using the [PM
 Submittal Register](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-register-form) form, the default approving firm and contact will populate in
 the Approving Firm and Approving Firm Contact fields on the form.

- When importing submittals in [IM Import ](/en/vista/vista/administration/imports/processing/about-the-im-import-form)using an
 import template where PMSubmittalRegisterGrid is selected in the Import Form field ([IM Template ](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form)), the
 approving firm and contact will populate on the imported submittals.

Click [here](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-submittals) for an
 overview of the submittals process.

Related concepts

- [PM Projects Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)

- [About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)

## Submittal Days for Review Responsible Firm / Approving Firm / Requesting Firm

Use these fields to set the default number of review days for each party that is involved in the submittal process. This allows you to set the default submittal schedule.
When creating a new project, these fields will populate with the values entered in the submittal days for review fields on the Info tab of the
[PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)
form.
Click
[here](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-submittals)
for an overview on submittal schedules.

[PM Projects Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)
[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)

## Auto Calculate Submittal Due Dates

Check this box if the submittal schedule set up on the project should automatically populate on a submittal when an activity date is entered. This applies to submittals in the [PM Submittal Register](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-register-form) form, and the lower portion of the [PM Submittal Package](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-package-form) form.
By default this box is checked when a new project is created.
Click [here](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-submittals) for an overview on submittal schedules.

[PM Projects Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)
[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)

## Seq

Enter the sequence number (0-255) for this
 reviewer. If left blank, defaults as sequence '1'.
For unapproved invoices only, if you are using
 a hierarchical method of invoice approval, this sequence number should represent the order
 in which this reviewer is to review and approve invoices associated with this project.
For example, if this reviewer must approve an
 invoice/invoice line before anyone else, enter the Seq as '1'. Reviewers with sequences
 greater than '1' (e.g. 2, 3, etc.) will be unable to review and approve an invoice/invoice
 line until this reviewer has marked it as approved. If not using a hierarchical method, all
 reviewers can be assigned Seq '1'.
Note: If the reviewer is authorized to review and approve
 both unapproved invoices and purchase requisitions, assign the sequence number based on the
 numbering system designated for unapproved invoices.

##  Reviewer

 Specify the reviewer (from HQ Reviewers)
 authorized to review unapproved invoices and/or requisitions (as designated by the
 'reviewer type' specified to the right) associated with this project. Reviewer's name
 displays to the right of this field.
Press F4 in the Reviewer field
 for a list of active reviewers.
Press F5 in the Reviewer field
 to access HQ Reviewers.

## Reviewer Type

Specify the reviewer type.

- Invoice – Select this option if this
 reviewer is authorized to review and approve (or reject) unapproved invoices
 associated with this project/job. Reviewer will be assigned automatically to all
 'job' lines on unapproved invoices that reference this project/job (in AP Unapproved
 Invoice Entry).

- Purchase – Select this option if this
 reviewer is authorized to review and approve (or reject) purchase requisitions
 associated with this project. Reviewer will be assigned automatically to all 'job'
 lines on requisitions (created via PM Material Detail) that reference this project.


- Both – Select this option if this
 reviewer is authorized to review and approve (or reject) unapproved invoices and
 purchase requisitions. Reviewer will automatically be assigned to any 'job' lines on
 unapproved invoices or requisitions that reference this job.

## Optional Reviewer

The Optional Reviewer checkbox on the PM Projects form, Reviewers tab.
Select this checkbox to designate this reviewer as optional for all invoice lines to which this reviewer is assigned. This allows for one of multiple optional reviewers to approve invoice lines with a given approval sequence. Changing this setting here does not affect existing invoices; changes only affect invoices created after the change.
As long as more than one optional reviewer is assigned to each invoice line’s approval sequence, only one reviewer must review and approve in order for the approval process to advance. However, if the only reviewer on an invoice line’s approval sequence is an Optional Reviewer, their approval becomes required in order for the approval process to advance.
Setting ALL reviewers on a sequence as optional does not eliminate the approval requirement for that sequence. If an invoice line’s approval sequence contains multiple reviewers, the following rules apply to allow the approval process to advance.

- if ALL reviewers on a sequence are set as optional, at least one must approve

- if ALL reviewers on a sequence are set as non-optional (Optional Reviewer checkbox is not selected), all must approve

- if some reviewers on a sequence are set as non-optional and some as optional, all non-optional must approve

##  Memo

Use this field to enter miscellaneous notes or
 information about this reviewer, up to 255 characters.

##  Cost Type

Initially defaults all cost types available on
 the system. Cost Types may be added/deleted as desired.
To delete a cost type, highlight the cost type
 and press Delete (keyboard or toolbar). To add a cost type, enter the cost type number or
 abbreviation.

## Markup %

For each applicable cost type, specify the
 markup rate that will be used to mark up costs on change orders created for this project
 (PM Change Orders), up to four decimal points.

## Round to Nearest Whole Dollar

Select this checkbox to round this add-on to
 the nearest dollar when calculating change orders.
Do not select this checkbox if not rounding this add-on to the nearest dollar when
 calculating change orders.

## Job Role

 Use this field to select a role. Press
 F4
 to select one from a list. Click [here](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow) for more information about how roles work in the Process Workflow
 feature.
Roles are created and maintained using the
 [HQ Roles](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) form. You can launch this form by pressing
 F5
 in this field.

## User Name

 Use this field to select a user account. You
 can only select a user that is associated with the role selected in the Role field.
Roles are created and maintained using the HQ
 Roles form, and users are associated with roles using either of the following forms:

- Users tab on the [HQ Roles](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) form - You can access this form by pressing
 F5 in the Job
 Role field.

- Roles tab on the [VA User Profile ](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form) form - You can access this form by
 pressing F5 in the User Name field.

Click [here](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow) for an overview on the Process Workflow feature.

## Lead

Check this box if the user is the lead at the
 selected role.
Currently the selection in this box has no
 affect on how which workflow is applied. This box is informational only.
Click [here](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow) for an overview on the Process Workflow feature.

## Active

Check this box if the selected role and user should be used when the system is calculating the workflow to apply to a PO.
The system will only use this user/role if this box is checked.
Click [here](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow) for an overview on the Process Workflow feature.

## Notes

Use this field to enter notes on the role/user.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field, right click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard note to copy (or select from F4 lookup) and click OK. The system inserts the selected note into the field.
Click [here](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow) for an overview on the Process Workflow feature.

[PM Projects Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)
[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)

## Document Type

The Document Type field on PM Projects form, Workflow tab.
 Select the type of document to which the workflow applies.

- PO - Purchase Order

- SL - Subcontracts

Note: You can have only one process for each document type.

Note: The workflows defined here override those defined in PM Company Parameters or HQ Company Setup.

For more information about the Workflow Process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

## Process

The Process field on the PM Projects form, Workflow tab.
Enter the workflow process to perform for the specified document type or press F4 to select from a list of valid workflows. Valid workflows are those that are associated with the same document type specified in the Document Type field or those that do not specify a document type.Note: When you create a workflow (in [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)), you will generally assign it to a specific document type (Purchase Order or Subcontract). However, you may have generic workflows that are not associated with a specific document type (that is, the Document Type field is blank). In this case, you may assign it to either or both document types on this tab.

Note: The workflows defined here override those defined in PM Company Parameters or HQ Company Setup.

## Active

The Active checkbox on the PM Projects form, Workflow tab.

Select this checkbox if this workflow should be applied when new POs or Subcontracts (depending on the document type) are created.
For more information about the workflow process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

## Notes

The Notes field on the PM Projects form, Workflow tab.
Enter any notes about the workflow.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.
