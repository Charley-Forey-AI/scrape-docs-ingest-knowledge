---
title: "Field Definitions: MS Price Find Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/about-the-ms-price-find-form/field-definitions-ms-price-find-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/about-the-ms-price-find-form/field-definitions-ms-price-find-form"
---

# Field Definitions: MS Price Find Form

The following is a list of field descriptions for the MS
 Price Find form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Customer Type

 Specify the type of purchaser for which you are trying to locate information. Corresponding inputs will display on the screen.

##  Customer

 Specify the customer (from AR Customers) for locating pricing information.

##  Cust Job

 Specify the customer job for locating pricing information. Press F4 for a list of jobs for the specified customer.

##  Cust PO#

 Specify the customer PO for locating pricing information. Press F4 for a list of POs for the specified customer.

##  JC Co#

 Specify the JC company for locating pricing information.

##  Job

 Specify the job (from JC Jobs) for locating pricing information.

##  INCo

 This field only displays when restricting by ‘Inventory’ sale type.
 Check this box to restrict the addition of tickets to this batch by Inventory company.
 Leave this box unchecked if not restricting tickets by IN company.

##  To Location

 Specify the “sell to” location (from IN Locations) for locating pricing
 information.

##  Price Template

 This field initially defaults the price template specified on the quote,
 if one exists. If a quote does not exist, this field defaults the price template specified
 for the purchaser in AR Customers, JC Jobs, or IN Locations, depending on the purchaser
 type selected in the Customer Type field. You can override this field or leave it blank.

##  Effective Date

 Enter the effective date (MS Price Templates) for template prices.

##  Discount Template

 This field is accessible when you select “C-Customer” in the Customer Type drop-down field.
 Initially defaults the discount template specified on the quote, if one exists. If a quote does not exist, this field defaults the discount template specified for the purchaser in AR Customers. You may be override this field or leave it blank.

##  Location

 Specify the “sell from” location (from IN Locations) for locating pricing
 information.

##  Material

 Specify the material (from HQ Materials) for locating pricing information. Press F4 for a list of valid materials.
Note: The F4 lookup options differ depending on the search criteria entered. The HQ Materials option will always be available; however, if a quote exists for the specified customer/customer job/customer PO, JC job, or IN location (depending on sale type specified), the lookup includes an option for MS Quote Materials. If you specify a price template, a discount template, and/or a location, the F4 also includes options for MS Price Template Materials, MS Disc Template Materials, and/or IN Location Materials.

##  Matl Vendor

 Specify the material vendor (from AP Vendors)
 for locating pricing information.

##  UM

 Initially defaults the “sales” unit of measure specified for the material in HQ Materials. You may override this field, but it must be either the standard unit of measure for the material or a unit of measure specified for the material in HQ Materials.

##  Matl Phase

 This field is
 accessible when you select “J-Job” in the Customer Type drop-down field.
 Specify the material phase (from JC Phases or
 JC Job Phases) for locating pricing information.

##  Haul Code

 Specify the haul code (from MS Haul Codes) for locating rate information.

##  Truck Type

 Specify the truck type (MS Truck Types) for locating rate information.

##  Zone

 For unit-based haul codes only, specify the haul zone for locating rate information.

##  Haul Phase

 This field is
 accessible when you select ‘J-Job’ in the Customer Type field.
 Specify the haul phase (from JC Phases or JC
 Job Phases) for locating pricing information.

##  Discount Type

 This field is accessible when you select “C-Customer” in the Customer Type drop-down field.
 This field is display only, showing the discount type specified for the payment terms assigned to the customer in AR Customers. If the payment terms are rate based, then “rate” displays. If the payment terms are material based, then the discount type (None, Rate, Unit) specified for the material in HQ Materials displays.
