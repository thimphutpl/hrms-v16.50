frappe.ui.form.on("Employee Grade", {
    setup: function (frm) {
        frm.set_query("default_salary_structure", function () {
            return {
                filters: { docstatus: 1, is_active: "Yes" },
            };
        });
        frm.set_query("default_leave_policy", function () {
            return {
                filters: { docstatus: 1 },
            };
        });
    },

    refresh: function (frm) {
        // Run once when form loads
        validate_increment_value(frm);
    },

    // Fires whenever increment_method is changed
    increment_method: function (frm) {
        validate_increment_value(frm);
    },

    // Fires whenever increment_value is changed
    increment_value: function (frm) {
        validate_increment_value(frm);
    },

    // Safety net on save
    validate: function (frm) {
        if (frm.doc.increment_method === "Percent" && frm.doc.increment_value > 100) {
            frappe.throw(__("Increment Value cannot be greater than 100 when Increment Method is Percent"));
        }
    },
});

function validate_increment_value(frm) {
    if (frm.doc.increment_method === "Percent" && frm.doc.increment_value > 100) {
        frappe.msgprint({
            title: __("Invalid Value"),
            indicator: "red",
            message: __("Increment Value cannot be greater than 100 when Increment Method is Percent"),
        });
       // frm.set_value("increment_value", 100);
    }
}