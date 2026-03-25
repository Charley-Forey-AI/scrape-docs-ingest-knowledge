---
title: "Field Definitions: EM Equipment Detail Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-detail-purge-form/field-definitions-em-equipment-detail-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-detail-purge-form/field-definitions-em-equipment-detail-purge-form"
---

# Field Definitions: EM Equipment Detail Purge Form

The following is a list of field descriptions for the EM
 Equipment Detail Purge form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Restrict By

- Equipment - Select this option to restrict purge of specified detail to a single piece of equipment (indicated below). The Component History and Through Transfer Date Off fields are not available when this option is used.

- Category - Select this option to restrict purge of specified detail to equipment within a single category (indicated below). The Component History and Through Transfer Date Off fields are not available when this option is used.

- Component - Select this option to restrict purge of specified detail to a specific component. When selected, only the Component History and Through Transfer Date Off fields are accessible.

- All - Select this option to purge all specified detail for all equipment, categories, and components.

##  Equipment

 This field is only accessible if restricting purge by ‘Equipment’.
 Specify the equipment for which to purge detail (indicated below).

##  Category

 This field is only accessible if restricting purge by ‘Category’.
 Specify the category for which to purge detail (indicated below). When purging by category, all detail is purged for all equipment within the category.

##  Component

 This field is only accessible if restricting purge by ‘Component’.
 Specify the component for which to purge detail (indicated below). When purging by component, only component history is purged. The equipment to which the component is attached is unaffected by the purge.

##  Meter Reading History

 Check this box to purge all meter reading history through the month indicated.
 Leave this box unchecked if not purging meter reading history.

##  Through Reading Month

 Enter the reading month through which to purge meter reading history.

##  Location Transfer History

 Check this box to purge all location transfer history through the month indicated.
 Leave this box unchecked if not purging location transfer history.
Note: This option is not available if purging by component.
 Additionally, if you selected the ‘restrict by all’ option above, components are unaffected
 by this purge option.

##  Through Transfer Out Date

 Enter the 'transfer out' date through which to purge location transfer history.
Note: This option is not available if purging by component.
 Additionally, if you selected the ‘restrict by all’ option above, components are unaffected
 by the location transfer history purge.

##  Include Last Transfer Record

 This option is only accessible when restricting by ‘Equipment’.
 Check this box to have the system purge the last transfer record for the equipment. Because the final transfer record for a piece of equipment will typically have a null ‘Out Date’, checking this box will allow the purge process to delete this record so it can delete the equipment. However, the system will only purge the final transfer record if it is the last transfer record in the file after purging through the specified date. If multiple transfer records are left after purging through the specified ‘transfer out date’, the system will not purge the last transfer record.
 Leave this box unchecked if you do not want to purge the last transfer record for the equipment (not recommended if you are trying to purge the equipment.)

##  Work Orders

 Check this box to purge all completed work orders, including headers, items, parts, and notes through the specified completion date.
 Leave this box unchecked if not purging work orders.
Note: This option is not available if purging by component.
 Additionally, if you selected the ‘restrict by all’ option above, components are unaffected
 by this purge option.

##  Through Completion Date

 Specify the completion date through which to purge completed work orders.
Note: This option is not available if purging by component.
 Additionally, if you selected the ‘restrict by all’ option above, components are unaffected
 by the work order purge.

##  Cost Detail

 Check this box to purge all records from the Cost Detail (EMCD) file.
 Leave this box unchecked if not purging cost detail.
Note: This option is not available if purging by component.
 Additionally, if you selected the ‘restrict by all’ option above, components are unaffected
 by this purge option.

##  Cost Detail: Through Month

 Specify the month through which to purge cost detail.
Note: This option is not available if purging by component.
 Additionally, if you selected the ‘restrict by all’ option above, components are unaffected
 by the cost detail purge.

##  Revenue Detail

 Check this box to purge all records from the Revenue Detail (EMRD) file.
 Leave this box unchecked if not purging revenue detail.
Note: This option is not available if purging by component.
 Additionally, if you selected the ‘restrict by all’ option above, components are unaffected
 by this purge.

##  Revenue Detail: Through Month

 Specify the month through which to purge revenue detail.
Note: This option is not available if purging by component.
 Additionally, if you selected the ‘restrict by all’ option above, components are unaffected
 by the revenue detail purge.

##  Component History

 Check this box to purge all component transfer history.
 Leave this box unchecked if not purging component transfer history.
Note: This option is not available if purging by equipment or category.

##  Through Transfer Date Off

 Specify the transfer 'date off' through which to purge component transfer history.
Note: This option is not available if purging by equipment or category.
