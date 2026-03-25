---
title: "Field Definitions: EM Usage Rules Table Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-usage-rules-table-form/field-definitions-em-usage-rules-table-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-usage-rules-table-form/field-definitions-em-usage-rules-table-form"
---

# Field Definitions: EM Usage Rules Table Form

The following is a list of field descriptions for the EM
 Usage Rules Table form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Rules Table

 Enter a code, up to 10 characters, that will identify this rules table.

##  Description

 Enter a description of this rules table, up to 30 characters.

##  Hours Basis

- Job to Date - Select this option to base billing rates on the total number of hours the equipment has been on the job ‘to date’ (i.e. since it was first placed on the job).

- Billing Period - Select this option to base billing rates on the total number of hours the equipment has been on the job during the billing period.

##  Seq

 Display only, the sequence number assigned to this entry once you save this record.

## Hours are Greater or Equal To

Specify the minimum number of hours (must be greater than 0.00) the equipment must be on the job to use the specified revenue code.
For subsequent lines, the system will default
 the minimum number of hours based on the maximum number of hours specified for the previous
 line. For example, if you entered 8.00 in the Hours are Less or Equal To field on the
 previous entry, this field will default to 8.00.

## Hours are Less or Equal To

Specify the maximum number of hours the equipment must be on the job (to date or for the billing period) to use the specified revenue code. If there is no hour limit for the specified revenue code, enter 999,999.00.

##  Revenue Code

 Specify the revenue code (from EM Revenue Codes) to use for this range of hours.
