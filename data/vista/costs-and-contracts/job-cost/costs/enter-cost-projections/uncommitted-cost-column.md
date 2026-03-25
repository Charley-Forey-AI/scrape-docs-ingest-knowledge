---
title: "Uncommitted Cost Column | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/uncommitted-cost-column"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/uncommitted-cost-column"
---

# Uncommitted Cost Column

The Uncommitted Cost column in JC Cost Projections displays costs that have been entered into the PM
 module but have not been interfaced with the accounting modules using PM Interface.
For example, subcontracts, subcontract
 change orders (SubCOs), purchase orders, and PO change orders (POCOs) that have been
 created in the PM module but have not been interfaced. The amounts in this column do not
 include taxes.
To add the Uncommitted Cost column to the form,
 select File > Projection
 Options. This will open JC Projection Options. Open the Display Columns tab and
 check the Uncommitted Cost box.
Below is a list of items that are included in the
 Uncommitted
 Cost column:

- Subcontract detail ([PM Subcontract Detail](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)) that is not associated with
 a pending change order(PCO) or subcontract change order(SubCO), and not interfaced
 with the accounting modules. This could be subcontract detail entered using an ACO(
 PM Approve Change Orders) or a new subcontract entered using PM Subcontract Detail.

- PO detail ([PM Material Detail](/en/vista/vista/project-management/materials/pm-material-detail-form)) that is not interfaced with the
 accounting modules, and not associated with a PCO or PO change order. This could be
 PO detail entered using an ACO( PM Approve Change Orders) or a new PO entered using
 PM Material Detail.

- Subcontract change orders ([PM Subcontract Change Orders](/en/vista/vista/project-management/subcontracts/pm-subcontract-change-orders-form)) – The SCO cannot be
 associated with a PCO and it cannot be interfaced with the accounting modules.

- PO Change Orders ([PM PO Change Orders ](/en/vista/vista/project-management/materials/pm-po-change-orders-form)) – The POCO cannot be
 associated with a PCO and it cannot be interfaced with the accounting modules.

- Uncommitted cost on a PCO – This is the purchase amount on the
 Estimate/Details tab of PM Pending Change Orders. This will be included if all of
 the following is true.

- It is not associated with a subcontract change order or PO change order.

- The PCO item has a status that is set up to display, or display and
 calculate in projections. A status is associated with a PCO item using the Status
 field on the Info tab in the lower portion of PM Pending Change Orders. Projection
 options on statuses are set up using the Projection Options field on [PM Status IDs](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form).

- The document type on the PCO is set up to be included in projections. A
 document type is associated with the PCO using the PCO
 Type field on [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form). The document type is set
 up to be included in projections using the Include in Projections box on PM Document
 Types.

- The selection in the Buyout box on JC Cost Projections
 is set to include PCO uncommitted costs.

If the Buyout box on JC Cost Projections is
 checked, the PCO uncommitted costs will be included.
If the Buyout box is not checked, the
 following applies:

- If the total committed cost is 0 or the current
 estimated cost is less than the total committed cost, then the PCO uncommitted
 cost will display in the Uncommitted Cost column.

- If the current estimated cost is greater than
 the total committed cost, then the Uncommitted Cost column is
 calculated using the following formula: (current estimated cost – total
 committed cost) + PCO uncommitted cost).
