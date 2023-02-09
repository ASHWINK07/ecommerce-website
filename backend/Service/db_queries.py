get_id_cat = '''select id from category_table where category=%s;''' 
get_pid_cat = '''select productid from category_table where parent_id=%s and category=%s;''' 
get_fields_prdinfo = '''select product_ID,product_name,product_price,product_description,product_image from productinfo where product_ID=%s;''' 
get_fields_order_prdinfo = '''select product_ID, product_name, product_price, product_description, product_image from productinfo order by product_name;''' 
get_cat_id_cat = '''select category, id from category_table where level=%s;''' 
get_cat_cat = '''select distinct category from category_table where parent_id=%s;''' 
get_all_rnd_limit_prdinfo = '''select product_ID, product_name, product_price,product_description,product_image from productinfo order by random() limit %s;''' 
set_all_prdinfo = '''insert into productinfo values(%s,%s,%s,%s,%s,%s,%s);''' 
set_cat_category = '''insert into category_table (category,parent_id,level) values(%s,%s,%s);''' 
set_all_category = '''insert into category_table (category,parent_id,productid,level) values(%s,%s,%s,%s);''' 
update_ptitle_prdinfo = '''update productinfo set product_title=%s where product_ID=%s;''' 
update_pprice_prdinfo = '''update productinfo set product_price=%s where product_ID=%s;''' 
update_pimage_prdinfo = '''update productinfo set product_image=%s where product_ID=%s;''' 
update_pdescription_prdinfo = '''update productinfo set product_description=%s where product_ID=%s;''' 
update_pavailability_prdinfo = '''update productinfo set product_availability=%s where product_ID=%s;''' 
update_pname_prdinfo = '''update productinfo set product_name=%s where product_ID=%s;''' 
get_all_cat = '''select * from category_table where category=%s;'''
get_all_prdinfo = '''select * from productinfo where product_ID=%s;''' 