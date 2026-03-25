---
title: "Field Definitions: IN Bill of Materials Override Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/production/about-the-in-bill-of-materials-override-form/field-definitions-in-bill-of-materials-override-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/production/about-the-in-bill-of-materials-override-form/field-definitions-in-bill-of-materials-override-form"
---

# Field Definitions: IN Bill of Materials Override Form

The following is a list of field descriptions for the IN Bill
 of Materials Override form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Location

Specify the finished good’s production location (from IN Locations).

## Finished Material

Enter the material code of the finished good. This must be a valid HQ material, stocked at the production location (IN Location Materials). This material can be both a finished good and a component in the production of another finished good. However, production posting is only ‘single level’, which means production of this material will not trigger production of a finished good for which this material is a component.

##  Component Location

 If the component material is at a location different than the production
 location, enter the location (IN Locations) here.

##  Component Material

 Specify the component material that will be used in the production of the finished good. Must be an active, valid HQ Material stocked at the specified location (IN Location Materials) and must be unique within this Bill of Materials.
Note: Component materials can be the same as the finished material, as long as they are from a different location. This might be useful if, for example, you sell the material from one location (or produce a material in one location) and relieve the inventory from another location. However, the finished material must have the Auto Production checkbox selected for the sales location in IN Location Materials.

## Units

Enter the number of units of this material needed to complete one unit of the finished good.

##  % Weight

 Entry in this field is only necessary if the amount of the component material is based on a percentage of the finished good’s weight.
 Specify what percent of the finished good’s weight is comprised of this component material. For example, if the component material makes up 6% of the finished good’s weight, enter .06.
