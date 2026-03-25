---
title: "Field Definitions: PM Document Types Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/pm-document-types-form/field-definitions-pm-document-types-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/pm-document-types-form/field-definitions-pm-document-types-form"
---

# Field Definitions: PM Document Types Form

The following is a list of field descriptions for the PM
 Document Types form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Document Type

 Enter a code, up to 10 characters, that will identify this type of document.

[](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)PM Document Types

## Description

Enter a description of this document type. The value in this field can be up to 30 characters long.

[](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)PM Document Types

## Document Category

Select the document category associated with the document type.
If you select "Pending Change Order", the fields on the form that only apply to PCO types will be enabled. Click [here](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) for information on creating PCO types.
RFQs
The Request For Quote document option only
 applies to the enhanced [PM Request For Quote](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview/pm-request-for-quote-form) form.
Document types associated with this category cannot be assigned to an RFQ created using the PM Request For Quote - 6.6 form.
Submittals - 6.5
The Submittals - 6.5 option is for document
 types that apply to the submittals created using the [PM
 Submittals - 6.5](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittals---6.5-form) form. The system will automatically assign this document
 category to submittal types created prior to upgrading to version 6.6.
[](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)PM Document Types

##  Active

 Check this box to activate a document type. Only active document types can be assigned to a record (RFIs, pending change orders, etc.).
 If you uncheck this box, the documents assigned to the 'inactive' document type can still be processed.
PM Document Tracking and PM Document Tracking History will include inactive document types because these forms are only used for viewing/tracking the status and activity of documents for a project. PM Transmittals will also allow inactive document types because it is only used to assign existing documents to transmittals. However, the Document Type lookups in these forms will not display inactive document types.

[](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)PM Document Types

## Include in Cost Projections

The Include in Cost Projections checkbox on the PM Document Types form.
This checkbox is only enabled for document types with a Document Category of
 ‘Pending Change Order’.
Select this checkbox to include pending change
 orders assigned this document type in cost and revenue projections.

- For
 Cost Projections, if you select this checkbox, pending
 change orders of this type will display on the Future COs tab of the PM Cost
 Projection Editor form.

- For
 Revenue Projections, if you select this checkbox, pending
 change orders of this type will display in the JC Revenue Future CO form
 (accessed from JC Revenue Projections by selecting Options > Future Change
 Orders).

Pending change order units and amounts will also be included in the Future CO columns in JC
 Cost Projections, JC Revenue Projections, and JC Override Projections (Cost and Revenue
 tabs).
Note: This checkbox works in conjunction with the
 Projections Option defined (in PM Status IDs) for the status code assigned to the pending
 change order when determining whether to include a pending change order in cost and/or
 revenue projections as follows:

- If the status code assigned to a PCO has a Projections Option of ‘None’, the
 PCO will not display in the JC Projection Future CO or JC Revenue
 Future CO forms, nor will the change order amounts be included in any
 of the ‘Future CO’ columns, regardless of whether this flag is checked
 for the PCO’s document type.

- If the status code’s Projections Option is set to ‘Display in Projections’
 or ‘Display & Calculate in Projections’, this flag must also be
 checked in order for pending change orders to be included in cost
 and/or revenue projections.

If this checkbox is not selected, pending change
 orders with this document type are excluded from cost and revenue projections.
