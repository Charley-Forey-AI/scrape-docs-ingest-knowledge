---
title: "Create a New Job from an Existing Job | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/create-a-new-job-from-an-existing-job"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/create-a-new-job-from-an-existing-job"
---

# Create a New Job from an Existing Job

You can use the JC Job Copy form to create a new job using a job that already exists in Vista.
If you are using data level security for jobs and/or contracts, the destination job and contract will inherit the security groups assigned to the source job and contract. You may override these assignments in the related programs. [More](/en/vista/vista/costs-and-contracts/job-cost/job-level-security)

1. Open the JC Job Copy
 form.

1. Enter the job that
 would like to copy in the Job
 field or press F4
 to select it from a list.

1. Use the Company field to select the company
 where you would like to create the new job.

1. Enter the job number
 that you would like to create in the Job
 field.

1. The Description field will populate based
 on the job being copied.

1. Select the Liability
 Template of the new job or press
 F4
 to select it from a list. This field will populate
 with the liability template on the copied job. The
 liability template defines how payroll burden
 (employer-paid liabilities) is charged.

1. Use the PR State field to select which state will default on the payroll timecards posted to this job.

1. Select the Contract that is associated with the
 new job.This field defaults the job number. If this
 contract has not already been created, the system
 will automatically create the new contract with a
 single contract item. If this job is associated
 with an existing contract, enter the contract or
 press F4 to select from a list of valid open or
 pending contracts.

1. Review the information in the Groups section. The Groups section displays the source and destination companies, along with the customer, tax, and phase groups assigned to each company (in HQ Company Setup). If the destination groups differ from the source groups, they are displayed in red.
If the phase groups differ between the two companies, the ‘Components to Copy’ options will not be available. However, you will still be able to copy the job and set up the new contract with a single contract item. If the customer or tax groups do not match, you will be able to copy contract items, phases/cost types, change orders, and original estimates; however, if you specify a customer and/or tax code for the new contract, the codes must exist for the destination company.

1. Enter the description
 of the contract in the Description field.

1. Use the Department field to select the
 department of the contract. This selection will
 also be applied to the items on the contract.


1. Use the Customer field to select the customer
 of the contract. This field populates with the
 customer on the contract that is associated with
 the job being copied. Customers are created and
 maintained using the [ AR Customers ](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form) form.


1. Enter the Tax Code for the contract. This selection will be applied to the contract and all contract items.

1. Use the Retainage % field to define the retainage percent for the contract and contract items.

1. Enter the start month and year of the contract in the Start Month field. It will default with the current month and year.

1. Select the additional
 information that you would like to copy to the new
 project in the Additional Information to Copy
 section. Press F1
 in any of these fields for more detailed
 information.

1. Click the Copy button when complete.

[About Copying Custom Fields](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-copying-custom-fields#concept-7286--en__concept-7286)
