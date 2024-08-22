import mysql.connector
from connection import ConnectorRead


def result_print(result):
    try:
        for index, i in enumerate(result, start=1):
            print(
                f'{index}. Title: {i[1]}\nDescription: {i[2]}\nYear: {i[3]}\nCategory: {i[4]}\nActor Name: {i[5]}\nActor Lastname: {i[6]}\n')
    except IndexError:
        for index, i in enumerate(result, start=1):
            print(
                f'{index}. Title: {i[1]}\nDescription: {i[2]}\nYear: {i[3]}\nCategory: {i[4]}\n')


def query_added(query):
    dbconfig = {
        'host': 'mysql.itcareerhub.de',
        'user': 'ich1',
        'password': 'ich1_password_ilovedbs',
        'database': '310524ptm_viktoriia'
    }
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM 310524ptm_viktoriia.top_ques WHERE queue = '{query}'")
    res = cursor.fetchall()

    if len(res) > 0:
        cursor.execute(f"UPDATE 310524ptm_viktoriia.top_ques SET count = {res[0][-1] + 1} WHERE id = {res[0][0]}")
    else:
        cursor.execute(f"INSERT INTO 310524ptm_viktoriia.top_ques (queue, count) VALUES ('{query}', 1)")

    connection.commit()
    cursor.close()
    connection.close()


def get_result_keyword(keyword):
    select = f"""select distinct
 t1.film_id, t1.title, t1.description, t1.release_year, 
t3.name as name, 
 t5.first_name, t5.last_name
from film as t1
left join film_category as t2
on t1.film_id = t2.film_id
left join category as t3
on t3.category_id = t2.category_id
left join film_actor as t4
on t1.film_id = t4.actor_id
left join actor as t5
on t4.actor_id = t5.actor_id
where title like '%{keyword}%' or 
description like '%{keyword}%' or 
release_year like '%{keyword}%' or
first_name like '%{keyword}%' or
name like '%{keyword}%' limit 15;
    """

    con = ConnectorRead.get_connect()
    con.connect()
    cursor = con.cursor()
    cursor.execute(select)
    result = cursor.fetchall()
    result_print(result)
    cursor.close()
    con.close()

    query_added(keyword)
    return result


def search_title(title):
    select = f"""select distinct 
            t1.film_id, t1.title, t1.description, t1.release_year, 
            t3.name as category_name, 
            t5.first_name, t5.last_name
            from film as t1
            left join film_category as t2 on t1.film_id = t2.film_id
            left join category as t3 on t3.category_id = t2.category_id
            left join film_actor as t4 on t1.film_id = t4.film_id
            left join actor as t5 on t4.actor_id = t5.actor_id
            where t1.title like '%{title}%' limit 15
            """
    con = ConnectorRead.get_connect()
    con.connect()
    cursor = con.cursor()
    cursor.execute(select)
    result = cursor.fetchall()
    cursor.close()
    con.close()
    result_print(result)
    return result


def search_year(year):
    select = f"""select distinct
            t1.film_id, t1.title, t1.description, t1.release_year, 
            t3.name as category_name
            from film as t1
            left join film_category as t2 on t1.film_id = t2.film_id
            left join category as t3 on t3.category_id = t2.category_id
            where t1.release_year = '{year}' limit 15
            """
    con = ConnectorRead.get_connect()
    con.connect()
    cursor = con.cursor()
    cursor.execute(select)
    result = cursor.fetchall()
    cursor.close()
    con.close()
    result_print(result)
    return result


def search_description(description):
    select = f"""select distinct
                    t1.film_id, t1.title, t1.description, t1.release_year, 
                    t3.name as category_name, 
                    t5.first_name, t5.last_name
                    from film as t1
                    left join film_category as t2 on t1.film_id = t2.film_id
                    left join category as t3 on t3.category_id = t2.category_id
                    left join film_actor as t4 on t1.film_id = t4.film_id
                    left join actor as t5 on t4.actor_id = t5.actor_id
                    where t1.description like '%{description}%' limit 15
                    """
    con = ConnectorRead.get_connect()
    con.connect()
    cursor = con.cursor()
    cursor.execute(select)
    result = cursor.fetchall()
    cursor.close()
    con.close()
    result_print(result)
    return result


def search_category(category):
    select = f"""select distinct
            t1.film_id, t1.title, t1.description, t1.release_year, 
            t3.name as category_name 
            from film as t1
            left join film_category as t2 on t1.film_id = t2.film_id
            left join category as t3 on t3.category_id = t2.category_id
            where t3.name like '%{category}%' limit 15
                            """
    con = ConnectorRead.get_connect()
    con.connect()
    cursor = con.cursor()
    cursor.execute(select)
    result = cursor.fetchall()
    cursor.close()
    con.close()
    result_print(result)
    return result


def search_actor(actor):
    select = f"""select distinct
            t1.film_id, t1.title, t1.description, t1.release_year, 
            t3.name as category_name, 
            t5.first_name, t5.last_name
            from film as t1
            left join film_category as t2 on t1.film_id = t2.film_id
            left join category as t3 on t3.category_id = t2.category_id
            left join film_actor as t4 on t1.film_id = t4.film_id
            left join actor as t5 on t4.actor_id = t5.actor_id
            where t5.first_name like '%{actor}%' or t5.last_name like '%{actor}%' limit 15
            """
    con = ConnectorRead.get_connect()
    con.connect()
    cursor = con.cursor()
    cursor.execute(select)
    result = cursor.fetchall()
    cursor.close()
    con.close()
    result_print(result)
    return result


def get_top_result():
    dbconfig = {
        'host': 'mysql.itcareerhub.de',
        'user': 'ich1',
        'password': 'ich1_password_ilovedbs',
        'database': '310524ptm_viktoriia'
    }
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM 310524ptm_viktoriia.top_ques order by count desc limit 10")
    res = cursor.fetchall()
    for i in res:
        print(f'{i[1]}\t{i[-1]}')
