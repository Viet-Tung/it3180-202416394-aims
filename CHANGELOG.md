# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2026-11-12
### Fixed
- Sửa lỗi `search_by_title` phân biệt chữ hoa/thường (#20).

## [1.0.0] - 2026-11-11

### Added
- Phương thức hiển thị giỏ hàng `Cart.print_cart()` và tích hợp vào luồng chạy chính trong `main.py`.
- Tính năng tìm kiếm đĩa theo tiêu đề (`search_by_title`) (#4).
- Tính năng tính chiết khấu hóa đơn (`total_cost_with_discount` / `Feature/discount`) (#9).
- Hỗ trợ thông báo thêm DVD bằng tiếng Việt (`feature/vietnamese-messages`).
- Bộ kiểm thử đơn vị toàn diện (comprehensive test suite) cho lớp `Cart`.
- Biểu đồ Use Case cho tài liệu hệ thống và Pull Request template cho kho mã nguồn.

### Fixed
- Lỗi cho phép giỏ hàng nhận vượt quá 20 đĩa (`Bugfix/cart limit off-by-one`) (#7).