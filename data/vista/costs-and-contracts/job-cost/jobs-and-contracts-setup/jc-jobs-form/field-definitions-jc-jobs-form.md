---
title: "Field Definitions: JC Jobs Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form/field-definitions-jc-jobs-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form/field-definitions-jc-jobs-form"
---

# Field Definitions: JC Jobs Form

The following is a list of field descriptions for the JC Jobs
 form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Job

Use
 this field to assign a unique job number.
Job Code Length and Format
The length and format of your job codes is set up when your system is installed. Job codes generally have multiple parts separated by dashes to allow sub jobs and sub-sub jobs to be set up within a job. For example, a project with multiple buildings could be set up as follows:
Job:
1025
Industrial Park

Sub-job:
1025-1
Building one

1025-2
Building two

Sub-sub-job:
1025-1-1
Bldg 1, 1st floor

1025-1-2
Bldg 1, 2nd floor

Note: Once established, the format of job codes must not be changed. Job number previously used error message
You cannot enter a job number that exists in the JC History by Job table. For example if you purged a contract/job but not the contract/job history, you will receive an error message when trying to create a new job using that number.
To fix this issue, use the [JC Contract Purge ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-contract-purge-form) form to purge the contract/job history. You will also need to make sure all related AP, PO, and SL detail is purged for the contract/job using the purge programs in the AP, PO, and SL modules.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Description

Enter
 a description of the job/project. You can enter up to 60 characters in this field.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Contract

 Enter the contract associated with the job/project
 or press F4 to select on from a list.
When creating a new job/project, this field defaults a contract number identical to the job number. You can accept the default or enter a new contract number.
Changing the contract assigned to a job
The contract assigned to a job can be changed, as long as there is no existing change order detail in JC or PM. All records in the [JC Job Phases ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) form will automatically be updated with the new contract. If the contract item to which a phase is linked does not exist on the new contract, the phase will be assigned to the first contract item on file for the contract. Incorrect links can be edited in JC Job Phases.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Department

Enter a department for the selected contract or press F4 to select one from
 a list.
Note: This field is only enabled if you entered a contract
 in the Contract field that is not set up in [JC Contracts ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form).
The department defines which GL accounts will be used when posting contract revenue and job costs, and it can be set up on each contract item using the [JC Contract Items ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form) form. The department selected in this field will be used as the default department when creating new items on the contract.
Departments are created and maintained using
 the [JC Departments ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-departments-form) form. You can open this form by pressing F5 in this field.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Customer

Use this field to select the customer that applies to the contract. Enter a
 customer from [
 AR Customers ](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)or press F4 to select one from a list.
 This field is only enabled if the contract
 selected in the Contract  field is not set up in [JC Contracts ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form).

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Retainage %

 Enabled only if the specified contract is not already set up in JC
 Contracts.
 Enter the retainage percent for this job.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Start Month

 This field is only enabled if the specified contract is not already set up
 in JC Contracts.
 Enter the starting month of the contract.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## T&M Template

The T&M Template field on the JC Jobs form, Info tab.

Enabled only if the specified contract is not already set up in JC
 Contracts.
Enter the T&M Template (from JB T&M Template Setup) to use when billing the specified contract.
 Initially defaults the template specified in the JB T&M Template field in JB Company Parameters, if one is designated. Otherwise, defaults as blank.

## Project Manager

Use
 this field to assign a project manager to a project. This allows you to sort and filter
 jobs/projects by the project manager associated with it (for example in the PM Work
 Center).
Enter a project manager or press F4 to select
 one from a list.
Project Managers are created and maintained in [JC Project Managers ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-project-managers-form).
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Bid Number

 Enter the bid number for this job. The bid number
 can be up to 10 characters long.
This is an optional field that can be used to tie the job back to either an estimate code in Project Management, or a quote number in Material Sales.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Tax Code (Costs)

The Tax Code (Costs) field on the JC Jobs form, Info tab.

