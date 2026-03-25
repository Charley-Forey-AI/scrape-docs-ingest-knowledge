---
title: "Add Compliance Codes to a Subcontract | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/add-compliance-codes-to-a-subcontract"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/add-compliance-codes-to-a-subcontract"
---

# Add Compliance Codes to a Subcontract

Once you have entered subcontract information in SL Subcontract Entry, you can use SL Compliance to add compliance codes to the subcontract.
Compliance codes added here are in addition to any compliance codes associated with the subcontract (in AP Vendor Compliance) or its compliance group (if applicable).
The following instructions discuss how to add compliance codes to a subcontract in SL Compliance.
Note: You can add a compliance code to multiple subcontracts via the SL Compliance Initialize form (accessed by selecting File > Initialize Compliance Code in SL Compliance). If you need to adjust settings to any specific instances of the initialized compliance codes, follow steps 2-7 for each applicable instance. For more information on initializing compliance codes, see [SL Compliance Initialize Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/sl-compliance-initialize-form).

1. Open the SL Compliance form.

1. In the Comp Code field, enter the compliance code or press F4 to select from a list of valid codes.The system automatically assigns a value in the Seq field.

1. Modify the Description field as necessary. Note: Modifying the Description field may be necessary if you are using a compliance code more than once and you want to distinguish between each instance of the code.

1. If applicable, use the Supplier field to enter the supplier. Press F4 for a list of valid vendors/suppliers.

1. If the system should verify compliance on this subcontract (in AP), select the Verify checkbox.Note: When the system verifies compliance in AP, the system either prevents payment to the subcontractor or displays a non-compliance warning. The action the system takes is dependent upon settings that you established in AP Company Parameters. For more information, refer to [Vendor Compliance Tracking](/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking).

1. If a limit applies, use the Limit field to enter a limit for the code. Note: This field is informational only; the system does not use it elsewhere. For example, use this field to indicate bond and insurance limits.

1. Use the Notes field to enter any additional information about this subcontract/compliance code.

1. Select Save.

You can now use this code to track compliance for this subcontract. For more information on compliance tracking, select the links below.[Tracking Subcontract Compliance](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/tracking-subcontract-compliance)
[SL Compliance Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/sl-compliance-form)
[About the SL Subcontract Entry Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)
