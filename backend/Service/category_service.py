from DAO.db_object import PostgresDB
from DAO.cache_object import RedisCache
from Service.db_queries import *


class CategoryService:

    def __init__(self):
        self.dboperator = PostgresDB()
        self.cacheoperator = RedisCache()

    def insert_redis_products(self, catlvl1, catlvl2, products):
        redis_query = f"{catlvl1.strip()}-{catlvl2.strip()}"
        for product in products:
            self.cacheoperator.redis.rpush(redis_query, *product)
        self.cacheoperator.redis.expire(redis_query, 60)
        return 1

    def get_redis_products(self, catlvl1, catlvl2):
        redis_query = f"{catlvl1.strip()}-{catlvl2.strip()}"
        final = []
        if self.cacheoperator.redis.exists(redis_query):
            products = self.cacheoperator.redis.lrange(redis_query, 0, -1)
            for length in range(len(products)//5):
                product = products[length*5: length*5+5]
                for index in range(len(product)):
                    product[index] = product[index].decode()
                final.append(product)
            print("Got products from redis...")
            return final
        else:
            return 1

    def get_category_lvl2_prods(self, category_lvl1, category_lvl2):
        status = self.get_redis_products(category_lvl1, category_lvl2)
        if status == 1:
            # self.dboperator.cursor.execute('''
            #     select id from category_table where category=%s''', (
            #     category_lvl1,))
            # result = self.dboperator.cursor.fetchone()
            response = self.dboperator.operation(get_id_cat, (category_lvl1, ), res=1)
            result = response[0]
            # self.dboperator.cursor.execute('''
            #     select productid from category_table where parent_id=%s and category=%s''', (
            #     result[0],
            #     category_lvl2,))
            # result = self.dboperator.cursor.fetchall()
            result = self.dboperator.operation(get_pid_cat, (result[0], category_lvl2, ), res=1)
            product_IDs = []
            final = []
            for product in result:
                product_IDs.append(product[0])
            for id in product_IDs:
                # self.dboperator.cursor.execute('''
                #     select product_ID,
                #             product_name,
                #             product_price,
                #             product_description,
                #             product_image 
                #         from productinfo where product_ID=%s''', (id,))
                # result = self.dboperator.cursor.fetchone()
                response = self.dboperator.operation(get_fields_prdinfo, (id,), res=1)
                result = response[0]
                final.append(result)
            insert_status = self.insert_redis_products(category_lvl1, category_lvl2, final)
            if insert_status == 1:
                print("Inserted into redis...")
            return final
        else:
            return status