Enter the tax code to use as the default when posting sales or use tax to this project in AP, PO, SL, and/or SM. Press F4 to select a tax code from a list.
Tax codes are created and maintained using HQ Tax Codes.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

## Base Tax On

Specify where to default the tax code from when entering job lines
 (for example when creating a PO item in PO Purchase Order Entry).

- J-Job - Default the tax code on the job/project
 (Tax
 Code field in either the JC Jobs or PM Projects form).

- V-Vendor - Default the vendor’s tax code (Tax Code
 field, AP Vendors).

- O-Vendor Override - Default the vendor's tax code
 (Tax
 Code field, AP Vendors). If there is not a tax code specified for the
 vendor, the system will use the job's tax code (Tax Code field, JC Jobs).
A change will also update PM Projects
Many of the fields on the JC Jobs form are also on
 the [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form) form.
Any change to this field on the JC Jobs form will
 also immediately update the same field on the PM Projects form.

Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Liability Template

The
 liability method determines how payroll burden is assigned. Enter a liability template
 number or press F4 to select one from a list.
Liability templates are created and maintained using the [JC Liability Template](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-liability-template-form) form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Insurance Template

The
 insurance template is used when processing payroll on the job/project.
Enter an insurance template code or press
 F4
 to select one from a list.
Insurance templates are created and maintained using the [JC Insurance Template](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-insurance-template-form) form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  PR State

 This field is used as the default when posting
 timecards (PR Timecard Entry) that reference this project. This field is used by the
 Payroll module if you are using the job state for tax state, unemployment state, or
 insurance state (options in PR Company Parameters).
 Enter the state where the project is located
 or press F4 to select one from a list. State codes are created and maintained using
 the [HQ States](/en/vista/vista/administration/headquarters/region-setup/hq-states-form) form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Job Status

 Display only, the current status of this job (should
 match the status of the associated contract).

- 1-Open. This status is automatically applied to all new jobs.

- 2-Soft Close. Posting is restricted, but closing GL entries have not been made. This status is automatically applied when the contract is Soft-Closed in the JC Contract Close program.

- 3-Hard Close. This status is automatically applied when the contract is Final Closed in the JC Contract Close program.

Click [here](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/close-a-contract) for information about closing a contract/job.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/close-a-contract)Close a contract/job
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Markup/Disc Rate

For
 use with the Inventory and Material Sales modules.
