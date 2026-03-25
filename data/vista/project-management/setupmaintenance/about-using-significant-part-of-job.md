---
title: "About Using Significant Part of Job | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/about-using-significant-part-of-job"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/about-using-significant-part-of-job"
---

# About Using Significant Part of Job

The Significant Part of SL Job and Significant Part of PO Job checkboxes (in PM Company Parameters) determine whether multiple projects can be combined on a single subcontract or purchase order (respectively).
You might typically use these options if you use sub-jobs to breakdown work within a master project and you want purchase orders and/or subcontracts to cover multiple sub-jobs.
If you check this box, the
 Significant
 SL Job Characters
 and
 Significant
 PO Job Characters
 fields (in PM Company Parameters) are used to determine the number of
 characters by which to validate the project/job number when initializing subcontracts or
 purchase orders.
For example:
Let's say you use a project/job format of 5-3 and
 have set the
 Significant
 SL Job Characters
 field to 5. When you initialize subcontracts, the system will validate
 the project/job specified for each subcontract detail line based on the significant job
 characters. Each subcontract detail line having the same vendor and matching the first 5
 job characters will be assigned as items on the same subcontract. Subcontract detail
 lines not meeting this criteria will be assigned a unique subcontract number.
Project
Significant SL Job Chars
Vendor
Subcontract #
Item #

15100-
5
1520
15100-5000
1

15100-100

1520
15100-5000
2

15100-200

1520
15100-5000
3

15100-
8
1520
15100-5000
1

15100-100

1520
15100-5001
1

15100-200

1520
15100-5002
1

The 'significant part of job' feature is used in conjunction with the numbering format. If you leave the ‘significant part of job’ flag unchecked, it is important that you specify a sufficient number of project characters to ensure that initialization will generate a unique subcontract or purchase order number. Otherwise, if you try to initialize subcontracts or purchase orders for projects having the same significant job characters (as in the example above where significant job characters is ‘5’), initialization will try to generate a number based on the specified format and will determine that the number already exists. You will then receive a message that the number already exists and no initialization will occur, nor will the transaction be added as a line on the existing subcontract or purchase order. In which case, you will need to manually assign the subcontract or purchase order number.
If you elect to not use the 'significant part of job' feature, the system will not allow the same subcontract or purchase order to be used on multiple projects. Using the example above, each job would be assigned to a different subcontract.
[](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats)Defining Subcontract, PO, and MO Numbers
[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
