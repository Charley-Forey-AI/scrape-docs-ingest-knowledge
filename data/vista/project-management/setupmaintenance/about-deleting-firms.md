---
title: "About Deleting Firms | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/about-deleting-firms"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/about-deleting-firms"
---

# About Deleting Firms

You can delete a firm as long as there is no detail
 associated with it.
If detail exists for a firm, you must delete it
 before you can delete the firm. The following is a list of tables that are checked by
 the system when you select a firm for deletion in PM Firms. If detail exists for the
 firm in any of these tables, you will receive an error message (for each table in which
 the firm exists) and the firm will not be deleted. To avoid this process, it is
 suggested that you first check these tables to ensure detail does not exist for the firm
 before you attempt to delete the firm.
Table
Table Name
Description

PMCO
Company Parameters
Firm cannot exist as Our
 Firm for any company using the same Vendor/Firm group

PMDD
Daily Log Detail
Firm cannot be
 referenced in the log detail for any project/log (e.g.
 Subcontractors, Equipment, etc.) using the same Vendor/Firm
 group.

PMOD
Other Documents
Firm cannot exist as
 Related Firm or Responsible Firm for any document type/document
 using the same Vendor/Firm group.

PMPD
Punch List Detail
Firm cannot exist as
 Responsible Firm for any punch list detail lines using the same
 Vendor/Firm group.

PMPI
Punch List Items
Firm cannot exist as
 Responsible Firm for any punch list items using the same Vendor/Firm
 group.

PMPM
Firm Contacts
Firm cannot exist as the
 Firm for firm contacts using the same Vendor/Firm group.

PMRI
RFI
Firm cannot exist as
 Responsible Firm or Requesting Firm for any RFI using the same
 Vendor/Firm group.

PMSM
Submittals
Firm cannot exist as
 Responsible Firm, Subcontractor firm, or Architect/ Engineer firm
 for any submittal using the same Vendor/Firm group.
