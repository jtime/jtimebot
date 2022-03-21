import os
import psycopg2
def insert(record_list):
    DATABASE_URL =os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    table_columns = '(alpaca_name, training, duration, date)'
    postgres_insert_query = f"""INSERT INTO alpaca_training {table_columns} VALUES (%s, %s, %s, %s);"""

    cursor.executemany(postgres_insert_query, record_list)
    conn.commit()
    result = f"恭喜你，{cursor.rowcount}筆資料成功匯入 alpaca_training 表單 !")

    print(result)

    cursor.close()
    conn.close()

    return result


