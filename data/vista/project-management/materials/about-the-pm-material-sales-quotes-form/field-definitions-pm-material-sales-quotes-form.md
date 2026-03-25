---
title: "Field Definitions: PM Material Sales Quotes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/materials/about-the-pm-material-sales-quotes-form/field-definitions-pm-material-sales-quotes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/materials/about-the-pm-material-sales-quotes-form/field-definitions-pm-material-sales-quotes-form"
---

# Field Definitions: PM Material Sales Quotes Form

The following is a list of field descriptions for the PM
 Material Sales Quotes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Specify the project for which to set up a quote. Must be a valid project set up in PM Projects.

##  MSCo

 Enter a valid material sales company.

##  Quote

 Enter the quote number. It can be up to 10 characters long.
If you the Auto-generate Quote
 #'s box is checked (MS Company
 Parameters > Info
 tab), enter a '+', 'n', 'N', or 'New' and then press TAB and the system will
 automatically assign the new record the next available number based on the Last Used
 Quote# field on the [MS Company Parameters](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-company-parameters-form) form.
 If a quote already exists for the project, the quote number will default automatically. Only one quote can exist per project and MS Co; therefore, you will not be able to add a new quote. Quote detail added for the project will be set up on the existing quote.

##  Description

 Enter a description for this quote, up to 30 characters. Initially defaults the project description.

##  Contact

 Enter the person to contact regarding this quote, up to 30 characters. Initially defaults the project manager for the project.

##  Phone

 Enter the contact's phone number. Initially defaults the job phone.

##  Price Template

 Specify the price template to use for material price defaults. This template will only be used if no material-specific pricing or pricing overrides exist for the quote. Must be a valid price template set up in MS Price Templates.

## Tax Code

Enter the tax code to use for calculating taxes on materials. Initially defaults as defined for the project (in PM Projects). If no tax code assigned to the project, defaults as null.
Note:This tax code will only be used if the tax option in MS Company Parameters is set to 2 (Sale Type/Purchaser) or 3 (Sale Type/Purchaser or Sales Location), and overrides the tax code specified for the project.

##  Active

 Check this box to activate this quote. Once interfaced, pricing set up on this quote will be used during ticket entry and hauler time sheet entry (in MS).
 Do not check this box if this quote is inactive.

[](/en/vista/vista/project-management/materials/about-the-pm-material-sales-quotes-form)PM Material Sales Quotes

##  Use Metric UM

 Check this box to use metric units of measure when selling materials set up on this quote. When quoted materials are specified on a ticket (MS Ticket Entry), the material's metric unit of measure will default as the sales unit of measure (i.e. the unit of measure in which the material is being sold). A metric unit of measure must be defined for the material in IN Location Materials (Add'l U/M tab). If no metric unit of measure is defined for the material, the sales unit of measure will be used. (Note:Checking this box does not affect the unit of measure default for materials added to the quote. Default will always be the sales unit of measure for the material, which may be overridden.)
 Leave this box unchecked if you do not want to use the metric unit of measure when selling materials on this quote. Materials specified on a ticket will default the sales unit of measure.
Note: If you will be using any of the MS Ticket Batch imports (e.g. Alkon, AMI, Libra, Seltec, etc.), and you specified to Use Viewpoint Default Value for UMs in your template, checking this option for a quote will cause the imported UM, Unit Price, and Units values to be converted to metric. If you do not want this conversion to occur, you will need to uncheck this option for the quote or uncheck the Use Viewpoint Default Value in the import template (IM Template Detail).

## Haul Tax Option

Indicate whether haul charges on this quote are taxable. The option specified here overrides the "Haul Tax Option" specified for this project in PM Projects.
0=Not Taxable. Haul charges are not taxable.
1=Taxable Using Haul Vendor. Haul charges are only taxable when using an outside vendor to haul materials.
2=Always Taxable. Haul charges are always taxable, regardless of whether using company vehicle or outside haul vendor.

