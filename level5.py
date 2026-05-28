orders = ["GE001 - PENDING", "GE002 - PENDING", "GE003 - ASSIGNED"]

while True:
    print("\n===== HỆ THỐNG ĐIỀU PHỐI GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Gán tài xế cho đơn hàng")
    print("3. Cập nhật trạng thái giao hàng")
    print("4. Hủy đơn hàng")
    print("5. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn: ")
    
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
    
    choice = int(choice)
    
    match choice:
        case 1:
            if len(orders) == 0:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("Danh sách đơn hàng hiện tại:")
                for i in range(len(orders)):
                    print(f"{i+1}. {orders[i]}")
        
        case 2:
            raw_code = input("Nhập mã đơn hàng cần gán tài xế: ")
            code = raw_code.strip().upper()
            
            found_index = -1
            for i in range(len(orders)):
                if orders[i].startswith(code + " - "):
                    found_index = i
                    break
            
            if found_index == -1:
                print("Không tìm thấy mã đơn hàng.")
            else:
                current_status = orders[found_index].split(" - ")[-1]
                match current_status:
                    case "PENDING":
                        orders[found_index] = f"{code} - ASSIGNED"
                        print("Đã gán tài xế cho đơn hàng.")
                    case _:
                        print("Chỉ có thể gán tài xế cho đơn hàng đang chờ xử lý.")
        
        case 3:
            raw_code = input("Nhập mã đơn hàng cần cập nhật trạng thái: ")
            code = raw_code.strip().upper()
            
            found_index = -1
            for i in range(len(orders)):
                if orders[i].startswith(code + " - "):
                    found_index = i
                    break
            
            if found_index == -1:
                print("Không tìm thấy mã đơn hàng.")
            else:
                current_status = orders[found_index].split(" - ")[-1]
                match current_status:
                    case "ASSIGNED":
                        orders[found_index] = f"{code} - DELIVERING"
                        print("Đã cập nhật trạng thái thành DELIVERING.")
                    case "DELIVERING":
                        orders[found_index] = f"{code} - COMPLETED"
                        print("Đã cập nhật trạng thái thành COMPLETED.")
                    case "PENDING":
                        print("Đơn hàng chưa được gán tài xế, không thể chuyển sang trạng thái giao hàng.")
                    case "COMPLETED":
                        print("Đơn hàng đã hoàn tất, không thể cập nhật tiếp.")
                    case "CANCELLED":
                        print("Đơn hàng đã bị hủy, không thể cập nhật.")
                    case _:
                        print("Trạng thái không hợp lệ.")
        
        case 4:
            raw_code = input("Nhập mã đơn hàng cần hủy: ")
            code = raw_code.strip().upper()
            
            found_index = -1
            for i in range(len(orders)):
                if orders[i].startswith(code + " - "):
                    found_index = i
                    break
            
            if found_index == -1:
                print("Không tìm thấy mã đơn hàng.")
            else:
                current_status = orders[found_index].split(" - ")[-1]
                match current_status:
                    case "PENDING" | "ASSIGNED":
                        orders[found_index] = f"{code} - CANCELLED"
                        print("Đã hủy đơn hàng.")
                    case "DELIVERING":
                        print("Đơn hàng đang được giao, không thể hủy.")
                    case "COMPLETED":
                        print("Đơn hàng đã hoàn tất, không thể hủy.")
                    case "CANCELLED":
                        print("Đơn hàng đã được hủy trước đó.")
                    case _:
                        print("Trạng thái không hợp lệ.")
        
        case 5:
            print("Thoát chương trình.")
            break
        
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
