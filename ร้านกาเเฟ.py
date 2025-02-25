import tkinter as tk
from tkinter import messagebox

# เมนูเครื่องดื่ม
menu = {
    "กาแฟดำ": 40,
    "ลาเต้": 50,
    "คาปูชิโน่": 50,
    "มอคค่า": 55,
    "ชาเขียว": 45
}

# ออเดอร์ของลูกค้า
order = {}

def add_to_order(item):
    if item in menu:
        order[item] = order.get(item, 0) + 1
        update_order_list()

def update_order_list():
    order_text.set("\n".join([f"{item} x {quantity}" for item, quantity in order.items()]))

def calculate_total():
    total = sum(menu[item] * quantity for item, quantity in order.items())
    messagebox.showinfo("ราคารวม", f"ราคารวมทั้งหมด: {total} บาท")

def reset_order():
    global order
    order = {}
    update_order_list()

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("ร้านกาแฟ")
root.geometry("400x500")
root.configure(bg="#2E2E2E")

# แสดงหัวข้อเมนู
label_menu = tk.Label(root, text="เมนูเครื่องดื่ม", font=("Arial", 16, "bold"), fg="#FFD700", bg="#2E2E2E")
label_menu.pack(pady=10)

# สร้างปุ่มเมนูที่มีดีไซน์
for item, price in menu.items():
    btn = tk.Button(root, text=f"{item} - {price} บาท", command=lambda i=item: add_to_order(i),
                    font=("Arial", 12), fg="white", bg="#4CAF50", activebackground="#45a049", relief="raised", bd=3)
    btn.pack(pady=5, fill="x", padx=20)

# แสดงออเดอร์ที่เลือก
order_text = tk.StringVar()
label_order = tk.Label(root, textvariable=order_text, font=("Arial", 12), fg="#00CED1", bg="#2E2E2E")
label_order.pack(pady=10)

# ปุ่มคำนวณราคารวม
btn_total = tk.Button(root, text="คำนวณราคารวม", command=calculate_total, font=("Arial", 12, "bold"),
                      bg="#FF5733", fg="white", activebackground="#E64A19", relief="raised", bd=3)
btn_total.pack(pady=5, fill="x", padx=20)

# ปุ่มล้างออเดอร์
btn_reset = tk.Button(root, text="ล้างออเดอร์", command=reset_order, font=("Arial", 12, "bold"),
                      bg="#DC143C", fg="white", activebackground="#B22222", relief="raised", bd=3)
btn_reset.pack(pady=5, fill="x", padx=20)

# เริ่มโปรแกรม
root.mainloop()
