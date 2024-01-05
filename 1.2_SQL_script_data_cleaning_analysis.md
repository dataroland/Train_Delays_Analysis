```sql
WITH cte AS (
  SELECT *,
         CASE
           WHEN train_arrtime_t = '00:00:00' AND train_arrtime_a = '00:00:00' THEN 0
           ELSE CASE
                  WHEN EXTRACT(EPOCH FROM (train_arrtime_a)) / 60 < 150 AND EXTRACT(EPOCH FROM (train_arrtime_t)) / 60 > 150 THEN EXTRACT(EPOCH FROM (train_arrtime_a - train_arrtime_t)) / 60 + 24 * 60
                  ELSE EXTRACT(EPOCH FROM (train_arrtime_a - train_arrtime_t)) / 60
                END
         END AS arrtime_diff,
         CASE
           WHEN train_deptime_t = '00:00:00' AND train_deptime_a = '00:00:00' THEN 0
           ELSE CASE
                  WHEN EXTRACT(EPOCH FROM (train_deptime_a)) / 60 < 150 AND EXTRACT(EPOCH FROM (train_deptime_t)) / 60 > 150 THEN EXTRACT(EPOCH FROM (train_deptime_a - train_deptime_t)) / 60 + 24 * 60
                  ELSE EXTRACT(EPOCH FROM (train_deptime_a - train_deptime_t)) / 60
                END
         END AS deptime_diff
  FROM train_delays_fin
  JOIN station_map_new on train_delays_fin.analyzed_line || train_delays_fin.train_station = station_map_new.analyzed_line_a || station_map_new.train_station_a
  WHERE
    (NOT (train_arrtime_a = '00:00:00' AND train_deptime_a = '00:00:00' AND train_deptime_t = '00:00:00')
    AND (train_arrtime_a != '00:00:00' AND train_deptime_t = '00:00:00' AND train_deptime_a = '00:00:00')
    OR (train_arrtime_a != '00:00:00' AND train_deptime_t != '00:00:00' AND train_deptime_a != '00:00:00'))
    OR (NOT (train_deptime_a = '00:00:00' AND train_arrtime_a = '00:00:00' AND train_arrtime_t = '00:00:00')
    AND (train_deptime_a != '00:00:00' AND train_arrtime_a = '00:00:00' AND train_arrtime_t = '00:00:00')
    OR (train_deptime_a != '00:00:00' AND train_arrtime_a != '00:00:00' AND train_arrtime_t != '00:00:00'))
    
),
line_station_counts AS (
  SELECT analyzed_line as analyzed_line_b, report_date as report_date_b, train_start_time as train_start_time_b, COUNT(*) AS line_station_count
  FROM cte
  where station_type IN (1, 2, 4)
  GROUP BY analyzed_line, report_date, train_start_time
)
SELECT *,
       CASE WHEN station_km = 0 THEN 0 ELSE arrtime_diff - LAG(deptime_diff) OVER (ORDER BY cte.analyzed_line, cte.report_date, cte.train_start_time, station_km) END as running_delay,
       CASE WHEN train_deptime_t = '00:00:00' OR LEAD(station_km = 0) OVER (ORDER BY cte.analyzed_line, cte.report_date, cte.train_start_time, station_km) THEN 0 ELSE deptime_diff - arrtime_diff END as stop_delay,
       CASE WHEN station_km = 0 THEN 0 ELSE arrtime_diff - LAG(deptime_diff) OVER (ORDER BY cte.analyzed_line, cte.report_date, cte.train_start_time, station_km) END + (CASE WHEN train_deptime_t = '00:00:00' OR LEAD(station_km = 0) OVER (ORDER BY cte.analyzed_line, cte.report_date, cte.train_start_time, station_km) THEN 0 ELSE deptime_diff - arrtime_diff END) as station_delay,
       EXTRACT(WEEK FROM cte.report_date) as week,
       EXTRACT(Month FROM cte.report_date) as month,
       CAST(REGEXP_REPLACE(distance, '\D', '', 'g') AS integer) AS distance_km,
       to_char(cte.report_date, 'Day') as day_of_week
       
FROM cte
JOIN line_station_counts ON cte.analyzed_line = line_station_counts.analyzed_line_b
                     AND cte.report_date = line_station_counts.report_date_b
                     AND cte.train_start_time = line_station_counts.train_start_time_b
WHERE 
((cte.analyzed_line = 'Budapest-Déli-Keszthely' AND line_station_count = 16 AND station_type IN (1, 2, 4))
OR (cte.analyzed_line = 'Keszthely-Budapest-Déli' AND line_station_count = 16 AND station_type IN (1, 2, 4))
OR (cte.analyzed_line = 'Budapest-Keleti-Békéscsaba' AND line_station_count = 6 AND station_type IN (1, 2, 4))
OR (cte.analyzed_line = 'Békéscsaba-Budapest-Keleti' AND line_station_count = 6 AND station_type IN (1, 2, 4))
OR (cte.analyzed_line = 'Budapest-Keleti-Pécs' AND line_station_count = 6 AND station_type IN (1, 2, 4))
OR (cte.analyzed_line = 'Pécs-Budapest-Keleti' AND line_station_count = 6 AND station_type IN (1, 2, 4))
OR (cte.analyzed_line = 'Budapest-Nyugati-Debrecen' AND line_station_count = 9 AND station_type IN (1, 2, 4))
OR (cte.analyzed_line = 'Debrecen-Budapest-Nyugati' AND line_station_count = 9 AND station_type IN (1, 2, 4))
OR (cte.analyzed_line = 'Budapest-Nyugati-Szeged' AND line_station_count = 11 AND station_type IN (1, 2, 4))
OR (cte.analyzed_line = 'Szeged-Budapest-Nyugati' AND line_station_count = 11 AND station_type IN (1, 2, 4))
OR (cte.analyzed_line = 'Keszthely-Győr' AND line_station_count = 15 AND station_type IN (1, 2, 4))
OR (cte.analyzed_line = 'Győr-Keszthely' AND line_station_count = 15 AND station_type IN (1, 2, 4)))

ORDER BY cte.analyzed_line, cte.report_date, cte.train_start_time, station_km
;
```
