CREATE DATABASE quan_ly_benh_nhan;
USE quan_ly_benh_nhan;

CREATE TABLE IF NOT EXISTS benh_nhan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_bn VARCHAR(50),
    ho_ten VARCHAR(100),
    gioi_tinh VARCHAR(10),
    ngay_sinh DATE,
    so_dt VARCHAR(20),
    dia_chi VARCHAR(255),
    chan_doan TEXT,
    ngay_nhap_vien DATE,
    ghi_chu TEXT
);
