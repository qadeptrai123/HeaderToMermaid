# Công cụ chuyển nhanh header C sang syntax mermaid

- Để phục vụ cho môn OOP, tôi đã rảnh rỗi viết ra cái tool tào lao này. Dưới đây là cách cài đặt và sử dụng.

- Trước hết bạn phải đã cài đặt git và python.

- Cài đặt các thư viện như sau nếu bạn chưa cài:

```bash
    pip install os 
    pip install shutil
    pip install subprocess
```

- Mở terminal hoặc VSCode lên và đi tới thư mục bạn muốn lưu trữ và gõ lệnh:

    - `git clone https://github.com/qadeptrai123/HeaderToMermaid`

- Việc clone như thế này giúp cho bạn sẽ có thể cập nhật nhanh nếu tôi có cập nhật phiên bản mới cho repo này.
- Sau khi clone về xong, gõ tiếp lệnh:
    - `cd HeaderToMermaid`
- Lúc này bạn đã vào thư mục chính, để sử dụng tool follow các bước sau: 
    - `python main.py`
- Nhập đường dẫn tuyệt đối vô:

    - ![image1](./Asset/1.png)

- Nhập tên file xuất ra (chú ý thêm đuôi .md):

    - ![image2](./Asset/2.png)

- File output sẽ được lưu trong thư mục Output.

- Để cho ra kết quả tốt nhất, class nên viết như thế này:
    ```C
        class X {
            private:
                int a;
                float b;
            public:
                int c;
                void d();
        };
    ```

- Nếu đủ sự bully dành cho thằng bucky Thế Anh thì tôi sẽ tiếp tục phát triển tool này đến khi kết thúc học phần OOP.

**Hãy để lại cho mình một like, subscribe, share, tim trên tiktok và star trên github nhé**

****

***Mọi thắc mắc, yêu cầu cải tiến, phát hiện bug. Hãy liên hệ với chủ Repo này để được giải quyết.***

**QA Đẹp Trai.**