[PM Document Types Form](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)
[About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

## Include Default Add-ons and Markups

This checkbox is only enabled when Pending
 Change Order is selected in the Document Category drop down.
Check this box to include add-ons and markups
 on pending change orders that impact estimates, purchase orders, and subcontracts. When a
 new pending change order is created using [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)and the Estimate,
 SL,
 or PO
 box on the Info tab is checked, the system will automatically include all add-ons defined
 for the project in PM Project Add-ons, in addition to any markups defined for cost types on
 the project that are specified on the change order.
Leave this box unchecked if you do not want
 add-ons and markups included on pending change orders that impact estimates, purchase
 orders, or subcontracts. When a new internal pending change order is added, the system will
 only include add-ons if the Contract box on the Info tab is checked.
 Markups will be initialized for cost types specified on the change order; however, all
 values will be set to 0.00.
[](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)PM Document Types

## Pricing Method

Use this field to set the default value of the
 Pricing
 Methodfield on the Info tab of PM Pending Change Order when creating a
 PCO of this document type. Click [here](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form/field-definitions-pm-pending-change-orders-form#ID-0002a250--en) for information on the Pricing Method field on PM
 Pending Change Orders.
This field only defines the default value. Users will be able to change the default selection if it does not apply.
This field is only enabled when Pending Change Order
 is selected in the Document Category drop down menu.
[](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)PM Document Types

## Estimate

This field is only enabled when Pending Change Order is selected in the
 Document
 Category
 drop down menu.
Select this checkbox to default the

 Estimate
 checkbox in PM Pending Change Orders (Info tab) as selected when creating a
 PCO of this document type.
Leave this checkbox unselected to default the Estimate  check
 box in PM Pending Change Orders as unselected when creating a PCO of this document
 type.
Click [here](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form/field-definitions-pm-pending-change-orders-form#ID-0002a1c7--en) for information about the
 Estimate

 field on PM Pending Change Orders.
Note: This field only defines the default value. You can change the default selection in PM
 Pending Change Orders if it does not apply.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form/field-definitions-pm-pending-change-orders-form#ID-0002a1c7--en)PM Pending Change Order - Budget field
[](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)PM Document Types

## SL

This field is only enabled when Pending Change Order is selected in the
 Document
 Category
 drop down menu.
Select this checkbox to default the
 SL
 checkbox in PM Pending Change Orders (Info tab) as selected when creating a PCO of this
 document type.
Leave this checkbox unselected to default the SL checkbox in
 PM Pending Change Orders as unselected when creating a PCO of this document type.
 Click [here](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form/field-definitions-pm-pending-change-orders-form#ID-0002a1e6--en) for information on the SL field on PM
 Pending Change Orders.
Note: This field only defines the default value. You can change the default selection in PM
 Pending Change Orders if it does not apply.

[](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)PM Document Types

## PO

This field is only enabled when Pending Change Order is selected in the
 Document
 Category
 drop down menu.
Select this checkbox to default the
 PO
 checkbox in PM Pending Change Orders (Info tab) as selected when creating a PCO of this
 document type.
Leave this checkbox unselected to default the PO checkbox in
 PM Pending Change Orders as unselected when creating a PCO of this document type.
 Click [here](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form/field-definitions-pm-pending-change-orders-form#ID-0002a20e--en) for information on the PO field on PM
 Pending Change Orders.
Note: This field only defines the default value. You can change the default selection in PM
 Pending Change Order if it does not apply.

[](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)PM Document Types

## Contract

This field is only enabled when Pending Change Order is selected in the
 Document
 Category drop down menu.
Select this checkbox to default the
 Contract
 checkbox in PM Pending Change Orders (Info tab) as selected when creating a
 PCO of this document type.
Leave this checkbox unselected to default the Contract check
 box in PM Pending Change Orders as unselected when creating a PCO of this document type.
 Click [here](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form/field-definitions-pm-pending-change-orders-form#ID-0002a236--en) for information on the Contract field
 on PM Pending Change Orders.
Note: This field only defines the default value. You can change the default selection in PM
 Pending Change Order if it does not apply.

[](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)PM Document Types

## PCO Date 1/2/3

Enabled only for document types with a
 Document
 Category of Pending Change Order.
These fields are user-defined date fields (up
 to 30 characters each) that are tracked at the pending change order header level for this
 document type. The data entered in these fields will be used as the headings for the
 corresponding date columns in PM Change Orders (Pending tab), PM Pending Change Orders
 (Grid and Info tabs), and PM Document Tracking (Pending Change Orders tab).
Examples
Date Received, Sent for Approval, Approved
[](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)PM Document Types

## Show PCO Date 1/2/3 in Grid

Check this box to have the selected PCO Date field displayed when working with pending change orders. When checked, the specified date field will display in PM Change Orders (Pending tab) and PM Pending Change Orders (Grid and Info tabs), as well as in PM Document Tracking for any view including Pending Change Orders.
Note:If no description was entered in the selected PCO Date field, and you check this box, the column heading will appear as Date 1, Date 2, or Date 3 (depending on the date field for which you checked this box).

Uncheck this box if you do not want the selected PCO Date field to display when working with pending change orders (in PM Change Orders, PM Pending Change Orders, and PM Document Tracking).

[](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)PM Document Types

## Item Date 1/2/3

Enabled only for document types with a Document Category of ‘Pending Change Order’.
These fields are user-defined date fields (up to 30 characters each) that are tracked at the pending change order item level for this document type. The data entered in these fields will be used as the headings for the corresponding date columns in PM Pending Change Orders (Items section, Grid and Add’l Info tabs).
Examples
Item Submitted, Item Approval Required By, Item Approved.

[](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)PM Document Types

## Show Item Date 1/2/3 in Grid

Check this box to have the selected Item Date field displayed when working with pending change order items. When checked, specified date field will display in PM Pending Change Orders (Grid and Add’l Info tabs).
Leave this box unchecked if you do not want the selected Item Date field to display when working with pending change order items (in PM Pending Change Orders).

[](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form)PM Document Types
