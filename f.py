# ร้านกาแฟ (Coffee Shop) ด้วย Python

# เมนูเครื่องดื่ม
menu = {
    "กาแฟดำ": 40,
    "ลาเต้": 50,
    "คาปูชิโน่": 50,
    "มอคค่า": 55,
    "ชาเขียว": 45
}

# ฟังก์ชันแสดงเมนู
def show_menu():
    print("\nเมนูเครื่องดื่ม:")
    for drink, price in menu.items():
        print(f"- {drink}: {price} บาท")

# ฟังก์ชันรับออเดอร์จากลูกค้า
def take_order():
    order = {}
    while True:
        show_menu()
        choice = input("กรุณาเลือกเครื่องดื่ม (หรือพิมพ์ 'เสร็จ' เพื่อจบการสั่ง): ").strip()
        if choice == "เสร็จ":
            break
        elif choice in menu:
            try:
                quantity = int(input(f"ต้องการ {choice} กี่แก้ว?: ").strip())
                if quantity > 0:
                    order[choice] = order.get(choice, 0) + quantity
                else:
                    print("จำนวนต้องมากกว่า 0 กรุณาเลือกใหม่")
            except ValueError:
                print("กรุณากรอกตัวเลขที่ถูกต้อง")
        else:
            print("ขออภัย ไม่มีเมนูนี้ในร้าน กรุณาเลือกใหม่")
    return order

# ฟังก์ชันคำนวณราคารวม
def calculate_total(order):
    if not order:
        return 0
    total = sum(menu[item] * quantity for item, quantity in order.items())
    return total

# ฟังก์ชันหลักของร้านกาแฟ
def coffee_shop():
    print("ยินดีต้อนรับสู่ร้านกาแฟของเรา!")
    order = take_order()
    if order:
        total_price = calculate_total(order)
        print("\nใบเสร็จของคุณ:")
        for item, quantity in order.items():
            print(f"{item} x {quantity} = {menu[item] * quantity} บาท")
        print(f"ราคารวมทั้งหมด: {total_price} บาท")
        print("ขอบคุณที่ใช้บริการร้านกาแฟของเรา!")
    else:
        print("คุณไม่ได้สั่งอะไรเลย ขอบคุณที่แวะมา!")

# เรียกใช้งานฟังก์ชันร้านกาแฟ
if __name__ == "__main__":
    coffee_shop()
