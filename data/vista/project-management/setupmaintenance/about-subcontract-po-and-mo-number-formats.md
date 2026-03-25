---
title: "About Subcontract, PO, and MO Number Formats | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats"
---

# About Subcontract, PO, and MO Number Formats

When defining the format of subcontract, purchase order, and material order numbers in PM Company Parameters, it is important that you understand the initialization process and how it uses the number formats assigned here.
When you initialize subcontracts,
 POs, and/or MOs, the system assigns a number based on the # of
 Project Characters you specify, and combines it with
 either a sequence number, the vendor number (subcontracts and purchase
 orders), or the location code (material orders). This includes any
 delimiters that you may have entered as part of your job or vendor numbers.
 If you specify the Project/Sequence format, it assigns the next available
 sequence number to the project number, adding zeros if necessary to bring
 the subcontract, purchase order, or material order number to the correct
 character total.
Example:
In this example, we will assign a
 subcontract number based on both the Project/Vendor and Project Sequence
 formats, using a number format of 10L.
Note: If you are using the 'significant part of job' feature for
 subcontracts, purchase orders, and/or material orders (flags in PM
 Company Parameters), the Significant Job Characters you specify for
 subcontracts, POs, and MOs should be defined so that they work in
 conjunction with the formats you specify here. See [About Using Significant Part of Job](/en/vista/vista/project-management/setupmaintenance/about-using-significant-part-of-job).

If you are using the Project/Seq numbering format and you prefer to use a
 specific range of sequence numbers, you can do so using the Starting
 Sequence option available for subcontract, material order, and purchase
 order number formats. This option allows you to specify the number with
 which to begin sequence assignment (for example, ‘5000’ for subcontracts,
 ‘6000’ for purchase orders, and ‘7000’ for material orders). It is important
 to note that the starting sequence is by project, not by company. So
 numbering for each project will begin with the same starting sequence.
For example, you set the SL Project
 Characters to ‘6’ and you specify a starting sequence of '5000'. You create
 two subcontracts for Project 11000 and two for Project 22000. The system
 applies the starting sequence as follows:ProjectSubcontract
1100011000-5000
11000-5001
2200022000-5000
22000-5001

Another point to consider when defining the formats for
 Subcontract and PO/MO numbers in PM, are the various code structures set up
 when your system was installed:

- Project Codes/Job
 Codes

- SL Subcontract
 Numbers

- AP Vendor Numbers


- PO Purchase Order
 Numbers

- IN Material Order
 Numbers

The way these codes are structured
 may have a bearing on how you set up the formats for subcontract and PO/MO
 numbers in PM Company Parameters. Since the system automatically converts PM
 Subcontract, Purchase Order, and Material Order numbers to the format
 defined in each of the related modules (SL, PO, IN, respectively), it is
 suggested that you define your PM Company Parameter formats as they are
 defined in their destination modules.
Note: When selecting the characters from the
 project, the system counts left to right. When selecting characters from the
 vendor number, the system has been set up to count right to left, since
 typically, vendor numbers are right justified.
In addition, because many project
 codes begin with the same numbers, it is suggested that when defining your
 formats, you specify a sufficient number of characters of the project to
 ensure individuality during initialization. Otherwise, you may inadvertently
 cause the system to add multiple detail lines as items on the same
 subcontract, purchase order, or material order that you meant to be set up
 as separate subcontracts, purchase orders, and material orders.
