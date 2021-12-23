from lcd import drivers
import time

display = drivers.lcd()

try:
    lcd_text = input("문자열을 입력하세요: ")
    display.lcd_display_string(lcd_text, 1)

finally:
    print("lcd 종료")
    display.lcd_clear()