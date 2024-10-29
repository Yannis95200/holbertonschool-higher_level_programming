-- Groups records in 'second_table' by 'score' and orders the results by 'score' in descending order
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;