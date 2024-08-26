from instagram_private_api import Client, ClientError

def report_user(api, user_id, num_reports):
    for i in range(num_reports):
        try:
            api.report_user(user_id)
            print(f'Report {i + 1} completed.')
        except ClientError as e:
            print(f"Failed to report {i + 1}: {str(e)}")

# اطلاعات ورود
your_username = 'saeednexa'
your_password = 's299218H!'

# شناسه کاربر هدف
user_to_report = 'mraiyamm'
num_reports = 10  # تعداد گزارش‌های مورد نظر

# ایجاد و ورود به حساب
api = Client(your_username, your_password)

# ریپورت کردن کاربر
report_user(api, user_to_report, num_reports)
