---
title: "Company Add-Ons: Revenue Redirect | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/company-add-ons-revenue-redirect"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/company-add-ons-revenue-redirect"
---

# Company Add-Ons: Revenue Redirect

Use the Revenue section in the PM Company Add-Ons form to redirect add-on revenue to a separate
 contract item without a phase/cost type association.
This allows including add-on fees for
 pending change orders (external only) without updating phase/cost type cost estimates.
Once you check the Re-direct Add-on Revenue
 When Approved option, you will need to specify the contract item to which you are
 redirecting the add-on amount. If you specify a contract item that does not exist for
 the contract, it will be added once the ACO Item is generated. The contract item
 description will default from the add-on description, the UM will be set to LS, and the
 amounts will be set to 0.00.
Pending change orders can only point to a
 single contract item; redirecting an add-on to a separate contract item will therefore
 require that a separate change order item be created. The Create ACO Item option allows
 you to specify the numbering method to use when creating ACO items:

- Use Revenue Item – This option will
 create an ACO item number equal to the specified Revenue Contract Item number.


- Sequential – This option will
 generate a sequential item number based on a specified Start at ACO Item #
 value.

- Fixed – This option allows you to
 use a specific ACO item number.

When approving a pending change order/item,
 the type of change order item determines how the system handles the revenue add-on
 amount. If a ‘pending’ amount (item amount changes based on markups, add-ons, and phase
 detail), the system will deduct the add-on amount from the original item. If a ‘fixed
 amount’ item, the add-on amount is not deducted from the PCO item amount.

Related concepts

- [PM Company Add-ons Form](/en/vista/vista/project-management/setupmaintenance/pm-company-add-ons-form)

- [PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)
