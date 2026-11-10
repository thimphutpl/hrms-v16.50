# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


from frappe.model.document import Document


class EmployeeGrade(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		currency: DF.Link | None
		default_base_pay: DF.Currency
		default_leave_policy: DF.Data | None
		default_salary_structure: DF.Link | None
		dsa: DF.Currency
		eligible_for_overtime: DF.Check
		employee_group: DF.Link | None
		fixed_allowance: DF.Currency
		gis: DF.Currency
		government_grade: DF.Data | None
		increment_method: DF.Literal["Lumpsum", "Percent"]
		increment_value: DF.Currency
		lower_limit: DF.Currency
		promotion_eligibility_years: DF.Int
		promotion_grade: DF.Link | None
		sub_level: DF.Data | None
		sws: DF.Currency
		upper_limit: DF.Currency
	# end: auto-generated types

	pass