Enter the mark-up and/or discount rate that is used to calculate prices when posting materials to this project in Job Cost or Material Sales.
Material pricing calculations are based on the pricing option specified in [IN Company Parameters ](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form) ([More](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form/field-definitions-in-company-parameters-form#ID-000137cb--en)).
 Example: 6% is entered as .06.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Minimum Projection %

Enter the minimum percent complete needed to
 calculate a cost projection for this project/job. If the percent complete is below this
 minimum, the projected costs will be calculated at the higher of estimated or actual costs.
The value in this field is only used if a minimum percent complete is not set up on the phases ([JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) / [PM Project Phases](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)).
Projection minimum percentage is set up in several places

- [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form) / [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) - This value is only used if a
 projection minimum percentage has not been set up on the project/job or phases.

- [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form) / [JC Jobs](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)
 - This value is only used if a projection minimum percentage has not been set up on
 the phases.

- [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) / [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) - This field defaults based on the
 projection minimum percentage set up using the JC Phases form.

- [JC Phases ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form) - This is the default value of the
 projection minimum percentage when new phases are added to a project/job.

Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)PM Cost Projections -
 Overview

##  Phases on This Job Are Locked

The Phases on This Job Are Locked checkbox in JC Jobs, Info tab.

Select this checkbox to lock phases for this job so that
 only those phases/cost types assigned to the job (in JC Job Phases or JC Job Original Job
 Estimates) can be used when posting committed or actual costs in the Accounting modules. In
 addition, phase F4 lookups for locked jobs will include only phases set up in JC Job Phases (JCJP), rather than phases set up in JC Phases (JCPM).
Note: Project Management and JC Change Orders do not follow this rule.
 Leave this box unselected to allow posting to
 any phase/cost type where the validated portion of the phase is set up in JC Phases. Phase lookups will list all phases set up in JC Phases or provide options for both job
 phases or all phases.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

## Compliance Groups: SL

If
 tracking compliance on subcontracts for this project/job, the compliance group that will be
 used as the default when entering subcontracts in [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form) or [SL Subcontract Entry](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form).
Enter a compliance group for the job or press
 F4
 to select one from a list. This default can be overridden when the subcontracts are being
 created.
Compliance groups are created and maintained using [HQ Compliance Groups ](/en/vista/vista/administration/headquarters/compliance-setup/about-the-hq-compliance-groups-form).
Click [here](/en/vista/vista/project-management/subcontracts/about-compliance-tracking-on-subcontracts-and-pos) for an overview on compliance.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Compliance Groups: PO

Enter
 a valid compliance group for this project/job or press F4 to select one from a list. This
 compliance group will be used as the default when entering purchase orders for this job in
 [PO Purchase Order Entry](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form) or [PM Purchase Orders](/en/vista/vista/project-management/materials/pm-purchase-orders-form). Default may be overridden.
Compliance groups are created and maintained using [HQ Compliance Groups ](/en/vista/vista/administration/headquarters/compliance-setup/about-the-hq-compliance-groups-form).
Click [here](/en/vista/vista/project-management/subcontracts/about-compliance-tracking-on-subcontracts-and-pos) for an overview on compliance.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Reviewer Groups: Invoices

Use
 this field to set up a default reviewer group for invoice lines that reference this job in
 [AP Unapproved Invoice Entry ](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form).
For example, if you create a subcontract for this job in the SL module, and then add it to a claim and send it to the AP Unapproved Invoice Entry process (using the [SL claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims) process), the invoice line items will default with this reviewer group.
 Press F4 in this field to select an active
 reviewer group from a list. Reviewer groups are created and maintained using the [HQ Reviewer Groups.](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form) If you need to manage reviewer groups,
 press F5 to go to the HQ Reviewer Group form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Reviewer Groups: Timesheet

If you
 are using [timesheet entry functionality](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-timesheets), enter the timesheet reviewer
 group for this project. Press F4 for a list of active timesheet
 reviewer groups.
Members of this group will review and approve
 timesheets that are entered for this project using PR My Timesheet Approval. If you need to
 manage reviewer groups, press F5 to go to the HQ Reviewer Group
 form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Structure Type

The Structure Type field on the JC Jobs form, Info tab.

For use with Trimble Analytics.
Enter the structure type for this job or press F4 to select from a list of valid structure types (set up in HQ Project Structure Types).
When reporting project data in Analytics, the system uses the structure type specified here to identify and group project data in a more accurate and meaningful manner.
For more information about Analytics, see [About Viewpoint
 Analytics.](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:Analytics_000001:Analytics:Analytics)
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

## Exclude from Analytics

The Exclude from Analytics checkbox on the JC Jobs form, Info tab.

For use with Trimble Analytics.
Select this checkbox to exclude this job from Analytics reporting. If you assigned a structure type (in the Structure Type field), the assignment will be informational only; the system will not include this job when reporting project data in Analytics.
If this job should be included in Analytics reporting, leave this checkbox unselected.
For more information about Analytics, see [About Viewpoint
 Analytics.](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:Analytics_000001:Analytics:Analytics)
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

## Security Grp

This
 field will only display if you have secured the 'bJob' datatype (in VA Data Security Setup)
 and checked the In Use flag for JCJM (Job Master).
Specify the security group for this job. Users assigned to this security group will be allowed access to information about this job. Initially defaults the security group assigned in VA Data Security Setup.

- It is important to note that in addition to the security group specified here, access to information about this project is automatically granted to the Default Security Group you specified in VA Data Security Setup. In addition, access may be granted to additional groups in VA Data Security Access.

- If you are also using data level security for contracts and you auto-add the contract for this project, the contract will not be assigned this security group. It will be assigned the default security group defined for ‘bContract’ in VA Data Security Setup.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Job Phone

 Enter
 the phone number of the project/job.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Job Fax

 Enter the
 fax number to use for this project.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Mail Address

Enter
 the mailing address for this job/project. The address can be up to 60 characters long.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.

Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Mail City

 Enter
 the city for this job/project.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Mail State

Use
 this field to enter the state of the mailing address. If the state is not in the company
 country (HQ Company Setup form,  Default Country field), you need to
 select a country in the Mail Country field.
 Enter a state or press F4 to select a
 state from a list.
States are created and maintained using the [HQ States ](/en/vista/vista/administration/headquarters/region-setup/hq-states-form) form.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Mail Zip Code

Enter
 the zip code for this project/job.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Mail Country

Use
 this field to enter the country of the address. This field is only necessary if the address
 is outside of the default country on the company (HQ Company Setup form, Default Country
 field).
Enter the country code for this job/project or
 press F4 to select one from a list. The selected country must be associated with
 the selected Mail
 State.
Country codes are created and maintained using the [ HQ Countries ](/en/vista/vista/administration/headquarters/region-setup/create-country-codes) form.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Mail: Additional Address

 Use this field to enter additional address
 information for this job. For example, if your place of business receives its mail at a
 P.O. Box, then you might enter the P.O. Box in the Mail Address field above, and use this
 field to enter the street address.
 The address information entered here is not used by any of the posting programs, but may be used on certain reports.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Ship Address

Enter
 the shipping address for this project/job. The shipping address can be up to 60 characters
 long.
This address is used as the shipping address on purchase orders unless overridden.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Ship City

Enter
 the shipping city for the project/job.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Ship State

Use
 this field to enter the state of the shipping address. If the state is not in the company
 country (HQ Company Setup form,  Default Country field), you need to
 select a country in the Ship Country field.
 Enter a state or press F4 to select a
 state from a list.
States are created and maintained using the [HQ States ](/en/vista/vista/administration/headquarters/region-setup/hq-states-form) form.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Ship Zip

Enter
 the zip code of the shipping address.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Ship Country

Use
 this field to enter the country of the shipping address. This field is only necessary if
 the address is outside of the default country on the company (HQ Company Setup form,
 Default
 Country field).
Enter a country code or press F4 to select
 one from a list. The selected country must be associated with the selected Ship State.
Country codes are created and maintained using the [ HQ Countries ](/en/vista/vista/administration/headquarters/region-setup/create-country-codes) form.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Ship: Additional Address

 Use
 this field to enter additional shipping address information for this job. For example, if
 your mailing address is a P.O. Box (which often cannot be used as a shipping address), then
 you would enter the street address in the Ship Address field above, and use this field to
 enter the P.O. Box.
 The address information entered here is not used by any of the posting programs, but may be used on certain reports.
If you have Internet access, you can select the Map button ( ) to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses theDefault Country defined in the HQ Company Setup form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Price Template

Enter
 a price template or press F4 to select one from a list.
Price templates are created and maintained using the [MS Price Templates ](/en/vista/vista/job-resources/material-sales/quotestemplates/templates/about-the-ms-price-templates-form) form. The selected template will be used to default prices when entering tickets in the MS module for materials purchased for this job/project.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Haul Tax Option

 Specify
 the tax option to use for haul charges.
 0=Not Taxable. Haul charges are not taxable.
 1=Taxable Using Haul Vendor. Haul charges are only taxable when using an outside vendor to haul materials.
 2=Always Taxable. Haul charges are always taxable, regardless of whether using company vehicle or outside haul vendor.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Apply Price Escalators

This field is only applicable if you are
 using the oil price escalation/de-escalation feature (HQ/MS).
Check this box to apply price escalators (set up in HQ Escalation Index) to this job. When checked, the MS Oil Price Escalation report tracks sales of applicable materials (e.g. asphalt mixes ) to this job in MS Ticket Entry and determines increases/decreases in pricing based on the bid index (this job’s contract start date) and pricing index (monthly escalation/de-escalation). Use the MS Oil Price Escalation report to review the resulting pricing adjustments.
Note: If you select this checkbox and quote exists for the
 job (in MS Quotes) that is set to use price escalators, the system overrides the quote's
 Bid Index Date and uses the Contract Start Month. The quote's Bid Index Date is only used
 if you do not select the Apply Price Escalator checkbox for the
 job.
Leave this checkbox unselected if you are not
 using the oil price escalation/de-escalation feature or if not applying price escalators to
 this job.
[Click here for more information about the price escalation feature](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-escalation-index-form).
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Hours Per Man Day

 Enter the
 number of hours that make up a standard 'man-day' for this job. This field defaults with
 a 8.00.
 This value will be used when using the 'ManDays' production option in JC Cost Projections to determine 'over/under', 'remaining' and 'final' hours.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Update Plugged Projections Automatically

Check
 this box to have plugged projections automatically updated with change order amounts at the
 phase/cost type level. When new change orders are entered using the [JC Change Orders ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form) form, the changes will update the
 projections based on the approved month on the change order.
Leave this box unchecked if plugged projections should not be automatically updated with change order amounts at the phase/cost type level.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Auto-Add Contract Item and Update Contract Item Amount

Check
 this box to automatically add contract items when adding phases to a job and to update
 contract item amounts with estimated costs. When checked, the following applies:

- Total estimated costs entered for all phases/cost types associated with a contract item will update that contract item's original amount.

- If you add a phase to a job and specify a contract item that does not exist, it will be added automatically. Estimated costs entered for all phases/cost types assigned to that contract item will update the contract item's original amount.

- If you change the contract item for an existing phase and the contract item does not exist, it will be added. Any estimated costs already set up for the phase's cost types will automatically be updated to the new contract item's original amount.

- If you add, delete, or change the cost types for a phase, contract item amount will be updated with changes.

Leave this box unchecked if you do not allow auto-adding contract items when adding phases or changing the contract item for an existing phase, and if you do not want to automatically update original contract item amounts with estimated costs. Original contract item amounts must be updated manually.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Update Units From Accounts Payable

Check
 this box to update actual units and unit cost to JCCD (JC Cost Detail) when posting AP
 invoices and PO receipts (if expensing receipts) to this job.
Leave this box unchecked if you do not want actual units and unit cost updated to JCCD when posting AP invoices and PO receipts to this job. Instead, actual units and unit cost will be set to 0.00 in JCCD. Actuals will be updated when posting progress in JC.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Update Units From Material Sales

 Check this box to update actual units and unit cost
 to JCCD (JC Cost Detail) when posting transactions in MS (tickets and hauler timesheets) to
 this job. Defaults as checked.
 Leave this box unchecked if you do not want actual units and unit cost updated to JCCD when posting transactions in MS to this job. Instead, actual units and unit cost will be set to 0.00 in JCCD. Actuals will be updated when posting progress in JC.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Use Default Tax Code for Subcontracts

Check
 this box if subcontract items should default with the tax code set up on the project/job or
 vendor (depending on the Base Tax On option selected on the Info
 tab).
This selection impacts subcontract items that are created in the following forms:

- [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)

- [PM Subcontract Detail](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)

- [SL Subcontract Entry ](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)

- [SL Add Item](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-add-item-form) (opened using [SL Change Order Entry ](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-change-order-entry-form))
If you leave this box unchecked, no tax code will default on the subcontract items.

Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form) JC Jobs

