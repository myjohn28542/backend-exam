"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number == 0:
            return "ศูนย์"
        
        units = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        tens = ["", "สิบ", "ยี่สิบ", "สามสิบ", "สี่สิบ", "ห้าสิบ", "หกสิบ", "เจ็ดสิบ", "แปดสิบ", "เก้าสิบ"]
        scales = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]

        num_text = ""
        num_str = str(number)
        length = len(num_str)
        
        for i in range(length):
            digit = int(num_str[i])
            scale = length - i - 1

            if scale > 0 and digit != 0:
                if scale % 6 == 0 and i > 0:
                    num_text += "ล้าน"
                if digit == 1:
                    if scale % 6 == 1: 
                        num_text += "เอ็ด"
                    else:
                        num_text += units[digit]
                elif digit == 2 and scale % 6 == 1:
                    num_text += "ยี่"
                else:
                    num_text += units[digit]

                num_text += scales[scale % 6]
            elif scale == 0:
                if digit == 1 and len(num_text) > 0:
                    num_text += "เอ็ด"
                else:
                    num_text += units[digit]
        
        return num_text
