---
title: "About the JC Material Use Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form"
---

# About the JC Material Use Form

Use this form to post job costs associated with stocked
 materials that you sell to jobs, or miscellaneous materials that you use on your own jobs.


## JC Type

Each transaction is assigned a JC Type. The JC type identifies whether you are posting for stocked or miscellaneous materials.

- IN-Inventory  — Use this type to post costs for materials sold from your own inventory (i.e. materials set up in IN Location Materials). Inputs are provided to allow for specifying the IN company and location from which the materials were sold. Units posted in this form will update the on-hand quantity and records in Inventory. Although a non-standard unit of measure can be used during entry, Inventory will be updated in the standard unit of measure using the conversion factor specified for the non-standard unit of measure. Non-standard units of measure must be defined for the material/location in IN Location Materials, Addl UMs tab.

- MI-Miscellaneous — Use this type to post costs for miscellaneous materials used on your own jobs. Miscellaneous materials include valid materials (set up in HQ Materials) or non-valid materials (not set up in HQ Materials). However, you can only use non-valid materials if the 'Validate Material' option in JC Company Parameters is set to N (unchecked).

## Field Tickets

Field tickets enable you to link various costs (such as materials, labor, and equipment) related to specific work activity on a job, and facilitate owner billing. When you add a material use entry, you can associate the entry to a field ticket for the specified job/contract. You can assign multiple entries to a single field ticket, as long as the ticket has a status of O-Open in JC Field Ticket. If the status is set to Close, Approved, Rejected, or Billed, you can no longer post costs to that ticket.
Once you post the material use batch, the system adds a detail record (with a Source of JC MatUse) to the Cost Detail tab in JC Field Ticket for each material use entry associated with that field ticket.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to material use entries for a job is only useful if the job's contract/contract item has a bill type of T&M or Both.

 For more information about field tickets, see the [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form) article.

## Taxes

The Use Tax checkbox in JC Company Parameters (Material tab) determines whether taxes can be posted in this form. If checked, tax inputs are enabled, allowing you to post taxes to any material, including stocked materials that are flagged as not taxable in HQ Materials. If not checked, the tax fields are disabled and taxes cannot be posted for any material, including stocked materials flagged as taxable in HQ Materials.

## General Ledger

If the GL Material Interface option (Material tab in JC Company Parameters) is set to Detail or Summary, this program creates batch entries to update GL. For each entry, you designate both a Transaction Account and an Offset Account.

- Transaction Account — The expense entry (including tax, if any) debits the account designated for the line's cost type (in JC Dept Mater) based on the contract item to which the phase is assigned. This is true for all materials regardless of whether they are stocked, non-stocked, or miscellaneous materials (not set up in HQ Materials).

- Offset Account — The offsetting entry will credit a GL account based on the following:

- If a stocked material (i.e.
 you specified an IN Co and Location), credits the Job Sales account
 specified for the location in IN Locations, IN Location Company
 Override, or IN Location Co & Category Override. In addition, the
 Cost of Goods Sold and Inventory accounts set up in those forms are
 updated. If the GL companies for IN and JC are different, cross-company
 AP and AR entries are created.Note: . Stocked
 materials are only used when the JC Type is IN-Inventory. When this
 type is selected, the Offset Account field is disabled and cannot be
 overridden.

- If a
 non-stocked material, credits the Non-Stocked GL
 Account defined in HQ Material
 Categories.

- If a
 miscellaneous material (not set up in HQ Materials),
 credits the Misc Matl GL
 Account specified in JC Company
 Parameters (Material tab), less any tax.

- If there is
 tax, the GL Account specified for the tax code in HQ Tax
 Codes is credited

Click the following link for related information about this form.
[JC Add Transaction To Batch Form](/en/vista/vista/costs-and-contracts/job-cost/costs/jc-add-transaction-to-batch-form)
