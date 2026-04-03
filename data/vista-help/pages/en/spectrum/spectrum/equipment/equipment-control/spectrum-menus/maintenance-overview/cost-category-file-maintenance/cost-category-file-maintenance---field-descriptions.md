---
title: "Cost Category File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/cost-category-file-maintenance/cost-category-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/cost-category-file-maintenance/cost-category-file-maintenance---field-descriptions"
---

# Cost Category File Maintenance - Field Descriptions

Use the field descriptions below for reference when setting up a new cost category or editing an existing one.
Fields
Descriptions

Cost category code
Cost categories are used to group equipment cost transactions. The cost categories entered on this screen will fall into one of the seven cost category types that were set up on the Equipment Control Installation screen during installation. Note the distinction between a cost category code and a cost category type. There must be at least one cost category for every type. For example, the cost category code F may be described as fuel, and be linked to cost category type #1 because FUEL is cost category type #1 from the installation screen. However, multiple cost categories for one cost category type are also possible. For example, cost category type #4 may be defined as LABOR on the installation screen, then through this maintenance screen the categories LER, labor: engine repair, and LBWR, labor: body work repair may both be linked to category type #4.
A note about use of numeric coding:
Because many users prefer alphabetic or combination alpha and numeric coding, this code is not a numeric-only field. Because of this, the code left-justifies when entered. Users preferring a strictly numeric coding scheme should be advised to use leading zeros when adding codes in order to produce desired sort results on screens and reports. Without leading zeros, '1', '10', '100' will appear before '2'. '20', '200'. Instead, codes should be set up '001', '002', and so forth. If more than 1000 codes are anticipated, instead enter '0001', '0002', and so forth.

Description
Enter the description for the cost category.

Category type
Enter the cost category type. Entry of a number 1-7 is required in this field.
The Cost Category Type pull down menu may be used to look up and select the desired cost category type. Cost category types 4-7 are user-defined during Equipment Control Installation and should not normally be changed.

> Cost Category Type
Automatically defined by the system as:

1
FUEL

2
LUBE and OIL

3
TIRES

4
User-Defined Field

5
User-Defined Field

6
User-Defined Field

7
User-Defined Field

G/L debit account
Enter the default G/L debit account code for use in Transaction Entry. The account name will display. Entry is required. A lookup window is available to view a list of valid account codes. The G/L account must have the Direct Cost option selected in the General Ledger Master File Maintenance screen.
Note: Data entry is prevented if the General Ledger account code
 status is Not
 Used. A warning message displays if the General Ledger account
 code status is Inactive.
Cost Center Information:
At this field, Spectrum verifies authorization and allows entry of a G/L account code only if you have permission to assign that code. The system compares the G/L account's list of shared cost centers with cost centers in your operator's assigned cost center scheme, and if there are no common cost centers, then that G/L account cannot be assigned.
Once a G/L account code has been assigned to an equipment cost category (by an authorized operator), then that G/L account will be used by all operators for processing involving that equipment type code.

G/L Restrictions
System Administrators can click this button to specify which G/L account code(s) can be used in data entry in transactions referencing a particular equipment cost category.
The Cost Category G/L Account Restrictions window will display a list of all G/L accounts to select which ones are allowed in data entry screens for the selected cost category code.

Component group
Enter the component group code, or press Enter to accept the system default of ALL When a code is entered, then the costs for this cost category will be combined with other cost categories assigned the same component group in the [Component Group Cost Inquiry](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/inquiries-overview/component-group-cost-inquiry) screen, in order to conveniently inquire on costs incurred at the equipment component level.

Status
All cost categories are Active by default but may be set to Inactive. When a cost category is set to inactive, the code does not display in the search window by default and a warning message will display when the code is entered (but the software will still permit entry).

Data entry
The Data entry section only displays when the Preventive Maintenance module is present. By default, this option is set to None when adding new cost categories. Otherwise, when this radio group is set to Optional or Require equipment work order, then in Data Entry screens the software will prompt for an Eq. work order code whenever this cost category is entered.
