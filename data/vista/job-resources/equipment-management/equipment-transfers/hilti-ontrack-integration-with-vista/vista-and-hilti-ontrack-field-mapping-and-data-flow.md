---
title: "Vista and Hilti ON!Track Field Mapping and Data Flow | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/equipment-transfers/hilti-ontrack-integration-with-vista/vista-and-hilti-ontrack-field-mapping-and-data-flow"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/equipment-transfers/hilti-ontrack-integration-with-vista/vista-and-hilti-ontrack-field-mapping-and-data-flow"
---

# Vista and Hilti ON!Track Field Mapping and Data Flow

With this integration enabled and configured, you can send
 equipment and tool tracking data between Vista
 and Hilti ON!Track. The following information maps the
 records and fields between the two systems.
For more information about setting up the Hilti ON!Track integration with Vista, contact your consultant.
Important: After completing
 the integration setup, create new location and equipment records in Vista only. If you create or edit them
 in Hilti ON!Track, these records will not be
 linked or tracked.

## Vista EM
 Equipment and Hilti ON!Track Assets

Equipment data from the Vista EM
 Equipment record flows into Hilti ON!Track
 Assets.
All new pieces of equipment created in Vista will display in Hilti ON!Track, populating Location and Responsible Employee fields with
 the default values entered during setup.
Important: If you add a new piece of equipment in ON!Track, the integration creates a new equipment record in Vista and links these two records together. However, you must *make all changes to this record in Vista*, as the data syncs from Vista into ON!Track.

Vista EM EquipmentHilti ON!Track Assets
Equipment Code Inventory Number
DescriptionName
VIN/Serial #Serial Number
MakeManufacturer
ModelModel
StatusStatus
Ownership StatusOwnership Type

## Vista EM
 Locations and Hilti ON!Track Locations

Equipment location data from the Vista
 EM Location record flows to the Hilti ON!Track
 Locations record.
Note: In Hilti ON!Track, a location Type set to Location Group
 will be a new record and will not be mapped to a project in Vista.

Vista EM LocationsHilti ON!Track Locations
DescriptionName
Active checkboxLocation State
NotesDescription

Note: In Hilti ON!Track Locations, the Name and Location State fields
 consolidate equipment and project location fields from Vista.

## Vista PM
 Projects and Hilti ON!Track Locations

Project location data from the Vista PM
 Projects record flows into Hilti ON!Track
 Locations.
Note: In Hilti ON!Track, a location Type set to Location Group
 will be a new record and will not be mapped to a project in Vista.

Vista PM ProjectsHilti ON!Track Locations
DescriptionName
Job StatusLocation State

## Vista PR
 Employees and Hilti ON!Track Employees

Employee data from the Vista PR
 Employees record flows to the Hilti ON!Track
 Employees record.
Important: If you create an equipment record in
 ON!Track, the integration creates a new equipment record in Vista and links these two records
 together. Make all changes to this record in Vista, as the data is pulled from Vista into ON!Track.

Vista PR EmployeesHilti ON!Track Employees
LastLast Name
FirstFirst Name
EmailNotification Email
CellMobile

## Hilti ON!Track
 Transfer and Vista EM Location
 Transfer

Equipment transfer data from Hilti ON!Track
 Transfer flows into the Vista EM
 Location Transfer record.
Note: Although employee data can be assigned to a piece of
 equipment in ON!Track, Vista only
 syncs the location transfer data for a piece of equipment. Vista disregards employee transfer
 data.

Hilti ON!Track TransferVista EM Location Transfer
LocationProject or LocationNote: Equipment
 location data can be transferred to either a project or
 location in Vista.

Set Transfer DateDate
