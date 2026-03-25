---
title: "Field Definitions: MS Vendor Trucks Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-vendor-trucks-form/field-definitions-ms-vendor-trucks-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-vendor-trucks-form/field-definitions-ms-vendor-trucks-form"
---

# Field Definitions: MS Vendor Trucks Form

The following is a list of field descriptions for the MS
 Vendor Trucks form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Vendor

 Enter the pay vendor to which this vehicle belongs. This must be a valid vendor from AP
 Vendors.

##  Truck

 Enter the truck code, up to 10 characters. Press F4 for a list of valid truck codes.

##  Description

 Enter a description of this vehicle, up to 60 characters.

## Truck Type

Enter a truck type or press F4 to select a
 truck type from a list. The the system can use truck types to determine pay and pay rates.
Truck types are created and maintained using the [MS Truck Types](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-truck-types-form) form.

##  # of Axles

 Specify the number of axles (0-255) on this vehicle. This field is informational only.

##  Vehicle Weights: Gross

 Enter this vehicle’s fully loaded legal weight limit. This value must be equal to or greater than 0.00.

##  Vehicle Weights: Tare

 Enter the weight of this vehicle when unloaded. Entry must be equal to or greater than 0.00.
Note: This value defaults in the Tare field in
 MS Ticket Entry when you are posting haul charges to an outside haul vendor.

##  Vehicle Weights: Capacity

 This field is the maximum load weight that this vehicle can carry and automatically defaults the difference between the Gross and Tare weights. You can override this field. Be aware that if you change the capacity, the vehicle’s gross and tare weights do not recalculate automatically. Change those fields manually as necessary.

##  Vehicle Weights: UM

 Specify the unit of measure (from HQ Units of Measure) in which this
 vehicle’s weights are expressed. Although this is the unit of measure for this vehicle, the
 Weight Option specified for the sales location (in IN Locations) determines how the system
 expresses weight in MS Ticket Entry. If the location’s weight unit of measure differs from
 this vehicle’s unit of measure, and the vehicle’s UM is TONS, LBS, or kg, the posted weight
 units will be converted accordingly. For example, if the vehicle’s weight is expressed in
 tons, and the location’s weight option is LBS, then weight units entered on tickets will be
 converted to pounds.However, if the vehicle’s weight is other than TONS, LBS, or kg, no
 default weight calculation will occur.

##  License: Plate #

 Enter the license number for this vehicle, up to 20 characters. This field is informational only.

##  License: State

 Enter the state (from HQ States) in which this vehicle is licensed. This field is informational only.

##  License: Exp Date

 Specify the date that this vehicle’s license expires.

##  Driver

 Enter the name of the individual that normally operates this vehicle. The system uses this nameas a default when entering tickets and/or payer time sheets referencing this vehicle.

##  Permit Date

 Enter the permit date for this vehicle. This field is informational only.

##  Insurance Date

 Enter the date the insurance on this vehicle went into effect.

##  Pay Code

 Enter the pay code (from MS Pay Codes) for this vehicle. The system uses this code as the default when entering tickets and hauler time sheets, and determines how the vendor will be paid for the use of this vehicle. May be overridden by quote and at time of ticket or hauler time sheet entry.
