---
title: "PM Contracts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form"
---

# PM Contracts Form

Use this program to set up and maintain contract information.

Information entered here automatically updates JC
 Contracts, since both programs share the same file (JCCM). However, data entered
 initially in this program is considered “pending," and therefore, will not be
 accessible in Job Cost until the project has been interfaced. Once interfaced, data
 entered in either PM Contracts or JC Contracts will automatically update the other.
You will typically set up a new contract for each
 new project, providing information on how the project is to be billed, and providing
 a link between project revenue (posted to the contract) and project costs (posted to
 the job). Each contract must have at least one item, but may have multiple items. If
 any part of a project is to be billed separately, it should be set up as a separate
 item on the contract.

- Contracts that are automatically created - When you create a project in
 [PM
 Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form), the form automatically generates a contract, assigns
 the project number as the contract number, and creates a single contract
 item with a LS (lump sum) unit of measure. Once the contract has been
 created, you can use this form to enter the remaining information on the
 contract. Note: Because of this auto-add
 feature, the length and format of your contract codes must be
 identical to the length and format of your job codes.

- Contract Status - All contracts set up in this form are assigned a status of
 ‘Pending’. This status will not change until the contract is updated to Job
 Cost, at which time it changes to ‘Open’. From that point on, the status is
 maintained in Job Cost and cannot be edited here.

- Contract Items - Contract items are generally used to
 break down a contract for billing purposes. Any piece of a contract that
 will be billed separately should be made a separate item. If the contract
 type is 'P' (Progress), the items come from the schedule of values or bid
 items. If the contract type is T (Time & Materials), you may only need
 to set up one item. Note: Contract items
 are set up using the Items tab. You can set them up directly in the
 grid or via the PM Contract Items form, which can be accessed by
 double-clicking any item in the grid or by placing focus in the grid
 and selecting the ‘Open Related Record in Form’ option from the
 Records menu.

- Auto Update Contract Items - If you change the
 Department, Retainage %, Tax Code, or Default Bill Type for a contract (at
 the header level), upon saving the record, you will receive a message
 indicating the change, and asking if you want to update any existing
 contract items having the 'old' value with the new value. Answer Yes to
 save the changes to the header and update all applicable contract items
 (i.e. those with the same 'old' value), No to save changes to the header
 only.

- Security Group - If you are implementing data level
 security at the contract level, you have the option to assign security
 groups to each contract you set up in this program. This can be very useful
 if you regularly set up new contracts, as it allows you to easily designate
 who will have access to the job without having to go to VA Data Security
 and set it up. For details, see [Contract Security Groups](/en/vista/vista/project-management/projects-and-contracts/contracts/contract-security-groups#concept-8045--en__concept-8045).

- Deleting Contracts - You can delete a contract in this
 program as long as no phases have been set up for the contract, the
 contract has not been interfaced to Job Cost, and/or no detail exist for
 the contract and its items (for example, JC, JB, and so on). If a contract
 is to be deleted, all existing contract items must be deleted before the
 contract can be deleted.

- JB Contract Info - This tab is used to set up additional
 information about a contract for billing purposes. For details, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

- Forecast Tab - Use this tab to set up the forecast for
 the contract. For details, see [About Contract Forecasts](/en/vista/vista/project-management/projects-and-contracts/contracts/about-contract-forecasts).

- Field Tickets Tab - Use this tab to create field tickets
 for contracts that will enable linking labor, material, and equipment costs
 related to specific work activity on a job, and facilitate owner
 billing.Note: You can only post costs to a field ticket
 set up here once you interface the contract to Job Cost (via PM
 Interface).

 For more information about field tickets, see
 [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

Click the links below for more information about this form.
[Setting Maximum Retention Amounts for Contracts](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/setting-maximum-retention-amounts-for-contracts)
[PM Contract Items Form](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contract-items-form)
[JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form)
[Revenue/Cost Forecast Options](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options)
[PM Forecast Initialize Form](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-forecast-initialize-form)
[VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)
