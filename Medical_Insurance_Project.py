class Patient:
    #this is the constructor of the object Patient
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        self.sex= sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker

    def estimated_insurance_cost(self):
        estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
        print("{}'s estimated insurance costs is {} dollars.".format(self.name, estimated_cost))

    #method to increase the age of the patient and recalculate insurance costs based upon the new age calling the estimated_insurance_cost method
    def update_age(self, new_age):
        self.age = new_age
        print("{} is now {} years old.".format(self.name, self.age))
        self.estimated_insurance_cost()

    #method to update the number of children the patients has
    def update_num_children(self, new_num_children):
        self.num_of_children = new_num_children
        if new_num_children > 1:
            print("{} has {} children.".format(self.name, self.num_of_children))
        else:
            print("{} has 1 child.".format(self.name))
        self.estimated_insurance_cost()

    #method to update the patients bmi and recalculate insurance costs
    def update_bmi(self, new_bmi):
        change_bmi = new_bmi - self.bmi
        print("{}'s BMI has changed by {:.2f}.".format(self.name, change_bmi))
        self.bmi = new_bmi
        self.estimated_insurance_cost()

    #method to update the patients smoker status and recalculate insurance costs
    def update_smoker(self, new_smoker):
        if new_smoker == 0 :
            print("{}'s is now a non-smoker".format(self.name))
        else:
            print("{}'s is now a smoker".format(self.name))
        self.smoker = new_smoker
        self.estimated_insurance_cost()

    #method to put patient profile in a dictionary format
    def patient_profile(self):
        patient_information = {}
        patient_information["Name"] = self.name
        patient_information["Age"] = self.age
        patient_information["Sex"] = self.sex
        patient_information["BMI"] = self.bmi
        patient_information["Number of Children"] = self.num_of_children
        patient_information["Smoker"] = self.smoker
        return patient_information

# #Class to create a Master Dictionary, although this separation means that I have to run a separate update to the master dictionary after one of the patients. It feels like the right thing to separate it into it's own class as I tried (unsuccessfully to combine it in the patient class), but will need to remember that if patient info changes, the master dictionary needs to be updated. Not sure how to update the master dictionary from the patient class
class MasterPatients:
    def __init__(self):
        self.master_patients = {}

    def update_master(self, patient_info):
        patient_key = patient_info["Name"]
        self.master_patients[patient_key] = patient_info
        return self.master_patients
    #this method allows the print function to be called from the main programme, allowing this in the main programme means print() doesn't need to be kept in the class
    def __repr__(self):
        return str(self.master_patients)

#patient1 is our first instance variable
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
patient1.estimated_insurance_cost()
print("patients name is: {}".format(patient1.name))
print("patients age is: {}".format(patient1.age))
if patient1.sex == 0:
    print("patient is female")
else:
    print("patient is male")
print("patient's bmi is: {}".format(patient1.bmi))
print("patient has {} children".format(patient1.num_of_children))
if patient1.smoker == 0:
    print("patient is not a smoker")
else:
    print("patient is a smoker")
#update patient1 age to 30 which will update age and recalc estimated insurance cost
patient1.update_age(26)
patient1.update_num_children(1)
patient1.patient_profile()
print()
patient2 = Patient("Victoria Eakins", 45, 0, 20, 2, 0)
patient2.estimated_insurance_cost()
print()
#Extensions - I have created a new class which holds a master dictionary and created a method to update this master dictionary which holds all of the patient profiles. Having tried to combine the master dictionary into the patient class this didn't really work as the master dictionary isn't an attribute of the patient object, it should be it's own object and then more methods can be added. I hesitated thinking we wouldn't need multiple master dictionary objects, however we could create additional dictionaries for UAT, so actually i am now convinced that having the master dictionary as a separate object is the right thing to do
master_patients = MasterPatients()
print(master_patients)
master_patients.update_master(patient1.patient_profile())
master_patients.update_master(patient2.patient_profile())
print("Master Patients dictionary includes:")
print(master_patients)
print()
#update patient object with new bmi, this will calculate a new insurance cost
patient1.update_bmi(25)
print()
#update master dictionary object with updated patient object
master_patients.update_master(patient1.patient_profile())
print("Updated Master Patients dictionary includes changes to patient info:")
print(master_patients)
print()
print("patient would like to update smoker status:")
patient1.update_smoker(1)
print()
master_patients.update_master(patient1.patient_profile())
print("Updated Master Patients dictionary includes changes to patient info:")
print(master_patients)
print()
#I haven't done the extension suggesting to have lists[] as the input for patient information as i was more focused on creating a master patient info dictionary for all patients. I can see that my programme is still quite manual and repetitive. I imagine that the user interface for this small programme would be a form with manual data entry. whereas a list would be to create more of an interface to create the objects. Will have a think about this and come back to it later.
