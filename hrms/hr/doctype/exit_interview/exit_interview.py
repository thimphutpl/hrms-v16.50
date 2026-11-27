# -*- coding: utf-8 -*-
# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.naming import make_autoname
from frappe.model.document import Document
from frappe import _

class ExitInterview(Document):
	def validate(self):
		self.validate_checkbox_answers()

	def on_submit(self):
		if not self.employee_separation:
			frappe.throw(_("Exit interview must be created from employee separation."))

		frappe.db.set_value("Employee Separation", self.employee_separation, "exit_interview", self.name)

	def validate_checkbox_answers(self):
		for js in self.job_satisfaction:
			if js.strongly_agree == 0 and js.agree == 0 and js.disagree == 0 and js.strongly_disagree == 0:
				frappe.throw("Please select an answer for Question: {}, in Part III: Job Satisfaction".format(js.question))
		for m in self.management:
			if m.strongly_agree == 0 and m.agree == 0 and m.disagree == 0 and m.strongly_disagree == 0:
				frappe.throw("Please select an answer for Question: {}, in Part IV: Management".format(m.question))
		for r in self.remuneration_benefits:
			if r.strongly_agree == 0 and r.agree == 0 and r.disagree == 0 and r.strongly_disagree == 0:
				frappe.throw("Please select an answer for Question: {}, in Part V: Remuneration & Benefits".format(r.question))
		for c in self.the_company:
			if c.strongly_agree == 0 and c.agree == 0 and c.disagree == 0 and c.strongly_disagree == 0:
				frappe.throw("Please select an answer for Question: {}, in Part VI : The Company".format(c.question))
		for s in self.supervisor:
			if s.strongly_agree == 0 and s.agree == 0 and s.disagree == 0 and s.strongly_disagree == 0:
				frappe.throw("Please select an answer for Question: {}, in Part VII : Supervisor".format(s.question))
	def autoname(self):
		name = "HR-EXIT-INT-"
		self.name = make_autoname(str(name)+".YYYY.-.####")

	@frappe.whitelist()
	def get_questions(self):
		self.check_permission("create" if self.is_new() else "write")

		parts = {
			"job_satisfaction": self.part_iii,
			"management": self.part_iv,
			"remuneration_benefits": self.part_v,
			"the_company": self.part_vi,
			"supervisor": self.part_vii
		}

		for fieldname, question_type in parts.items():
			fields = ["question"]

			if fieldname == "the_company":
				fields.append("name as table_name")

			questions = frappe.get_list(
				"Exit Interview Question",
				filters={"type": question_type},
				fields=fields,
				order_by="idx asc",
				limit_page_length=0
			)

			self.set(fieldname, [])

			for question in questions:
				question.update({
					"strongly_disagree": 0,
					"disagree": 0,
					"agree": 0,
					"strongly_agree": 0
				})

				self.append(fieldname, question)