## Sync to ProjectSight

The Sync to ProjectSight checkbox on the JC Jobs form, Add'l Info tab.
Important: Only if you have a legacy integration with ProjectSight, use this checkbox to sync records. If you have the current integration, this checkbox is *not used at this time*. For information about syncing records with the current integration, see [ProjectSight Integration with Vista](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:vista_60033).

Select this checkbox to sync this job to ProjectSight. When selected, the system sends the job record to ProjectSight as a project.

##  PR Local Code

Use
 this field to identify the city, county, or other taxing district in which the job/project
 is located.
Enter a local code or press F4 to select
 one from a list. Local codes are created and maintained using the [PR Local Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-local-codes-form) form.
 If the [Use Job or Office Local for Local Tax ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form/field-definitions-pr-company-parameters-form#ID-00035bce--en) box is checked (PR Company Parameters> State/Local tab), this code will be used as a default when posting timecards ([PR Timecard Entry ](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)) that reference this job/project.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Geographic Code

Enter
 the geographic code for the job/project. The geographical code can be up to 10 characters
 long.
This code is currently only used by the state of New York for form NYS-45-CC (PR NY Quarterly Supplemental Return report).
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Certified Payroll

 For
 use with the Payroll module only.
 Check this box if this job is certified and should be included on Certified Payroll reports. If checked and the ‘Certified Jobs Only?’ option for the selected Certified Payroll report is set to Y, this job will be included when printing the report. However, detail included on the report is based on how the ‘Include on Certified Reports’ option is set in PR Employees.
 Leave this box unchecked if this job is not certified. Certified Payroll reports will only include this job if the ‘Certified Jobs Only?’ option for the selected Certified Payroll report is set to N (unchecked).
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Start Date for Certifieds

 If
 you are including this job on certified payroll reports, enter the start date for certified
 payrolls (should be the date labor actually started on this job). This date will be used to
 calculate the week number on the certified payroll reports (e.g. PR Certified Payroll
 Transcript, PR Certified Report with Liabilities, etc.). This should represent the first
 week ending date for the job/project.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

Date field shortcuts
T ort
Set the date to the current date.

MMDD
Four digit month and day
Enter a four digit month and date (MMDD) and the system will automatically add the current year.

+
The system will automatically set the date to tomorrow.

+5
The system will automatically set the date to 5 days in the future.
You can actually enter any value after the +, for
 example you can enter +7 to set the date to next week.

-
The system will automatically set the date to the previous day.

-5
The system will automatically set the date to 5 days in the past.
Just like with +, you can enter any value after the
 -, for example you can enter -7 to set the date to the
 previous week.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Construction Type

Construction Type drop down in the JC Jobs form, PR Info
 tab.

 Used by the Payroll module for certified reporting purposes. Only required if sub-jobs for this project represent different types of construction (that is, distinct wage determinations).
Select the type for each job. The PR Certified Export - eMars report (U.S. only, ReportID 1315) will then break out your payroll data by construction type as needed, displaying the appropriate value for each employee wage-and-hour record in the Construction Type column. This meets the requirement for projects governed by multiple wage determinations (wage schedules).
Valid types are:

- B-Building

- D-Dredging

- H-Heavy

- R-Residential

- W-Highway

Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

##  EEO Region

 Used
 by the Payroll module for EEO reporting purposes.
 Enter a code, up to 8 characters, that identifies the region (such as county) for this job. This field is not validated, but allows you to print the EEO reports by region.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  SMSA Code

Use
 this field to identify the SMSA area in which this job is being performed.
Enter a SMSA code or press F4 to select
 one from a list.
SMSA codes are created and maintained using the [ HQ SMSA Codes ](/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-smsa-codes-forms) form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Craft Template

Use this field to select the set of craft/class pay rates to use as
 defaults when posting timecards to the project/job.
Enter a PR template code or press F4 to select
 one from a list.
Templates are created and maintained using the
 [PR Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-templates-form) form, and crafts templates are added to the
 template using the Craft Templates tab. Click [here](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-crafts-classes-and-templates) for an overview on crafts, classes, and templates.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  PR Overtime Schedule

Use
 this field to select the overtime schedule that will be used to calculate PR overtime when
 timecards are posted to this job/project.
Enter the overtime schedule or press
 F4
 to select a schedule from a list.
Overtime schedules are created and maintained using the [PR Overtime Schedule](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-overtime-schedule-form) form.
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Fixed Rate Template

Use
 this field to select the fixed rate template that will be used when charging labor and
 burden to the job/project.
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
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## PR Leave Level

PR Leave Level field in the JC Jobs form, PR Info
 tab.
When you process PR Auto Leave, the system compares the following two rates and uses the highest of the two in leave accrual calculations:

- the rate set for the employee in the PR Employee Leave form, or if there is not one there, the PR Leave Codes form

- the rate associated with the leave level code (as set in the PR Leave Codes form, Leave Level Overrides tab)

If the job leave rate happens to be the highest of the two, the amount of leave accrued by the employee is also based on how much they worked on the job. Note: Job-specific Leave Level overrides affect only *accruals* . These accruals cannot override limits, nor do they impact frequencies or usage.

Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

##  Use Weighted Average Overtime Rates

The Use Weighted Average Overtime Rates checkbox on the JC
 Jobs form, PR Info tab.
 Select this checkbox to use weighted-average overtime rates when applying auto overtime
 to timecards posted to this job. Because this option is used in conjunction with the
 Use Weighted Average Overtime Rates option in PR Craft Classes,
 you must also check this option for each craft/class to which this job applies.
Once you select this checkbox, the Average By field is enabled, and
 you must select the weighted-average overtime calculation method (Week or Day). When the
 system applies auto overtime to timecards posted to jobs, crafts, and classes for which
 both Use Weighted Average Overtime Rates options are selected, the
 system uses a weighted-average overtime rate adjustment based on the Average By calculation
 method you selected. If both options are not selected, regular overtime rates are used.
Do not select this checkbox if you are using regular overtime rates.
For more information about weighted-average overtime rates, see [Weighted Average Overtime Rates](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/weighted-average-overtime-rates).
Note: Many of the fields on the JC Jobs form are also on the PM Projects form. When you make a change to this field on the JC Jobs form, the system immediately updates the same field on the PM Projects form.

Related concepts

- [JC Jobs Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)

## Average By

The Average By field on the JC Jobs form, PR Info
 tab.
This field is only enabled when you select the Use weighted average overtime rates checkbox.

- Week (Default) - Calculate weighted-average overtime based on the employee's weighted-average regular rate for the weekly or bi-weekly pay period.

- Day - Calculate weighted-average overtime based on the employee's weighted-average regular rate for the day.

Note: It is suggested that the option you select here be assigned to each applicable craft/class associated with this job to ensure the correct weighted-average overtime rate is used. If you set one option to Weekly and one to Day, the systems uses the daily weighted-average rate.

##  Sequence

 Enter
 the sequence number (0-255) for this reviewer. If left blank, defaults as sequence '1'.
 For unapproved invoices only, if you are using a hierarchical method of invoice approval, this sequence number should represent the order in which this reviewer is to review and approve invoices associated with this job.
For example, if this reviewer must approve an invoice/invoice line before anyone else, enter the Seq as '1'. Reviewers with sequences greater than '1' (i.e. 2, 3, etc.) will be unable to review and approve an invoice/invoice line until this reviewer has marked it as approved. If not using a hierarchical method, all reviewers can be assigned Seq '1'.
Note: If the reviewer is authorized to review and approve both unapproved invoices and purchase requisitions, assign the sequence number based on the numbering system designated for unapproved invoices.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Reviewer

 Specify the reviewer (as defined in HQ Reviewers) authorized to review unapproved invoices
 and/or requisitions (as designated by the 'reviewer type' specified to the right)
 associated with this job. Reviewer's name displays to the right of this field.
 Press F4 for a list of active Reviewers from
 which to choose.
Press F5 in the Reviewer field
 to access HQ Reviewers.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Reviewer Type

 Specify the reviewer type.

- Invoice – Select this option if this reviewer is authorized to review and approve (or reject) unapproved invoices associated with this job. Reviewer will be assigned automatically to all 'job' lines on unapproved invoices that reference this job (in AP Unapproved Invoice Entry).

- Purchase – Select this option if this reviewer is authorized to review and approve (or reject) purchase requisitions associated with this job. Reviewer will be assigned automatically to all 'job' lines on requisitions that reference this job (in PO Requisition Entry).

- Both – Select this option if this reviewer is authorized to review and approve (or reject) unapproved invoices and purchase requisitions. Reviewer will automatically be assigned to any 'job' lines on unapproved invoices (AP Unapproved Invoice Entry) or requisitions (PO Requisition Entry) that reference this job.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

## Optional Reviewer

The Optional Reviewer checkbox on the JC Jobs form, Reviewers tab.
Select this checkbox to designate this reviewer as optional for all invoice lines to which this reviewer is assigned. This allows for one of multiple optional reviewers to approve invoice lines with a given approval sequence. Changing this setting here does not affect existing invoices; changes only affect invoices created after the change.
As long as more than one optional reviewer is assigned to each invoice line’s approval sequence, only one reviewer must review and approve in order for the approval process to advance. However, if the only reviewer on an invoice line’s approval sequence is an Optional Reviewer, their approval becomes required in order for the approval process to advance.
Setting ALL reviewers on a sequence as optional does not eliminate the approval requirement for that sequence. If an invoice line’s approval sequence contains multiple reviewers, the following rules apply to allow the approval process to advance.

- if ALL reviewers on a sequence are set as optional, at least one must approve

- if ALL reviewers on a sequence are set as non-optional (Optional Reviewer checkbox is not selected), all must approve

- if some reviewers on a sequence are set as non-optional and some as optional, all non-optional must approve

##  Memo

 Use
 this field to enter miscellaneous notes or information about this reviewer, up to 255
 characters.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs

##  Document Type

The Document Type field on JC Jobs form, Workflow tab.
 Select the type of document to which the workflow applies.

- PO - Purchase Order

- SL - Subcontracts

Note: You can have only one process for each document type.

Note: The workflows defined here override those defined in JC Company Parameters or HQ Company Setup.

For more information about the Workflow Process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

##  Process

The Process field on the JC Company Parameters form, Workflow tab.
Enter the workflow process to perform for the specified document type or press F4 to select from a list of valid workflows. Valid workflows are those that are associated with the same document type specified in the Document Type field or those that do not specify a document type.Note: When you create a workflow (in [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)), you will generally assign it to a specific document type (Purchase Order or Subcontract). However, you may have generic workflows that are not associated with a specific document type (that is, the Document Type field is blank). In this case, you may assign it to either or both document types on this tab.

Note: The workflows defined here override those defined in JC Company Parameters or HQ Company Setup.

##  Active

The Active checkbox on the JC Jobs form, Workflow tab.

Select this checkbox if this workflow should be applied when new POs or Subcontracts (depending on the document type) are created.
For more information about the workflow process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

##  Notes

The Notes field on the JC Jobs form, Workflow tab.
Enter any notes about the workflow.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.

## Job Role

 Use
 this field to select a role. Press F4 to select one from a list. Click [here](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow) for more information about how roles work in the
 Process Workflow feature.
Roles are created and maintained using the
 [HQ Roles](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) form. You can launch this form by pressing
 F5
 in this field.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs
[](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)Process Workflow - Overview

## User Name

 Use this field to select a user account. You can
 only select a user that is associated with the role selected in the Role field.
Roles are created and maintained using the HQ Roles form, and users are associated with roles using either of the following forms:

- Users tab on the [HQ Roles](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) form - You can access this form by pressing
 F5 in the Job
 Role field.

- Roles tab on the [VA User Profile ](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form) form - You can access this form by
 pressing F5 in the User Name field.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs
[](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)Process Workflow - Overview
[](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)VA User Profile

## Lead

Check
 this box if the user is the lead at the selected role.
Currently the selection in this box has no affect on how which workflow is applied. This box is informational only.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs
[](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)Process Workflow - Overview

## Active

Check
 this box if the selected role and user should be used when the system is calculating the
 workflow to apply to a PO.
The system will only use this user/role if this box is checked.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs
[](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)Process Workflow - Overview

## Notes

Use
 this field to enter notes on the role/user.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs
[](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)Process Workflow - Overview
