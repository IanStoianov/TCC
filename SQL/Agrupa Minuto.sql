select concat(cast(horario as date), ' ', lpad(hour(horario), 2, 0), ':', lpad(minute(horario), 2, 0), ':00') horario, 
    avg(temp1) temp1, 
    avg(temp2) temp2, 
    avg(temp3) temp3 
    from Temperaturas 
    group by hour(horario), MINUTE(horario) 
    order by hour(horario) asc, 
        minute(horario) asc;
