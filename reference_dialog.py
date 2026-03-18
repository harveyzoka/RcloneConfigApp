# reference_dialog.py
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QHeaderView
from PyQt5.QtCore import Qt

class ReferenceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Bảng tham số dòng lệnh rclone gợi ý")
        self.resize(700, 400)
        
        layout = QVBoxLayout(self)
        
        label = QLabel("Dưới đây là các tham số thường dùng khi mount. Bạn có thể chép và dán vào phần cài đặt nâng cao của mỗi ổ đĩa:")
        layout.addWidget(label)
        
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Cờ (Flag)", "Tác dụng", "Khuyên dùng?"])
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        
        flags = [
            ("--vfs-cache-mode full", "Bật đệm toàn diện (ghi tạm ra ổ cứng). Cần thiết để phần mềm Windows (Word, Excel...) có thể mở, sửa và lưu file trực tiếp trên Cloud.", "Rất khuyên dùng"),
            ("--vfs-cache-max-size 10G", "Giới hạn dung lượng tối đa của bộ nhớ đệm trên ổ cứng (VD: 10G, 50G). Khi đầy rclone sẽ tự động xóa các file tạm cũ nhất.", "Khuyên dùng"),
            ("--vfs-cache-max-age 24h", "Thời gian giữ file đệm trên máy tính. Nếu sau 24h không mở lại file đó, file sẽ tự bị xóa để giải phóng ổ cứng.", "Khuyên dùng"),
            ("--buffer-size 64M", "Dung lượng RAM dùng để tải/đệm trước cho MỖI file khi stream/đọc. Tăng tốc độ với máy nhiều RAM (Mặc định là 16M).", "Khuyên dùng (32M-64M)"),
            ("--dir-cache-time 1000h", "Nhớ sẵn cấu trúc thư mục để duyệt nhanh không bị lác. Tuy nhiên file mới do người khác thêm trên web có thể bị chậm cập nhật trên máy bạn.", "Tùy chọn"),
            ("--allow-other", "Cho phép các phần mềm chạy dưới quyền Admin hoặc tài khoản khác trên Windows truy cập được vào ổ đĩa rclone.", "Rất khuyên dùng"),
            ("--log-file \"C:\\rclone.log\"", "Lưu nhật ký chạy ngầm ra file để tiện bắt lỗi nếu ổ đĩa bị ngắt kết nối.", "Khuyên dùng khi fix lỗi"),
            ("--network-mode", "Giả lập ổ mount là một ổ đĩa mạng LAN (Network Drive). Khắc phục được lỗi không mở được file ở một vài phần mềm khó tính.", "Khuyên dùng tùy PC"),
            ("--vfs-read-chunk-size 32M", "Tăng kích thước chia nhỏ mảnh file (Mặc định 128M). Số chuẩn (32M-64M) giúp cải thiện độ mượt khi xem video/steam file lớn.", "Tùy chọn")
        ]
        
        table.setRowCount(len(flags))
        for row, data in enumerate(flags):
            table.setItem(row, 0, QTableWidgetItem(data[0]))
            table.setItem(row, 1, QTableWidgetItem(data[1]))
            table.setItem(row, 2, QTableWidgetItem(data[2]))
            
        layout.addWidget(table)
