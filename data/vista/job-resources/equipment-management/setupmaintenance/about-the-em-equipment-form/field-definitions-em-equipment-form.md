---
title: "Field Definitions: EM Equipment Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form/field-definitions-em-equipment-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form/field-definitions-em-equipment-form"
---

# Field Definitions: EM Equipment Form

The following is a list of field descriptions for the EM
 Equipment form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Equipment Code

 Assign a code, up to 10 characters, that identifies this equipment, attachment, or component.

##  VIN/Serial #

 Enter the equipment’s VIN (Vehicle Identification Number) or Serial number, up to 40 characters.

##  Description

 Enter a description of this equipment, up to 60 characters.

##  Make

 Enter the make (manufacturer) of this equipment, up to 20 characters (e.g. Ford, Peterbilt, etc.).

##  Model

 Enter the model of this equipment, up to 20 characters (e.g. F150).

##  Year

 Enter the year this equipment was manufactured.

##  Type

 Specify the equipment type.

- Equipment – Select this option if this is a primary piece of equipment or an attachment.

- Component – Select this option if this is a component of a primary piece of equipment.

##  Status

 Specify the status for this equipment or attachment. Not used for components.

- Active – Select this option if this equipment is currently active. Usage and costs can be posted to this equipment.

- Inactive – Select this option if this equipment is not currently active. Usage and costs cannot be posted to this equipment.

Note: You cannot flag equipment as ‘inactive’ if it has attachments. You will need to transfer the attachments off the equipment before you can set the status to 'inactive'.

- Down – Select this option if this equipment is currently down. This option typically used when equipment is inoperable or out for repairs. Usage and costs may still be posted to this piece of equipment. Primarily used for reporting purposes.

##  Category

 Specify the category (from EM Categories) to which this piece of equipment is associated.

##  Department

 Specify the department (from EM Departments) for this piece of equipment. The department specified here determines which set of GL accounts will be updated when costs and revenue are posted to this piece of equipment.

