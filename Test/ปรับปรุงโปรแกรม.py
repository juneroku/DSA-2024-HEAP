import heapq
from datetime import datetime
import time

class BankCustomer:
    def __init__(self, name, service_type, is_premium=False):
        self.name = name
        self.service_type = service_type
        self.is_premium = is_premium
        self.arrival_time = datetime.now()
        self.ticket_number = None  # เลขคิว
        
        # กำหนดลำดับความสำคัญตาม service_type และสถานะลูกค้า
        self.priority = self._calculate_priority()
        
    def _calculate_priority(self):
        # ลำดับความสำคัญ (ยิ่งน้อยยิ่งสำคัญ)
        priority = {
            'ฝาก-ถอน': 3,
            'ชำระค่าบริการ': 2,
            'เปิดบัญชี': 1,
            'สินเชื่อ': 0
        }
        
        # ลูกค้า Premium จะได้ priority สูงกว่าปกติ 1 ระดับ
        base_priority = priority.get(self.service_type, 4)
        if self.is_premium:
            base_priority -= 0.5
            
        return base_priority
        
    def __lt__(self, other):
        # เปรียบเทียบลำดับความสำคัญ
        if self.priority == other.priority:
            # ถ้าความสำคัญเท่ากัน ใช้เวลามาก่อน-หลัง
            return self.arrival_time < other.arrival_time
        return self.priority < other.priority
        
class BankQueue:
    def __init__(self):
        self.queue = []  # heap queue
        self.waiting_count = 0
        self.ticket_counter = {  # ตัวนับเลขคิวของแต่ละประเภทบริการ
            'ฝาก-ถอน': 1,
            'ชำระค่าบริการ': 1,
            'เปิดบัญชี': 1,
            'สินเชื่อ': 1
        }
        
    def add_customer(self, customer):
        # กำหนดเลขคิวตามประเภทบริการ
        customer.ticket_number = f"{customer.service_type[0].upper()}-{self.ticket_counter[customer.service_type]:03}"
        self.ticket_counter[customer.service_type] += 1
        
        heapq.heappush(self.queue, customer)
        self.waiting_count += 1
        print(f"ลูกค้า: {customer.name}")
        print(f"บริการ: {customer.service_type}")
        print(f"เลขคิว: {customer.ticket_number}")
        print(f"สถานะ: {'Premium' if customer.is_premium else 'ทั่วไป'}")
        print(f"จำนวนคิวรอ: {self.waiting_count}")
        print("-" * 30)
        
    def serve_next_customer(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
            return None
            
        customer = heapq.heappop(self.queue)
        self.waiting_count -= 1
        
        wait_time = datetime.now() - customer.arrival_time
        print(f"\nเรียกลูกค้า: {customer.name}")
        print(f"บริการ: {customer.service_type}")
        print(f"เลขคิว: {customer.ticket_number}")
        print(f"เวลารอ: {wait_time.seconds} วินาที")
        print(f"จำนวนคิวรอ: {self.waiting_count}")
        print("-" * 30)
        
        return customer
        
    def display_queue(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
            return
            
        print("\nรายการคิวที่รอ:")
        # สร้าง copy ของคิวเพื่อไม่ให้กระทบคิวจริง
        temp_queue = self.queue.copy()
        position = 1
        
        while temp_queue:
            customer = heapq.heappop(temp_queue)
            print(f"{position}. {customer.name} ({customer.ticket_number}) - {customer.service_type}")
            position += 1
        print("-" * 30)

# ตัวอย่างการใช้งาน
def demo_bank_queue():
    bank = BankQueue()
    
    # เพิ่มลูกค้าเข้าคิว
    customers = [
        BankCustomer("คุณแดง", "ฝาก-ถอน"),
        BankCustomer("คุณขาว", "สินเชื่อ", is_premium=True),
        BankCustomer("คุณเขียว", "ชำระค่าบริการ"),
        BankCustomer("คุณม่วง", "เปิดบัญชี"),
        BankCustomer("คุณฟ้า", "สินเชื่อ")
    ]
    
    for customer in customers:
        bank.add_customer(customer)
        time.sleep(1)  # จำลองการมาถึงต่างเวลากัน
        
    print("\nแสดงลำดับคิว:")
    bank.display_queue()
    
    # จำลองการเรียกลูกค้าเข้ารับบริการ
    print("\nเริ่มเรียกลูกค้า:")
    for _ in range(len(customers)):
        bank.serve_next_customer()
        time.sleep(1)

if __name__ == "__main__":
    demo_bank_queue()