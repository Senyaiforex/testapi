import asyncio
import time
#
#
# async def deap_mean():
#     await asyncio.sleep(5)
#
#
# async def keap_mean():
#     await asyncio.sleep(5)
#
# async def main():
#     now = time.time()
#     task_1 = asyncio.create_task(keap_mean())
#     task_2 = asyncio.create_task(deap_mean())
#     await task_1
#     await task_2
#     print(f"{time.time() - now}")
#
# if __name__ == "__main__":
#     asyncio.run(main())


# import math
#
#
# def calculate_percent(value_one: int, value_two: int) -> str:
#     """
#     Функция считает процентную разницу между двумя числами относительно второго числа.
#     Второе число берется как 100%. Округление всегда происходит в большую сторону.
#
#     :param value_one: первое число
#     :param value_two: второе число
#     :return: процентная разница со знаком + или -, либо 0 если числа равны
#     :rtype: str
#     """
#     try:
#         if value_one == value_two:
#             return "0"
#
#         percent_difference = ((value_one - value_two) / value_two) * 100
#         rounded_difference = math.ceil(abs(percent_difference))
#         if rounded_difference == 0:
#             rounded_difference = 1
#         sign = "+" if percent_difference > 0 else "-"
#
#         return f"{sign}{rounded_difference}%"
#
#     except ZeroDivisionError:
#         return "0"
#
# print(calculate_percent(120, 120))
#
#
# def get_friend_word(number: int) -> str:
#     if number % 10 == 1 or 2 <= number % 10 <= 4:
#         return "друга"
#     else:
#         return "друзей"
#
# number = 11
# print(f"Пригласить {number} {get_friend_word(number)}")