##  Location

 Specify the location (set up in EM Locations) to which this piece of equipment is assigned. When adding a new piece of equipment or changing the location for existing equipment, the location must be an [active location](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-locations-form/field-definitions-em-locations-form#ID-0000c62b--en) (EM Locations).
 The location will be updated automatically when this equipment is transferred using the EM Location Transfers program or when posting usage in EM, MS, and/or PR (if specified to do so in EM Company Parameters, Updates tab). Although you can change this field manually after initial setup, it is not recommended.
Note: Updates from EM Usage Posting will occur upon the
 creation of the batch record. However, updates from PR Timecard Entry and MS Ticket Entry
 will occur only once you post the batch.

##  Shop

 Specify the shop (EM Shops) that is responsible for the maintenance and repair of this piece of equipment, if applicable.

##  Revenue Code

 Enter the revenue code that will be used as a default when posting usage to this equipment.
Press F4 to select a revenue code from a list.
Revenue codes are created and maintained using
 the [EM Revenue Codes ](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-codes-form) form. You can open this form by pressing
 F5
 in this field.

##  PR Company

 Enter the Payroll company to use for validating employees when posting equipment usage (in EM Usage Posting). Initially defaults the PR Co specified in EM Company Parameters.

##  Operator

 This field is only accessible if you specified a PR company above.
 Specify the employee (from PR Employees) that will be this equipment’s standard operator.

##  JC Company

 Enter the JC company to update when posting equipment usage (in EM Usage Posting). Initially defaults the JC Co specified in EM Company Parameters.

##  JC Job

 Specify the job to which this piece of equipment is currently assigned.
 If you specified to update the job when posting equipment usage in EM, MS, and/or PR (EM Company Parameters, Updates tab), this field will be updated with the posted job if the posted job differs from the job currently assigned to the equipment.
Note: Updates from EM Usage Posting will occur upon the
 creation of the batch record; however, updates from PR Timecard Entry and MS Ticket Entry
 will only occur once you post the batch.
 If you post to multiple jobs in a single day, it is important that you post your entries in the correct order, as updates will be based on the last entry. For example, if Equipment #100 was used on Job #55000- from 6:00 a.m. to Noon, and then used on Job #63500- from 1:00 p.m. to 5 p.m., you would need to post the usage for Job #63500- last to ensure that this field is correctly updated to show Job #63500- as the 'current' job.

##  Usage CT

 Enter the JC cost type to which usage for this piece of equipment should be posted.

##  Check for Usage Transactions

 Check this box to be notified if you make a a transfer entry on the EM Location Transfer form that affects past posted usage transactions for a particular piece of equipment.

##  Date of Last Usage

 Enter the last usage date of this equipment, if applicable.
 This field is updated automatically when posting equipment usage in EM Usage Posting, PR Timecard Entry, and/or MS Ticket Entry where the new usage date is greater than the 'date of last usage' for the equipment. Therefore, it is recommended that you do not manually change this date after the initial setup.
Note: The update from EM Usage Posting will occur upon the
 creation of the batch record; however, the updates from PR Timecard Entry and MS Ticket
 Entry will not occur until you post the batch.

##  License: Number

 Enter the license plate number for this vehicle/equipment, up to 10 characters.

##  License: State

 Enter the state in which this vehicle/equipment is registered. The state specified must be a valid state as defined in HQ States. The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, and the record will not be saved.
Note: The name of this field differs depending on the
 Default
 Country specified in HQ Company Setup. For the United States (US) and
 Australia (AU), the label displays as "State". For Canada (CA), the label displays as
 "Province".

##  License: Expiration Date

 Specify the date that the license for this vehicle/equipment expires.

##  License: IRP Fleet #

 Specify the IRP (International Registration Program) fleet number for this vehicle/equipment.

##  License: IFTA State

 Specify the IFTA (International Fuel Tax Agreement) state for this vehicle/equipment if different from the license state. This field is used for reporting purposes only.
 The state specified must be a valid state as defined in HQ States. The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, and the record will not be saved.
Note: The name of this field differs depending on the
 Default
 Country specified in HQ Company Setup. For the United States (US) and
 Australia (AU), the label displays as "State". For Canada (CA), the label displays as
 "Province".

##  Fuel

 Specify the type of fuel used for this vehicle/equipment.

- Diesel - Select this option if this equipment uses diesel fuel.

- Gas - Select this option if this equipment uses gasoline.

- Other – Select this option if this equipment uses a fuel type other than diesel or gas (e.g. propane).

- None - Select this option if this equipment does not use fuel.

##  Material Code

 If tracking fuel usage, specify the material code for fuel used by this equipment. Must be a valid material (from HQ Materials) or an equipment part (set up in EM Equipment Parts) cross-referenced to a valid HQ material. Entry in this field must be valid regardless of how you have set the ‘Validate Parts’ flag in EM Company Parameters.
Note: The material code specified here will default as the
 ‘Fuel Matl Code’ when entering transactions in EM Fuel Posting.
 If you want to update the ‘Fuel Used’ and ‘Last Fuel Date’ fields (Meters tab, EM Equipment) when posting fuel usage, the material code entered here must match the material code entered in EM Fuel Posting, AP Transaction Entry (Equip Type), or EM Cost Adjustments (Fuel Type).

##  Cost Code

 Enter the cost code (defined in EM Cost Codes) used for fuel. This code will be used as the default when posting fuel usage in EM Fuel Posting.

##  Cost Type

 Enter the cost type (defined in EM Cost Types) used for fuel. This code will be used as the default when posting fuel usage in EM Fuel Posting.

##  Capacity

 Specify this equipment’s fuel capacity. The UM used to measure the fuel capacity for this vehicle/equipment is specified to the right.

##  Capacity U/M

 Specify the unit of measure (HQ Units of Measure) by which the fuel capacity specified above is measured (e.g. gallons, liters). If the unit of measure specified here is different from the standard unit of measure for fuel, it must be set up in HQ Materials (Additional Units of Measure tab) with the appropriate conversion factor. This will allow the system to properly convert the unit of measure when posting fuel usage in EM Fuel Posting.

##  Weight UM

 Specify the unit of measure used to weigh this vehicle/equipment.

##  Weight

 Specify the weight capacity of this vehicle/equipment. This is the maximum amount of weight this vehicle/equipment can haul.

##  Volume U/M

 Specify the unit of measure used to measure the volume capacity of this vehicle/equipment.

##  Volume

 Specify the volume capacity of this vehicle/equipment. This is the maximum volume (e.g. cubic yards, cubic feet, etc.) of material this vehicle/equipment can hold.

##  Tare Weight

 Specify the tare weight of this vehicle/equipment (i.e. the weight of this vehicle/equipment when empty). This amount is used in conjunction with the Gross Weight specified during ticket entry to determine the net weight of the cargo.
Note: This value defaults in the Tare field in
 MS Ticket Entry when you are posting haul charges to your own equipment.

##  Gross Weight

 Specify the gross weight of this vehicle/equipment. The gross weight is generally the weight for which the vehicle/equipment is licensed.
Note: This field is informational only. It is not used
 anywhere in the system.

##  Height

 Enter the total height of this equipment, up to 20 characters.
Note: This field is informational only. It is not used
 anywhere in the system.

##  Wheelbase

 Enter the length of this equipment’s wheelbase, up to 20 characters.
Note: This field is informational only. It is not used
 anywhere in the system.

##  Number of Axles

 Enter the total number of axles (0-255) on this piece of equipment.
Note: This field is informational only. It is not used
 anywhere in the system.

##  Width

 Enter the width of this piece of equipment, up to 20 characters.
Note: This field is informational only. It is not used
 anywhere in the system.

##  Overall Length

 Enter the total length of this piece of equipment, up to 20 characters.
Note: This field is informational only. It is not used
 anywhere in the system.

##  Horsepower

 Specify this equipment’s horsepower, up to 20 characters.
Note: This field is informational only. It is not used
 anywhere in the system.

##  Tire Size

 Specify the tire size for this piece of equipment, up to 20 characters.
Note: This field is informational only. It is not used
 anywhere in the system.

##  Truck Type

 Used in Material Sales only.
 Specify the truck type (from MS Truck Types) for this vehicle/equipment, if applicable. The truck type specified here will be used as a default when entering haul charges referencing this vehicle/equipment on MS tickets or hauler time sheets.

##  Ownership Status

- Owned – Select this option if your company owns this piece of equipment. Use the Purchase Information section to enter the purchase information for this equipment.

- Leased – Select this option if your company leases this piece of equipment from an outside vendor. Use the Lease/Rental Information section to allow enter lease information for the equipment.

- Rented – Select this option if your company rents this piece of equipment from an outside vendor. Use the Lease/Rental Information section to enter rental information.

- Customer – Select this option if a customer owns this equipment. Use the Customer Information section to enter information about the customer.

##  Dealer

 Specify the party from whom your company purchased this piece of equipment, up to 30 characters.

##  Date

 Enter the date your company purchased this equipment.

##  Price

 Specify this equipment’s purchase price.

## AP Company

Specify the AP company to use for validating vendors for this equipment.
Note: If you purchase this equipment later, this field will be disabled, but data entered here will be saved.

##  Leased From

 Specify the vendor (from AP Vendors) from which your company is renting/leasing this
 equipment.
Note: If you purchase this equipment later, this field will be disabled, but data entered here will be saved.

##  Start Date

 Specify the start date for the lease or rental agreement.
Note: If you purchase this equipment later, this field will be disabled, but data entered here will be saved.

##  End Date

 Specify the date the lease or rental agreement terminates.
Note: If you purchase this equipment later, this field will be disabled, but data entered here will be saved.

##  Lease Payment

 Specify the monthly lease or rental amount.
Note: If you purchase this equipment later, this field will be disabled, but data entered here will be saved.

##  Residual Value

 Specify what the equipment’s residual (remaining) value is expected to be at the end of the lease or rental agreement.
Note: If you purchase this equipment later, this field will
 be disabled, but data entered here will be saved.

##  AR Company

 Specify the AR company to use for validating customers for this equipment.

##  Customer

 Specify the customer (from AR
 Customers) to whom this equipment belongs.

##  Customer Equipment #

 Enter the customer’s equipment number, up to 20 characters.

##  In Service Date

 Enter the date this equipment was put into service.

##  Replacement Cost

 Enter the estimated cost to replace this equipment.

## Expected Life

Indicate this equipment’s life expectancy (0-32000). Use the drop-down menu to the right to specify whether this number represents Months or Years.

##  Current Appraisal

 Enter this equipment’s current estimated value.

##  Sold Date

 Specify the date your company sold this equipment, if applicable.

##  Sale Price

 Specify the sale price for this equipment, if applicable.

##  Capitalized

 This flag is informational only. It can be used for reporting purposes but is not otherwise used by the software.
 Check this box if this equipment (or component) is a capitalized asset.
 Leave this box unchecked if you are expensing this equipment (or component) rather than setting it up as a capitalized asset.

##  Attached To Equipment

 Specify the primary equipment to which this piece of equipment is attached. If you transfer this attachment’s primary equipment to a job or location (using EM Location Transfers), the attachment will be transferred as well.

##  Post Revenue To Attachment

 Check this box to allow revenue to be posted to this attachment. When posting revenue to the primary piece of equipment, the same revenue code and hours will be used to post usage to the attachment, and the rate used will be either the standard rate for the attachment/revenue code (by category) or an override rate (by equipment or template).
 Leave this box unchecked if not posting revenue to this attachment.

##  Component of Equipment

Specify the primary piece of equipment to which this component is attached. The component is assumed to always be in the same location as the primary piece of equipment.

## Component Type

Press F4 to select a component type from a
 list.
 Component types are created and maintained using the [EM Component Types ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-component-types-form) form.

##  Update Hours

Check this box to update the hours for this component. When posting hours to the primary piece of equipment, the same hours will be posted to this component.
Leave this box unchecked if not updating (posting) hours for this component.

##  Update Miles

Check this box to update the mileage for this component. When posting mileage for the primary piece of equipment, the same mileage will be posted to this component.
Leave this box unchecked if not updating (posting) mileage for this component.

##  Update Fuel

Check this box to update fuel usage for this component. When posting fuel usage for the primary piece of equipment, the same fuel usage will be posted to this component.
Leave this box unchecked if not updating (posting) fuel usage for this component.

##  Post Costs To Components

 Check this box to allow posting costs to this equipment at the component level. Cost posting forms will prompt for component type and component whenever you specify this equipment.
 Leave this box unchecked if not posting equipment costs at the component level. Component type and component inputs will be disabled whenever you specify this equipment on a cost posting form.
Note: Initially defaults as defined in EM Company
 Parameters.

## Hour Meter: Reading

The Hour Meter: Reading field on the EM Equipment form, Meters tab.
Enter the current hour meter reading for this equipment. Once you enter the initial reading here, use the EM Meter Readings form to update the hour meter to ensure accurate tracking of hours and units.
Note: You can also enter the initial hour meter reading using the EM Meter Readings form.

### Replacing Meters

If you are replacing the hour meter for this
 equipment, add the existing value in this field to the existing value in the Replaced Meter
 Reading field. For example, if the existing value in this field is
 100,000.00 and the existing Replaced Meter Reading value is 400,000.00, you would enter
 500,000.00 as the new Replaced Meter Reading value. Then in this field, enter the reading
 for the new meter. This will ensure accuracy when entering meter readings in EM Meter
 Readings.

##  Hour Meter: Date

 Enter the reading date of the hour meter.
 This field is required if the Hour Meter
 Reading field is greater than 0.00.

## Hour Meter: Replaced Meter Reading

Enter the sum of the readings from all replaced hour meters (i.e., add the existing value from the Reading field to the existing value in this field).
 For example, if the existing Reading value is 100,000.00 and the existing value in this field is 400,000.00, you would enter 500,000.00 as the new value in this field. The new meter's reading should be entered in the Reading field.

##  Hour Meter: Replacement Date

 Specify the replacement date for this equipment’s hour meter.

## Odometer: Reading

Specify this equipment’s current odometer reading. After initial entry, use the EM Meter Readings form to update this field to ensure accurate tracking of hours and units.
Note: You can also enter initial readings in the EM Meter Readings program. Replacing Meters
If you are replacing the odometer for this
 equipment, add the existing value in this field to the existing value in the Replaced Meter
 Reading field. For example, if the existing value in this field is
 100,000.00 and the existing Replaced Meter Reading value is 400,000.00, you would enter
 500,000.00 as the new Replaced Meter Reading value. Then in this field, enter the reading
 for the new meter. This will ensure accuracy when entering meter readings in EM Meter
 Readings.

## Odometer: Date

Enter the reading date of the odometer.
This field is required if the Odometer
 Reading field is greater than 0.00.

## Odometer: Replaced Meter Reading

Enter the sum of the readings from all replaced odometers (i.e., add the existing value from the Reading field to the existing value in this field).
 For example, if the existing Reading value is 100,000.00 and the existing value in this field is 400,000.00, you would enter 500,000.00 as the new value in this field. The new meter's reading should be entered in the Reading field.

##  Odometer: Replacement Date

 Specify the replacement date for this equipment’s odometer.

## Fuel Used

 Specify the total gallons of fuel used ‘to-date’ for this piece of equipment. After initial entry, use the EM Fuel Posting form to update this field to ensure accurate tracking of units.
Note: Updates to this field will only occur when posting fuel usage if the part code entered for the equipment (Add’l Info tab, EM Equipment) matches the material code entered in EM Fuel Posting, AP Transaction Entry (Equip Type), or EM Cost Adjustments (Fuel Type).

## Last Fuel Date

 Indicate the last fuel date for this equipment (i.e. the last date you posted fuel to this equipment).
Note: Updates to this field will only occur when posting fuel usage if the part code entered for the equipment (Add’l Info tab, EM Equipment) matches the material code entered in EM Fuel Posting, AP Transaction Entry (Equip Type), or EM Cost Adjustments (Fuel Type).
