import heapq

class Patient:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class ERQueue:
    def __init__(self):
        self.queue = []

    def add_patient(self, patient):
        if isinstance(patient, Patient):
            heapq.heappush(self.queue, patient)
        else:
            print("Invalid patient object")

    def treat_next_patient(self):
        if self.queue:
            return heapq.heappop(self.queue)
        return None

# ตัวอย่างการใช้งาน
er = ERQueue()

er.add_patient(Patient("คนไข้ A", 1))  # หัวใจวาย
er.add_patient(Patient("คนไข้ B", 3))  # ปวดท้อง
er.add_patient(Patient("คนไข้ C", 2))  # กระดูกหัก

# แสดงคิวผู้ป่วยทั้งหมด
print("คิวผู้ป่วยทั้งหมด:")
for patient in er.queue:
    print(f"- {patient.name} (Priority: {patient.priority})")

# รักษาผู้ป่วยตามลำดับความสำคัญ
print("\nรักษาผู้ป่วยตามลำดับความสำคัญ:")
while er.queue:
    next_patient = er.treat_next_patient()
    if next_patient:
        print(f"- รักษา {next_patient.name} (Priority: {next_patient.priority})")

# ตรวจสอบว่าคิวยังมีผู้ป่วยเหลือหรือไม่
if not er.queue:
    print("\nคิวผู้ป่วยว่างแล้ว")