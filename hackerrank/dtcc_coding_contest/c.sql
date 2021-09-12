/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/
-- select avg(b) from (
-- select count(*) as b from customer group by city_id) as t;
SET @av = (SELECT AVG(b) from (select count(*) as b from customer group by city_id) as tt);

select country_name, city_name, c from
(select country_name, city_name, count(*) as c
from customer join city on customer.city_id=city.id join country on city.country_id=country.id group by city_id) as t
where c > @av;