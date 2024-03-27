class employee:
    def __init__(self, name, mounth, bs_salary, nb_work_day, coefficients_salary):
        self.name = name
        self.mounth = mounth
        self.bs_salary = bs_salary
        self.nb_work_day = nb_work_day 
        self.coefficients_salary = coefficients_salary
    
    def calculate_salary(self):
        salary_sum = self.bs_salary * self.nb_work_day * self.coefficients_salary - 1000000
        if(salary_sum > 9000000):
            salary_sum = 0.9 * salary_sum
            return salary_sum
        else:
            return salary_sum
        
    def out(self):
        print("Salary of employee {} received in the month {}: ".format(self.name, self.mounth) + str(self.calculate_salary()) + " VND")

class managers(employee):
    def __init__(self, name, mounth, bs_salary, nb_work_day, coefficients_salary, efficiency_coefficient):
        super().__init__(name, mounth, bs_salary, nb_work_day, coefficients_salary)
        self.efficiency_coefficient = efficiency_coefficient
    
    def calculate_salary_bonus(self):
        if(self.efficiency_coefficient < 1):
            return (self.calculate_salary() * self.efficiency_coefficient)
        else:
            return (self.calculate_salary() + ((self.bs_salary * self.nb_work_day * self.coefficients_salary - 1000000) * (self.efficiency_coefficient - 1) * 0.85))
    
    def out(self):
        print("Salary of employee {} received in the month {}: ".format(self.name, self.mounth) + str(self.calculate_salary_bonus()) + " VND")

name = str(input("Manager name: ")).strip()
inf = list(map(float, input("Information: ").split()))
managers(name, inf[0], inf[1], inf[2], inf[3], inf[4]).out()