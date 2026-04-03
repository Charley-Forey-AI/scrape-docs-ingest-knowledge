---
title: "Copy from Master Service Contract | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/maintenance-overview/service-contracts/copy-from-master-service-contract"
fetched_at: "2026-04-03T20:47:07.463050+00:00"
menu_path: "/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/maintenance-overview/service-contracts/copy-from-master-service-contract"
---

# Copy from Master Service Contract

This window will facilitate setting up contracts across sites by allowing the operator to specify the From and To contract. It will be used when setting up similar contracts across sites. It will also be used to set up contracts from a 'master contract'.
This window will permit you to enter a 'To contract' that does not exist in the system. If the Service Contract Installation for 'Use auto-sequenced service contract numbers?' checkbox is selected, then when you leave the 'Contract #' field blank, the next available contract number will default automatically. If a non-sequenced code is desired, the simply type the alternate code here. The window will then prompt for Contract description and Contract type, defaulting from the specified 'From contract'. The update will copy contract properties not yet defined in the 'To contract', including equipment codes or types, scheduled visits and tasks, and will then set the 'budget hours' and 'budget costs' for each visit from the Task Table cost setup.
When copying to an existing contract, the Earned revenue basis and Contract type will not be changed. When copying to a new contract, if you select the default Contract type from the master contract, the Earned revenue basis will also be copied, unless it is set to 'Other'. In this case, the software will set the Earned revenue basis for the new contract from the 'Default earned revenue basis' specified for the contract. It may be useful to set the Earned revenue basis of the master contract to 'Other' in order to force the system to assign the Earned revenue basis to the new contract.
Note: This update will not copy billing schedules. Billings
 will need to be created in the new contract, rather than copied from a past contract. The New/Edit Service Contract > Billing tab will offer a billing generator.
Fields/Buttons
Descriptions

From master contract

Site Contract Contract type
The selected site and contract codes
 will default in these fields, but can be changed to a different site and valid
 contract code. The contract type will default from the selected contract.
Equipment
Specify an equipment code, or press
 Enter to copy ALL.
To service contract

Site Contract Contract type
Enter a site code and valid contract
 code to copy the master contract to. The contract type will default from the
 selected contract.
Add equipment to contract?
Select this checkbox to include the
 equipment code(s) specified above on the new service contract
Add scheduled billings?
Select this checkbox to include any
 scheduled billings from the master service contract on the new service
 contract.
Add scheduled visits?
Select this checkbox to include any
 scheduled visits from the master service contract on the new service contract.
 As each visit is copied to the new contract, the price
 of the visit will be copied from the source visit and the new contract
 amount will be calculated and stored if the billing source is set to Work
 Order. The newly calculated Contract price will display in the list box.

Basis for copying equipment/visits?
If adding equipment or scheduled
 visits, select a basis for copying:

- Equipment code

- Equipment type
