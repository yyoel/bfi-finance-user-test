with cte_transformed_customer as(
	select 	plate_number
			,split_part(owner,'(a.k.a.', 1 ) as owner_name_1
			,split_part(split_part(owner,'(a.k.a.', 2 ), ';', 1) as owner_name_2
			,split_part(split_part(owner,'; a.k.a.', 2), '),', 1) as owner_name3
			,split_part(split_part(split_part(owner,'; a.k.a.', 2), '),', 2), ';' ,1 ) as address
			,to_char(to_date(regexp_replace(split_part(split_part(split_part(owner,'; a.k.a.', 2), '),', 2), ';' ,2 ), 'DOB', ''), 'DD Mon YYYY'), 'YYYYMMDD') as dob
			,regexp_replace(split_part(split_part(split_part(owner,'; a.k.a.', 2), '),', 2), ';' ,3 ), 'POB', '') as pob
			,case 
				when length(regexp_replace(split_part(split_part(split_part(owner,'; a.k.a.', 2), '),', 2), ';' ,4 ), 'Gender', '')) = 19 
				then 'Male'
				else 'Female'
			 end as gender
			
	from customer_asset
) 
select * from cte_transformed_customer;	