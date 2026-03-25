---
title: "SM Flat Price Revenue Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-flat-price-revenue-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-flat-price-revenue-form"
---

# SM Flat Price Revenue Form

Use the SM Flat Price Revenue form to enter split revenue entries for work scopes and flat price work order quotes, work orders, and agreement services.
You can access this form as follows:

- In SM Work Orders and SM Work Order Scopes, for Flat Price scopes only, enter the scope price and click Split.

- In SM Service, for Time of Service, Flat Rate services only, enter the service price and click Split.

- In SM Work Scopes, click Revenue Split Setup.

Splitting revenue allows you to designate which portion of the revenue should be applied to labor, equipment, materials, subcontracts, and/or other expenses. The system requires a minimum of one split revenue sequence; therefore, you will only need to set up multiple revenue sequences if you require a more detailed revenue breakdown.

## Work Scopes

The system automatically defaults the split revenue sequences set up for a work scope when the scope is referenced on a flat price quote or work order. You may add, delete, or modify split revenue entries as applicable.Additionally, any split revenue entries defined for a work scope override any split revenue entries defined at the quote or work order sequence level. For example, if you set up split revenue entries for a flat price quote sequence, and then later assign a work scope with split revenue entries, the system replaces the quote's split revenue entries with the work scope's split revenue entries. The same applies if you change the work scope on a quote or work order sequence. The existing split revenue entries are replaced by the split revenue entries defined for the new work scope.
If you remove a work scope with split revenue entries, the system retains the split revenue entries for the quote or work order sequence.

## Work Order Quotes

If you are using the ​Derived Flat Price​
 pricing method for a quote scope, the system automatically generates revenue
 sequences based on the total billable values entered on the Material, Equipment,
 Labor, and Misc tabs. If you need to edit the revenue entries, you must do so by
 changing the total billable values for the appropriate material, equipment, labor,
 or miscellaneous entries.
When you approve a work order quote, the system automatically
 generates a work order from the quote, adding a separate work order scope for each
 quote sequence. If flat price quote sequences exist, the system automatically adds
 the split revenue entries to the generated work order scope and disables the revenue
 entries for the quote scope. If you need to change the revenue entries, you can do
 so using one of the following methods:

- Edit Quote Scope Entries - If
 you prefer to edit the entries for the quote scope, you must first unapprove
 the quote. This deletes the work order and enables the fields in the
 SM Flat Price Revenue form. Once you edit the entries as needed, you
 can then re-approve the quote and generate a new work order.

- Edit Work Order Scope Entries -
 If you do not require edits at the quote level, you can edit the revenue
 entries for the generated work order scope. Entries edited in this manner do
 not update the source quote scope.

## Agreement Services

When you activate an agreement, the system automatically disables all split revenue entries for flat price agreement services. You can only change these entries by either [deactivating the agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-activation--deactivation-form) or [amending the agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-amendments/amend-an-agreement).
Note: You will typically only use the deactivation method if changes to the revenue entries do not affect the original terms of the agreement.
When you generate work orders for agreements (via SM Generate PM Work Orders), the system creates a work order for each applicable agreement/agreement service. All split revenue entries defined for a flat price service are set up for the related work order scope; however, they cannot be edited.

Related tasks

- [Enter Flat Price Revenue](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-flat-rate-agreement-service/enter-flat-price-revenue)
