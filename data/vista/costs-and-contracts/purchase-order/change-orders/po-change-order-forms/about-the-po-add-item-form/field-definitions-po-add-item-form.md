---
title: "Field Definitions: PO Add Item Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form/field-definitions-po-add-item-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form/field-definitions-po-add-item-form"
---

# Field Definitions: PO Add Item Form

## Type

The Type field on the PO Add Item form.

Select the type of PO item that you would like to create. The data required for the purchase order item will differ slightly depending on the type selected.
Note: This field is disabled if there has been activity posted against the PO item (for example, if you have posted a receipt to it).

1-JobUse this type to order materials for jobs. Multiple jobs may be on the same PO and do not have to match the job specified in the PO header. Job items interface with the JC module to update committed costs and units to specific job/phase/cost type combinations. Actual costs are updated through the processing of an invoice against the Purchase Order.When you select this type, additional fields display for entering JC Co, Job, Phase, CT, and Ticket.
2-InventoryRequires the Inventory module.Use this type to purchase items that you stock in your inventory. This type of PO interfaces with the IN module to automatically track items on order and those that have been received but not yet posted as payable in AP.
When you select this type, additional fields display for entering the IN Co and Location. In addition, display only On Hand and On Order fields show the on-hand and on-order amounts for the specified location/material.
3-ExpenseUse this type of PO for ordering goods to be expensed for your company. For example, office supplies and office machines. If you are using the EM module, you should use this type for actual equipment purchases. This type of purchase order only interfaces with AP and GL, and does not generate any committed costs.4-EquipmentRequires the Equipment Management module.
Use this type to purchase items for use with equipment (such as oil, fuel, etc.). Items that fall in this category are typically operating costs such as parts and repair costs. Assigning cost types and cost codes (EM) allows you to track these costs for each piece of equipment. Entries for this type of PO do not directly update EM. The update to EM occurs when the invoice is posted in AP. If you selected the Display last used date for parts in AP/PO/EM checkbox in EM Company Parameters (Parts tab), the screen displays the last used date of the part specified for the PO item (in the informational display above the Item tabs).When you select this type, additional fields display for entering the EM Co, Equip, Comp Type, Component, Cost Code, and CT. The Comp Type and Component fields are only enabled if the equipment is flagged as a component type in EM Equipment.
5-EM Work OrderRequires the Equipment Management module.
Use this type of PO to order items needed to complete work orders set up in the EM module. Entries for this type of PO do not directly update EM. The update to EM occurs when the invoice is posted in AP. If you selected the Display last used date for parts in AP/PO/EM checkbox in EM Company Parameters (Parts tab), the screen displays the last used date of the part specified for the PO item (in the informational display above the Item tabs).When you select this type, additional fields display for entering the EM Co, WO, WO Item, Cost Code, and CT.
6-SM Work OrderRequires the Service Management module.
Use this type of PO to purchase the material needed to complete service work orders (that is, work orders set up in Service Management). Entries of this type will generate a work completed purchase line in SM Work Orders (Work Completed tab), and update the Purchase Orders grid (in SM Work Orders). You can also enter purchase orders for SM work orders in SM Purchase Order Entry. For more information, see [SM Purchase Order Entry
 Form](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form).Note: You cannot edit purchase order information from a work completed purchase line; edits must be made directly to the purchase order item via PO Purchase Order Entry or SM Purchase Order Entry, or to the PO item line in PO Item Distribution. Changes will be updated to the related work completed purchase line.

When you select this type, additional fields display for entering the SM Co, SM Work Order, and SM Scope. If you reference a Job SM work order, additional fields include Phase (display only) and JC Cost Type.

Related information

- [About the PO Add Item Form](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form)

- [PO Change Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/po-change-order-entry-form)

## JC Co/IN Co/EM Co

The JC Co, IN Co, or EM Co fields on the PO Add Item form.
Depending on the type of purchase order, this field will prompt for JC company (Job PO), IN company (Inv PO), or EM company (Equip & Work Order POs).
 Specify the company for posting this purchase order item.

##  Job

 This field initially defaults the job code specified in the purchase order header (PO Purchase Order Entry). Accept the default, or enter the purchasing job for the specified material.

[](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form)PO Add Item
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

##  Phase

 Enter the applicable job phase
 for this purchase order item. This field initially defaults the material phase assigned to
 this line's specified material (in HQ Materials, Matl Phase field). If you did not specify
 a material phase for the material, this field defaults blank.
Note: If you checked the ‘Phases on this job are locked’ box
 in JC Jobs, this phase must be set up for the specified job in JC Job Phases. If you did
 not check the box, you must enter a valid phase from JC Phases.
[](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form)PO Add Item
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

##  CT

The CT field on the PO Add Item form.

This field only displays when the line type is 1-Job.
 Enter the JC cost type that applies to this purchase order. This field initially defaults the material cost type assigned to this line's specified material (in HQ Materials, Matl CT field). If you did not specify a material cost type, this field defaults as blank.
Note: If you selected the Phases on this job are locked checkbox in the JC Jobs form, this cost type must be set up for the specified job in JC Job Phases. If you did not select the checkbox, you must enter a valid phase cost type from JC Phases.

##  Location

 Enter the purchasing inventory location for the specified material or
 press F4
 to select it from a list.
The location must be set up in [IN Locations](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form), and the material must be assigned to this
 location in [IN Location Materials](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form).

[](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form)PO Add Item
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## Equip

The Equip field on the PO Add Item form.
This field only displays for line type 4-Equipment.
Enter the equipment for which you are purchasing the specified material. Press F4 to select from a list of valid equipment.

##  Comp Type

The Comp Type field on the PO Add Item form.
This field only displays for line type 4-Equipment.
Enter the component type (from EM Component Types) for the equipment (if applicable) or press F4 to select from a list of valid component types.

## Component

The Component field on the PO Add Item form.
This field only displays for line type 4-Equipment.
Enter a component for the equipment or press F4 to select from a list of valid components.
 If you entered a component type in the Comp Type field, this field defaults the first component of this type for the indicated equipment (as defined in EM Equipment).

##  WO

The WO field on the PO Add Item form.
This field only displays for line type 5-EM Work Order.
Enter the purchasing EM work order for the specified material or press F4 to select from a list of valid EM work orders.

##  WO Item

The WO Item field on the PO Add Item form.
This field only displays for line type 5-EM Work Order.
Enter the work order item for this purchase order item or press F4 to select from a ist of items for the specified work order.

##  Cost Code

The JC Co, IN Co, or EM Co fields on the PO Add Item form.

This field only displays for line types 4-Equipment and 5-EM Work Order.
 Enter the applicable cost code (as defined in EM Cost Codes) for this Equipment order item or press F4 to select from a list of valid cost codes.
 If this is an Equipment line and you entered a component for this equipment, this field defaults the cost code assigned to the component's type in EM Component Types.

##  CT

The CT field on the PO Add Items form.

This field only displays when the line type is 4-Equipment or 5-EM Work Order.
 Enter the equipment cost type for this Equipment or Equipment Work Order item or press F4 to select from a list of valid equipment cost types.

## SM Co

The SM Co field on the PO Add Item form.

This field only displays when the line type is
 6-SM Work Order.
Enter the SM company to which this purchase
 order item applies. This will be the SM company in which the SM work order was set up.
 Press F4 for a list of valid SM companies.

## SM Work Order

The SM Work Order field on the PO Add Item form.

This field only displays when line type is 6-SM Work Order.
Enter the SM work order to which this purchase order item applies or press F4 to select from a list of valid work orders for the specified SM company.
Note: If you specify a job-related work order and the job associated with the work order has been soft or hard-closed, the system will allow the entry if you allow posting to closed jobs (that is, the Allow Posting to Hard-Closed Jobs and/or Allow Posting to Soft-Closed Jobs checkboxes are selected in JC Company Parameters). If you do not allow posting to closed jobs, a message displays indicating the job is closed and you will be unable to proceed.

