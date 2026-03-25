---
title: "Field Definitions: SL Add Item Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-add-item-form/field-definitions-sl-add-item-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-add-item-form/field-definitions-sl-add-item-form"
---

# Field Definitions: SL Add Item Form

The following is a list of field descriptions for the SL Add
 Item form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Job

 Enter the job associated with the subcontract
 item or press F4 to select one from a list.
 This is the job that the committed costs will
 be posted to in the Job Cost module.

## Phase

Enter
 the phase that committed costs will be posted to in the Job Cost module or press F4 to select it
 from a list.
Note: If the Phases on this job are locked box is
 checked for the job (in JC Jobs), the default phase must be set up for the job in JC Job
 Phases before it will be accepted here.

## CT

Enter a cost type or press F4 to select
 one from a list.

##  UM

 Enter a unit of measure for the subcontract
 item or press F4 to select it from a list.
Units of measure are created and maintained using the [ HQ Units of Measure ](/en/vista/vista/administration/headquarters/company-setup/hq-units-of-measure-form) form.

## GL Account

This is the GL account that will be debited when AP transactions
 are posted to this SL item. This field initially defaults the cost type’s GL account. GL
 accounts are assigned (in JC Departments) to cost types based on the department assigned to
 the phase’s contract item.
Entry in this field is only allowed if:

- The Allow GL Account Override box is
 checked in JC Company Parameters (GL Cost tab) or,

- The Allow GL Account Override box is
 not checked, but a GL account was not specified for the cost type in JC
 Departments.

## Work Complete Retainage %

 Enter the work complete retainage percentage for the subcontract item.
This field will default based on the phase
 entered in the Phase field.
The diagram below outlines how the system determines the default value for this field.

## Stored Materials Retainage %

Enter the stored materials retainage percentage.
This field defaults based on the phase entered
 in the Phase field.
The diagram below outlines how the system determines the default value for this field.

## Supplier#

For use with subcontract items in which a second party, other than the
 subcontractor, is involved.
Enter the supplier number from [AP Vendors ](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form) or press F4 to select it from a list.

## Description

Enter a description of the subcontract item. The description can be up to 60 characters long.

## Tax Type

Select
 the tax type for the subcontract item.

- 1-Sales– Tax amounts are payable to the vendor and are added to the invoice total. This tax amount is directly charged to Job Cost, Equipment, and GL.

- 2-Use– Tax amounts are accrued, and will be paid at a later date to the appropriate State or Local taxing authority. Calculated tax amounts do not affect the gross or net balance due to the vendor. Instead, the transaction’s gross amount and tax amount is charged to Job Cost, Equipment, and GL account with an offsetting liability account as defined in HQ Tax Codes. Use the AP Tax Report to obtain an itemization of use tax amounts.

- 3-VAT(Value Added Tax) – This tax is paid on goods and services at each stage of production or distribution, and is based on the value added at each stage. This tax is tracked in the GL and reduces the payment to a taxing authority through an Input Tax Credit (ITC). This tax is not directly expensed. This option is the default for Canadian and Australian companies (Default Country field, HQ Company Setup). Use the AP Value Added Tax Report to obtain an itemization of VAT amounts.

 This field initially defaults as follows:

- If the Use default tax code for
 subcontracts box is checked in JC Jobs and, the active company's
 Default Country is 'US' (in HQ Company Setup), defaults as 1-Sales. the active
 company's Default Country is other than 'US' (e.g Canada or Australia), defaults as
 3-VAT.

- If the Use default tax code for
 subcontracts box is unchecked, tax type defaults as null, regardless
 of country.

Note: Once you specify a code in this field and a tax type
 in the Tax
 Type field, the system displays the tax amount in the Tax Rate
 display field. The tax amount will also display on the Purchase Order when printed, and
 will also show when invoicing in AP.

## Tax Code

Enter
 a tax code for this subcontract item, if applicable. Press F4 for a list of valid tax
 codes.
This field initially defaults as follows.

- If the Use default tax code for
 subcontracts box is checked in JC Jobs and,

- the active company's Default
 Country is other than 'US' (in HQ Company Setup), defaults the
 tax code defined for the job (in JC Jobs).

- the active company's Default
 Country is 'US' (in HQ Company Setup), the default for this
 field is determined by the setting of the Base Tax On drop-down field
 in JC Jobs. If the field is set to J-Job, the tax code defaults
 from JC Jobs (Tax Code field). If the field
 is set to V-Vendor, the tax code
 defaults from AP Vendors (Tax Code field). If the field
 is set to O-Vendor Override, the tax
 cod defaults from AP Vendors. If a tax code is not specified there, the tax
 code will default from JC Jobs. You can override the default as necessary.

- If the
 Use default tax code for subcontracts
 box is unchecked, tax code defaults as null, regardless of country.

- If using F4 to look up valid tax codes, the Tax Type determines the lookup to display. For Sales and Use tax, the standard Tax Codes lookup is used. If the tax type is VAT, the VAT Tax Codes lookup displays.

- Once you specify a code in this field and a tax type
 in the Tax
 Type field, the system displays the tax amount in the Tax Rate
 display field. The tax amount will also display on the Purchase Order when printed,
 and will also show when invoicing in AP.
