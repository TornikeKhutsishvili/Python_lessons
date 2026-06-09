# ---------------------------------------------------------------------------------------------------------------------
import logging
logging.basicConfig(
    filename="lesson8.log",
    level=logging.DEBUG,
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# ---------------------------------------------------------------------------------------------------------------------


# 1. SQL დავალება1
# გამოიტანე ProductName, CategoryID, Unit, Price ცხრილი- “პროდუქტები”,
# სადაც ფასი მოთავსებული 18-სა და 25-ს შორის დაალაგე კლებადობით ფასის მიხედვით

# SELECT ProductName, CategoryID, Unit, Price FROM Products Where price > 18 and price < 25 ORDER BY Price DESC;

# Result:
# Number of Records: 14

# ProductName	                    CategoryID	           Unit	                        Price
# Pâté chinois	                        6	               24 boxes x 2 pies	        24.00
# Tofu	                                7	               40 - 100 g pkgs.	            23.25
# Chef Antons Cajun Seasoning	        2	               48 - 6 oz jars	            22.00
# Fløtemysost	                        4	               10 - 500 g pkgs.	            21.50
# Chef Antons Gumbo Mix	                2	               36 boxes	                    21.35
# Louisiana Fiery Hot Pepper Sauce	    2	               32 - 8 oz bottles	        21.05
# Queso Cabrales	                    4	               1 kg pkg.	                21.00
# Gustafs Knäckebröd	                5	               24 - 500 g pkgs.	            21.00
# Maxilaku	                            3	               24 - 50 g pkgs.	            20.00
# Ravioli Angelo	                    5	               24 - 250 g pkgs.	            19.50
# Gula Malacca	                        2	               20 - 2 kg bags	            19.45
# Chang	                                1	               24 - 12 oz bottles	        19.00
# Inlagd Sill	                        8	               24 - 250 g jars	            19.00
# Boston Crab Meat	                    8	               24 - 4 oz tins	            18.40




# 2. SQL დავალება2
# გამოიტანე ყველა ველი, სადაც რაოდენობა ტოლია 15-ის ან 12-ის
# დაალაგე ზრდადობით ცხრილი - “OrderDetails”

# SELECT * FROM OrderDetails Where quantity = 12 or quantity = 15 Order BY quantity ASC;

# Result:
# Number of Records: 71

# OrderDetailID	    OrderID	    ProductID     Quantity
# 1	                10248	        11	        12
# 26	            10256	        77	        12
# 41	            10262	        5	        12
# 52	            10266	        12	        12
# 73	            10275	        24	        12
# 84	            10280	        24	        12
# 78	            10277	        62	        12
# 120	            10293	        18	        12
# 130	            10296	        11	        12
# 177	            10313	        36	        12
# 203	            10325	        13	        12
# 220	            10329	        56	        12
# 248	            10340	        41	        12
# 281	            10353	        11	        12
# 283	            10354	        1	        12
# 288	            10356	        55	        12
# 310	            10363	        75	        12
# 311	            10363	        76	        12
# 331	            10372	        20	        12
# 370	            10387	        59	        12
# 432	            10409	        14	        12
# 433	            10409	        21	        12
# 495	            10435	        22	        12
# 147	            10302	        43	        12
# 518	            10443	        28	        12
# 150	            10303	        68	        15
# 501	            10437	        53	        15
# 502	            10438	        19	        15
# 504	            10438	        57	        15
# 505	            10439	        12	        15
# 457	            10418	        74	        15
# 466	            10421	        53	        15
# 371	            10387	        71	        15
# 372	            10388	        45	        15
# 376	            10389	        55	        15
# 427	            10407	        69	        15
# 428	            10407	        71	        15
# 338	            10374	        58	        15
# 339	            10375	        14	        15
# 359	            10383	        50	        15
# 362	            10384	        60	        15
# 366	            10386	        24	        15
# 368	            10387	        24	        15
# 319	            10367	        65	        15
# 327	            10370	        1	        15
# 258	            10343	        76	        15
# 270	            10348	        1	        15
# 273	            10350	        50	        15
# 223	            10331	        54	        15
# 243	            10338	        30	        15
# 132	            10296	        69	        15
# 138	            10298	        62	        15
# 139	            10299	        19	        15
# 125	            10294	        17	        15
# 126	            10294	        43	        15
# 80	            10278	        59	        15
# 83	            10279	        17	        15
# 96	            10284	        27	        15
# 107	            10287	        46	        15
# 113	            10290	        29	        15
# 114	            10290	        49	        15
# 75	            10276	        10	        15
# 55	            10267	        76	        15
# 67	            10273	        31	        15
# 42	            10262	        7	        15
# 29	            10257	        77	        15
# 37	            10260	        62	        15
# 8	                10250	        65	        15
# 10	            10251	        57	        15
# 18	            10254	        24	        15
# 25	            10256	        53	        15




# 3. მოცემულია JSON მასივი:
# [
#     {"id": 1, "price": 50},
#     {"id": 2, "price": 200},
#     {"id": 3, "price": 150}
# ]
# ამოიღე მხოლოდ ის პროდუქტები, რომელთა ფასი 100-ზე მეტია.

# JSON_Array = [
#     {"id": 1, "price": 50},
#     {"id": 2, "price": 200},
#     {"id": 3, "price": 150}
# ]
#
# for i in JSON_Array:
#     if i["price"] > 100:
#         print(i)




# 4. მოცემულია რთული JSON:
# {
#   "company": {
#       "departments": [
#           {"name": "IT", "employees": [{"name": "Ana"}, {"name": "Beka"}]},
#           {"name": "HR", "employees": [{"name": "Nino"}]}
#       ]
#   }
# }
# ამოიღე ყველა თანამშრომლის სახელი

# JSON_Array_diff = {
#   "company": {
#       "departments": [
#           {"name": "IT", "employees": [{"name": "Ana"}, {"name": "Beka"}]},
#           {"name": "HR", "employees": [{"name": "Nino"}]}
#       ]
#   }
# }
#
# for department in JSON_Array_diff["company"]["departments"]:
#     for employee in department["employees"]:
#         print(employee["name"])




# 5. მოცემულია სტუდენტების სია:
# [
#   {"name": "Ana", "grades": [90, 80, 95]},
#   {"name": "Beka", "grades": [70, 85, 88]},
#   {"name": "Nino", "grades": [100, 95, 99]}
# ]
# იპოვე სტუდენტი, რომელსაც აქვს საშუალო ქულის მიხედვით საუკეთესო შედეგი.

# students = [
#   {"name": "Ana", "grades": [90, 80, 95]},
#   {"name": "Beka", "grades": [70, 85, 88]},
#   {"name": "Nino", "grades": [100, 95, 99]}
# ]
#
# best_student = ""
# best_average = 0
#
# for student in students:
#     total = 0
#     logging.debug("for loop started\n")
#
#     for grade in student["grades"]:
#         total += grade
#
#     average_score = total / len(student["grades"])
#     logging.info(f"averages is {average_score}\n")
#
#     if average_score > best_average:
#         best_average = average_score
#         best_student = student["name"]
#
#     logging.debug("for loop end\n")
#
# logging.info(f"current best: {best_student}, {best_average:.2f}")
# print(f"current best: {best_student}, {best_average:.2f}")




# 6. მოცემულია კომპანიების სია:
# {
#     "companies": [
#         {
#             "name": "TechCorp",
#             "employees": [
#                 {"name": "Ana", "salary": 3000},
#                 {"name": "Beka", "salary": 4500}
#             ]
#         },
#         {
#             "name": "SoftPlus",
#             "employees": [
#                 {"name": "Nino", "salary": 5000},
#                 {"name": "Giorgi", "salary": 2500}
#             ]
#         }
#     ]
# }
# იპოვე ყველა თანამშრომელი, რომლის ხელფასი მეტია 4000-ზე და დაბეჭდე მათი სახელები + კომპანიის სახელი.

# companies_list = {
#     "companies": [
#         {
#             "name": "TechCorp",
#             "employees": [
#                 {"name": "Ana", "salary": 3000},
#                 {"name": "Beka", "salary": 4500}
#             ]
#         },
#         {
#             "name": "SoftPlus",
#             "employees": [
#                 {"name": "Nino", "salary": 5000},
#                 {"name": "Giorgi", "salary": 2500}
#             ]
#         }
#     ]
# }
#
# for company in companies_list["companies"]:
#     company_name = company["name"]
#
#     for employee in company["employees"]:
#         if employee["salary"] > 4000:
#             print(f"{company_name} - {employee["name"]}")




# 7. გააგზავნე GET მოთხოვნა https://jsonplaceholder.typicode.com/users და დაბეჭდე პირველი მომხმარებლის სახელი.
# import httpx
# import asyncio
#
# BASE_URL = "https://jsonplaceholder.typicode.com/"
# USER_ENDPOINT = "users"
#
# # async ფუნქცია — ასინქრონულად იღებს მომხმარებლების სიას
# async def get_users():
#     logging.info("\nget_users() started\n")
#
#     try:
#         # ვქმნით async HTTP client-ს
#         async with httpx.AsyncClient() as client:
#             logging.debug("HTTP client created")
#
#             # ვაგზავნით GET მოთხოვნას API-ზე
#             response = await client.get(BASE_URL + USER_ENDPOINT)
#             logging.info(f"Request sent to {BASE_URL + USER_ENDPOINT}")
#
#             if response.status_code == 200:
#                 logging.info("Response status: 200 OK")
#
#                 users = response.json()
#                 logging.debug(f"Users received: {len(users)} items")
#
#                 if users:
#                     first_user = users[0]["name"]
#                     logging.info(f"First user found: {first_user}")
#
#                     return first_user
#
#                 logging.warning("Users list is empty")
#                 return None
#
#             else:
#                 logging.error(f"Bad response status: {response.status_code}")
#                 return None
#     except Exception as e:
#         logging.error(f"Error in get_users(): {e}")
#         return None
#     finally:
#         logging.info("\nget_users() finished\n")
#
# # მთავარი async ფუნქცია, სადაც ვიძახებთ get_users()
# async def main():
#     logging.info("main() started")
#
#     name = await get_users()
#     logging.info(f"Result from get_users(): {name}")
#
#     print(name)
#     logging.info("main() finished")
#
# # პროგრამის გაშვება event loop-ში
# # async პროგრამა იწყებს მუშაობას event loop-ის კონტროლით (აკონტროლებს როდის გაგრძელდეს/შეჩერდეს კოდი)
#
# logging.info("Program started")
# asyncio.run(main())
# logging.info("Program finished")




# 8. გააგზავნე POST მოთხოვნა https://jsonplaceholder.typicode.com/posts და
# შექმენი ახალი პოსტი შემდეგი მონაცემებით: {"title": "Test", "body": "Hello World", "userId": 5}

# import httpx
# import asyncio
#
# BASE_URL = "https://jsonplaceholder.typicode.com/"
# POST_ENDPOINT = "posts"
#
# async def add_post():
#     logging.info("\nadd_post() started\n")
#
#     try:
#         async with httpx.AsyncClient() as client:
#             logging.debug("HTTP client created")
#
#             post_obj = { "title": "Test", "body": "Hello World", "userId": 5 }
#
#             # ვაგზავნით POST მოთხოვნას API-ზე
#             response = await client.post(
#                 BASE_URL + POST_ENDPOINT,
#                 headers={"Content-Type": "application/json"},
#                 json=post_obj
#             )
#             logging.info(f"POST request sent to {BASE_URL + POST_ENDPOINT}")
#
#             # 201-ია თუ სერვერზე ახალი რესურსი წარმატებით შეიქმნა
#             if response.status_code == 201:
#                 data = response.json()
#                 logging.info(f"Post created successfully: {data}")
#
#                 return data
#             else:
#                 logging.error(f"Failed to create post: {response.status_code}")
#                 return None
#     except Exception as e:
#         logging.error(f"Error in add_post: {e}")
#     finally:
#         logging.info("\nadd_post() finished\n")
#
# async def main():
#     logging.info("Program started")
#
#     result = await add_post()
#     print(result)
#
#     logging.info(f"Program result: {result}")
#     logging.info("Program finished")
#
# asyncio.run(main())




# 9. წამოიღე ყველა TODO task და დაბეჭდე მხოლოდ ის, სადაც "completed": False -
# https://jsonplaceholder.typicode.com/todos
# ბოლოს დათვალე რამდენი შეუსრულებელი ტასკია (რაოდენობაში)

# import httpx
# import asyncio
#
# BASE_URL = "https://jsonplaceholder.typicode.com/"
# TODOS_ENDPOINT = "todos"
#
# async def get_all_todo_task():
#     try:
#         async with httpx.AsyncClient() as client:
#             logging.debug("HTTP client created")
#             uncompleted_todos = 0
#
#             # ვაგზავნით GET მოთხოვნას API-ზე
#             response = await client.get(BASE_URL + TODOS_ENDPOINT)
#             logging.info(f"Request sent to {BASE_URL + TODOS_ENDPOINT}")
#
#             if response.status_code == 200:
#                 logging.info("Response status: 200 OK")
#
#                 todos = response.json()
#                 logging.debug(f"Todos received: {len(todos)} items")
#
#                 if todos:
#                     logging.info(f"First user found: {todos}")
#
#                     for todo in todos:
#                         if todo["completed"] == False:
#                             print(todo)
#                             uncompleted_todos += 1
#
#                     logging.info(f"Uncompleted todos count: {uncompleted_todos}")
#                     return uncompleted_todos
#
#                 logging.warning("Todos list is empty")
#                 return None
#             else:
#                 logging.error(f"Bad response status: {response.status_code}")
#                 return None
#     except Exception as e:
#         logging.error(f"Error in add_post: {e}")
#     finally:
#         logging.info("\nadd_post() finished\n")
#
# async def main():
#     logging.info("Program started")
#
#     result = await get_all_todo_task()
#
#     print("Uncompleted todos:", result)
#
#     logging.info(f"Program result: {result}")
#     logging.info("Program finished")
#
# asyncio.run(main())




# 10. ამოიღე ყველა პოსტი
# https://jsonplaceholder.typicode.com/posts,
# შემდეგ იპოვე ავტორის სახელი (users API-დან) და დაბეჭდე:
# "Post Title – Author Name". გამოიტანე მხოლოდ პირველი 5

import httpx
import asyncio

BASE_URL = "https://jsonplaceholder.typicode.com/"
POSTS_ENDPOINT = "posts"
USERS_ENDPOINT = "users"

async def get_posts():
    try:
        async with httpx.AsyncClient() as client:
            logging.debug("HTTP client created")

            # ვაგზავნით GET მოთხოვნას API-ზე
            response = await client.get(BASE_URL + POSTS_ENDPOINT)
            logging.info(f"Request sent to {BASE_URL + POSTS_ENDPOINT}")

            if response.status_code == 200:
                logging.info("Response status: 200 OK")

                posts = response.json()
                logging.debug(f"Todos received: {len(posts)} items")

                if posts:
                    logging.info(f"Posts found: {posts}")
                    return posts

                logging.warning("Posts list is empty")
                return None
            else:
                logging.error(f"Bad response status: {response.status_code}")
                return None
    except Exception as e:
        logging.error(f"Error in get_posts: {e}")
    finally:
        logging.info("\nget_posts() finished\n")


async def get_users():
    logging.info("\nget_users() started\n")

    try:
        # ვქმნით async HTTP client-ს
        async with httpx.AsyncClient() as client:
            logging.debug("HTTP client created")

            # ვაგზავნით GET მოთხოვნას API-ზე
            response = await client.get(BASE_URL + USERS_ENDPOINT)
            logging.info(f"Request sent to {BASE_URL + USERS_ENDPOINT}")

            if response.status_code == 200:
                logging.info("Response status: 200 OK")

                users = response.json()
                logging.debug(f"Users received: {len(users)} items")

                if users:
                    logging.info(f"Users found: {users}")
                    return users

                logging.warning("Users list is empty")
                return None
            else:
                logging.error(f"Bad response status: {response.status_code}")
                return None
    except Exception as e:
        logging.error(f"Error in get_users(): {e}")
        return None
    finally:
        logging.info("\nget_users() finished\n")


# MAIN
async def main():
    logging.info("Program started")

    res_users = await get_users()
    res_posts = await get_posts()

    if not res_users or not res_posts:
        logging.error("Failed to load users or posts")
        return

    # userId -> name
    users_obj = {
        user["id"]: user["name"]
        for user in res_users
    }

    # მხოლოდ პირველი 5 პოსტი გამოვიტანოთ
    for post in res_posts[:5]:
        author_name = users_obj.get(post["userId"], "Unknown Author")

        print(f'Post: {post["title"]} - Author: {author_name}')
        logging.info(f'Post: "{post["title"]}" - Author: {author_name}')

    logging.info("Program finished")

asyncio.run(main())