## SM Scope Seq

The SM Scope Seq field on the PO Add Item form.

This field only displays when the line type is 6-SM Work Order.
Enter the work order scope to which this purchase order item applies or press F4 to select from a list of valid scopes for the specified work order.

## Phase

This field only displays if the line type is 6-SM
 Work Order and you specified a job-related SM work order.
The system only enables this field when you
 specify a work order scope (in the SM Scope field) that is not assigned a
 phase (in SM Work Orders).
Required.
Enter the phase (from JC Job Phases) to which
 this purchase order item applies.
Note: If the job specified for the work order is locked
 (i.e. the Phases on
 this job are locked box is checked in JC Jobs), the phase entered here must
 be set up for the job in JC Job Phases. If the phase is not set up for the job, you can
 press F5 from this field to access JC Job Phases. Once you add the phase and exit
 JC Job Phases, you can specify the phase here.
If the job is not locked (that is, the
 Phases on this
 job are locked box is not checked in JC Jobs), you can enter any phase from
 JC Job Phases or JC Phases, or any phase that matches the valid part of phase defined in JC
 Company Parameters.
 For example, say the Number of valid characters
 in Phase code field is set to 8 (in JC Company Parameters). The JC Phases
 contains phases 03110-120 and 03110-140-. If you enter phase 03110-120-100, the system will
 allow it since the first 8 characters (bolded) match the first 8 characters of phase
 03110-120-. However, if you enter phase 03110-130-, it will not be allowed, since the first
 8 characters do not match any phase in JC Phases.

[](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form)PO Add Item
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## JC Cost Type

The JC Cost Type field on the PO Add Item form.
This field only displays if the line type is
 6-SM Work Order and you specified a job-related SM work
 order.
Enter the JC cost type (from JC Cost Types)
 for this purchase order item. Initially defaults as follows:

- If you specified an SM Cost Type for the purchase
 order item, this field defaults the JC Cost Type assigned to the SM Cost Type (in SM
 Cost Types).

- If a JC Cost Type is not specified for the SM Cost
 Type or you did not enter an SM Cost Type, this field defaults the Matl CT from HQ
 Materials for the material specified on the purchase order.

- If no Matl CT is specified for the material, this
 field defaults as blank.
Note: The system will assign this cost type to the work completed
 purchase line generated (during the batch process) for this PO item. Edits to this
 cost type can only be made at the PO item level; they cannot be made at the work
 completed purchase line level.Locked Phases vs. Non-Locked Phases.
If the job specified for the work order is locked
 (that is, the Phases on this job are locked checkbox is selected in the JC Jobs
 form), the cost type specified here must be set up for the job/phase in JC Job
 Phases. If the cost type is not set up for the job phase, you can add it by pressing
 F5 from this field to access JC Job Phases. Once you exit JC Job
 Phases, you can enter the cost type here.
If the job is not locked (i.e. the Phases on this job
 are locked box is not checked in JC Jobs), you can use any cost type
 defined for the phase in JC Job Phases or JC Phases.

##  Material

 Enter the material for this purchase order
 item. You can enter any material, valid or invalid, unless entering an Inventory line, in
 which case the material must be a valid material set up for the location in IN Location
 Materials.
 If you enter a invalid material, the material
 description defaults as 'Not in material file' and unit of measure defaults as lump sum
 (LS). If you enter a valid material (set up in HQ Materials), the description, unit of
 measure, and unit cost default from HQ Materials.
 If the material exists in PO Vendor Materials
 for the specified vendor/material group/material, the description, unit of measure, and
 unit cost defaults from PO Vendor Materials.

