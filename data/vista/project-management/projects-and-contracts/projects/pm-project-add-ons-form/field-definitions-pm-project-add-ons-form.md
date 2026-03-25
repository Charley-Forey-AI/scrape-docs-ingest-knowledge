---
title: "Field Definitions: PM Project Add-ons Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form/field-definitions-pm-project-add-ons-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form/field-definitions-pm-project-add-ons-form"
---

# Field Definitions: PM Project Add-ons Form

The following is a list of field descriptions for the PM
 Project Add-ons form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Add-on

Add-ons defined in PM Company Add-Ons will be set up here automatically. You may override default add-ons as necessary.
If this is a new add-on, enter a number (0-255) for this add-on.
Note:Add-ons set up here are not updated to PM Company Add-Ons.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

##  Description

 Enter the description for this add-on, up to 30 characters.
 If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

## Standard

Check this toggle if the add-on should by default be included on all new pending change orders on this project.
 Changes made to the add-ons on a project will not update the add-ons on the company record. If you would like to update the add-ons associated with a company record, use [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form).

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

## Round Amounts to Nearest Whole Dollar

Select this checkbox if this add-on should be rounded to the nearest whole dollar when change orders are calculated.
If not selected, change orders will include the actual add-on amount.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

## Basis

Specify the basis for this add-on.

- Percent – Add-on amounts will be calculated based on a percentage (indicated below) of the transaction’s net amount.

- Amount – Add-on amount will be a specified fixed amount (indicated below).

- Cost Type – Select this option to calculate the add-on amount based on a percentage of the total cost for a selected cost type (specified below).

If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

##  Basis Cost Type

 This field is enabled only when add-on basis is ‘C-Cost Type’.
 Specify the cost type on which to calculate the add-on amount. Calculation will be a percent (specified below) of the total cost for the cost type.
 If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

##  Percent %

 This field is enabled only when add-on basis is ‘P-Percent’ or ‘C-Cost Type’.
 Indicate the percentage (-999.0000 to 999.0000) by which to calculate costs for this add-on.
 If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

## Amount

This field is enabled only when add-on basis is ‘A-Amount’.
Enter the fixed amount for this add-on.
If the Round Amount to Nearest Whole Dollar box
 is checked, the value in this field must be a whole dollar.
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

## Add-On Total Type

This field is disabled and set to ‘Net Total’ when add-on basis is ‘C-Cost Type’.
Specify the type for this project add-on. The add-on type determines how the add-on will be calculated and in what order.

- Net Total – This add-on type is calculated first, and will be based on Cost, Cost plus Markup, or Total, depending on the ‘Net Add-On Calculation Level’ selected below.

- Sub Total – This type of add-on will calculate an add-on amount based on the net amount plus markups plus net total add-ons. The cycle calculation is performed five times to provide the most accurate add-on total.

- Grand Total – This type of add-on will calculate an add-on amount based on the net amount plus markups, plus net total add-ons, plus sub total add-ons.

Add-ons defined here are automatically set up and calculated for each item you enter on a change order. The system bases calculations on the item's net amount and the add-on type (in PM Change Order Totals). Net total add-ons are calculated first, sub total add-ons next, and grand total add-ons last.
If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

## Include in Subtotal Add-On Calculations

This field is enabled only when the add-on total type is 'Grand Total'.
Check this box to include grand total add-ons in subtotal add-on calculations. The system will calculate grand total add-ons after net add-ons, with the resulting amount accumulated into the pending total. Subtotal add-ons will be calculated next, and will include the grand total add-ons. The sum of the grand total add-ons will then be subtracted from the pending total, and the grand total add-ons recalculated.
Leave this box unchecked if you do not want grand total add-ons included in subtotal add-on calculations. Add-ons will be calculated as normal (i.e. net totals add-ons, then subtotal add-ons, then grand total add-ons).
If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.
Note:If you change this flag for an existing add-on, the system will update all associated records in PMOA (CO Add-ons) and recalculate pending change order items.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

## Net Add-On Calculation Level

This field is enabled only when the add-on total type is ‘Net Total’.
Specify on which total to base the add-on calculation.

- C – Cost. Calculation will be based on the net amount only.

- M – Cost plus Markup. Calculation will be based on the net amount plus markups.

- T – Total. Calculation will be based on net amount, plus markups, plus lower sequential add-ons.

If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

## Phase Code

Enter the phase to which the costs for this add-on will be posted when pending change order is approved. Any valid phase may be used, regardless of whether using the ‘locked phases’ feature for a project.
If you do not want these costs interfaced to accounting or if distributing costs proportionally to phases on changes orders with a specific cost type (defined below), leave this field blank.
If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

## Cost Type

Required if phase entered above.
Enter the cost type to which the add-on costs will be posted when pending change order is approved. Any valid cost type may be specified, regardless of whether using the ‘locked phases’ feature for a project. If you do not want these costs interfaced to accounting, leave this field blank.
Note:If you enter a cost type without entering a phase, add-on costs will be distributed proportionally to every phase on a change order with this cost type, adjusting the last phase/cost type for rounding (if necessary).

If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

## Contract Item

Entry in this field is only needed if you specified a phase above.
Indicate to which contract item costs for this add-on will be posted when pending change order is approved. If the phase does not already exist for the project, the system will add the phase to the project and assign it to this contract item. If you leave this field blank, the system will assign the first item on the contract.
If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

## Re-direct Add-on Revenue When Approved

Check this box to redirect the revenue for this add-on to a separate contract item.
Leave this box unchecked if revenue for this add-on will be posted to the contract item for the change order item.
If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

## Revenue Contract Item

This field is enabled only if ‘Re-direct Add-on Revenue When Approved’ option is checked.
Required.
Specify the contract item to which revenue will be redirected when approving pending change order items assigned this add-on. If you specify a contract item that does not exist for the contract, it will be added once the ACO Item is generated. The contract item description will default from the add-on description, the UM will be set to LS, and the amounts will be set to 0.00.
If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

## Create ACO Item

This field is enabled only if ‘Re-direct Add-on Revenue When Approved’ option is checked.
Specify the numbering method to use for ACO items created when redirecting revenue for this add-on.

- U – Use Revenue Item. Select this option to create ACO items using the Revenue Contract Item number (specified below).

- S – Sequential. Select this option to create ACO items using a sequential number based on the Start at ACO Item # specified below.

- F – Fixed. Select this option to use a specific ACO item number (designated below).

If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

##  Start at ACO Item #

 Enter the starting number for ACO items created when redirecting revenue for this add-on.
This number should be a high number (for example 500) so that the generated ACO items won't interfere with the items already on the change order.
If this number is set to 1 (or a low number), you may have issues when approving pending change orders using the PM Approve PCOs form.
 If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.
Why is this field disabled?
 This field is enabled only when S-Sequential is
 selected in the Create ACO Item field.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects

##  ACO Item

 This field is enabled only when ‘Create ACO Item’ option is set to ‘F-Fixed’.
 Enter the number to use for all ACO items created when redirecting revenue for this add-on.
 If a company add-on, defaults as defined in PM Company Add-Ons; however, you may override as necessary. Overrides will not be updated to PM Company Add-Ons.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)PM Project Add-Ons
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)Overview: Setting up a project
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects
