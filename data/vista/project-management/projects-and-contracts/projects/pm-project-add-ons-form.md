---
title: "PM Project Add-Ons Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form"
---

# PM Project Add-Ons Form

Use this form to input project add-ons. You can open this form in
 two ways:

- Double-clicking in a grid row on the Add-Ons tab of PM
 Projects

- Highlighting a grid row and selecting Open Related Record
 in Form from the Records menu.

 You can also enter add-on information directly into the grid
 using the Add-On tab in PM Projects.
The system will automatically add any add-on costs to the project
 that are set up for the company in PM Company Parameters (Add-ons tab). You can modify or
 delete these default add-ons if needed, but only standard add-ons (those with the
 Standard checkbox selected in PM Company Add-ons) are including
 on every pending change order when they are created in PM Pending Change Orders.

## Add-On Basis

For each project add-on, you must specify the basis for the
 add-on; that is, the amount on which to base the add-on cost. You can specify to use a
 flat amount or have the calculation based on a percentage of the overall change order or
 the total costs for a specific cost type.
If the add-on is for additional costs (e.g. bonds), you can
 redirect the costs to a specific phase/cost type and/or contract item. If you wish to
 distribute the add-on amount to all phases on a change order with a specific cost type,
 leave the phase blank and enter only the desired cost type. The system will distribute
 the add-on amount proportionally to all phases on the change order with that cost type,
 adjusting the last phase/cost type for rounding (if necessary).
Example:
Add-on
 100

Basis
Cost Type

Basis CT
1(Labor)

Percent
10.00

Redirect CT
7(Burden)

Redirect Phase
(blank)

Pending CO:
Phase
CT
Amount
Add-on Amt

02210-   -
1
300.00
30.00

03310-   -
1
300.00
30.00

04410-   -
1
    400.00
    40.00

Total:
$1000.00
$100.00

Approved CO:
Phase
CT
Amount

02210-   -
1
300.00

7
30.00

03310-   -
1
300.00

7
30.00

04410-   -
1
400.00

7
     40.00

Total:
$1100.00

## Add-On Total Type

This section is used to specify the add-on type, which
 determines how the add-on will be calculated.

- Net Total – This add-on type is calculated first, and
 will be based on either Cost, Cost plus Markup, or Total, depending on the ‘Net
 Add-On Calculation Level’ selected (see below).

- Sub Total – This type of add-on will calculate an add-on
 amount based on the net amount plus markups plus net total add-ons. Sub total
 add-ons do a cycle calculation 5 times to provide the most accurate add-on total.


- Grand Total – This type of add-on will calculate an
 add-on amount based on the net amount plus markups plus net total add-ons plus sub
 total add-ons.

Add-ons defined here are automatically set up and calculated
 for each item you enter on a change order. Calculations are based on the item's net
 amount and the add-on type. Net total add-ons are calculated first, then sub total
 add-ons, and lastly, grand total add-ons.

## Net Add-On Calculation Level

This option is used in conjunction with the Net Total add-on
 type and allows you to specify the amounts on which to base the add-on calculation.
 Options are as follows:

- C-Cost – Calculation is based on net amount only.

- M-Cost plus Markup – Calculation is based on net amount
 plus markups.

- T-Total – Calculation is base on net amount, plus
 markups, plus lower sequential add-ons.

## Revenue

Use this section to redirect add-on revenue to a separate
 contract item (when approving pending change order items). Once you check the Re-direct
 Add-on Revenue When Approved option, you will need to specify the contract item to which
 you are redirecting the add-on amount. If you specify a contract item that does not
 exist for the contract, it will be added once the ACO Item is generated. The contract
 item description will default from the add-on description, the UM will be set to LS, and
 the amounts will be set to 0.00.
Pending change orders can only point to a single contract
 item; redirecting an add-on to a separate contract item will therefore require that a
 separate change order item be created. The Create ACO Item option allows you to specify
 the numbering method to use when creating ACO items:

- Use Revenue Item – This option will create an ACO item
 number equal to the specified Revenue Contract Item number.

- Sequential – This option will generate a sequential item
 number based on a specified Start at ACO Item # value.

- Fixed – This option allows you to use a specific ACO
 item number.

When approving a pending change order/item, the type of change
 order item determines how the system handles the revenue add-on amount. If a ‘pending’
 amount (item amount changes based on markups, add-ons, and phase detail), the system
 will deduct the add-on amount from the original PCO item. If a ‘fixed amount’ item, the
 add-on amount is not deducted from the PCO item amount.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-add-ons-form)PM
 Company Add-ons
[](/en/vista/vista/project-management/change-orders/pco-setup-options/add-ons)Change
 Order Totals
