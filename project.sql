SELECT * FROM actions2load;
select count(*) from actions2load;


# Number of account_id available
select distinct(account_id) from actions2load;
select count(distinct(account_id)) from actions2load;

# Number of events available
select distinct(event_type) from actions2load;
select count(distinct(event_type)) from actions2load;


# event type and frequency of event
SELECT 
    event_type, COUNT(account_id) AS frequency_of_event
FROM
    actions2load
GROUP BY event_type
ORDER BY frequency_of_event DESC;


# account id and number of events
SELECT 
    account_id, COUNT(event_type) AS number_of_event
FROM
    actions2load
GROUP BY account_id
ORDER BY number_of_event DESC;


# Day of the week
select event_type, dayname(event_time) from actions2load;
SELECT 
    DAYNAME(event_time) AS day_of_the_week,
    COUNT(event_type) AS event_count
FROM
    actions2load
GROUP BY day_of_the_week
ORDER BY event_count desc;

# Time of the day in hours and minutes with event count  
select event_type, time_format(event_time, "%H %i") as time_of_the_day from actions2load;
SELECT 
    TIME_FORMAT(event_time, '%H : %i') AS time_of_the_day,
    COUNT(event_type) AS event_count
FROM
    actions2load
GROUP BY time_of_the_day
ORDER BY time_of_the_day;

# Time of the day in hours with event count
SELECT 
    TIME_FORMAT(event_time, '%H') AS time_of_the_day,
    COUNT(event_type) AS event_count
FROM
    actions2load
GROUP BY time_of_the_day
ORDER BY time_of_the_day;


select event_time, event_type from actions2load where account_id = 'caffe2b03e6057845c52212acaaa1a34';
