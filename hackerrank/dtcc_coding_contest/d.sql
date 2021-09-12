/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/
set @max_loc = (select location_id as c 
from companies
group by location_id
order by count(*)
DESC
limit 1);

select people.name, companies.name
from people join companies on people.COMPANY_ID=companies.id
where companies.location_id=@max_loc;