##  Quoted By

 Informational only.
 Enter the name of the person who prepared this quote, up to 30 characters.

##  Quote Date

 Informational only.
 Enter the date for this quote.

##  Expiration Date

 Informational only.
 Enter the expiration date for this quote; that is, the date through which the pricing on this quote is valid.

## Apply Price Escalators

This
 field is only applicable if you are using the oil price escalation/de-escalation feature
 (i.e. have set up price indexes in HQ Escalation Index).
Check this box to apply price escalators (defined in HQ Escalation Index) to this job quote. When checked, the MS Oil Price Escalation report tracks sales of applicable materials (e.g. asphalt mixes) to this job in MS Ticket Entry, and determines increases/decreases in pricing based on the bid index date specified below and the price index (monthly escalation/de-escalation). Use the MS Oil Price Escalation report to review the resulting pricing adjustments.
Note: If you checked the Apply Price Escalators box for
 the project (in PM Projects/JC Jobs), the bid index date specified on the quote will
 take precedence over the job/contract start date. The job/contract start date will only
 be used if no quote exists for the job.

Leave this box unchecked if you are not using the oil price escalation/de-escalation feature or if not applying price escalators to this job.
[Click here for more information about the price escalation feature](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-escalation-index-form).

## Bid Index Date

This field is only enabled when you have checked the Apply Price Escalators box, and is only applicable if you are using the oil price escalation/de-escalation feature (i.e. have set up price indexes in HQ Escalation Index).
Enter the bid index date for this job quote. This is generally the first day of the job’s start month and will become the starting date for price escalation. The system will use this date in conjunction with the price index (defined in HQ Escalation Index) to determine price escalation adjustments.
Note: If you have also checked the Apply Price Escalators for the project PM Projects, the bid index date specified here will take precedence over the job/contract start date. The job/contract start date will only be used if no quote exists for the job.

##  Phase

 Enter the phase that will be charged for this material. Must be a valid phase or job phase (if locked phases).

##  Cost Type

 Enter the cost type for this material. Must be a valid cost type for the phase.

##  Location

 Enter the location from which the quoted material will be sold. Must be a
 valid location set up in IN Locations.

##  Material

 Enter the material you are quoting. Must be an active material set up in HQ Materials. Quoted material does not need to be stocked at the specified IN location.

##  UM

 Specify the unit of measure for this material. Initially defaults the sales UM specified for the material in HQ Materials. May be overridden, but must be either the standard unit of measure for the material or a valid unit of measure for this material (i.e. set up for the material in HQ Materials, Add’l UMs tab).

##  Units

 Enter the number of units needed of this material.

##  Unit Price

 Enter the unit cost for this material. If the material is stocked, defaults a value based on the Pricing Option for Jobs in IN Company Parameters, the cost/price values in IN Location Materials, and the markup/discount rate specified in IN Location Materials.
 If the material is not stocked in Inventory, default the unit cost specified in HQ Materials (for the specified UM).

##  ECM

 Specify the quantity the unit cost represents.

- E = Per Each Unit

- C = Per 100 Units

- M = Per 1,000 Units

##  Date Required

 Enter the date by which this material is required.

##  Send

Select this checkbox if this material sales quote item is ready to be interfaced. This box must be selected in order for this item to be updated when the material sales quote is interfaced to MS (via PM Interface).
 Clear this checkbox if this material sales quote item is not ready to interface. When interfacing this material sales quote to MS, the system will skip this item.

##  Notes

Enter any miscellaneous notes about this material sales quote item. The space allowance is virtually unlimited.
 To use the Spell Check feature, click the Spelling
 icon on the toolbar or select Tools >  Spelling
  to spell check the text in this field.
You can add a Standard Note for this material sales quote item. Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field, right
 click the mouse while focus is in the field and select Standard
 Notes from the shortcut menu, which opens the Standard Note Copy window.
 Then enter the standard note to copy (or select from F4 lookup) and click OK. The
 system inserts the selected note into the field.

## Notes

Enter any notes that apply to the quote.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.