Equipment Lines
 If the material number exists in EM Equipment
 Parts, the description and unit of measure default from EMEP. Unit cost defaults from
 HQMT.
 If the material number also exists in PO
 Vendor Materials, the description and unit of measure default from EM Equipment Parts, but
 the unit cost defaults from PO Vendor Materials.

Work Order Lines
 If the material number exists in EM Work
 Order Parts or EM Equipment Parts, the description and unit of measure default from EM Work
 Order Parts or EM Equipment Parts, respectively. Unit cost defaults from HQ Materials.
 If the material number also exists in PO
 Vendor Materials, the description and unit of measure will default from EM Work Order Parts
 or EM Equipment Parts, but the unit cost defaults from PO Vendor Materials.
Note: If notes exist for this material in HQ Materials, you
 can add them to the notes for the purchase order item by clicking the Copy Notes
 button (to the right of the tax fields). The system appends material notes to any existing
 PO item notes. If no notes exist for the material, the system disables the Copy Notes
 button.
[About the PO Add Item Form](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form#ID-0002f6ea--en__ID-0002f6ea)
[PO Change Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/po-change-order-entry-form#ID-0002f57c--en__ID-0002f57c)

## Vendor Matl

Enter the vendor’s identification number for this material, if applicable. Press F4 for a list of vendor material numbers.
Note: When using the F4 lookup, sort by the HQMT Material column. This groups the standard and substitute vendor materials together for selection.
If a material exists in PO Vendor Materials for the specified vendor/material group/material, and the vendor material UM is equal to the HQ materials purchase UM, the field defaults the Vendor’s Material ID number. If the vendor material UM does not equal the HQ purchase UM, the field defaults the Vendor’s Material ID from the lowest UM (in PO Vendor Materials) for the vendor/material group/material.
Equipment Lines
If you specify a material number that exists in PO Vendor Materials, but that material number also exists in EM Equipment Parts, the system uses the description and UM from EM Equipment Parts, and the vendor material number will not default.
EM Work Order Lines
If you specify a material number that exists in PO Vendor Materials, but that material number also exists in EM Work Order Parts (EMWP) or EM Equipment Parts (EMEP), it will pull the description and UM from EMWP or EMEP, respectively, and the vendor material number will not default.
Note: Because the system uses the vendor’s material ID# as a cross-reference to the HQ material, you can enter this number if you do not know the HQ material number, and the HQ material number will be provided. This feature is only applicable to materials set up in PO Vendor Materials.
You can also enter the vendor material ID# for any substitute materials that may have been set up for the HQ material in PO Vendor Materials, and have the HQ material number provided.
The system does not validate vendor material numbers.

[](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form)PO Add Item
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

##  Receiving

 Check this box if you will be receiving this item in PO Initialize Receipts or PO Receipts Entry. Using either of these forms to receive purchased items updates the Backordered, Received, and Invoiced fields.
 Do not check this box if you will be using AP Transaction Entry to receive this item.

[](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form)PO Add Item
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

##  Description

The Description field on the PO Add Item form.

 Enter a description for this material, up to 60 characters.
 If you entered a material in the Material field, this field defaults the description from HQ Materials. Otherwise, this field defaults as blank.
This field can default differently depending on the line type and materials that you choose as discussed below.
Job, Inventory, Expense Lines

- If you entered a valid vendor material in the Vendor Matl field, this field defaults the description from PO Vendor Materials.

- If you entered a valid vendor material in the Vendor Matl field and the UM in PO Vendor Materials does not equal the Purchase UM in HQ Materials, the system searches each UM record associated with the vendor/material group/material in PO Vendor Materials looking for a match. If the system does not find a match, this field defaults the description from the last UM record found in PO Vendor Materials.

Equipment , EM Work Order Lines

- If you entered a valid vendor material in the Vendor Matl field, this field defaults from the Description field in PO Vendor Materials.

- If you entered a valid vendor material in the Vendor Matl field and the UM field (PO Vendor Materials) does not equal the Purchase UM field (HQ Materials), the system searches each UM record associated with the vendor/material group/material in PO Vendor Materials looking for a match. If the system does not find a match, this field defaults the description from the last UM record found in PO Vendor Materials.

- For Equipment lines only, if the specified material exists in EM Equipment Parts (EMEP) for the equipment, this field defaults the description from EM Equipment Parts.

- For EM Work Order lines only, if the specified material exists in EM Work Order Parts (EMWP) or EM Equipment Parts (EMEP), this field defaults the description from EMWP or EMEP, respectively.

## GL Co

The GL Co field on the PO Add Item form.

This field is enabled for line type 3-Expense only.
Enter the GL company for this purchase order item or press F4 to select from a list of valid GL companies. Initially defaults the GL company specified in AP Company Parameters.
For all other line types, this field defaults as follows:

- Job - Defaults the GL company assigned to the JC company in JC Company Parameters.

- Inventory - Defaults the GL company assigned to the IN Company in IN Company Parameters.

- Equipment / EM Work Order - Defaults the GL company assigned to the EM company in EM Company Parameters.

- SM Work Order - Defaults the GL company assigned to the SM company in SM Company Parameters.

## GL Account

The GL Account field on the PO Add Item form.

Enter the GL account to charge for this purchase order item. The system uses this account as the default account in AP Transaction Entry; GL updates do not occur from the PO module.
Note: You can override the default value if you selected the Allow GL Account Override when Posting Costs checkbox in JC Company Parameters; otherwise, this field is disabled. If the default is blank, the system allows entry, but disables the field when you save the record.

The defaults for this field depend on the line type:

- Job – Defaults the GL Account defined for the selected cost type or phase (respectively) in JC Departments.

- Inventory – Defaults the Inventory Account specified for the location/category in IN Location Category Override or location in IN Locations (respectively).

- Expense – Defaults from AP Vendors.

- Equipment & Work Order – Defaults from the EM Department file based on cost code or cost type (respectively).

- SM Work Order – Defaults the Cost or Cost WIP (if call type is tracking WIP) GL account from SM Departments assigned to the service center or division specified on the SM work order. The system determines the default based on the cost type category as follows:

- If you specified a division on the work order scope and an alternate department is assigned to the division, the system will first look for an override GL account based on the cost type assigned to the work order scope. If an override account is found for the cost type category, it will default here.

- If no override GL account is found for the cost type category, the system uses the GL account defined for the cost type category in SM Departments.

- If no alternate department is assigned to the division, the system will then use the department assigned to the service center to determine the default GL account.

##  Required Date

 Enter the date this item is required.

[](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form)PO Add Item
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## Pay Category

This field only displays if you checked the Using Payable Category box in AP Company Parameters and if you checked the Specify Pay Type during PO Entry box in PO Company Parameters.
Enter a valid pay category for this purchase order item. The pay category specified here, along with this item's type, determines the default pay type. Initially defaults a pay category as follows:

- If you have set up a standard or user override in F3 Properties (not recommended), this field defaults the F3 pay category.

- If an F3 override does not exist, this field defaults the pay category specified for the current user in VA User Profile.

- If you did not enter an override pay category for the current user, this field defaults the pay category defined in AP Company Parameters (Payable Category Default field).

- If you did not define a default pay category in AP Company Parameters, this field defaults as blank. (In this case, the pay type will default from AP Company Parameters based on the line's type.)

You can leave this field blank or override the default value.
Note: The pay category specified here will override any defaults set by F3, VA User Profile, or AP Company Parameters when you invoice the purchase order in AP Transaction Entry.
[](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form)PO Add Item
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

##  Pay Type

 This field displays only if you checked the Specify Pay Type during PO Entry box in PO Company Parameters.
 Enter the pay type for this purchase order item.
 If you are using pay categories (you checked the Using Payable Category in AP Company Parameters), this field defaults the pay type from this line's pay category based on the line type. May be overridden; however, pay type must be either 'assigned' to the specified pay category or an 'unassigned' pay type. In this case, 'assigned' pay types refer to pay types that have designated the pay category in the 'Restrict Pay Type to Pay Category' field in AP Payable Types. Unassigned pay types are those with the 'Restrict Pay Type to Pay Category' left blank.
 If you are not using pay categories, default will be the standard pay type from AP Company based on the line type. May be overridden.
Note: The pay type specified here will override any defaults set by F3, VA User Profile, or AP Company Parameters when the purchase order is invoiced in AP Transaction Entry.
[](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form)PO Add Item
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## UM

Enter a valid unit of measure for this material.
This field initially defaults as follows:
If a non-valid material was specified (Job, Exp, Equip, and WO lines only), defaults as LS. If a valid HQ material is specified, defaults the purchase unit of measure.
Job/Inv/Exp Lines
If overrides exist for the specified material/vendor in PO Vendor Materials (POVM), defaults the vendor material UM if it matches the HQMT Purchase UM; otherwise, defaults the lowest UM (in POVM) for the vendor/material group/material.
Equipment Lines
If the specified material exists in EMEP (Equipment Parts) for the equipment, UM will default from EMEP if it matches the HQMT Purchase UM; otherwise, default will be the HQMT Purchase UM.
If you specified a vendor material that does not also exist in EMEP, defaults the vendor material UM if it matches the HQMT Purchase UM; otherwise, defaults the lowest UM (in POVM) for the vendor/material group/material.
If material does not exist in EMEP or POVM, defaults the HQMT Purchase UM.
WO Lines
If the specified material exists in EMWP (Work Order Parts) for the work order, UM will default from EMWP, regardless of whether it matches the HQMT Purchase UM.
If the specified material exists in EMEP (Equipment Parts) and does not also exist in EMWP for the work order, UM will default from EMEP if matches the HQMT Purchase UM; otherwise, default will be the HQMT Purchase UM.
If you specified a vendor material that does not also exist in EMWP and/or EMEP for the work order, defaults the vendor material UM if it matches the HQMT Purchase UM; otherwise, defaults the lowest UM (in POVM) for the vendor/material group/material.
If material does not exist in EMWP, EMEP, or POVM, defaults the HQMT Purchase UM.

[](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form)PO Add Item
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## Unit Cost

Enter the unit cost for this material. This
 field initially defaults a unit cost as follows:
Job, Exp, Equip, WO Lines – Defaults the unit
 cost defined for the material in HQ Materials, unless pricing overrides exist in PO
 Category Discounts or PO Vendor Materials. In which case, unit cost defaults as described
 below in the “Category/Vendor Pricing Overrides” section.
Inventory Lines – Defaults the Last Unit Cost
 for the material from IN Location Materials, unless pricing overrides exist in PO Category
 Discounts or PO Vendor Materials. In which case, unit cost defaults as described below in
 the “Category/Vendor Pricing Overrides” section.

Category/Vendor Pricing Overrides
If you have set up vendor pricing overrides in
 either PO Category Discounts or PO Vendor Materials, the unit cost will default from these
 overrides for all line types. If a discount exists for the vendor and material category in
 PO Category Discounts, it will apply the discount to the standard unit price in HQMT to
 determine the default unit cost. If an override exists for the material and vendor in PO
 Vendor Materials, it will default a unit cost based on the cost option (std unit cost,
 vendor unit cost, std book price less discount, or vendor book price less discount) or the
 job override (if one exists).
Note: If the unit of measure is other than LS, and you enter
 a zero unit cost, the total cost must be zero. In addition, you will need to invoice the
 items to ensure that JCCD (Cost Detail) and POIT (PO Items) are in balance before you close
 the PO.
[About the PO Add Item Form](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form#ID-0002f6ea--en__ID-0002f6ea)
[PO Change Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/po-change-order-entry-form#ID-0002f57c--en__ID-0002f57c)

##  ECM

The ECM dropdown on the PO Add Item form.
Select which quantity the unit cost represents or accept the default.

- E – Per each

- C – Per Hundred

- M – Per Thousand

## Tax Type

The Tax Type field on the PO Add Item form.

Select the tax type for this PO item line.

- 1-Sales – Tax amounts are payable to the vendor and are added to the purchase order total. This tax amount is directly charged to GL.

- 2-Use - Tax amounts are accrued and paid at a later date to the appropriate State or Local taxing authority. Calculated tax amounts do not affect the gross or net balance due to the vendor. Instead, the transaction's gross and tax amounts are charged to a GL account with an offsetting liability account as defined in HQ Tax Codes. Use the AP Tax Report to obtain an itemization of use tax amounts.

- 3-VAT (Value Added Tax) – This tax applies to Australian and Canadian companies. It is paid on goods and services at each stage of production or distribution, and is based on the value added at each stage. This tax is tracked in GL and reduces the payment to a taxing authority through an Input Tax Credit (ITC). This tax is not directly expensed. Use the AP Value Added Tax Report to obtain an itemization of VAT amounts.

### SM Work Order Lines

For purchase order items with a line type of 6-SM Work
 Order, this field defaults based on the SM Cost Type entered for the
 purchase order item, and the Matl Tax Override and Tax Option Override options selected
 on the associated work order scope. You may override the defaults as needed.
The following table describes the default behavior for SM-related
 purchase order line items.
SM Cost TypeMaterialTax Option OverrideMatl Tax OverrideDefault
Note: If the PO vendor is not
 assigned a tax code and the work order scope's tax source (service site
 or service center) is not assigned a tax code, all tax fields default as
 blank, but may be overridden.

Not TaxableBlankAllAllBlank
Not Taxable
Taxable
TaxableNot TaxableAllAllBlank
TaxableAllN - No TaxBlank
P - Taxable at Purchase Only, M -
 Taxable at Purchase/Markup at Billing, F - Full Tax at Purchase and
 BillingIf Blank or 1-Sales1-Sales (US) or 3-VAT (AU/CA)
If 2-Use (US only)2-Use (US only)
N - Not Taxable, B - Taxable at Billing
 OnlyAllBlank
BlankP - Taxable at Purchase Only, M -
 Taxable at Purchase/Markup at Billing, F - Full Tax at Purchase and
 BillingIf Blank or 1-Sales1-Sales (US) or 3-VAT (AU/CA)
If 2-Use (US only)2-Use (US only)
N - Not Taxable, B - Taxable at Billing
 OnlyAllBlank

## Tax Code

The Tax Code field on the PO Add Item form.

Entry in this field requires that you first enter a Tax Type.
Enter the tax code to use for this purchase order item or accept the defaulted value. Press F4 to select from a list of valid tax codes for the specified Tax Type.
This field defaults as follows:
Job LinesThe default for job lines is determined by the setting of the Base Tax On field in JC Jobs.

- J-Job - The tax code defaults from JC Jobs ( Tax Code field). If no tax code is specified for the job, the default will be null.

- V-Vendor - The tax code defaults from AP Vendors ( Tax Code field). If a tax code is not specified for the vendor, the default will be null.

- O-Vendor Override - The tax code defaults from AP Vendors. If a tax code is not specified for the vendor, the tax code will default from JC Jobs. You can override the default as necessary.

Inv / Exp / Equip / EM WO / SM WO LinesFor all non-job lines, the tax code defaults as follows:

- If you specified a Ship Location (PO header) and the ship location is assigned a tax code, that tax code defaults here.

- If the ship location is not assigned a tax code or you do not specify a ship location, this field defaults as follows:

- Inventory lines - Defaults the tax code specified for the inventory location. If no tax code is specified for the location, this field defaults as blank.

- Exp / Equip / EM Work Order lines - Defaults the tax code from AP Vendors for the vendor specified in the PO header. If a tax code is not assigned to the vendor, this field defaults as blank.

- SM Work Order lines - Defaults the tax code from AP Vendors for the vendor specified in the PO header. If a tax code is not assigned to the vendor, this field defaults based on the Tax Type.

- If the tax type is Sales or VAT, this field defaults the Tax Code assigned to the service site or service center, depending on the tax source specified for the work order scope.

- If the tax type is Use, this field defaults the Use Tax Code assigned to the service site or service center, depending on the scope's tax source. If no Use Tax Code is specified, it defaults the Tax Code specified for the tax source.

- If no tax codes (sales or use) are defined for the tax source, this field defaults as blank.

Note: If the SM work order is a job work order, the default behavior is the same as described above for Job Lines.

Intercompany TransactionsFor intercompany invoices, the tax code defaults as follows:

- If the tax type is Sales or VAT (Value Added Tax), the tax code defaults based on the Tax Group assigned to the AP Company.

- If the tax type is Use, the tax code defaults based on the Tax Group assigned to the 'posted to' company

### Committed Costs (Job Lines)

If you post a job cost line (JC type) with tax, the system relieves committed costs from the phase/cost type in JC Cost Detail table for the tax amount as follows:

- if phase or cost type overrides do not exist for the tax code, the system uses the phase and cost type specified for the PO item.

- if phase and cost type overrides exist for the tax code, the system uses the tax code phase and cost type.

- if a phase override exists for the tax code, but a cost type override does not exist, the system uses the tax code phase and the cost type from the PO line.

- if a cost type override exists for the tax code, but a phase override does not exist, the system uses the phase from the PO line and the tax code cost type.
Note: In all cases, the system updates JC with the tax rate amount. When you create an AP transaction for this PO item, the system relives the original tax rate amount from JC, but uses the current tax rate when creating an invoice.

### Redirect Phase/Cost Type

If this PO item is for a job (line type 1-Job) or a job-related SM work order (line type 6-SM Work Order) and the tax code is assigned a redirect phase and/or cost type (JC Tax Phase and/or JC Cost Type in HQ Tax Codes), the system validates the phase and/or cost type based on the Phases on this job are locked checkbox in JC Jobs.
If the Phases on this job are locked checkbox is selected and:

- The tax code specifies a redirect phase only, the phase must exist in JC Job Phases for the PO Item job (if a 1-Job line) or the work order job (if a 6-SM Work Order line).

- The tax code specifies both a redirect phase and cost type, the phase/cost type combination must exist for the specified job in JC Job Phases.

- The tax code specifies a redirect cost type only, the cost type must exist in JC Job Phases for the PO item phase (Job line) or the work order scope phase (SM Work Order line). For SM Work Order lines, if you have not assigned a phase to the work order scope, the cost type must exist for the PO item phase.

If the Phases on this job are locked checkbox is not selected and

- The tax code specifies a redirect phase only, the phase must exist in JC Job Phases or JC Phases for the PO Item job or the SM work order job.

- The tax code specifies both a redirect phase and cost type, the phase/cost type combination must exist for the specified job in JC Job Phases or JC Phases.

- The tax code specifies a redirect cost type only, the cost type must exist in JC Job Phases or JC Phases for the PO item phase (Job line) or the work order scope phase (SM Work Order line). For SM Work Order lines, if you have not assigned a phase to the work order scope, the cost type must exist for the PO item phase.

Note: If validation determines that the conditions indicated above do not exist, you will need to either use a different tax code or add the phase and/or cost type combination to JC Job Phases or JC Phases (depending on the "locked phases" flag) before you can post the batch.

##  Supplier

 Enter the supplier number for this purchase order. Press F4 for a list of vendors from AP
 Vendors.
 Use this field for purchase order items where a second party, other than the vendor, is involved.

[](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/about-the-po-add-item-form)PO Add Item
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry
