from employeedata import employee_details

def test_employee_details_Rahul():
    result = employee_details("Rahul", 101, "IT", 45000)

    expected_emp = (
        "Employee Name: Rahul\n"
        "Employee ID: 101\n"
        "Department: IT\n"
        "Salary: 45000"
    )

    assert result == expected_emp