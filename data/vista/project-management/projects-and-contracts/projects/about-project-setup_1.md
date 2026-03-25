---
title: "About Project Setup | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup_1"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup_1"
---

# About Project Setup

A project is used to define and track the work you perform. You must set up projects before you can begin tracking bids and estimations, posting progress on work completed, and tracking/posting actual costs and costs of completion.
The terms "projects", "jobs", and "contracts" are sometimes used interchangeably in the construction industry, but each of these terms has a specific meaning in the application.

- Contract - Contracts are associated with the revenue side of the work. For example, contracts are used to enter the schedule of values or billing items that are billed to customers.

- Project / Job - These are associated with the cost side of the work (for example, tracking estimations and actual costs). A project is different from a job in that the work is considered a project until it is interfaced with the Job Cost module and accounting begins posting transactions to it. Once the project is interfaced, the project becomes a job.

Each project in the Project Management module is made up of phases and cost types. Phases represent a portion of work that must be performed to complete the project, for example foundation, excavation, or exterior work. Cost types represent categories of work such as labor, materials, equipment, and subcontracts. Cost types are associated with phases and then costs are posted to the cost types.
Once you have defined the phases and cost types on a project, you can set up materials, subcontracts, and change orders for any phase and cost type on the project. Once you interface a project to the accounting modules, you can post projections, commitments, and actual costs to the project using transactions from Payroll, AR, and AP.
One of the most important steps in setting up a project is linking the project with the contract. This associates the cost side of the work with the revenue side. Contracts and projects are linked together using phases and contract items. For detailed information about the effects of linking projects to contracts, see [About Linking Projects and Contracts](/en/vista/vista/project-management/projects-and-contracts/projects/about-linking-projects-and-contracts).

## Project Setup - Basic Steps

The following outlines the basic steps for creating a project in the PM module.

1. Create the Project - You can create a project in one of four ways:

- [Manual Entry](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/create-a-project-manually#ID-00020a25--en__ID-00020a25) - Enter the project information manually in the PM Projects form.

- [Import the Project](/en/vista/vista/project-management/import-project-estimates/import-estimate-data) - Import the project from a third-party estimating package using PM Import Estimates. The import process pulls in the estimated units, hours, and costs. Items created by the import become contract items in Project Management, and may represent bid items, summary codes, or other estimating codes, depending on the exported data.

- [Copy an Existing Project](/en/vista/vista/project-management/projects-and-contracts/projects/pm-copy-project-form#ID-00024861--en__ID-00024861) - You can copy an existing project using PM Copy Project. When you are creating the new project, you can select which information on the original project you would like to copy, such as the original estimates, subcontract detail, and project budgets.

- [Create Project from a PC Potential Project](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/potential-project-conversion/create-a-new-pm-project-and-contract#task-656--en__task-656) - You can create a potential project in the Pre-Construction module and then use the potential project to create a project in the PM module using PC Create PM Project.

1. [Set up the Contract](/en/vista/vista/project-management/projects-and-contracts/contracts/set-up-a-contract) - A contract is the contractual agreement you make with the owner (your customer) to perform some work, and it defines how the project is billed and is where the project revenue is posted. Linking a contract to a project relates the project costs with the project revenue. For more information, see [About Linking Projects and Contracts](/en/vista/vista/project-management/projects-and-contracts/projects/about-linking-projects-and-contracts).Note: When you set up a project, by default the system automatically creates a contract using the same number as the project number. If the contract does not exist in the PM Contracts form, the system automatically creates it with one contract item using the project description and a lump sum unit of measure. Automatically created contracts are pending and not accessible in the JC Contracts form until the project and contract are interfaced using the PM Interface form.

.

1. [Set up Project Phases](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project#ID-00020b07--en__ID-00020b07) - Job and cost type estimates are created when you set up phases on the project. You can either import these estimates (using PM Import Estimates) or you can manually enter them in PM Project Phases. Once you create a project and set up the contract, you can then set up the phases on the contract.

1. [Interface the Project to Job Cost](/en/vista/vista/project-management/projects-and-contracts/projects/interface-the-project-to-job-cost#ID-00020b3b--en__ID-00020b3b) - Interfacing a project changes the project status from pending to active, updates the Job Cost module with the job information and original estimates defined on the project phases, and allows accounting to begin processing transactions on the project. You can interface a project using the PM Interface form.
