product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:
    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Bán sản phẩm")
    print("3. Nhập thêm hàng")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát")

    try:
        choice = int(input("Nhập lựa chọn: "))

        # Hiển thị sản phẩm
        if choice == 1:
            for p in product_list:
                if p["quantity"] == 0:
                    status = "Hết hàng"
                elif p["quantity"] <= 5:
                    status = "Sắp hết hàng"
                else:
                    status = "Còn hàng"

                print(
                    f"Mã SP: {p['product_id']} | "
                    f"Tên: {p['product_name']} | "
                    f"Giá: {p['price']} | "
                    f"Tồn kho: {p['quantity']} | "
                    f"Đã bán: {p['sold']} | "
                    f"Trạng thái: {status}"
                )

        # Bán sản phẩm
        elif choice == 2:
            product_id = input("Nhập mã sản phẩm: ").strip().upper()

            found = False

            for p in product_list:
                if p["product_id"] == product_id:
                    found = True

                    try:
                        quantity = int(input("Nhập số lượng mua: "))

                        if quantity <= 0:
                            print("Số lượng mua không hợp lệ")

                        elif quantity > p["quantity"]:
                            print("Số lượng trong kho không đủ để bán")

                        else:
                            p["quantity"] -= quantity
                            p["sold"] += quantity

                            total = quantity * p["price"]

                            print("Bán hàng thành công")
                            print("Khách cần thanh toán:", total)

                    except ValueError:
                        print("Số lượng mua không hợp lệ")

                    break

            if not found:
                print("Không tìm thấy sản phẩm cần bán")

        # Nhập kho
        elif choice == 3:
            product_id = input("Nhập mã sản phẩm: ").strip().upper()

            found = False

            for p in product_list:
                if p["product_id"] == product_id:
                    found = True

                    try:
                        quantity = int(input("Nhập số lượng nhập thêm: "))

                        if quantity <= 0:
                            print("Số lượng nhập kho không hợp lệ")
                        else:
                            p["quantity"] += quantity
                            print("Nhập kho thành công")

                    except ValueError:
                        print("Số lượng nhập kho không hợp lệ")

                    break

            if not found:
                print("Không tìm thấy sản phẩm cần nhập kho")

        # Báo cáo doanh thu
        elif choice == 4:
            total_revenue = 0
            best_product = ""
            max_sold = 0

            print("\n===== BÁO CÁO DOANH THU =====")

            for p in product_list:
                revenue = p["price"] * p["sold"]
                total_revenue += revenue

                print(
                    f"{p['product_name']} | "
                    f"Đã bán: {p['sold']} | "
                    f"Doanh thu: {revenue}"
                )

                if p["sold"] > max_sold:
                    max_sold = p["sold"]
                    best_product = p["product_name"]

            if total_revenue == 0:
                print("Chưa có doanh thu phát sinh.")
            else:
                print("Tổng doanh thu:", total_revenue)
                print("Sản phẩm bán chạy nhất:", best_product)

        # Thoát
        elif choice == 5:
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
