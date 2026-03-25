---
title: "Field Definitions: PM Company Add-ons Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/pm-company-add-ons-form/field-definitions-pm-company-add-ons-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/pm-company-add-ons-form/field-definitions-pm-company-add-ons-form"
---

# Field Definitions: PM Company Add-ons Form

The following is a list of field descriptions for the PR
 Company Add-ons form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Add-On

 Enter a number (0-255) for this add-on.

##  Description

 Enter the description for this add-on (e.g. Indirect, Overhead, Profit, etc.).

## Standard

 Check this box if by default the add-on should be included on all pending change orders.

When a project is created that is associated with this company, the add-ons on the company record will be copied onto the project. You can view the add-ons on a project record using the Add-Ons tab of PM Projects. Changes made to the add-ons on a project record will only affect the project, they will not update the add-ons on the company record. When a pending change order is created on a project in [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form), only add-ons on the project record that are setup as 'Standard' will by default be included on the pending change order.
For example, if you have an add-on that only applies to a few projects a year, you can setup that add-on on the company record, but leave the 'Standard' box unchecked. The add-on will be copied to all projects associated with that company, but it will not affect pending change orders since the 'Standard' box is not checked. When the add-on applies to a project, check the 'Standard' box on the add-on on the project record in PM Projects. The add-on will then by default be applied to all pending change orders on the project.

## Round to Nearest Whole Dollar

Check this box if this add-on should be rounded to the nearest whole dollar when change orders are calculated.

## Basis

- Percent – Select this option to calculate the add-on amount based on a percentage (specified below) of the overall change order.

- Amount – Select this option if the add-on cost will be a flat amount (specified below).

- Cost Type – Select this option to calculate the add-on amount based on a percentage of the total cost for a selected cost type (specified below).

##  Basis Cost Type

 This field is enabled only when add-on basis is ‘C-Cost Type’.
 Specify the cost type on which to calculate the add-on amount. Calculation will be a percent (specified below) of the total cost for the cost type.

##  Percent %

 This field is enabled only when add-on basis is ‘P-Percent’ or ‘C-Cost Type’.
 Indicate the percentage (-999.0000 to 999.0000) by which to calculate costs for this add-on.

## Amount

This field is enabled only when add-on basis is ‘A-Amount’.
Enter the net amount for this add-on.
If the Round Amount to Nearest Whole Dollar box
 is checked, the value in this field must be a whole dollar amount.

## Add-on Total Type

This field is disabled and set to ‘Net Total’ when add-on basis is ‘C-Cost Type’.
Specify the type for this company add-on. The add-on type determines how the add-on will be calculated and in what order.

- Net Total – This add-on type is calculated first, and will be based on Cost, Cost plus Markup, or Total, depending on the ‘Net Add-On Calculation Level’ selected below.

- Sub Total – This add-on type will calculate second, and is based on the net amount plus markups plus net total add-ons. Sub total add-ons are calculated using a 5-cycle method to provide the most accurate add-on total (i.e. five calculations will occur for each sub total add-on, with the final calculation being the add-on amount).

- Grand Total – This add-on type will calculate an add-on amount based on the net amount plus markups plus net total add-ons plus sub total add-ons.

##  Include in Subtotal Add-On Calculations

 Enabled only when the Add-On Total Type is 'Grand Total'.
 Check this box to include grand total add-ons in subtotal add-on calculations. Grand total add-ons will be calculated after net add-ons, with the resulting amount accumulated into the pending total. Subtotal add-ons will be calculated next, and will include the grand total add-ons. The sum of the grand total add-ons will then be subtracted from the pending total, and the grand total add-ons recalculated.
 Do not check this box if you do not want grand total add-ons included in subtotal add-on calculations. Add-ons will be calculated as normal (i.e. net totals add-ons, then subtotal add-ons, then grand total add-ons).

## Net Add-On Calculation Level

Enabled only when Add-On Total Type is ‘Net Total’.
Specify on which total to base the calculation.

- C – Cost. Calculation will be based on the net amount only.

- M – Cost plus Markup. Calculation will be based on the net amount plus markups.

- T – Total. Calculation will be based on net amount, plus markups, plus lower sequential add-ons.

## Phase Code

Enter the phase to which the costs for this add-on will be posted when pending change order is approved. Any valid phase may be used, regardless of whether using the ‘locked phases’ feature for a project.
If you do not want these costs interfaced to accounting or if distributing costs proportionally to phases on changes orders with a specific cost type (defined below), leave this field blank.

## Cost Type

Required if phase entered above.
Enter the cost type to which the add-on costs will be posted when pending change order is approved. Any valid cost type may be specified, regardless of whether using the ‘locked phases’ feature for a project. If you do not want these costs interfaced to accounting, leave this field blank.
Note:If you enter a cost type without entering a phase, add-on costs will be distributed proportionally to every phase on a change order with this cost type, adjusting the last phase/cost type for rounding (if necessary).

## Contract Item

Entry in this field is only needed if you specified a phase above.
Indicate to which contract item costs for this add-on will be posted when pending change order is approved. If the phase does not already exist for the project, the system will add the phase to the project and assign it to this contract item. If you leave this field blank, the system will assign the first item on the contract.

##  Re-direct Add-on Revenue When Approved

 Check this box to redirect the revenue for this add-on to a separate contract item.
 Leave this box unchecked if revenue for this add-on will be posted to the contract item for the change order item.

## Revenue Contract Item

This field enabled and required only if the ‘Re-direct Add-on Revenue When Approved’ option is checked.
Specify the contract item to which revenue will be redirected when approving pending change order items assigned this add-on. If you specify a contract item that does not exist for the contract, it will be added once the ACO Item is generated. The contract item description will default from the add-on description, the UM will be set to LS, and the amounts will be set to 0.00.

## Create ACO Item

This field enabled only if ‘Re-direct Add-on Revenue When Approved’ option is checked.
Specify the numbering method to use for ACO items created when redirecting revenue for this add-on.

- U – Use Revenue Item. Select this option to create ACO items using the Revenue Contract Item number (specified below).

- S – Sequential. Select this option to create ACO items using a sequential number based on the Start at ACO Item # specified below.

- F – Fixed. Select this option to use a specific ACO item number (designated below).

##  Start at ACO Item #

 This field enabled only when ‘Create ACO Item’ option is set to ‘S-Sequential’.
 Enter the starting number (1-999999) for ACO items created when redirecting revenue for this add-on.

##  ACO Item

 This field enabled only when ‘Create ACO Item’ option is set to ‘F-Fixed’.
 Enter the number to use for all ACO items created when redirecting revenue for this add-on.
