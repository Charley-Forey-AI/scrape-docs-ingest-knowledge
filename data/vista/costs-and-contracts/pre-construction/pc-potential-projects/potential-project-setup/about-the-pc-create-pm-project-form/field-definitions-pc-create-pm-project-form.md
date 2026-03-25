---
title: "Field Definitions: PC Create PM Project Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-create-pm-project-form/field-definitions-pc-create-pm-project-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-create-pm-project-form/field-definitions-pc-create-pm-project-form"
---

# Field Definitions: PC Create PM Project Form

The following is a list of field descriptions for the PC
 Project form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Enter the project number that you would like to create from the potential project. This must be a unique number, so you cannot select a project number that has already been used.
Press F4 to see a list of projects that have already been created.
Note: If you are using this form to create PM module subcontract detail, use this field to select the PM project that should be associated with the subcontract detail. Click [here](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/potential-project-conversion/create-pm-subcontract-detail) for more information on using PC module vendor bids to create PM module subcontract detail.

## Description

Enter a description of the project. By default this field will populate with the project name of the potential project.
The entry in this field can be up to 60 characters long.

## Contract

The function of this field depends on if you are selecting an existing PM contract or creating a new PM contract from this form.

- To create a new PM contract, enter an unused PM contract number. You can press F4 to see a list of contract numbers that have already been used.

- To select an existing PM module contract, enter the contract number or press F4 to select it from a list. You can only select a contract with a pending status, which means you cannot select contracts that have been interfaced with JC using [PM Interface ](/en/vista/vista/project-management/setupmaintenance/pm-interface-form). PM module contracts are created and maintained using [PM Contracts . ](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form)

Note: You can also press F5 to open [PM Contracts ](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form) and create a new contract, and then you can select the new
 contract in the Contract field on PC Create PM Project.

## Contract Description

The function of this field varies depending on if you are creating a new contract in the form, or if you are selecting an existing contract.

- If you are creating a new contract in the form by
 entering a new contract number in the Contract field, enter the
 description of the contract you are creating. This will be used as the description of
 the new contract.

- If you have selected an existing contract in the
 Contract field, this field will display the description of the
 selected contract. Making changes to this field will not update the description on
 the contract in PM.

The entry in this field can be up to 60 characters long.

## Department

The function of this field varies depending on if you are creating a new PM contract in the form , or selecting an existing contract.

- If you are creating a new contract in the form, the department in
 this field will be associated with the new contract. Enter a department or press F4 to
 select one from a list. If there is a department set up on the potential project
 (PC Potential Project > Bid Info tab > Department field), that department will by default populate in this field, but you
 can change it if it does not apply.

- If you are selecting an existing contract, this field will display
 the department already assigned to the selected contract.

## Create Subcontract Detail

Check this box if you would like to create PM subcontract detail using the awarded vendor bids on the potential project.
Vendor bids are maintained using the [PC Bid Coverage](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/bids/about-the-pc-bid-coverage-form) tab of PC Potential Projects.

[](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/potential-project-conversion/create-pm-subcontract-detail)Create PM subcontract detail using the awarded bids on a bid package

## Cost Type

Enter the cost type that will be used to create the subcontract detail items or press F4 to select one from a list.
This field will default to the subcontract cost type set up in the
 SL Cost Type 1
 field on the Subcontract Parameters tab of [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form). If the
 SL Cost Type 1
 field is blank, it will display the value in the
 SL Cost Type 2
 field.
Note: This field is only enabled when the
 Create Subcontract Detail
 box is checked.

## Assign PM Firm Contacts

Check this box to add the project team members on the potential project to the new project as contacts. Only project team members that are PM firm contacts will be added to the new project.
Project team members are added to a potential
 project using the Project Team tab on [PC
 Potential Projects](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-potential-projects-form). Only contacts with PM Firm Contact in the Contact Source
 column will be included on the new project.
