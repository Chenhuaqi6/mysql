mysql> create table customers(c_id int primary key,c_name varchar(20),c_age tinyint unsigned,c_sex enum("M","F"),c_city varchar(20),c_salary float(12,2));
Query OK, 0 rows affected (0.01 sec)

mysql> desc customers;
+----------+---------------------+------+-----+---------+-------+
| Field    | Type                | Null | Key | Default | Extra |
+----------+---------------------+------+-----+---------+-------+
| c_id     | int(11)             | NO   | PRI | NULL    |       |
| c_name   | varchar(20)         | YES  |     | NULL    |       |
| c_age    | tinyint(3) unsigned | YES  |     | NULL    |       |
| c_sex    | enum('M','F')       | YES  |     | NULL    |       |
| c_city   | varchar(20)         | YES  |     | NULL    |       |
| c_salary | float(12,2)         | YES  |     | NULL    |       |
+----------+---------------------+------+-----+---------+-------+
6 rows in set (0.03 sec)

mysql> insert into customers values
    -> (1,"Zhangsan",25,"M","Beijing",8000),
    -> (2,"Lisi",30,"F","Shanghai",10000),
    -> \c
mysql> insert into customers values(1,"zhangsan",25,"M","Beijing",8000),
    -> (2,"lisi",30,"F","shanghai",10000),(3,"wangwu",27,"M","shenzhen",3000); 
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from customers;
+------+----------+-------+-------+----------+----------+
| c_id | c_name   | c_age | c_sex | c_city   | c_salary |
+------+----------+-------+-------+----------+----------+
|    1 | zhangsan |    25 | M     | Beijing  |  8000.00 |
|    2 | lisi     |    30 | F     | shanghai | 10000.00 |
|    3 | wangwu   |    27 | M     | shenzhen |  3000.00 |
+------+----------+-------+-------+----------+----------+



mysql> create table orders(o_id int,o_name varchar(30),o_price float(12,2),foreign key(o_id) references customers(c_id) on delete cascade on update cascade);
Query OK, 0 rows affected (0.01 sec)

mysql> desc orders;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| o_id    | int(11)     | YES  | MUL | NULL    |       |
| o_name  | varchar(30) | YES  |     | NULL    |       |
| o_price | float(12,2) | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+

mysql> insert into orders values
    -> (1,"iphone",5288),
    -> (1,"ipad",3299),
    -> (3,"mate9",3688),
    -> (2,"iwatch",2222),
    -> (2,"r11",4400);
Query OK, 5 rows affected (0.00 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from orders;
+------+--------+---------+
| o_id | o_name | o_price |
+------+--------+---------+
|    1 | iphone | 5288.00 |
|    1 | ipad   | 3299.00 |
|    3 | mate9  | 3688.00 |
|    2 | iwatch | 2222.00 |
|    2 | r11    | 4400.00 |
+------+--------+---------+
5 rows in set (0.00 sec)


mysql> select c_name,c_salary,c_age from customers where c_salary > 4000 or c_age < 29;
+----------+----------+-------+
| c_name   | c_salary | c_age |
+----------+----------+-------+
| zhangsan |  8000.00 |    25 |
| lisi     | 10000.00 |    30 |
| wangwu   |  3000.00 |    27 |
+----------+----------+-------+


mysql> select c_name,c_age,c_city,c_salary*1.15 as zhanggongzi from customers where c_age >= 25 and c_city in ("Beijing","shanghai");
+----------+-------+----------+-------------+
| c_name   | c_age | c_city   | zhanggongzi |
+----------+-------+----------+-------------+
| zhangsan |    25 | Beijing  |     9200.00 |
| lisi     |    30 | shanghai |    11500.00 |
+----------+-------+----------+-------------+
2 rows in set (0.00 sec)


mysql> select * from customers where c_city = "Beijing" order by c_salary desc limit 0,1;
+------+----------+-------+-------+---------+----------+
| c_id | c_name   | c_age | c_sex | c_city  | c_salary |
+------+----------+-------+-------+---------+----------+
|    1 | zhangsan |    25 | M     | Beijing |  8000.00 |
+------+----------+-------+-------+---------+----------+
1 row in set (0.00 sec)


mysql> select * from customers order by c_salary asc limit 0,1;
+------+--------+-------+-------+----------+----------+
| c_id | c_name | c_age | c_sex | c_city   | c_salary |
+------+--------+-------+-------+----------+----------+
|    3 | wangwu |    27 | M     | shenzhen |  3000.00 |
+------+--------+-------+-------+----------+----------+
1 row in set (0.00 sec)



mysql> select * from orders where o_id in (select c_id from customers where c_salary > 5000);
+------+--------+---------+
| o_id | o_name | o_price |
+------+--------+---------+
|    1 | iphone | 5288.00 |
|    1 | ipad   | 3299.00 |
|    2 | iwatch | 2222.00 |
|    2 | r11    | 4400.00 |
+------+--------+---------+
4 rows in set (0.00 sec)


mysql> show create table orders\G;
*************************** 1. row ***************************
       Table: orders
Create Table: CREATE TABLE `orders` (
  `o_id` int(11) DEFAULT NULL,
  `o_name` varchar(30) DEFAULT NULL,
  `o_price` float(12,2) DEFAULT NULL,
  KEY `o_id` (`o_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`o_id`) REFERENCES `customers` (`c_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.00 sec)

ERROR: 
No query specified

mysql> alter table orders drop foreign key `orders_ibfk_1`;
Query OK, 0 rows affected (0.00 sec)
Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table customers drop primary key;
Query OK, 3 rows affected (0.02 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> desc customers;
+----------+---------------------+------+-----+---------+-------+
| Field    | Type                | Null | Key | Default | Extra |
+----------+---------------------+------+-----+---------+-------+
| c_id     | int(11)             | NO   |     | NULL    |       |
| c_name   | varchar(20)         | YES  |     | NULL    |       |
| c_age    | tinyint(3) unsigned | YES  |     | NULL    |       |
| c_sex    | enum('M','F')       | YES  |     | NULL    |       |
| c_city   | varchar(20)         | YES  |     | NULL    |       |
| c_salary | float(12,2)         | YES  |     | NULL    |       |
+----------+---------------------+------+-----+---------+-------+
6 rows in set (0.00 sec)

