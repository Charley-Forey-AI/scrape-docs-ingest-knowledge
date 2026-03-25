---
title: "Job Cost | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost"
---

# Job Cost

Job Cost is the core of the Vista™ integrated construction management system.
It is the place where estimated job costs, actual job costs, projected and committed job costs, and contract revenue posted throughout the accounting modules are accumulated. Click on a topic below for more information.

- Jobs/Phases/Cost Types - The Job Cost module is made up of jobs, phases, and cost types. It is each unique combination of job, phase, and cost type to which estimates, projections, commitments, and actual costs will be posted throughout all accounting modules, which in turn updates Job Cost.

- A job defines a scope of work to be done and is identified throughout Job Cost and all other modules by a Job Code you assign in the Job Master program. Job codes can be up to 10 characters in length.

- A phase is a division of work that must be performed to complete the job (for example, rough carpentry, mobilization, or concrete form work). Every job must have at least one phase associated with it, and may have hundreds, depending on the scope of the job to be done and the level of detail at which you want to record costs. Phase codes can be up to 20 characters in length.

- A cost type is a category of work (such as labor, materials, equipment, and subcontracts) to which costs are posted within a phase. You define each of your cost types in the JC Cost Types program, and then assign one or more of them to each of your phases in the JC Phases program. Phases may have as few as one, or as many as 255, cost type categories assigned to them.

- Contracts and contract items.

- A contract is the contractual agreement you make with the owner (your customer) to perform some work.

- A contract item is a way to itemize the contract so that each piece of the contract you and your customer wants billed separately is made a separate contract item. A contract must always have at least one contract item. It is each contract/contract item that you can bill through the Job Billing module and track through the Accounts Receivable module, and which is interfaced to Job Cost as revenue.

- Linking contracts and jobs - One of the most important concepts is the link between contracts and jobs. Every job is assigned to a contract, and every phase of the job must be linked to a contract item. For details, see [About Linking Contracts and Jobs](/en/vista/vista/costs-and-contracts/job-cost/about-linking-contracts-and-jobs).

- Automatic contract set up - When you set up a job in the [JC Jobs ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form), the system automatically creates a contract of the same number with one contract item in [JC Contracts ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form). If the contract does not already exist in the Contract Master, you will have the option to assign a department and customer to the contract; the Contract Master will automatically be set up with the contract number, department, customer, and a single contract item, with LS (lump sum) as the unit of measure. The contract’s description defaults to the job description, as does the contract item description.

- Automatic phase-item links - When you add a phase to a job using [JC Job Phases ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form), you indicate which contract item it should be linked to. However, in some cases a phase can be set up for you automatically because you post to it from Payroll, AP, etc. When that happens, the system looks to see whether that phase has been used already in its valid part form. If it has, the system links the new phase to the same contract item as that assigned to the valid part of the new phase. If not, the new phase is automatically linked to the first contract item, and you must use JC Job Phases to re-assign it. Click [here](/en/vista/vista/costs-and-contracts/job-cost/phases-and-phase-validation) for examples of phase validation.

- Module Interaction - Job Cost interfaces with almost all of the other Vista modules. For details, see [JC Module Interaction](/en/vista/vista/costs-and-contracts/job-cost/jc-module-interaction#concept-4470--en__concept-4470).
