---
title: "PM Company Add-ons Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/pm-company-add-ons-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/pm-company-add-ons-form"
---

# PM Company Add-ons Form

Use the PM Company Add-ons form to set up company defaults for add-on cost calculations, such as overhead, profit, and other indirect costs to change orders.
Access this form by double-clicking any row on the Add-ons tab in PM Company Parameters.Note: You can also enter add-on information directly into the Add-ons tab in PM Company Parameters.

## Add-On Basis

Use this section to specify the amount on which to base the add-on cost. You can use a flat amount or have the calculation based on a percentage of the change order or the total costs of a specific cost type. If the add-on is for additional costs (e.g. bonds), you can redirect the costs to a specific phase/cost type and/or contract item.
 For more information, see [Company Add-Ons: Add-on Basis](/en/vista/vista/project-management/setupmaintenance/company-add-ons-add-on-basis).

## Add-On Total Type

Use this section to specify the add-on type. The Add-on Type determines how the add-on will be calculated.

- Net Total – This add-on type is calculated first and is based on either Cost, Cost plus Markup, or Total, depending on the 'Net Add-On Calculation Level' selected.

- Sub Total – This type of add-on is calculated next and is a calculated amount based on the net amount plus markups plus net total add-ons. Sub total add-ons do a cycle calculation 5 times to provide the most accurate add-on total.

- Grand Total – This type of add-on is calculated last, and is a calculated amount based on the net amount plus markups plus net total add-ons plus sub total add-ons.

## Net Add-On Calculation Level

This option is used in conjunction with the Net Total add-on type and allows you to specify whether to base the add-on calculation on Cost (net amount only), Cost plus Markup (net amount plus markups) or Total (net amout, plus markups, plus lower sequential add-ons).

## Revenue

Use the Revenue section to redirect add-on revenue to a separate contract item without a phase/cost type association. This allows including add-on fees for pending change orders (external only) without updating phase/cost type cost estimates.
For more information, see [Company Add-Ons: Revenue Redirect](/en/vista/vista/project-management/setupmaintenance/company-add-ons-revenue-redirect).

Related concepts

- [PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)
